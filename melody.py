from random import randint, sample

from rich.console import Console
from rich.table import Table

melody = Table(title="MELODY")

melody.add_column("degree", justify="left", style="magenta", no_wrap=True)

for degree in sample(["1", "3", "4", "5", "7"], randint(2, 5)):
    melody.add_row(degree)

console = Console()
console.print(melody)
