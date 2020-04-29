rm(list=ls())
library(tidyverse)
library("ggplot2")
require(gridExtra)

df <- read.csv("TEST_ion.csv", sep = ";", header = TRUE)


double_box_plot <- function(df, title = "title", x_lab = "MS", y_lab = "MSMS") {
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
    
    xlab(x_lab) + ylab(y_lab) +
    ggtitle(title) +
    #coord_cartesian(xlim = c(0, 0.1), ylim = c(0, 0.1)) +
    theme_classic()
}

df1 <- read.csv("TEST_13C.csv", sep = ";", header = TRUE)
df2 <- read.csv("TEST_15N.csv", sep = ";", header = TRUE)
df3 <- read.csv("TEST_2H.csv", sep = ";", header = TRUE)
df4 <- read.csv("TEST_18O.csv", sep = ";", header = TRUE)

plot1 <- double_box_plot(df1, title = "12C/13C")
plot2 <- double_box_plot(df2, title = "14N/15N")
plot3 <- double_box_plot(df3, title = "1H/2H")
plot4 <- double_box_plot(df4, title = "16O/18O")

grid.arrange(plot1, plot2, plot3, plot4, ncol=2)

# THIS IS THE CODE FOR 4x4 plotting
plots <- list()

for (i in list.files()){
  splitted <- unlist(strsplit(i, "\\, |\\__|, |\\.| "))
  title <- splitted[1]
  x_lab <- splitted[2]
  y_lab <- splitted[3]
  df <- read.csv(i, sep = ";", header = TRUE)
  plots[[i]] <- double_box_plot(df, title = title, x_lab = x_lab, y_lab = y_lab)
}
#do.call(grid.arrange, plots)
#png(filename="MS_vs_MS.png")
do.call(grid.arrange, plots)

set.seed(154)
D <- data.frame(
  x1 = runif(100),
  x2 = rnorm(100)
)

library(ggplot2)
plots <- list()
for(nm in names(D)) {
  plots[[nm]] <- ggplot(data=D) + geom_density(aes_string(x=nm))
}

print(plots[["x1"]])
print(plots[["x2"]])
do.call(grid.arrange, plots)
                            