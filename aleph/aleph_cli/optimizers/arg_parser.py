import argparse
import inspect
import os

def add_subparsers(subparsers):
  optimizers_group = subparsers.add_parser('optimizers')
  optimizers_subparser = optimizers_group.add_subparsers(dest='subcommand')
  optimizers_subparser.required = True

  # list

  list_subparser = optimizers_subparser.add_parser('list')

  # add

  add_subparser = optimizers_subparser.add_parser('add')

  add_subparser.add_argument(
    'name'
    )

  add_subparser.add_argument(
    'type',
    nargs='?',
    choices=available_optimizers()
    )

  # remove

  remove_subparser = optimizers_subparser.add_parser('remove')

  remove_subparser.add_argument(
    'name'
    )

# Utilities

# TODO: move all path stuff to aleph_filesystem?

# package paths

def templates_path():
  import aleph.aleph_cli.optimizers.templates
  return os.path.dirname(inspect.getfile(aleph.aleph_cli.optimizers.templates))

def available_optimizers():
  optimizers_dir = templates_path()
  optimizers_list = os.listdir(optimizers_dir)
  return [os.path.splitext( os.path.splitext( f )[0] )[0] for f in optimizers_list if os.path.isfile(os.path.join(optimizers_dir,f)) and os.path.splitext(f)[1] == '.jinja2']