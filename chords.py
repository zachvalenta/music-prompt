from random import randint, sample

from rich.console import Console
from rich.table import Table

changes = Table(title="CHANGES")

changes.add_column("chord", justify="left", style="cyan", no_wrap=True)

for chord in sample(["I", "ii", "iii", "IV", "V", "vi", "vii°"], randint(2, 4)):
    changes.add_row(chord)

console = Console()
console.print(changes)
