import sys
import os
import json
import glob
from datetime import datetime
from rich.text import Text
from rallies.manager import Manager
from rallies import console
from rallies.config import get_llm_provider, set_llm_provider, CONFIG_DIR
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from pathlib import Path

def display_application_banner():
    banner_text = """
██╗    ██████╗ █████╗ ██╗     ██╗     ██╗███████╗███████╗
  ██╗  ██╔══██╗██╔══██╗██║     ██║     ██║██╔════╝██╔════╝
    ██ ╗█████╔╝███████║██║     ██║     ██║█████╗  ███████╗
  ██╔╝ ██╔══██╗██╔══██║██║     ██║     ██║██╔══╝  ╚════██║
██╔╝   ██║  ██║██║  ██║███████╗███████╗██║███████╗███████║
╚╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝╚══════╝
"""
    
    lines = banner_text.strip().split('\n')
    gradient_colors = ['bright_blue', 'blue', 'cyan', 'bright_cyan', 'magenta', 'bright_magenta']
    
    styled_lines = [Text(line, style=f"bold {gradient_colors[i % len(gradient_colors)]}") for i, line in enumerate(lines)]
    
    full_banner = Text("\n\n")
    for line in styled_lines:
        full_banner.append(line)
        full_banner.append('\n')
    
    subtitle = Text("AI powered investment research, backed by real-time data", style="bold bright_magenta")
    full_banner.append('\n')
    full_banner.append(subtitle)
    
    console.print(full_banner)

def interactive_shell(session_file=None):
    display_application_banner()
    
    console.print("\n[dim white]Tips for getting started:[/dim white]")
    console.print("[white]1. Ask questions about stocks, analyze trends, or get market insights.[/white]")
    console.print("[white]2. Be specific for the best results.[/white]")
    console.print("[white]3. Type /provider <openai|gemini> to switch LLM provider.[/white]")
    console.print("[white]4. Type /help for more information.[/white]\n")
    
    selected_agent = Manager()
    llm_provider = get_llm_provider().capitalize()

    history_file = Path(CONFIG_DIR) / "history.txt"
    history_file.parent.mkdir(parents=True, exist_ok=True)
    session = PromptSession(history=FileHistory(str(history_file)))

    messages = []
    session_subject = None
    if session_file and session_file.exists():
        try:
            with open(session_file, "r") as f:
                data = json.load(f)
                messages = data.get("messages", [])
                session_subject = data.get("subject", "Resumed Session")
            console.print(f"[bold green]Resumed session: {session_file.name}[/bold green]")
            console.print(f"[bold]Subject: [i]{session_subject}[/i][/bold]")
            for message in messages:
                role = "User" if message["role"] == "user" else "Agent"
                color = "cyan" if role == "User" else "magenta"
                console.print(f"[bold {color}]{role}:[/bold {color}] {message['content']}")
        except (json.JSONDecodeError, FileNotFoundError):
            console.print(f"[bold red]Could not load session: {session_file.name}[/bold red]")
            session_file = None
            messages = []

    if not session_file:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        session_file = Path(CONFIG_DIR) / f"session_{timestamp}.json"

    print("\nType your queries below. Press Ctrl+C to exit.\n")
    
    try:
        while True:
            prompt_text = f"({llm_provider}) > "
            user_input_text = session.prompt(prompt_text)

            if user_input_text.strip().startswith("/"):
                parts = user_input_text.strip().split()
                command = parts[0]
                if command == "/provider":
                    if len(parts) == 2:
                        provider = parts[1].lower()
                        if provider in ["openai", "gemini"]:
                            set_llm_provider(provider)
                            llm_provider = get_llm_provider().capitalize()
                            selected_agent = Manager()
                            console.print(f"[green]LLM provider switched to: {llm_provider}[/green]\n")
                        else:
                            console.print(f"[red]Invalid provider: {provider}. Please use 'openai' or 'gemini'.[/red]\n")
                    else:
                        console.print("[red]Usage: /provider <openai|gemini>[/red]\n")
                else:
                    console.print(f"[red]Unknown command: {command}[/red]\n")
                continue
            
            if user_input_text.strip():
                if not session_subject:
                    session_subject = (user_input_text[:70] + '...') if len(user_input_text) > 70 else user_input_text
                    console.print(f"[bold green]Started new session: {session_file.name}[/bold green]")
                    console.print(f"[bold]Subject: [i]{session_subject}[/i][/bold]")

                messages.append({"role": "user", "content": user_input_text})
                response = selected_agent.process_prompt(user_input_text, messages)
                messages.append({"role": "agent", "content": response})
                
                session_data = {"subject": session_subject, "messages": messages}
                with open(session_file, "w") as f:
                    json.dump(session_data, f, indent=2)
            else:
                console.print("[yellow]Please enter a query.[/yellow]\n")
                
    except (KeyboardInterrupt, EOFError):
        print("\n\nGoodbye!")
        sys.exit(0)

def get_session_files():
    return sorted(glob.glob(str(Path(CONFIG_DIR) / "session_*.json")), key=os.path.getmtime, reverse=True)

def main():
    args = sys.argv[1:]
    
    if "--continue" in args:
        session_files = get_session_files()
        if session_files:
            interactive_shell(session_file=Path(session_files[0]))
        else:
            console.print("[yellow]No sessions found to continue.[/yellow]")
            interactive_shell()
        return

    if "--resume" in args:
        resume_index = args.index("--resume")
        session_id = args[resume_index + 1] if len(args) > resume_index + 1 and not args[resume_index + 1].startswith("-") else None

        session_files = get_session_files()
        if not session_files:
            console.print("[yellow]No sessions found to resume.[/yellow]")
            interactive_shell()
            return

        if session_id:
            target_file = Path(CONFIG_DIR) / f"session_{session_id}.json"
            if target_file.exists():
                interactive_shell(session_file=target_file)
            else:
                console.print(f"[red]Session '{session_id}' not found.[/red]")
        else:
            console.print("[bold]Available sessions to resume:[/bold]")
            for i, f_path_str in enumerate(session_files):
                f_path = Path(f_path_str)
                subject = "No subject"
                try:
                    with open(f_path, 'r') as sf:
                        data = json.load(sf)
                        subject = data.get("subject", "No subject")
                except (json.JSONDecodeError, FileNotFoundError):
                    subject = "[red]Error reading session[/red]"
                console.print(f"  [cyan]{i + 1}[/cyan]: {f_path.name} - [i]{subject}[/i]")
            
            try:
                choice_str = input("Choose a session number (or press Enter to cancel): ")
                if not choice_str:
                    sys.exit(0)
                choice = int(choice_str) - 1
                if 0 <= choice < len(session_files):
                    interactive_shell(session_file=Path(session_files[choice]))
                else:
                    console.print("[red]Invalid selection.[/red]")
            except ValueError:
                console.print("[red]Invalid input.[/red]")
        return

    if args:
        command = args[0]
        if command == "provider":
            if len(args) > 2 and args[1] == "set":
                provider = args[2].lower()
                if provider in ["openai", "gemini"]:
                    set_llm_provider(provider)
                    console.print(f"[green]LLM provider set to: {provider}[/green]")
                else:
                    console.print(f"[red]Invalid provider: {provider}. Please use 'openai' or 'gemini'.[/red]")
            else:
                console.print("[red]Usage: rallies provider set <openai|gemini>[/red]")
        else:
            console.print(f"[red]Unknown command: {command}[/red]")
    else:
        interactive_shell()

if __name__ == '__main__':
    main()
