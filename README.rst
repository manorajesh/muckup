muckup
******

A simple backup utility built with Python and
`Click <https://click.palletsprojects.com/en/8.1.x/>`__.

Installation
------------

| ``pip install muckup``

| or

| ``git clone https://github.com/manorajesh/pyty.git``
| ``pip install -r requirements.txt``
| ``bin/muckup``

Usage
-----

| ``muckup [-dntHi] SOURCE DESTINATION``
 
| Simply type in the source path (can be relative) and destination path (can also be relative). The script will copy everything in the source (or the entire file) and copy it to the destination with the default name (``backup-%Y-%m-%d_%H:%M:%S``).

| Note: when copying one file, the extension will **not** be preserved.

Command Option Help
~~~~~~~~~~~~~~~~~~~

| ``-d, --dry-run``: Run the command without actually copying or pasting files (use for testing purposes)
| ``-n, --name TEXT``: Change the default name from ``backup`` to any string 
| ``-t, --timestamp``: Remove timestamp from the name
| ``-H``: Dereference symbolic links (i.e. copy files and/or folders pointed to by symbolic links)
| ``-i``: Request a ``(y/n)`` confirmation before preforming backup command (WIP) 
| ``-g TEXT``: Change timestamp format using the `time.strftime directives <https://docs.python.org/3/library/time.html#time.strftime>`__.
| ``-h, --help``: Show this message in shorter form.

.. raw:: html

   <hr>

.. _contents-of-requirementstxt:

Contents of requirements.txt
''''''''''''''''''''''''''''

``click==8.1.3``
