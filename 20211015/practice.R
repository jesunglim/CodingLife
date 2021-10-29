wt <- mtcars$wt
mpg <- mtcars$mpg
plot(wt, mpg,
     main="Car Weight-mpg",
     xlab="Car Weight",
     ylab="Miles Per Gallon ",
     col="red",
     pch=4,
     type="p")

head(mtcars)

vars <- c("mpg", "disp", "drat", "wt")
target <- mtcars[,vars]
class(target)
pairs(target,
      main="Multi plots")

head(iris)
iris.2 <- iris[,3,4]
point <- as.numeric(iris$Species)
color <- c("red","green","blue")
plot(iris.2,
     main="Iris plot",
     pch=c(point),
     col=color[point])

beers = c(5,2,9,8,3,7,3,5,3,5)
bal = c(0.1, 0.03, 0.19, 0.12, 0.04, 0.0095, 0.07,
        0.06, 0.02, 0.05)
tbl = data.frame(cbind(beers, bal))
tbl; class(tbl)
plot(bal~beers, data=tbl)
res=lm(bal~beers, data=tbl)
abline(res)
cor(beers,bal)

cor(iris[,1:4])



month = 1:12
late1 = c(5,8,7,9,4,6,12,13,8,6,6,4)
late2 = c(4,6,5,8,7,8,10,11,6,5,2,1)
plot(month,
     late1,
     main="Late students",
     type= "b",
     lty=1,
     lwd=1,
     xlab="Month ",
     ylab="Late cnt")
lines(month,
      late2,
      type="b",
      col = "blue")

sd(iris[,1])
sd(iris[,2])
sd(iris[,3])
sd(iris[,4])

par(mfrow = c(2,2))

point <- as.numeric(iris$Species)
color <- c("red","green","blue")
pairs(iris[,-5],
      pch=c(point),
      col=color[iris[,5]])
