tiempolibreria1<-c(28.67193398,37.67445752,11.15839875,14.13138197,15.80249413,19.69257731,14.25780042,17.43216654,43.59123231)

tiempolibreria2<-c(113.4356293,147.1395946,44.94758459,57.6075922,53.6704862,61.83368747,123.8178965,58.2579331,47.17653714)

mean(tiempolibreria1)

mean(tiempolibreria2)

#Estimación del error estándar

sd(tiempolibreria1)/sqrt(length(tiempolibreria1))

sd(tiempolibreria2)/sqrt(length(tiempolibreria2))

#Estimación de la diferencia de medias

mean(tiempolibreria1)- mean(tiempolibreria2)

#¿Esto sugiere un efecto considerable para prolongar la vida causada por la asignación del tratamiento?

#Para dar respuesta a la pregunta se debe estimar la exactitud de los

#promedios de los tratamientos, es decir se debe obtener el estimador

#del error estándar de la diferencia de medias

#Estimación del error estándar de la diferencia de medias

sqrt(var(tiempolibreria1)/length(tiempolibreria1)+ var(tiempolibreria2)/length(tiempolibreria2))

#Estimación de las medianas

median(tiempolibreria1)

median(tiempolibreria2)

#Estimación de la diferencia de medianas

median(tiempolibreria1)- median(tiempolibreria2)

B<-5000

vec<-matrix(,B,3)

for(i in 1:B){

d<-sample(tiempolibreria1,9,replace=T)

vec[i,1]<-mean(d)

h<-sample(tiempolibreria2,9,replace=T)

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

t.test(tiempolibreria1, y = tiempolibreria2)