import argparse

def add_subparsers(subparsers):
  features_group = subparsers.add_parser('features')
  features_subparser = features_group.add_subparsers(dest='subcommand')
  features_subparser.required = True

  # list

  list_subparser = features_subparser.add_parser('list')

  # add

  add_subparser = features_subparser.add_parser('add')

  add_subparser.add_argument(
    'name',
    default=None
    )

  add_subparser.add_argument(
    'type',
    default=None
    )
  
  add_subparser.add_argument(
    'shape',
    default=None
    )

  # remove

  remove_subparser = features_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name',
    default=None
    )