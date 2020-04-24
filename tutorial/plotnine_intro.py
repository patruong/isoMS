#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:13:19 2020

@author: ptruong

Tutorial script for: https://www.pythoncharts.com/2019/04/11/intro-to-plotnine/

"""

import pandas as pd
import numpy as np
from io import StringIO
from tabulate import tabulate

##############################################
# https://plotnine.readthedocs.io/en/stable/ #
##############################################

from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))

###########################


# Load plotnine.
from plotnine import *

# Import vega datasets and load iris dataset.
from vega_datasets import data

df = data.iris()

# Create a simple scatter plot.
# Note, the parens wrapping the statement allow you to use `+` at the end of the line
# without escaping with a backslash.
(ggplot(df, aes('petalWidth', 'petalLength')) +
  geom_point())

(ggplot(df, aes('petalWidth', 'petalLength')) +
  geom_point(color='darkgreen', size=4)
)

(ggplot(df, aes('petalWidth', 'petalLength', color='species')) +
  geom_point() +
  stat_smooth(method='lm')
)

####################################################################################
####### BOX PLOT IRIS - DOUBLE BOX PLOT                                          ###
####### https://stackoverflow.com/questions/46068074/double-box-plots-in-ggplot2 ###
####################################################################################
(ggplot(df, aes('species', 'sepalLength', color='species')) +
  geom_boxplot() 
)

(ggplot(df, aes('species', 'sepalWidth', color='species')) +
  geom_boxplot() 
)

(ggplot(df, aes('petalWidth', 'petalLength', color='species')) +
  geom_point() +
  stat_smooth(method='lm')
)


(ggplot(df, aes('petalWidth', 'petalLength', color='species')) +
  geom_boxplot() 
)

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm'))


########################
# DOUBLE BOX PLOT IRIS #
########################

boxplot_cols = [
  "x_count", "x_mean", "x_std","x_min", "x_lower", "x_middle", "x_upper", "x_max",  
  "y_count", "y_mean", "y_std","y_min", "y_lower", "y_middle", "y_upper", "y_max",
  "category"
]

df_boxplot = pd.DataFrame(data = None, columns = boxplot_cols)
#df 

#var_x - sepalLength
#var_y - sepalWidth

# Beräkna boxplot värdena för x och y variabler.
category = "setosa"

for category in df["species"].unique():
    df_category = df[df["species"] == category]

    var_x = df_category["sepalLength"].describe()
    var_y = df_category["sepalWidth"].describe()
    data_boxplot = np.concatenate((var_x, var_y))
    data_boxplot = np.append(data_boxplot, category)
    
    df_boxplot_values = pd.DataFrame(data = [data_boxplot],
                                     columns = boxplot_cols)
    df_boxplot = df_boxplot.append(df_boxplot_values)

print(tabulate(df_boxplot, headers='keys', tablefmt='psql'))
#print(tabulate(df_boxplot.describe(), headers='keys', tablefmt='psql'))


# plot sample size (count as well?)

"""
# NOTE UNFINISHED CODE BELOW
(ggplot(df_boxplot, aes(fill = "category", color = "category"))+

  # 2D box defined by the Q1 & Q3 values in each dimension, with outline
  geom_rect(aes(xmin = "x_lower", xmax = "x_upper", ymin = "y_lower", ymax = "y_upper"), alpha = 0.3) +
  geom_rect(aes(xmin = "x_lower", xmax = "x_upper", ymin = "y_lower", ymax = "y_upper"), 
            color = "black", fill = None) +

  # whiskers for x-axis dimension with ends
  geom_segment(aes(x = "x_min", y = "y_middle", xend = "x_max", yend = "y_middle")) + #whiskers
  geom_segment(aes(x = "x_min", y = "y_lower", xend = "x_min", yend = "y_upper")) + #lower end
  geom_segment(aes(x = "x_max", y = "y_lower", xend = "x_max", yend = "y_upper")) + #upper end

  # whiskers for y-axis dimension with ends
  geom_segment(aes(x = "x_middle", y = "y_min", xend = "x_middle", yend = "y_max")) + #whiskers
  geom_segment(aes(x = "x_lower", y = "y_min", xend = "x_upper", yend = "y_min")) + #lower end
  geom_segment(aes(x = "x_lower", y = "y_max", xend = "x_upper", yend = "y_max")) + #upper end

  xlab("Sepal.Length") + ylab("Sepal.Width") +
  coord_cartesian(xlim = (0, 14), ylim = (0, 12)) +
  theme_classic()
)
"""

