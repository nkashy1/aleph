import argparse

def add_subparsers(subparsers):
  subparsers.add_parser('activate')
  subparsers.add_parser('deactivate')

  