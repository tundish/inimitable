:author:    D Haynes
:made_at:   2020-10-12
:nodes:     {0:02d}

..  In this repo the top-level index page is a soft link to the real one within.
    I did this in Linux (ln -rs docs/index.html index.html).

    The index page presents a challenge. It is replicated at different levels
    of the site, and so all links must have absolute URLs.

    It would be nice to use a variable substitution from the Settings object
    to achieve this, but it's not possible in reST to modify a hyperlink reference
    with a substitution reference. Hence the hard coding.

.. entity:: SETTINGS
   :types: turberfield.punchline.types.Settings


Index
=====

0
-

.. property:: SETTINGS.punchline-states-refresh none

This is a short work for the `Philosophy Game Jam`_.

The day is `Monday <https://tundish.github.io/inimitable/monday/00.html>`_.

1
-

This is a short work for the `Philosophy Game Jam`_.

The day is `Tuesday <https://tundish.github.io/inimitable/tuesday/00.html>`_.

2
-

This is a short work for the `Philosophy Game Jam`_.

The day is `Wednesday <https://tundish.github.io/inimitable/wednesday/00.html>`_.

3
-

This is a short work for the `Philosophy Game Jam`_.

The day is `Thursday <https://tundish.github.io/inimitable/thursday/00.html>`_.

.. _Philosophy Game Jam: https://itch.io/jam/philosophy-game-jam-3
