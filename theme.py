import logging
import pathlib
import shutil

from turberfield.punchline.theme import Theme
from turberfield.punchline.widget import Widget


class Inimitable(Theme):

    @property
    def widgets(self):
        return Widget.register(
            Widget(self.parent_package, "css", "fonts", optional=False),
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(*self.widgets, sep="\n")
        for w in self.widgets:
            if w.config in self.cfg:
                for resource in w.resources:
                    path = pathlib.Path(__file__).parent.joinpath(resource).resolve()
                    try:
                        shutil.copytree(path, self.output.joinpath(resource), dirs_exist_ok=True)
                    except FileNotFoundError as e:
                        logging.error(e)

