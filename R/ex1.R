a<-3
a
a=4
a
4+3
sqrt(25)
ls()
a=c(1,2,3,4,5)
a
a+1
a[2]
mean(a)
var(a)
a[0]
a[6]
a=numeric(10)
a
typeof(a)
a='hello'
a
typeof(a)
a=character(10)
a
library("readxl")
df=read_excel("footballData.xlsx")
setwd("/home/boss/Desktop/Sumithra1/R")
df
summary(df)
summary(df$Name)
summary(df$`Preferred Foot`)
summary(df$Overall)
a<-c(1,2,3,4)
b=c(4,5,6,7)
c=factor(c('A','B','A','B'))
df=data.frame(first=a,second=b,thrid=c)
df
df$thrid
df$first
a=TRUE
typeof(a)
is.numeric(a)
table(c)
attributes(df)
res<-table(c)
res
summary(res)
table(df)
M=matrix(c(2,3,4,5),ncol=2,byrow=2)
M
colnames(M)<-c('A','B')
M<-as.table(M)
M
colnames(M)<-c('1','2')
M
a<-c(4,9,16,25)
sqrt(a)
log(a)
exp(a)
names(df)
mean(df$weightInKg)
var(df$weightInKg)
min(df$weightInKg)
max(df$weightInKg)
df$weightInKg
sd(df$weightInKg)
summary(df)
a=c(3,2,1,78,10)
a
sort(a)
sort(a,decreasing=TRUE)
a<-data.frame(one=c(1,2,3,4),two=c(3,4,5,6))
b<-data.frame(one=c('A','B','C','D'),two=c('K','L','M','N'))
c=rbind(a,b)
c
c=cbind(a,b)
c
typeof(c)
x<-list(a=rnorm(10,mean=10,sd=3),b=rexp(10,10.0),c=as.factor(c('a','b','c','d')))
x        
res<-lapply(x,summary)
res
res1=sapply(x,summary)
res1
res1[1]
res1[2]
x1<-data.frame(one=c(1,2,3,4),two=as.factor(c('A','B','A','B')))
x1
res=tapply(x1$one,x1$two,mean)               
res
a=c(1,2,3,4,5)
b=c(TRUE,FALSE,FALSE,TRUE,FALSE)
a[b]
max(a[b])
sum(a[b])
a=c(1,2,3,4,NA)
sum(a)
sum(a,na.rm=TRUE)
is.na(a)
!is.na(a)
stripchart(df$weightInKg,method="stack")
hist(df$weightInKg,main="Distribution",xlab="x1")
hist(df$Age,breaks=4)
boxplot(df$Crossing)
plot(df$Age,df$Overall)
cor(df$Age,df$Overall)
qqline(df$heightInCm)

