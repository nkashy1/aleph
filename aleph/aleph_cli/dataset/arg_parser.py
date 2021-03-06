import argparse

def add_subparsers(subparsers):
  dataset_group = subparsers.add_parser('dataset')
  dataset_subparser = dataset_group.add_subparsers(dest='subcommand')
  dataset_subparser.required = True

  # list

  list_subparser = dataset_subparser.add_parser('list')

  # add

  add_subparser = dataset_subparser.add_parser('add')

  add_subparser.add_argument(
    'name',
    default=None
    )

  add_subparser.add_argument(
    'url',
    default=None
    )

  # remove

  remove_subparser = dataset_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name',
    nargs='?',
    default=None
    )