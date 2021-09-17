d1 <- 1:50
d2 <- 51:100

d1
d2
sort(d1, decreasing = FALSE)
sort(d1, decreasing = TRUE)
d3 <- c(sort(d1, decreasing = TRUE)[1:10] , sort(d2, decreasing = TRUE)[1:10])
d3
