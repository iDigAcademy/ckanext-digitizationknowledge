import click


@click.group(short_help="digitizationknowledge CLI.")
def digitizationknowledge():
    """digitizationknowledge CLI.
    """
    pass


@digitizationknowledge.command()
@click.argument("name", default="digitizationknowledge")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [digitizationknowledge]
