#!/bin/env python
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2018
# Author: Amador Pahim <apahim@redhat.com>

from setuptools import setup, find_packages


VERSION = open("VERSION", "r").read().strip()

setup(name='avocado-framework-plugin-glib',
      description='Avocado Plugin for Execution of GLib Test Framework tests',
      version=VERSION,
      author='Avocado Developers',
      author_email='avocado-devel@redhat.com',
      url='http://avocado-framework.github.io/',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['avocado-framework==%s' % VERSION],
      entry_points={
          'avocado.plugins.cli': [
              'glib = avocado_glib:GLibCLI',
          ],
          'avocado.plugins.resolver': [
              'glib = avocado_glib:GLibResolver'
          ]}
      )
