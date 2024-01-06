#!/usr/bin/env python
import sys, os, argparse
from dorothy.parsers import *

from rich_argparse import RichHelpFormatter
from rich_argparse import RichHelpFormatter

RichHelpFormatter.styles["argparse.args"]     = "green"
RichHelpFormatter.styles["argparse.prog"]     = "bold grey50"
RichHelpFormatter.styles["argparse.groups"]   = "bold green"
RichHelpFormatter.styles["argparse.help"]     = "grey50"
RichHelpFormatter.styles["argparse.metavar"]  = "blue"

def run():

  parser   = argparse.ArgumentParser(formatter_class=RichHelpFormatter)
  commands = parser.add_subparsers(dest='mode')

  parsers = [
              dataset_parser(commands),
            ]

  if len(sys.argv)==1:
    print(parser.print_help())
    sys.exit(1)

  args = parser.parse_args()

  # Run!
  for p in parsers:
    p.parser(args)

if __name__ == "__main__":
  run()

















