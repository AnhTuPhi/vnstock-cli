# vnstock-cli

A command-line interface for the [vnstock](https://github.com/thinh-vu/vnstock) library — bringing Vietnamese stock market data directly to your terminal.

## Overview

`vnstock-cli` wraps the vnstock Python library in a clean, interactive CLI built with [Typer](https://typer.tiangolo.com/) and [Rich](https://github.com/Textualize/rich). Instead of writing Python scripts to fetch stock quotes, financial reports, or market data, you run a single command and get a beautifully formatted table or chart right in your terminal.

## Tech Stack

| Layer | Library | Role |
|-------|---------|------|
| Data | [vnstock](https://github.com/thinh-vu/vnstock) | Vietnamese stock market data source |
| CLI framework | [Typer](https://typer.tiangolo.com/) | Command parsing, help generation, type safety |
| Terminal UI | [Rich](https://github.com/Textualize/rich) | Tables, progress bars, color output |

## Planned Features

- **Stock quotes** — real-time and historical price data for any ticker
- **Financial statements** — income statement, balance sheet, cash flow
- **Market overview** — market indices, top movers, sector performance
- **Watchlist** — save and monitor a personal list of tickers
- **MCP server** — expose vnstock data as an [MCP](https://modelcontextprotocol.io/) resource so AI assistants can query it
- **AI integration** — natural language interface to query stock data (e.g. "show me FPT's revenue trend over the last 3 years")

## Getting Started

```bash
# Clone the repo
git clone https://github.com/chantroimoi1002/vnstock-cli.git
cd vnstock-cli

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the CLI
python main.py --help
```

## Usage

```
Usage: vnstock [OPTIONS] COMMAND [ARGS]...

  Vietnamese stock market data in your terminal.

Options:
  --help  Show this message and exit.

Commands:
  quote    Get current price and basic info for a ticker
  history  Fetch historical OHLCV data
  finance  View financial statements
  market   Market overview and indices
```

## Project Status

Early development. Core CLI structure is being built out.

## License

MIT
