tiempolibreria2<-c(113.4356293,147.1395946,44.94758459,57.6075922,53.6704862,61.83368747,123.8178965,58.2579331,47.17653714)

mean(tiempolibreria2)

#Estimación del error estándar

sd(tiempolibreria2)/sqrt(length(tiempolibreria2))

#Estimación de la diferencia de medias

mean(tiempolibreria2)- mean(tiempolibreria2)

#¿Esto sugiere un efecto considerable para prolongar la vida causada por la asignación del tratamiento?

#Para dar respuesta a la pregunta se debe estimar la exactitud de los

#promedios de los tratamientos, es decir se debe obtener el estimador

#del error estándar de la diferencia de medias

#Estimación del error estándar de la diferencia de medias

sqrt(var(tiempolibreria2)/length(tiempolibreria2))

#Estimación de las medianas

median(tiempolibreria2)

#Estimación de la diferencia de medianas

median(tiempolibreria2)- median(tiempolibreria2)

B<-5000

vec<-matrix(,B,2)

for(i in 1:B){

h<-sample(tiempolibreria2,9,replace=T)

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