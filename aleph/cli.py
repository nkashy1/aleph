#!/usr/bin/env python

import argparse

from termcolor import cprint

import aleph.aleph_cli.init.arg_parser
import aleph.aleph_cli.dataset.arg_parser
import aleph.aleph_cli.activate.arg_parser
import aleph.aleph_cli.features.arg_parser

import aleph.aleph_cli.init.generator
import aleph.aleph_cli.dataset.generator
import aleph.aleph_cli.activate.generator
import aleph.aleph_cli.features.generator

from aleph.aleph_cli.utils.generator_exception import GeneratorException

def generate_arg_parser():
  parser = argparse.ArgumentParser(description='...')
  
  subparsers = parser.add_subparsers(dest='command')
  subparsers.required = True

  aleph.aleph_cli.init.arg_parser.add_subparsers(subparsers)
  aleph.aleph_cli.dataset.arg_parser.add_subparsers(subparsers)
  aleph.aleph_cli.activate.arg_parser.add_subparsers(subparsers)
  aleph.aleph_cli.features.arg_parser.add_subparsers(subparsers)

  return parser


def main():
  parser = generate_arg_parser()
  args = parser.parse_args()

  try:
    if args.command == 'init':
      aleph.aleph_cli.init.generator.run(args)
    if args.command == 'dataset':
      aleph.aleph_cli.dataset.generator.run(args)
    if args.command == 'feature':
      aleph.aleph_cli.features.generator.run(args)
    if args.command == 'activate':
      aleph.aleph_cli.activate.generator.run(args)
    if args.command == 'deactivate':
      aleph.aleph_cli.activate.generator.run(args)
  except GeneratorException as error:
    cprint(error, 'red')