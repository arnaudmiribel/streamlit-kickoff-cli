import os

import click
from custom_logging import choice
from dev.command import _dev
from new.command import _new


@click.command()
@click.pass_context
def kick(ctx: click.Context,):
    """🚀 New app + dev set up NOW!"""

    choice("🚀 New app + dev set up NOW!")

    directory_name = _new(ctx)
    if directory_name:
        os.chdir(directory_name)
        _dev(ctx)
