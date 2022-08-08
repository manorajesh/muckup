import os

os.makedirs('tests/source_test')
os.chdir('tests/source_test')
os.makedirs('dir1')
os.makedirs('dir2')

with open('file1', 'w') as f:
    f.write('buttcheeks' * 100)