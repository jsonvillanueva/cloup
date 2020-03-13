import click

import cloup
from cloup import option, option_group


@cloup.command('clouptest', align_option_groups=True)
@option_group('Option group A',
    option('-o', '--one', help='1st option of group A'),
    option('--two', help='2nd option of group A'),
    option('--three', help='3rd option of group A'),
    help='This is a very useful description of group A'
)
@option_group('Option group B',
    option('--four / --no-four', help='1st option of group B'),
    option('--five', help='2nd option of group B'),
    option('--six', help='3rd option of group B')
)
@option('--seven', help='first uncategorized option',
    type=click.Choice('yes no ask'.split()))
@option('--height', help='second uncategorized option')
def example_cli(**kwargs):
    """ A CLI that does nothing. """
    print(kwargs)


if __name__ == '__main__':
    example_cli('--help'.split())
