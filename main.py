import yahooquery as yq
import pandas as pd
from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run()


# add a section to simply enter the ticker
#Collect 10 years of data, put into nice table so we can compare
# Add an option to use matplot do graph the last 10 years
# tooltips to elaborate on what each section means -> red and green flags 