import click

@click.command()
@click.option('-v', '--verbose', count=True)
def cli(verbose):
    click.echo("Verbosity: %s" % verbose)

