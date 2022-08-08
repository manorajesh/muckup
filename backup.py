import click
import os
import shutil

@click.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path())
@click.option('-d', '--dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-n', '--name', default='backup', help='Name of the backup')
@click.option('-t', '--timestamp', is_flag=True, default=True, help='Add timestamp to name')
@click.option('-H', 'deref_sym', is_flag=True, default=False, help='Dereference symlinks')
@click.help_option('-h', '--help')

def backup(source, destination, dry_run, name, timestamp, deref_sym):
    """Backup SOURCE to DESTINATION"""
    click.echo('Backing up "%s" to "%s"' % (source, destination))

    if timestamp:
        name = '%s-%s' % (name, click.format_filename(click.format_datetime()))
        destination = os.path.join(destination, name)
        click.echo('Creating backup: "%s"' % name)
    
    if not dry_run:
        shutil.copytree(source, destination, symlinks=not deref_sym, ignore_dangling_symlinks=True)
        click.echo('Backup created at "%s"' % destination)
        click.echo('Symbolic links are %s' % ('dereferenced' if deref_sym else 'preserved'))

if __name__ == '__main__':
    try:
        backup()
    except Exception as e:
        click.echo('Error: %s\nExiting' % e)
        exit()