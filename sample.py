import time
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import print as rprint
from rich.text import Text
from rich.align import Align

app = typer.Typer()
console = Console()


@app.command()
def welcome(name: str = typer.Argument("Investor")):
    # Header banner
    console.print()
    console.print(
        Panel.fit(
            Align.center(
                Text.assemble(
                    ("  vnstock", "bold cyan"),
                    ("-", "white"),
                    ("cli  ", "bold green"),
                    ("\nVietnamese Stock Market • Terminal Edition", "dim white"),
                )
            ),
            border_style="cyan",
            padding=(1, 4),
        )
    )

    # Greeting
    console.print()
    rprint(f"  [bold white]Welcome back,[/bold white] [bold yellow]{name}[/bold yellow] [green]— glad to have you.[/green]")
    console.print()

    # Fake loading sequence
    with Progress(
        SpinnerColumn(spinner_name="dots", style="cyan"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=30, style="cyan", complete_style="green"),
        TextColumn("[green]{task.percentage:>3.0f}%"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Connecting to market data...", total=100)
        for _ in range(100):
            time.sleep(0.01)
            progress.advance(task, 1)

    # Market snapshot table
    table = Table(
        title="Market Snapshot",
        title_style="bold cyan",
        border_style="bright_black",
        header_style="bold white",
        show_lines=True,
    )

    table.add_column("Ticker", style="bold yellow", justify="center")
    table.add_column("Price", justify="right")
    table.add_column("Change", justify="right")
    table.add_column("Volume", justify="right", style="dim")
    table.add_column("Signal", justify="center")

    rows = [
        ("FPT", "125,400", "+2.3%", "4.2M", "[bold green]BUY[/bold green]"),
        ("VNM", "78,200",  "-0.8%", "1.8M", "[bold red]SELL[/bold red]"),
        ("HPG", "26,500",  "+1.1%", "9.1M", "[bold green]BUY[/bold green]"),
        ("MWG", "43,900",  "+0.0%", "2.5M", "[bold yellow]HOLD[/bold yellow]"),
        ("VIC", "38,700",  "-1.4%", "3.3M", "[bold red]SELL[/bold red]"),
    ]

    for ticker, price, change, volume, signal in rows:
        change_style = "green" if "+" in change else "red" if "-" in change else "white"
        table.add_row(ticker, price, f"[{change_style}]{change}[/{change_style}]", volume, signal)

    console.print(table)

    # Footer hint
    console.print()
    rprint("  [dim]Run [bold white]vnstock --help[/bold white] to explore all commands.[/dim]")
    console.print()


if __name__ == "__main__":
    app()
