# ------------------- PREPROCESSING ---------------------------

# LOAD LIBRARIES - install with:
# install.packages(c("kohonen", "dummies", "ggplot2", "maptools", "sp", "reshape2", "rgeos"))
library(kohonen)
#library(dummies)
library(ggplot2)
library(sp)
library(maptools)
library(reshape2)
library(rgeos)

# Color palette definition
pretty_palette <- c("#1f77b4", '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2')

# DATA PREPARATION
setwd("C:/Users/User/Desktop/SIM/INFO411/Assignment/a1/a1_support_files")
data <- read.csv("./creditworthiness.csv")

# Rows with 0 credit rating are rows that have not been assess, i will exclude those rows
# and find interesting data based on the subset of the data created (using subset() function)
classifiedData = subset(data, data[,46]>0)
# Use correlation method to find interesting attribute
corTable = abs(cor(classifiedData, y=classifiedData$credit.rating, method="spearman"))
# To identify which features have a higher correlation value, i arrange the correlation table in descending order
corTable = corTable[order(corTable, decreasing = TRUE),,drop = FALSE]
head(corTable,6)

data_plot <- data

data_plot$credit.rating <- factor(data$credit.rating, labels = c('NR', 'A', 'B', 'C'))
data_plot$functionary <- factor(data$functionary, labels = c('no', 'yes'))
data_plot$FI3O.credit.score <- factor(data$FI3O.credit.score, labels = c('not ok', 'ok'))
data_plot$re.balanced..paid.back..a.recently.overdrawn.current.acount <- factor(data$re.balanced..paid.back..a.recently.overdrawn.current.acount, labels = c('no', 'yes'))
data_plot$credit.refused.in.past. <- factor(data$credit.refused.in.past., labels = c('no', 'yes'))
data_plot$gender <- factor(data$gender, labels = c('male', 'female'))

#Plot the data using bar graph based on the attributes decided above

##1
ggplot(data_plot, aes(x=functionary, fill=factor(credit.rating))) + 
  geom_bar(position="dodge") + 
  xlab("Functionary") + 
  ylab("Count") + 
  ggtitle("Credit Rating by Functionary")

no_count <- sum(data_plot$functionary == "no")
yes_count <- sum(data_plot$functionary == "yes")
print(no_count)
print(yes_count)

##2
ggplot(data_plot, aes(x=FI3O.credit.score, fill=factor(credit.rating))) + 
  geom_bar(position="dodge") + 
  xlab("FI3O.credit.score") + 
  ylab("Count") + 
  ggtitle("Credit Rating by FI3O.credit.score")

##3
ggplot(data_plot, aes(x=re.balanced..paid.back..a.recently.overdrawn.current.acount, fill=factor(credit.rating))) + 
  geom_bar(position="dodge") + 
  xlab("re.balanced..paid.back..a.recently.overdrawn.current.acount") + 
  ylab("Count") + 
  ggtitle("Credit Rating by re.balanced..paid.back..a.recently.overdrawn.current.acount")

##4
ggplot(data_plot, aes(x=credit.refused.in.past., fill=factor(credit.rating))) + 
  geom_bar(position="dodge") + 
  xlab("credit.refused.in.past.") + 
  ylab("Count") + 
  ggtitle("Credit Rating by credit.refused.in.past.")

##5
ggplot(data_plot, aes(x=gender, fill=factor(credit.rating))) + 
  geom_bar(position="dodge") + 
  xlab("gender") + 
  ylab("Count") + 
  ggtitle("Credit Rating by gender")

#Another plot that i can use
#1
plot(data_plot$credit.rating ~ data_plot$functionary,
     xlab = 'functionary',ylab = 'credit rating',
     main = 'credit rating vs functionary')
#2
plot(data_plot$credit.rating ~ data_plot$FI3O.credit.score,
     xlab = 'FI3O.credit.score',ylab = 'credit rating',
     main = 'credit rating vs FI3O.credit.score')
#3
plot(data_plot$credit.rating ~ data_plot$re.balanced..paid.back..a.recently.overdrawn.current.acount,
     xlab = 're.balanced..paid.back..a.recently.overdrawn.current.acount',ylab = 'credit rating',
     main = 'credit rating vs re.balanced..paid.back..a.recently.overdrawn.current.acount')
#4
plot(data_plot$credit.rating ~ data_plot$credit.refused.in.past.,
     xlab = 'credit.refused.in.past.',ylab = 'credit rating',
     main = 'credit rating vs credit.refused.in.past.')
#5
plot(data_plot$credit.rating ~ data_plot$gender,
     xlab = 'gender',ylab = 'credit rating',
     main = 'credit rating vs gender')



