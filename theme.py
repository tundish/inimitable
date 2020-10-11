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
            "inimitable-data-coins": "12",
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
                    path = pathlib.Path(__file__).parent.joinpath(resource).resolve()
                    try:
                        shutil.copytree(path, self.output.joinpath(resource), dirs_exist_ok=True)
                    except FileNotFoundError as e:
                        with importlib.resources.path(w.package, resource) as path:
                            shutil.copytree(path, self.output.joinpath(resource), dirs_exist_ok=True)

