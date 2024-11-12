"""Console script for {{cookiecutter.plugin_slug}}."""
import {{cookiecutter.plugin_slug}}

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for {{cookiecutter.plugin_slug}}."""
    console.print("Replace this message by putting your code into "
               "{{cookiecutter.plugin_slug}}.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
