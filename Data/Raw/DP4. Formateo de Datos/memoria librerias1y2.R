memorialibreria1<-c(78,89.6,65.9,63.6,65,92.9,87.9,74.7,94.3)

memorialibreria2<-c(89,94.5,76.4,78.8,79,94.7,93.2,91.4,84)

mean(memorialibreria1)

mean(memorialibreria2)

#Estimación del error estándar

sd(memorialibreria1)/sqrt(length(memorialibreria1))

sd(memorialibreria2)/sqrt(length(memorialibreria2))

#Estimación de la diferencia de medias

mean(memorialibreria1)- mean(memorialibreria2)

#¿Esto sugiere un efecto considerable para prolongar la vida causada por la asignación del tratamiento?

#Para dar respuesta a la pregunta se debe estimar la exactitud de los

#promedios de los tratamientos, es decir se debe obtener el estimador

#del error estándar de la diferencia de medias

#Estimación del error estándar de la diferencia de medias

sqrt(var(memorialibreria1)/length(memorialibreria1)+ var(memorialibreria2)/length(memorialibreria2))

#Estimación de las medianas

median(memorialibreria1)

median(memorialibreria2)

#Estimación de la diferencia de medianas

median(memorialibreria1)- median(memorialibreria2)

B<-5000

vec<-matrix(,B,3)

for(i in 1:B){

d<-sample(memorialibreria1,9,replace=T)

vec[i,1]<-mean(d)

h<-sample(memorialibreria2,9,replace=T)

vec[i,2]<-mean(h)

vec[i,3]<-vec[i,1]-vec[i,2]

}

thet<-mean(vec[,3])

thet

dif<-0

i<-1

repeat{

dif<- dif+(vec[i,3]-thet)^2

i<-i+1

if(i>B){

break}

}

#error estándar de theta estimado

sqrt(dif/B-1)

#error estandar de theta estimado con respecto al modelo.

sqrt(var(vec[,3]))

hist(vec[,3])        

?t.test

t.test(memorialibreria1, y = memorialibreria2)