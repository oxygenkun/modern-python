import textwrap
import locale

import click
import requests

from . import __version__

LAN = locale.getlocale()[0].split("_")[0]

def api_utl(api_lan: str = "en") -> str:
    return f"https://{api_lan}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.option('-l', '--language', default=LAN, help='Language of the app')
@click.version_option(version=__version__)
def main(language):
    """The hypermodern Python project."""
    try:
        with requests.get(api_utl(language)) as response:
            response.raise_for_status()
            data = response.json()
        title = data["title"]
        extract = data["extract"]
        click.secho(title, fg="green")
        click.echo(textwrap.fill(extract))
    except requests.RequestException:
        click.secho("API is not reachable", fg="red")
