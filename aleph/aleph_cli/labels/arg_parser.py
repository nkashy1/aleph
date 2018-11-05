import argparse

def add_subparsers(subparsers):
  labels_group = subparsers.add_parser('labels')
  labels_subparser = labels_group.add_subparsers(dest='subcommand')
  labels_subparser.required = True

  # list

  list_subparser = labels_subparser.add_parser('list')

  # add

  add_subparser = labels_subparser.add_parser('add')

  add_subparser.add_argument(
    'name'
    )

  add_subparser.add_argument(
    'type',
    choices=['image', 'float32', 'int64']
    )
  
  add_subparser.add_argument(
    'shape'
    )

  # remove

  remove_subparser = labels_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name',
    default=None
    )