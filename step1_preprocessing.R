# Preprocessing

### LOAD LIBRARIES - install with:
install.packages(c("kohonen", "dummies", "ggplot2", "maptools", "sp", "reshape2", "rgeos"))
install.packages("dplyr")
install.packages(c("mosaic", "vcd"))
library(kohonen)
#library(dummies)
library(ggplot2)
library(sp)
library(maptools)
library(reshape2)
library(rgeos)
library(dplyr)
library(mosaic)
library(vcd)

# Colour palette definition
pretty_palette <- c("#1f77b4", '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2')

### DATA PREPARATION

# Census data comes in counts of people per area. 
# To compare areas, we will convert a number of the
# stats collected into percentages. Without this, 
# the primary differentiator between the different 
# areas would be population size.

# Load the data into a data frame
# Get the map of these areas and filter for Dublin areas.
setwd("C:/Users/Anpanchiman/Downloads/INFO411/a1/a1_support_files")
data <- read.csv("./creditworthiness.csv")  #idcol="functionary"
df_asd = data%>%filter(credit.rating !=0)

#names(data_raw)[1] <- "functionary"
corr_matrix = cor(data)
melted_corr = melt(corr_matrix)
ggplot(data = melted_corr, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile()

colnames(df_asd)
avg_acc_balance = data[, grepl("avrg..account", names(data))]

oneMontHist = subset(df_asd, select=c("avrg..account.balance.1.months.ago", "min..account.balance.1.months.ago"))

credit_hist = subset(df_asd, select=c("credit.refused.in.past.", "credit.rating"))
mosaic(table(credit_hist), shade=TRUE)


employment = subset(df_asd, select=c("self.employed.", "credit.rating"))
mosaic(table(employment), shade=TRUE)


#mosaic plot shows a large population of credit rating 2 for ppl who are not self employed
