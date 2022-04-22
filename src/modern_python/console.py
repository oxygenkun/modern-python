import textwrap
import locale

import click
import requests

from . import __version__, wikipedia

LAN = locale.getlocale()[0].split("_")[0]


@click.command()
@click.option('-l', '--language', default=LAN, help='Language of the app')
@click.version_option(version=__version__)
def main(language):
    """The hypermodern Python project."""
    try:
        data = wikipedia.random_page(language)
        title = data["title"]
        extract = data["extract"]
        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract))
    except requests.RequestException:
        click.secho("API is not reachable", fg="red")
