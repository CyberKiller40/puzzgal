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

class PuzzGal:
  def __init__(self, path):
    self.path = path
    print(self.path)

  def read_config(self):
    raise NotImplementedError()

  def gen_minis(self):
    raise NotImplementedError()

  def gen_html(self):
    raise NotImplementedError()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='PuzzGal - a static jigsaw puzzle gallery creator', epilog='Project website: https://github.com/CyberKiller40/puzzgal')
  parser.add_argument('path', nargs=1, help='path to a directory with puzzle photos')
  parser.add_argument('-v', '--version', action='version', version=app_version)
  args = parser.parse_args()

  app = PuzzGal(args.path[0])
