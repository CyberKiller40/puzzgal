#!/usr/bin/env python3

class PuzzGal:
  def __init__(self, path):
    self.path = path

  def read_config(self):
    raise NotImplementedError()

  def gen_minis(self):
    raise NotImplementedError()

  def gen_html(self):
    raise NotImplementedError()

if __name__ == "__main__":
  path = ""
  app = PuzzGal(path)
