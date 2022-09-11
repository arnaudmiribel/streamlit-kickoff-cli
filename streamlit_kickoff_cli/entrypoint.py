import webbrowser
from typing import List

import click

from .dev import command as dev_command
from .kick import command as kick_command
from .kill import command as kill_command
from .list import command as list_command
from .new import command as new_command

AVAILABLE_COMMANDS: List[click.Command] = [
    new_command.new,
    dev_command.dev,
    kick_command.kick,
    list_command.list,
    kill_command.kill,
]

def set_context_object(
    ctx: click.Context,
) -> click.Context:
    """Get useful environment information and store it.
    Throw exception if environment is not supported

    Args:
        ctx (click.Context): Current context

    Raises:
        e: Exception when environment is not supported

    Returns:
        click.Context: Updated context
    """
    try:
        ctx.ensure_object(dict)
        ctx.obj["BROWSER"] = webbrowser.get()
    except Exception as e:
        raise e
    return ctx

# Subclassing Click CLI to display commands in a specific order
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx: click.Context):
        return self.commands.keys()


@click.group(cls=NaturalOrderGroup)
@click.pass_context
def stk(ctx: click.Context,):
    """Welcome to stk 👞

    This is a simple CLI to help you kick off and
    maintain Streamlit projects as fast as possible!
    """

    ctx = set_context_object(ctx)

def add_commands_to_stk():
    for command in AVAILABLE_COMMANDS:
        stk.add_command(command)

add_commands_to_stk()

if __name__ == '__main__':
    stk()
