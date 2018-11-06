import argparse

def add_subparsers(subparsers):
  init_subparser = subparsers.add_parser('train')

  init_subparser.add_argument(
    'model',
    help='The name of the model to train.'
    )

  init_subparser.add_argument(
    'optimizer',
    help='The name of the optimizer to use for training.'
    )

  init_subparser.add_argument(
    'module',
    nargs='?',
    help='The TF Hub module to use with the model.'
    )