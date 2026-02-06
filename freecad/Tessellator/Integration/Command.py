# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Tessellator project.

from ..Task import BoxTaskPanel
from ..Misc import asIcon

from FreeCAD import Gui


class Command:

    def GetResources ( self ):
        return {
            'MenuText' : 'Tesselate' ,
            'ToolTip' : 'Fill area with masonry patterns.' ,
            'Pixmap' : asIcon('Logo')
        }

    def Activated ( self ):

        panel = BoxTaskPanel()

        Gui.Control.showDialog(panel)
