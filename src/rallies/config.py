import os
import json

CONFIG_DIR = os.path.expanduser("~/.rallies")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def get_config():
    """Reads the configuration file."""
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_config(config):
    """Saves the configuration file."""
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def get_llm_provider():
    """Gets the LLM provider from the config file."""
    config = get_config()
    return config.get("llm_provider", "openai")

def set_llm_provider(provider: str):
    """Sets the LLM provider in the config file."""
    config = get_config()
    config["llm_provider"] = provider
    save_config(config)
