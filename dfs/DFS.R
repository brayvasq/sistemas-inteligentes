# Author: brayan stiven vasquez villa
# Date: 10-04-2018

# Librerias
library(igraph)

# Construcción grafo
caminos_grafo = c(1,2, 2,3, 3,4, 4,5, 2,6, 6,7, 4,7, 7,5, 7,8)
grafo = graph(caminos_grafo, n = 8, directed = FALSE)
nombres_nodos = c('A','B','C','D','E','F','G','H')
E(grafo)$weight = c(2,2,1,2,1,3,4,1,1)
#matriz = get.adjacency(get.adjacency(graph = grafo,attr = 'weight'))

########################### FUNCIONES #####################################

# Verifica si un nodo es respuesta
es_respuesta <- function(nodo,objetivo){
  nombres_nodos[nodo] == nombres_nodos[objetivo]
}

# Algoritmo recursivo de busqueda por profundidad
dfs <- function(nodo,objetivo,visitados){
  respuesta = es_respuesta(nodo,objetivo)
  resp = "NOT"
  if(respuesta){
    visitados = c(visitados,nodo)
    str("Respuesta")
    str(nodo)
    str("Camino")
    str(visitados)
    resp = "OK"
    visualizar_respuesta(visitados)
    return(resp)
  }else{
    visitados = c(visitados,nodo)
    vecinos  = neighbors(grafo,nodo)
    for(item in vecinos){
      if(resp != "OK"){
        if(!(item %in% visitados)){
          resp = dfs(as.numeric(item),objetivo,visitados)
        } 
      }
    }
    x = c(nodo)
    visitados = visitados[!visitados %in% x]
  }
  return(resp)
}

# Muestra la respuesta en consola y grafica un grafo solo con los nodos del camino respuesta
visualizar_respuesta <- function(vector_ruta){
  str(vector_ruta)
  caminos_resp = c()
  for (i in 2:length(vector_ruta)){
    caminos_resp = c(caminos_resp,i-1,i)
  }
  grafo_respuesta = graph(caminos_resp,n = length(vector_ruta),directed = FALSE)
  par(mfcol = c(1,2))
  plot(grafo,vertex.label=paste(nombres_nodos,1:length(nombres_nodos)),edge.label=E(grafo)$weight)
  plot(grafo_respuesta,vertex.label=paste(vector_ruta,1:length(vector_ruta)))
}

# función principal
main <- function(objetivo){
  nodo = 1
  camino = c()
  visitados = c()
  dfs(nodo,objetivo,visitados)
}

main(5)