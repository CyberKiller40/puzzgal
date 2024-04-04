#!/usr/bin/env python3

app_version = '0.0.1'
"""
PuzzGal - a static jigsaw puzzle gallery creator
Copyright (C) 2024 Łukasz 'CyberKiller' Korpalski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import pathlib
import logging
logger = logging.getLogger(__name__)

class PuzzGal:
  def __init__(self, path):
    self.path = path
    logger.info(self.path)

  def read_config(self):
    raise NotImplementedError()

  def gen_minis(self):
    raise NotImplementedError()

  def gen_html(self):
    raise NotImplementedError()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='PuzzGal - a static jigsaw puzzle gallery creator', epilog='Project website: https://github.com/CyberKiller40/puzzgal')
  parser.add_argument('path', nargs=1, type=pathlib.Path, help='path to a directory with puzzle photos')
  parser.add_argument('-v', '--version', action='version', version=app_version)
  parser.add_argument('-l', '--loglevel', dest='loglevel', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO', help='logging level, defaults to INFO')
  parser.add_argument('--no-logfile', dest='nologfile', action='store_true', help='set to ommit creating a log file and output messages to the terminal')
  args = parser.parse_args()

  logformat='%(asctime)s %(levelname)s: %(message)s'
  if args.nologfile == True:
    logging.basicConfig(format=logformat)
  else:
    try:
      logging.basicConfig(filename=args.path[0]/'puzzgal.log', format=logformat)
    except FileNotFoundError:
      logging.basicConfig(format=logformat)
      logging.warning("Path invalid, logging to terminal.")
  if args.loglevel == 'ERROR':
    logger.setLevel(logging.ERROR)
  elif args.loglevel == 'WARNING':
    logger.setLevel(logging.WARNING)
  elif args.loglevel == 'INFO':
    logger.setLevel(logging.INFO)
  elif args.loglevel == 'DEBUG':
    logger.setLevel(logging.DEBUG)
  else:
    logger.setLevel(logging.INFO)

  app = PuzzGal(args.path[0])
  logging.shutdown()
