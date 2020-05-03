## Importar librerias
library(igraph)

ejes = c(1,2,2,3,3,4,4,5,2,6,6,7,4,7,7,5,7,8)
g=graph(ejes,n=8,directed=FALSE)
nombres = c('Salon A','Entrada','Hall','Parrilla','Edificio Ing','Cafeteria','Tia','Jardin')

plot(g,vertex.label=paste(nombres,1:length(nombres)))

finalizar = function(nodo){
  nombres = c('Salon A','Entrada','Hall','Parrilla','Edificio Ing','Cafeteria','Tia','Jardin')
  nombres[nodo] == 'Edificio Ing'
}

frontera = c(1)
visitados = c()
cond=0;
while(cond==0){
  nodo = frontera[1]
  frontera = frontera[-1]
  visitados = c(visitados,nodo)
  vecinos = neighbors(g,nodo)
  hijos = setdiff(vecinos,c(visitados,frontera)) #cuales elementos de un conjunto A no está en un conjunto B
  prueba = sapply(hijos, finalizar) # aplica a todos los elementos de un vector una función.
  if(any(prueba)){
    salida = hijos[which(prueba)] # wich dice donde hay un true
    cond=1
    str(salida)
  }
  frontera = c(frontera,hijos)
}