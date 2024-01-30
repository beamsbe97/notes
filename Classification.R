library(RSNNS)
library(caret)

#Load dataset
fullDataSet <- read.csv("creditworthiness.csv")

#select all entries for which the credit rating is known
knownData <- subset(fullDataSet, fullDataSet[,46] > 0)

#select all entries for which the credit rating is unknown
unknownData <- subset(fullDataSet, fullDataSet[,46] == 0)

#separate value from targets
trainValues <- knownData[,1:45]
trainTargets <- decodeClassLabels(knownData[,46])
unknownsValues <- unknownData[,1:45]

#split dataset into traing and test set
trainset <- splitForTrainingAndTest(trainValues, trainTargets, ratio=0.15)
trainset <- normTrainingAndTestSet(trainset)

model <- mlp(trainset$inputsTrain, trainset$targetsTrain, size=15, learnFuncParams=c(0.01), maxit=100, inputsTest=trainset$inputsTest, targetsTest=trainset$targetsTest)

predictTestSet <- predict(model,trainset$inputsTest)

confusionMatrix(trainset$targetsTrain,fitted.values(model))
testsetACC<-confusionMatrix(trainset$targetsTest,predictTestSet)

overallACC <- (sum(diag(testsetACC)))/sum(testsetACC) * 100
print(paste("Overall accuracy:", overallACC, "%"))

Atest<-(testsetACC[1,1]/sum((testsetACC[1,])))*100
Btest<-(testsetACC[2,2]/sum((testsetACC[2,])))*100
Ctest<-(testsetACC[3,3]/sum((testsetACC[3,])))*100

print(paste("Test set accuracy cr 1:" , Atest, "%"))
print(paste("Test set accuracy cr 2:", Btest, "%"))
print(paste("Test set accuracy cr 3:", Ctest, "%"))

par(mfrow=c(2,2))
plotIterativeError(model)
plotRegressionError(predictTestSet[,2], trainset$targetsTest[,2])
plotROC(fitted.values(model)[,2], trainset$targetsTrain[,2])
plotROC(predictTestSet[,2], trainset$targetsTest[,2])
 
#confusion matrix with 402040-method
confusionMatrix(trainset$targetsTrain, encodeClassLabels(fitted.values(model),method="402040", l=0.4, h=0.6))

#show detailed information of the model
summary(model)
model
weightMatrix(model)
extractNetInfo(model)
 
