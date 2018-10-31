import argparse

def add_subparsers(subparsers):
  init_subparser = subparsers.add_parser('init')

  init_subparser.add_argument(
    'name',
    nargs='?',
    default=None
    )