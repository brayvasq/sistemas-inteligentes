### Importar librerias necesarias
library(igraph)

# Para el siguiente vector cada pareja representa una arista que conecta
# los nodos indicados 
caminos_grafo = c(1,2, 2,3, 3,4, 4,5, 2,6, 6,7, 4,7, 7,5, 7,8)

# Se crea un grafo con los caminos indicados en el vector anterior
# Se indica que el numero de nodos es 8 y que es un grafo no dirigido.
grafo = graph(caminos_grafo,n=8,directed=FALSE)

# Vector con las etiquetas o nombres de los nodos
nombres_nodos = c('Salon A','Entrada','Hall','Parrilla','Edificio Ing','Cafeteria','Tia','Jardin')

# Graficar el grafo
plot(grafo,vertex.label=paste(nombres_nodos,1:length(nombres_nodos)))

######################### Sección Funciones ################################

# Función que me indica si el nodo entrante es un nodo respuesta
es_respuesta <- function(nodo,nombres_nodos){
  nombres = c('Salon A','Entrada','Hall','Parrilla','Edificio Ing','Cafeteria','Tia','Jardin')
  nombres[nodo] == 'Edificio Ing'
}

contiene <- function(nodo,vector){
  respuesta = FALSE;
  if(length(vector)>0){
    for (j in 2:length(vector)){
      if(as.integer(vector[j]) == as.integer(nodo)){
        respuesta = TRUE
      }
    }
  }
  return(respuesta)
}

ver_camino <- function(camino_respuesta,nodo){
  tamano = length(camino_respuesta)
  padre = nodo
  respuesta = c();
  i = tamano;
  while(i>0){
    valor = contiene(padre,camino_respuesta[[i]])
    respuesta = c(respuesta,padre)
    if(valor){
      padre = camino_respuesta[[i]][1]
    }
    i = i-1
  }
  respuesta = c(respuesta,1)
  respuesta = unique(respuesta)
  return(sort(respuesta))
}

######################### Sección Principal ###############################
frontera = c(1)
visitados = c()
cond=0;
i=1;

camino_respuesta = list(length=8)

while(cond==0){
  nodo = frontera[1]
  frontera = frontera[-1]
  visitados = c(visitados,nodo)
  
  vecinos = neighbors(grafo,nodo)
  hijos = setdiff(vecinos,c(visitados,frontera)) #cuales elementos de un conjunto A no está en un conjunto B

  camino_respuesta[[i]] = c(nodo,hijos)
  i = i+1;
  
  prueba = sapply(hijos, es_respuesta) # aplica a todos los elementos de un vector una función.
  if(any(prueba)){
    salida = hijos[which(prueba)] # wich dice donde hay un true
    cond=1
    str(salida)
    resp = ver_camino(camino_respuesta,salida)
    str(resp)
  }
  frontera = c(frontera,hijos)
}
