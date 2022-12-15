tiempolibreria1<-c(28.67193398,37.67445752,11.15839875,14.13138197,15.80249413,19.69257731,14.25780042,17.43216654,43.59123231)
mean(tiempolibreria1)
median(tiempolibreria1)
hist(tiempolibreria1)
#Estimación del error estándar
sd(tiempolibreria1) 

tiempolibreria2<-c(113.4356293,147.1395946,44.94758459,57.6075922,53.6704862,61.83368747,123.8178965,58.2579331,47.17653714)
mean(tiempolibreria2)
median(tiempolibreria2)
hist(tiempolibreria2)
#Estimación del error estándar
sd(tiempolibreria2) 
t.test(tiempolibreria1,tiempolibreria2)


memorialibreria1<-c(78,89.6,65.9,63.6,65,92.9,87.9,74.7,94.3)
mean(memorialibreria1)
median(memorialibreria1)
hist(memorialibreria1)
#Estimación del error estándar
sd(memorialibreria1) 

memorialibreria2<-c(89,94.5,76.4,78.8,79,94.7,93.2,91.4,84)
mean(memorialibreria2)
median(memorialibreria2)
hist(memorialibreria2)
#Estimación del error estándar
sd(memorialibreria2) 
t.test(memorialibreria1,memorialibreria2)

