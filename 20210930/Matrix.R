z <- matrix(1:20, nrow=4, ncol=5)
z
x <- 1:4
y <- 5:8

m1 <- cbind(x,y)
m2 <- rbind(x,y)
m1
m2
m3 <- rbind(m2, x)
m4 <- cbind(z,x)
m3
m4
z[2,3]
z[1,4]
z[2,]
z[,4]
rownames(z)
colnames(z) 
rownames(z) <- c("row1", "row2","row3","row4")
colnames(z) <- c("col1","col2", "col3", "co4", "col5")
z[,"col3"]
z["row2",]

a <- matrix(1:20, 4, 5)
b <- matrix(21:40, 4,5)
a
b
a+b
b-a
b/a
a*b
# 행과 열이 다르다면 에러
e1 <- matrix(1:20, 3,3)
e2 <- matrix(1:20, 4,4)
e1 + e2
# error in e1 + e2 : non-conformable arrays
a%*%b
3*a
b-5
2*a + 3*b

a <- a*3
a
b <- b-5
b

#Practice
m <- c(10, 40, 60, 20)
f <- c(21, 60, 70, 30)
score <- cbind(m, f)
score
colnames(score) <- c('male', 'female')
score[,"male"]
score[,"female"]
score[3,2]
