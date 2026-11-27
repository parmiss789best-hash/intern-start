from rich.console import Console
from rich.panel import Panel
from rich.table import Table


def main():
    console = Console()

    weather = Table(show_header=False, box=None)
    weather.add_column("Information", style="cyan")
    weather.add_column("Value", style="bold white")

    weather.add_row("City", "Tehran")
    weather.add_row("Temperature", "18°C")
    weather.add_row("Condition", "Partly Cloudy")
    weather.add_row("Humidity", "45%")
    weather.add_row("Wind Speed", "12 km/h")

    card = Panel(
        weather,
        title="[bold yellow]WEATHER REPORT[/bold yellow]",
        subtitle="[dim]Sample Weather Data[/dim]",
        border_style="bright_blue",
        padding=(1, 3),
    )

    console.print(card)


if __name__ == "__main__":
    main()
