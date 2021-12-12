from setuptools import setup
setup(
    name='ShellPy',
    version='1.0',
    author='Raj Chowdhury',
    description='A Tiny Python Tool for generating reverse shells easily and automating the boring stuff like '
                'URL encoding the command and setting up a listener.',
    install_requires=['pyperclip', 'colorama', 'readchar', 'netifaces']
)

