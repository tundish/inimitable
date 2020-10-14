#!/usr/bin/env python3
# encoding: utf-8

# This file is part of inimitable.
#
# Inimitable is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Inimitable is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with inimitable.  If not, see <http://www.gnu.org/licenses/>.


import importlib.resources
import logging
import pathlib
import shutil

from turberfield.punchline.theme import Theme
from turberfield.punchline.widget import Widget
from turberfield.punchline.widget import WebBadge


class Inimitable(Theme):

    @property
    def definitions(self):
        return {
            #"inimitable-data-coins": "12",
        }

    @property
    def widgets(self):
        return [
            Widget(self.parent_package, "css", "fonts", optional=False),
            WebBadge("turberfield.punchline", "assets", config="turberfield.punchline"),
        ]

    def __exit__(self, exc_type, exc_val, exc_tb):
        for w in self.widgets:
            if w.config in self.cfg:
                for resource in w.resources:
                    src = pathlib.Path(__file__).parent.joinpath(resource).resolve()
                    dst = self.output.joinpath(resource)
                    if src == dst: continue
                    try:
                        shutil.copytree(path, dst, dirs_exist_ok=True)
                    except FileNotFoundError as e:
                        with importlib.resources.path(w.package, resource) as src:
                            shutil.copytree(src, dst, dirs_exist_ok=True)

