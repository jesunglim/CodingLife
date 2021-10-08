ans=c("Y","Y","N","Y","Y")
table(ans)
table(ans) / length(ans)


favorite.color <- c("red", "green", "green", "yellow",
                    "red", "green", "red", "red")
sum <- table(favorite.color)
sum
barplot(sum, main="Favorite color")

mtcars
head(mtcars)
carb <- mtcars[,"carb"]
barplot(table(carb),
        main="Barplot of Carburetors",
        xlab="#of carburetors",
        ylab="frequency",
        col="red")
table(mtcars$carb)

par(mfrow=c(1,3))
barplot(table(mtcars$carb),
        main="Barplot of Carburetors",
        xlab="#of carburetors",
        ylab="frequency",
        col="blue")
barplot(table(mtcars$cyl),
        main="Barplot of Cylender",
        xlab="#of cykebder",
        ylab="frequency",
        col="red")
barplot(table(mtcars$gear),
        main="Barplot of gear",
        xlab="#of gear",
        ylab="frequency",
        col="green")
par(mfrow=c(1,1))

favorite.color <- c("red","green","yellow",
                    "red","green","red","red")
sum <- table(favorite.color)
pie(sum,main="Favorite color")


mydata = c(50, 60, 100, 75, 200)
mydata.big = c(mydata, 50000)
mean(mydata)
mean(mydata.big)
median(mydata)
median(mydata.big)
mean(mydata, trim=0.2)
mean(mydata.big, trim=0.2)
quantile(mydata)
quantile(mydata, (0:10)/10)
summary(mydata)
summary(mydata.big)
fivenum(mydata)

diff(mydata)
diff(range(mydata))
var(mydata)
sd(mydata)

head(state.x77)
st.income <- state.x77[,"Income"]
boxplot(st.income, ylab="Income value")

boxplot(Petal.Width~Species,data=iris,
        ylab="Petal.Width")

st.income <- state.x77[,"Income"]
hist(st.income,
     main="Histogram for Income",
     xlab = "income",
     ylab = "frequency",
     border = "blue",
     col="green",
     las=2,
     breaks = 5)
