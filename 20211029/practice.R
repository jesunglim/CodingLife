library(treemap)
data(GNI2014)
head(GNI2014)
class(GNI2014)
treemap(GNI2014,
        index=c("continent", "iso3"),
        vSize="population",
        vColor="GNI",
        type="value",
        bg.labels="yellow",
        title="World's GNI")

st <- data.frame(state.x77)
st <- data.frame(st, stname=rownames(st))

treemap(st,
        index=c("stname"),
        vSize="Area",
        vColor = "Income",
        type="value",
        title="USA states area and income")

st <- data.frame(state.x77)
symbols(st$Illiteracy, st$Murder,
        circles=st$Population,
        inches=0.3,
        fg="white",
        bg="lightgray",
        lwd=1.5,
        xlab="rate of Illiteracy",
        ylab="Illiteracy and Crime")
text(st$Illiteracy, st$Murder,
     rownames(st),
     cex=0.6,
     col="brown")

head(mtcars)
mosaicplot(~gear+vs, data=mtcars, color=TRUE,
           main = "Gear and Vs")
mosaicplot(~gear+vs, data=mtcars, color=c("green", "blue"),
           main = "Gear and Vs")

Titanic
mosaicplot(Titanic, color =TRUE, off=5)
mosaicplot(Titanic, 
           main = "Survival on the TItanic",
           color = c("red", "green"),
           off=3)

library(ggplot2)

month <- c(1,2,3,4,5,6)
rain <- c(55,50,45,50,60,70)
df <- data.frame(month,rain)
df

ggplot(df, aes(x=month, y=rain)) +
  geom_bar(stat="identity",
            width=0.7,
            fill="steelblue")

ggplot(iris, aes(x=Petal.Length)) +
  geom_histogram(binwidth = 0.5)

ggplot(iris, aes(x=Sepal.Width, fill=Species, color=Species)) +
  geom_histogram(binwidth = 0.5, position="dodge") +
  theme(legend.position = "top")

ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width, color=Species)) +
  geom_point(size=3) +
  ggtitle("꽃잎의 길이와 폭") +
  theme(plot.title = element_text(size=25, face="bold",
                                  colour = "steelblue"))

ggplot(data=iris, aes(y=Petal.Length)) +
  geom_boxplot(fill="yellow")

ggplot(data=iris, aes(y=Petal.Length, fill=Species)) +
  geom_boxplot()

year <- 1937:1960
cnt <- as.vector(airmiles)
df <- data.frame(year,cnt)
head(df)

ggplot(data=df, aes(x=year, y=cnt)) +
  geom_line(col="red")
