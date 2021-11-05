setwd("c:/Rworks")
ds <- read.csv("seoul_temp_2017.csv")
head(ds)
summary(ds$avg_temp)

boxplot(ds$avg_temp,
        col="yellow",
        ylim=c(-20,40),
        xlab="서울1년기온",
        ylab="기온")

month.avg <- aggregate(ds$avg_temp,
                       by=list(ds$month),median)[2]

odr <- rank(-month.avg)

boxplot(avg_temp~month, data=ds,
        col=heat.colors(12)[odr],
        ylim=c(-20, 40),
        ylab="기온",
        xlab="월",
        main="서울 월별기온분포(2017)")


View(ds)
