import click

@click.command()
@click.option('--n', default=1)
def cli(n):
    """Example, script."""
    click.echo('.' * n)

