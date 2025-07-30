<div align="center">
  
  # 🚀 Rallies CLI
  
  **AI-Powered Investment Research Platform**
  
  *ChatGPT for traders, backed by real-time financial data*

  [![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
  [![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg)](https://openai.com/)
  [![Rallies.ai](https://img.shields.io/badge/Data%20by-Rallies.ai-ff6b6b.svg)](https://rallies.ai)

  ![Rallies CLI Demo](https://via.placeholder.com/800x400/1a1a1a/ffffff?text=Rallies+CLI+Demo)
  
</div>

## ✨ What is Rallies CLI?

Rallies CLI is an intelligent investment research assistant that combines the conversational power of AI with real-time financial data. Think of it as ChatGPT specifically designed for traders and investors, equipped with live market data, news feeds, and comprehensive financial analysis capabilities.

### 🎯 Key Features

- **🤖 AI-Powered Analysis**: Advanced GPT-4 powered financial analysis and insights
- **📊 Real-Time Data**: Live market prices, news, and financial metrics
- **🔍 Smart Planning**: Intelligent multi-step research planning and execution  
- **💬 Interactive Chat**: Natural language interface for complex financial queries
- **📈 Market Intelligence**: Technical analysis, fundamental research, and trend identification
- **⚡ Fast & Responsive**: Streaming responses with live progress indicators
- **🎨 Beautiful Interface**: Rich terminal UI with colors, markdown, and live updates

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI (coming soon)
pip install rallies

# Or install from source
git clone https://github.com/your-username/rallies-cli.git
cd rallies-cli
pip install -e .
```

### Setup

1. **Get your OpenAI API key** from [OpenAI Platform](https://platform.openai.com/)
2. **Set environment variable**:
   ```bash
   export OPENAI_API_KEY="sk-your-api-key-here"
   ```
3. **Launch Rallies**:
   ```bash
   rallies
   ```

That's it! You're ready to start researching.

## 💡 Usage Examples

### Basic Queries
```
> What's happening with AAPL today?
> Analyze Tesla's recent performance
> Show me top gainers in tech sector
```

### Advanced Analysis  
```
> Compare MSFT vs GOOGL over the last quarter
> Find stocks with cup and handle patterns
> What's the market sentiment on cryptocurrency?
```

### Technical Analysis
```
> Show me NVDA's technical indicators
> Find oversold stocks in the S&P 500
> Analyze Bitcoin's recent price action
```

### News & Events
```
> Latest earnings reports this week
> Federal Reserve meeting impact on markets
> Breaking news affecting my portfolio
```

## 🛠️ CLI Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands and usage |
| `/key API_KEY` | Set your Rallies.ai API key for enhanced features and more usage |
| `/feed` | Browse recent high-scoring community questions |
| `/clear` | Clear conversation history |
| `/compact` | Compress conversation while preserving context |
| `/exit` or `/quit` | Exit the application |

## 🏗️ How It Works
## 🔧 Architecture

### Core Components

- **CLI Interface** (`src/cli.py`): Beautiful terminal interface with rich formatting
- **Agent System** (`src/agent/`): Multi-step planning and execution engine
- **Manager** (`src/manager.py`): Orchestrates the entire research workflow
- **LLM Integration** (`src/llm.py`): OpenAI API integration with streaming
- **Helpers** (`src/helpers.py`): Utilities for token counting, config management

### Data Sources

- **Real-time Market Data**: Live prices, volume, and trading metrics
- **Financial News**: Breaking news and market-moving events  
- **Company Fundamentals**: Earnings, ratios, and financial statements
- **Technical Indicators**: Charts, patterns, and trading signals
- **Economic Data**: Macro indicators and market sentiment

## 🔑 API Keys & Authentication

### OpenAI API Key (Required)
```bash
export OPENAI_API_KEY="sk-your-openai-key"
```

### Rallies.ai API Key (Optional - Higher usage limits)
```bash
# Set via CLI
rallies
> /key your-rallies-api-key
```

The Rallies.ai API key provides you higher rate limits.


### Project Structure

```
rallies-cli/
├── src/
│   ├── __init__.py
│   ├── cli.py              # Main CLI interface
│   ├── manager.py          # Workflow orchestration
│   ├── llm.py             # OpenAI integration
│   ├── helpers.py         # Utilities and helpers
│   └── agent/
│       ├── __init__.py
│       ├── agent.py       # Core agent logic
│       └── prompts.py     # System prompts
├── pyproject.toml         # Package configuration
├── setup.py              # Setup script
├── LICENSE               # GPL v3 License
└── README.md            # This file
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run tests**: `pytest`
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Contributing Guidelines

- Follow Python PEP 8 style guidelines
- Add docstrings to new functions and classes
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📋 Requirements

- **Python 3.8+**
- **OpenAI API Key** (required)
- **Terminal with color support** (recommended)
- **Internet connection** for real-time data

### Dependencies

- `openai` - GPT-4 integration
- `rich` - Terminal formatting and colors  
- `requests` - HTTP requests for data APIs
- `inquirer` - Interactive prompts
- `tiktoken` - Token counting and management
- `numpy` - Numerical computations

## 🐛 Troubleshooting

### Common Issues

**"OpenAI API Key not found"**
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**"Rate limit exceeded"**
- Get a Rallies.ai API key for higher limits
- Use `/compact` to reduce token usage

**"Network connection error"**  
- Check internet connection
- Verify firewall settings
- Try again after a few moments

**"Import errors"**
```bash
pip install --upgrade rallies
```

### Getting Help

- 📧 **Email**: [support@rallies.ai](mailto:support@rallies.ai)
- 💬 **Community**: [Rallies.ai Discord](https://discord.gg/xKbBExMTYc)

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI** for providing the GPT-4 API
- **Rich** library for beautiful terminal output
- **Python community** for excellent financial libraries
- **Contributors** who make this project better

## 🌐 Links

- **Website**: [rallies.ai](https://rallies.ai)
- **Mobile app**: [Rallies](https://apps.apple.com/us/app/rallies-ai-stocks-trading/id6745213959?platform=iphone)
- **Twitter**: [@RalliesAI](https://x.com/ralliesai)
- **LinkedIn**: [Rallies AI](https://www.linkedin.com/company/107790814/)

---

<div align="center">
  
  **Built with ❤️ by the Rallies team**
  *Making financial research accessible to everyone*

</div>