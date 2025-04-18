from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(f"👋 Hi, I'm [link=https://github.com/dfabianus]Fabi[/]", guide_style="bold bright_black")

current_projects_tree = tree.add("🛠️ Current Projects", guide_style="bright_black")
current_projects_tree.add(f"[bold link=https://github.com/dfabianus/dotfiles]dotfiles[/] - [bright_black]My dotfiles for my linux setup.")
#current_projects_tree.add(f"[bold link=https://github.com/dfabianus/project2]Project 2[/] - [bright_black]Details about project 2.")
# Add more current projects

planned_projects_tree = tree.add("🔭 Planned Projects", guide_style="bright_black")
planned_projects_tree.add("[bold]Project A Idea[/] - [bright_black]My vision for project A and planned technologies.")
#planned_projects_tree.add("[bold]Concept B[/] - [bright_black]Initial thoughts on concept B.")
# Add more planned projects

# You can add more sections like "Skills", "Contact", etc.

console.print(tree)
console.print("")
console.print("[green]Find more on my GitHub: [bold link=https://github.com/dfabianus]github.com/dfabianus[/]")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)