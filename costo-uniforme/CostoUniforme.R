# Author : brayan stiven vasquez villa

# Librerias
library(igraph)

# Construcción grafo.
caminos_grafo = c(1,2, 2,3, 3,4, 4,5, 2,6, 6,7, 4,7, 7,5, 7,8)
grafo = graph(caminos_grafo,n = 8,directed = FALSE)
nombres_nodos = c('A','B','C','D','E','F','G','H')
E(grafo)$weight = c(2,2,1,2,1,3,4,1,1)
matriz  = get.adjacency(graph = grafo,attr = 'weight')

### Sección Funciones
# Verifica si un nodo es respuesta
es_respuesta <- function(nodo,objetivo){
  nombres_nodos[nodo] == nombres_nodos[objetivo]
}

# Calcula el costo Acumulado de un nodo
obtener_suma <- function(vector_costo,vector_padre,item,raiz){
  suma = 0.0
  nodo_actual = item
  
  while(nodo_actual != raiz){
    suma = suma + vector_costo[[nombres_nodos[nodo_actual]]]
    nodo_actual = vector_padre[[nombres_nodos[nodo_actual]]]
  }

  return(suma)
}

# Verifica si está en la frontera y si el costo actual es menor que el existente
en_frontera <- function(item,raiz,nuevo_padre,frontera,vector_costo,vector_padre,costo_item){
  respuesta = FALSE
  
  if(item %in% frontera){
    suma = obtener_suma(vector_costo,vector_padre,item,raiz)
    
    nuevo_vector_padre = vector_padre
    nuevo_vector_padre[[nombres_nodos[item]]] = nuevo_padre

    nuevo_vector_costo = vector_costo
    nuevo_vector_costo[[nombres_nodos[item]]] = costo_item

    nueva_suma = obtener_suma(nuevo_vector_costo,nuevo_vector_padre,item,raiz)#(suma - vector_costo[[nombres_nodos[item]]]) + costo_item
    if(nueva_suma < suma){
      respuesta = TRUE
    }
  }
  
  return(respuesta)
}
# Calcula la ruta desde el origen al objetivo
hallar_camino <- function(raiz,objetivo,vector_costo,vector_padre){
  vector_ruta = c()
  nodo_actual = objetivo
  while(nodo_actual != raiz){
    vector_ruta = c(vector_ruta,nombres_nodos[nodo_actual])
    nodo_actual = vector_padre[[nombres_nodos[nodo_actual]]]
  }
  vector_ruta = c(vector_ruta,nombres_nodos[raiz])
  vector_ruta = rev(vector_ruta)
  
  vizualizar_respuesta(vector_ruta)
}

# Muestra la respuesta en consola y grafica un grafo solo con los nodos del camino respuesta
vizualizar_respuesta <- function(vector_ruta){
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

# Algoritmo principal
costo_uniforme <- function(grafo,raiz,objetivo){
  nodo = raiz
  costo_total = 0
  
  vector_costo = list(nombres_nodos) #Vector con el costo individual
  vector_costo[[nombres_nodos[nodo]]] = 0
  vector_padre = list(nombres_nodos) #Vector con el padre de cada nodo
  
  frontera = c(nodo)
  explorados = c()
  
  encontrado = FALSE
  respuesta = NULL
  
  while(encontrado == FALSE){

    if(length(frontera) <= 0){
      encontrado = TRUE
      respuesta = "Error frontera vacía"
    }
      
    nodo = frontera[1]
    frontera = frontera[-1]
    
    if(es_respuesta(nodo,objetivo)){
      encontrado = TRUE
      respuesta = cat("Respuesta",nodo)
    }
    
    explorados = c(explorados,nodo)
    vecinos = neighbors(grafo,nodo)
    
    for(item in vecinos){
      if(!(item %in% explorados)){
        if(!(item %in% frontera)){
          frontera = c(frontera,item)
          costo_item = matriz[nodo,item]
          vector_costo[[nombres_nodos[item]]] = costo_item
          vector_padre[[nombres_nodos[item]]] = nodo
        }else{
          costo_item = matriz[nodo,item]
          if(en_frontera(item,raiz,nodo,frontera,vector_costo,vector_padre,costo_item)){
            vector_costo[[nombres_nodos[item]]] = costo_item
            vector_padre[[nombres_nodos[item]]] = nodo
          }
        }
      }
    }
  }
  hallar_camino(raiz,objetivo,vector_costo,vector_padre)
}

costo_uniforme(grafo,1,8)