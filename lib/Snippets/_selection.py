# -*- coding: uft8 -*-

# IMPORTS
from Autodesk.Revit.DB import *

#Variables
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

#Functions
def get_selected_elements(uidoc):
    """This function will return elements that are currently selected in Revit UI
    :param uidoc:   uidoc where elements are selected
    :return:        List of selected elements"""
    selected_elements = []

    for elem_id in uidoc.Selection.GetElementsIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)

    return selected_elements