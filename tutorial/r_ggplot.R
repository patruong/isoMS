rm(list=ls())
library(tidyverse)
library("ggplot2")

df <- read.csv("TEST.csv", sep = ";", header = TRUE)

ggplot(df, aes(fill = category, color = category)) +
  
  # 2D box defined by the Q1 & Q3 values in each dimension, with outline
  geom_rect(aes(xmin = x_lower, xmax = x_upper, ymin = y_lower, ymax = y_upper), alpha = 0.3) +
  geom_rect(aes(xmin = x_lower, xmax = x_upper, ymin = y_lower, ymax = y_upper), 
            color = "black", fill = NA) +
  
  # whiskers for x-axis dimension with ends
  geom_segment(aes(x = x_min, y = y_middle, xend = x_max, yend = y_middle)) + #whiskers
  geom_segment(aes(x = x_min, y = y_lower, xend = x_min, yend = y_upper)) + #lower end
  geom_segment(aes(x = x_max, y = y_lower, xend = x_max, yend = y_upper)) + #upper end
  
  # whiskers for y-axis dimension with ends
  geom_segment(aes(x = x_middle, y = y_min, xend = x_middle, yend = y_max)) + #whiskers
  geom_segment(aes(x = x_lower, y = y_min, xend = x_upper, yend = y_min)) + #lower end
  geom_segment(aes(x = x_lower, y = y_max, xend = x_upper, yend = y_max)) + #upper end
  
  # outliers
  #geom_point(data = df.outliers, aes(x = x.outliers, y = y.middle), size = 3, shape = 1) + # x-direction
  #geom_point(data = df.outliers, aes(x = x.middle, y = y.outliers), size = 3, shape = 1) + # y-direction
  
  xlab("Sepal.Length") + ylab("Sepal.Width") +
  coord_cartesian(xlim = c(4, 8), ylim = c(2, 4.5)) +
  theme_classic()
