import click


def header():
    click.echo(
        click.style(
            "\n\nWelcome to streamlit-kickoff-cli (stk) 👞\n\n",
            fg="red",
            bold=True,
        ),
        nl=True,
    )


def choice(text: str):
    click.echo(
        click.style(f"\n{text}", bold=True),
        nl=True,
    )


def new_step(text: str):
    click.echo(click.style(f"➕ {text}", bold=False), nl=True)


def warning(text: str):
    click.echo(click.style(f"\n⚠️ {text}", fg="red", bold=True), nl=True)


def error(text: str):
    click.echo(click.style(f"\n💀 {text}", fg="red", bold=True), nl=True)


def success(text: str):
    click.echo(click.style(f"\n🎉 {text}\n", bold=True), nl=True)
