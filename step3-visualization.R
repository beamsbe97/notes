# -------------------- SOM VISUALISATION -----------------

# Visualize the SOM model results
# Plot of the training progress - how the node distances have stabilized over time.

source('./coolBlueHotRed.R')

plot(som_model, type = "changes")
#counts within nodes
plot(som_model, type = "counts", main="Node Counts", palette.name=coolBlueHotRed)
#map quality
plot(som_model, type = "quality", main="Node Quality/Distance", palette.name=coolBlueHotRed)
#neighbor distances
plot(som_model, type="dist.neighbours", main = "SOM neighbour distances", palette.name=grey.colors)
#code spread
plot(som_model, type = "codes")

# Plot the original scale heat map for a variable from the training set:
var <- 1 #define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)

var <- 2 #define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)

var <- 3 #define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)

var <- 4 #define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)

var <- 6 #define the variable to plot
var_unscaled <- aggregate(as.numeric(data_train[,var]), by=list(som_model$unit.classif), FUN=mean, simplify=TRUE)[,2]
plot(som_model, type = "property", property=var_unscaled, main=names(data_train)[var], palette.name=coolBlueHotRed)
rm(var_unscaled, var)

#plot a variable from the original data set (will be uncapped etc.)
# This function produces a menu for multiple heatmaps.
source('./plotHeatMap.R')
plotHeatMap(som_model, data, variable=0)

