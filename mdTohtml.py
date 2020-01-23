import easygui
import markdown
# import md-to-html
filename = print(easygui.fileopenbox())
# md-to-html --input filename --output temp.html
markdown filename > output.html