# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Tessellator project.

import freecad.Tessellator as module
from importlib.resources import as_file , files


resources = files(module) / 'Resources'

interfaces = resources / 'Interfaces'
icons = resources / 'Icons'


Paths = {
    'Save' : str( resources / 'Save.json' )
}


def asIcon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with as_file(icon) as path:
        return str( path )


def asInterface ( name : str ):

    file = name + '.ui'

    interface = interfaces / file

    with as_file(interface) as path:
        return str( path )