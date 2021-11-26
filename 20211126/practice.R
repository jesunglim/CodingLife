require(graphics)
library(graphics)

x <- rbind(matrix(rnorm(100, sd = 0.3), ncol=2),
                  matrix(rnorm(100, mean = 1, sd = 0.3),ncol=2))
colnames(x) <- c("x","y")
c1 <- kmeans(x,2)
c1
plot(x,col=c1$cluster)
points(c1$centers,col=1:2, pch=8, cex=2)

c1 <- kmeans(x,5,nstart = 25)
plot(x,col=c1$cluster)
points(c1$centers, col=1:5, pch=8)
s