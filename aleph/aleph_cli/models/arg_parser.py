import argparse

def add_subparsers(subparsers):
  models_group = subparsers.add_parser('models')
  models_subparser = models_group.add_subparsers(dest='subcommand')
  models_subparser.required = True

  # list

  list_subparser = models_subparser.add_parser('list')

  # add

  add_subparser = models_subparser.add_parser('add')

  add_subparser.add_argument(
    'name',
    default=None
    )
  

  # remove

  remove_subparser = models_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name',
    default=None
    )