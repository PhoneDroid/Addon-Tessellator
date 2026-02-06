# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Tessellator project.

from .Task import BoxTaskPanel
from .Misc import asIcon

from FreeCAD import Gui


class Command:

    def GetResources ( self ):
        return {
            'MenuText' : 'Command' ,
            'ToolTip' : 'Logs a debug message.' ,
            'Pixmap' : asIcon('Logo')
        }

    def Activated ( self ):

        print('Command::Activated')

        panel = BoxTaskPanel()

        Gui.Control.showDialog(panel)
