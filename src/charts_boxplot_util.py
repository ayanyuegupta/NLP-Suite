import sys
import GUI_util
import IO_libraries_util

if IO_libraries_util.install_all_Python_packages(GUI_util.window, "charts_boxplot_util",
                                          ['pandas', 'plotly']) == False:
    sys.exit(0)

import pandas as pd
import plotly.express as px

#var is the variable of choice to apply the boxplot on
#bycategory is a boolean that chooses whether we want to split it by category along a categorical variable, determined by the following category argument
#points is the choice to represent all points of data, the outliers, or none of them, it should be given through a dropdown menu
#color is another choice of categorical variable to split the data along
def boxplot(data,outputFilename,var,points=None,bycategory=None,category=None,color=None):
    if type(data)==str:
        data=pd.read_csv(data)
    if bycategory==False:
        fig=px.box(data,y=var,points=points,color=color)
    else:
        fig=px.box(data,x=category,y=var,points=points,color=color)
    fig.write_html(outputFilename)
    return outputFilename
