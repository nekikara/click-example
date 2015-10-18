import click

@click.command()
@click.option('--pos', nargs=2, type=float)
def cli(pos):
    click.echo('%s / %s' % pos)

