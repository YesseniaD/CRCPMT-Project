memorialibreria1<-c(78,89.6,65.9,63.6,65,92.9,87.9,74.7,94.3)

mean(memorialibreria1)

#Estimaci�n del error est�ndar

sd(memorialibreria1)/sqrt(length(memorialibreria1))

#Estimaci�n de la diferencia de medias

mean(memorialibreria1)- mean(memorialibreria1)

#�Esto sugiere un efecto considerable para prolongar la vida causada por la asignaci�n del tratamiento?

#Para dar respuesta a la pregunta se debe estimar la exactitud de los

#promedios de los tratamientos, es decir se debe obtener el estimador

#del error est�ndar de la diferencia de medias

#Estimaci�n del error est�ndar de la diferencia de medias

sqrt(var(memorialibreria1)/length(memorialibreria1))

#Estimaci�n de las medianas

median(memorialibreria1)

#Estimaci�n de la diferencia de medianas

median(memorialibreria1)- median(memorialibreria1)

B<-5000

vec<-matrix(,B,2)

for(i in 1:B){

d<-sample(memorialibreria1,9,replace=T)

vec[i,1]<-mean(d)

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

#error est�ndar de theta estimado

sqrt(dif/B-1)

#error estandar de theta estimado con respecto al modelo.

sqrt(var(vec[,1]))

hist(vec[,1])        