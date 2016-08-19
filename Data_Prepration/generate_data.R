library(MASS)
# generate a muli-normal dataset
Sigma = matrix(c(1,0,0,0,1,0,0,0,1),3,3)
N_obs = 10
C1 = mvrnorm(n = N_obs, c(1,2,3), Sigma)
C2 = mvrnorm(n = N_obs, c(4,5,6), Sigma)
C3 = mvrnorm(n = N_obs, c(7,8,9), Sigma)

ALLobs = rbind(C1,C2,C3)
a = data.frame(ALLobs)

# random assign cluster firstly
a$cluster = sample(c(1,2,3),(3*N_obs), replace = TRUE)

clusterNum = 3
dimension = 3

for(i in 1:clusterNum){
  for(j in 1:dimension){
    name = paste(as.character(i), as.character(j),sep="")
    a[,name] = mean(a[which(a$cluster==i),j])
  }
}

write.table(a, file = "a.txt", quote = FALSE, col.names = FALSE, sep = "\t")


##############################################################

library(MASS)
# generate a muli-normal dataset
Sigma = matrix(c(1,0,0,1),2,2)
N_obs = 333333
C1 = mvrnorm(n = N_obs, c(1,1), Sigma)
C2 = mvrnorm(n = N_obs, c(5,5), Sigma)
C3 = mvrnorm(n = N_obs, c(10,10), Sigma)

ALLobs = rbind(C1,C2,C3)
a = data.frame(ALLobs)

# random assign cluster firstly
a$cluster = sample(c(1,2), (2*N_obs), replace = TRUE)

clusterNum = 3
dimension = 2

for(i in 1:clusterNum){
  for(j in 1:dimension){
    name = paste(as.character(i), as.character(j),sep="")
    a[,name] = mean(a[which(a$cluster==i),j])
  }
}

write.table(a, file = "newdata.txt", quote = FALSE, col.names = FALSE, row.names=FALSE, sep = ",")



# For chang's MR
library(MASS)
# generate a muli-normal dataset
Sigma = matrix(c(1,0,0,1),2,2)
N_obs = 333333
C1 = mvrnorm(n = N_obs, c(1,1), Sigma)
C2 = mvrnorm(n = N_obs, c(5,5), Sigma)
C3 = mvrnorm(n = N_obs, c(10,10), Sigma)

ALLobs = rbind(C1,C2,C3)
a = data.frame(ALLobs)
write.table(a, file = "ChangMR.txt", quote = FALSE, col.names = FALSE, row.names=FALSE, sep = ",")


# For yang's MR
library(MASS)
# generate a muli-normal dataset
Sigma = matrix(c(1,0,0,1),2,2)
N_obs = 250000
clusterNum = 3
dimension = 2
C1 = mvrnorm(n = N_obs, c(1,1), Sigma)
C2 = mvrnorm(n = N_obs, c(5,5), Sigma)
C3 = mvrnorm(n = N_obs, c(10,10), Sigma)

ALLobs = rbind(C1,C2,C3)
a = data.frame(ALLobs)

# random assign cluster firstly
a$cluster = sample(c(1,2,3), (clusterNum*N_obs), replace = TRUE)

setwd('F:/U course/ECS 289/kmeans')
write.table(a, file = "YangMR75.txt", quote = FALSE, col.names = FALSE, row.names=TRUE, sep = ",")


# For Shuxin's MR
library(MASS)
# generate a muli-normal dataset
Sigma = matrix(c(1,0,0,1),2,2)
N_obs = 333333
C1 = mvrnorm(n = N_obs, c(1,1), Sigma)
C2 = mvrnorm(n = N_obs, c(5,5), Sigma)
C3 = mvrnorm(n = N_obs, c(10,10), Sigma)

ALLobs = rbind(C1,C2,C3)
a = data.frame(ALLobs)
write.table(a, file = "ShuxinMR.txt", quote = FALSE, col.names = FALSE, row.names=FALSE, sep = " ")

