__title__ = "Hello BIM World!"
__author__ = "User3"
__doc__ = """This is the button to go to hell"""

#Variables
uidoc = __revit__.ActiveUIDocument

#custom import
from Snippets._selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))