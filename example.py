import click

@click.command()
@click.option('--item', nargs=2, type=click.Tuple([str, int]))
def cli(item):
    click.echo('name=%s id=%d' % item)

