import locale
import textwrap

import click

from . import __version__, wikipedia

LAN = locale.getlocale()[0].split("_")[0]


@click.command()
@click.option(
    "-l",
    "--language",
    default=LAN,
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language):
    """The hypermodern Python project."""
    data = wikipedia.random_page(language=language)
    title = data["title"]
    extract = data["extract"]
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
