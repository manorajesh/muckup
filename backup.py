from unittest import defaultTestLoader
import click
import os
import shutil

@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path())
@click.option('-d', '--dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-n', '--name', default='backup', help='Name of the backup')
@click.option('-t', '--timestamp', is_flag=True, default=True, help='Add timestamp to name')
@click.option('-H', is_flag=True, default=False, help='Dereference symlinks')

def backup(source, destination, dry_run, name, timestamp):
    click.echo('Backing up "%s" to "%s"' % (source, destination))
    if dry_run:
        click.echo('Dry run, nothing will be copied')
    if timestamp:
        name = '%s-%s' % (name, click.format_filename(click.format_datetime()))
        destination = os.path.join(destination, name)