import argparse

def add_subparsers(subparsers):
  optimizers_group = subparsers.add_parser('optimizers')
  optimizers_subparser = optimizers_group.add_subparsers(dest='subcommand')
  optimizers_subparser.required = True

  # list

  list_subparser = optimizers_subparser.add_parser('list')

  # add

  add_subparser = optimizers_subparser.add_parser('add')

  add_subparser.add_argument(
    'name',
    default=None
    )

  # remove

  remove_subparser = optimizers_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name',
    default=None
    )