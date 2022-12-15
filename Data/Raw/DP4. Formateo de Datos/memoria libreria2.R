memorialibreria2<-c(89,94.5,76.4,78.8,79,94.7,93.2,91.4,84)

mean(memorialibreria2)

#Estimación del error estándar

sd(memorialibreria2)/sqrt(length(memorialibreria2))

#Estimación de la diferencia de medias

mean(memorialibreria2)- mean(memorialibreria2)

#¿Esto sugiere un efecto considerable para prolongar la vida causada por la asignación del tratamiento?

#Para dar respuesta a la pregunta se debe estimar la exactitud de los

#promedios de los tratamientos, es decir se debe obtener el estimador

#del error estándar de la diferencia de medias

#Estimación del error estándar de la diferencia de medias

sqrt(var(memorialibreria2)/length(memorialibreria2))

#Estimación de las medianas

median(memorialibreria2)

#Estimación de la diferencia de medianas

median(memorialibreria2)- median(memorialibreria2)

B<-5000

vec<-matrix(,B,2)

for(i in 1:B){

h<-sample(memorialibreria2,9,replace=T)

vec[i,1]<-mean(h)

vec[i,2]<-vec[i,1]

}

thet<-mean(vec[,2])

thet

dif<-0

i<-1

repeat{

dif<- dif+(vec[i,1]-thet)^2

i<-i+1

if(i>B){

break}

}

#error estándar de theta estimado

sqrt(dif/B-1)

#error estandar de theta estimado con respecto al modelo.

sqrt(var(vec[,1]))

hist(vec[,1])