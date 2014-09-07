#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

from tornado.ioloop import IOLoop

import dungeon

parser = argparse.ArgumentParser(description='Start the main roygbivs server.')
parser.add_argument("--environment", "-e", default="development",
                    help='development, production, or testing')
args = parser.parse_args()

environment = dungeon.DungeonApplication.get_environment(args.environment)

print(" 🚀  starting in {0} mode.".format(
    dungeon.DungeonApplication.environment_as_string(environment)))

application = dungeon.make_application(environment)
port = int(os.environ.get("PORT", 5000))
application.listen(port)
IOLoop.instance().start()
