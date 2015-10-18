import click

@click.command()
@click.option('--message', '-m', multiple=True)
def cli(message):
    click.echo('\n'.join(message))

