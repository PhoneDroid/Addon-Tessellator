# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileNotice: Part of the Tessellator project.

from .Manipulator import Manipulator
from .Command import Command

from FreeCAD import Gui


def integrate ():

    Gui.addCommand('Tessellator_Task',Command())

    Gui.addWorkbenchManipulator(Manipulator())
