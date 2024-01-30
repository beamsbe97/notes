# ------------------- SOM TRAINING ---------------------------

#choose the variables with which to train the SOM
#the following selects column 1,2,3,4,6 according to the attributes selected
#data_train <- data[, c(1,2,3,4,6)]

# To train the SOM model, i chose to include all features for better
# insight to the relationship of the features exclude credit rating
data_train = data[, c(1:45)]

# now train the SOM using the Kohonen method
data_train_matrix <- as.matrix(scale(data_train))
names(data_train_matrix) <- names(data_train)
require(kohonen)
x_dim=20
y_dim=20

som_grid <- somgrid(xdim = x_dim, ydim=y_dim, topo="hexagonal")

if (packageVersion("kohonen") < 3){
  system.time(som_model <- som(data_train_matrix, 
                             grid=som_grid, 
                             rlen=1500, 
                             alpha=c(0.9,0.01),
                             n.hood = "circular",
                             keep.data = TRUE ))
}else{
  system.time(som_model <- som(data_train_matrix, 
                             grid=som_grid, 
                             rlen=1500, 
                             alpha=c(0.9,0.01),
                             mode="online",
                             normalizeDataLayers=false,
                             keep.data = TRUE ))
}
summary(som_model)
rm(som_grid, data_train_matrix)

