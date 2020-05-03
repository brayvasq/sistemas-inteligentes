# Modificación del programa para que funcione con DFS(busqueda en profundidad)
# Author: brayan stiven vasquez villa
# Date: 12-04-2018

#================================================================================================

#Clase 3: Métodos de búsqueda sin información en espacios discretos /////////////////////////////
#================================================================================================

#-----------------------------------------------------------------------------------------------

#Función para graficar el rompecabezas ::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------------

graph.puzzle=function(m){
  
  df <- expand.grid(x=1:ncol(m),y=1:nrow(m))
  
  df$val <- m[as.matrix(df[c('y','x')])]
  
  par(mar=c(.5,.5,.5,.5))
  
  plot(x=df$x,y=df$y,pch=as.character(df$val), asp=1,cex=3,xlim=c(0.5,3.5),ylim=c(3.5,0.5),xaxt="n",yaxt="n",xlab="",ylab="",
       xaxs="i", yaxs="i", axes=F)
  abline(v=0.5+(0:3),h=0.5+(0:3))
}


#-----------------------------------------------------------------------------------------------

#Función generadora de estados para el rompecabezas ::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------------

puzzle.states=function(m){
  
  p=which(is.na(m),arr.ind=TRUE); #Posición del espacio vacío
  
  ph=matrix(c(1,0,0,1,-1,0,0,-1)+rep(p,4),nrow=4,byrow=TRUE);#Posiciones a donde se va a mover el espacio vacío
  
  ph=apply(ph,2,pmin,3); #Corrección de las posiciones para que no sean mayores a 3
  
  ph=apply(ph,2,pmax,1); #Corrección de las posiciones para que no sean menores a 1
  
  estados=vector(length=4,mode='list');
  
  for(i in 1:nrow(ph)){
    
    e=m;
    
    e[p[1],p[2]]=e[ph[i,1],ph[i,2]];
    
    e[ph[i,1],ph[i,2]]=NA;
    
    estados[[i]]=e;
  }
  
  return(estados);
  
}


#-----------------------------------------------------------------------------------------------

#Esta función verifica si se llegó al nodo objetivo:::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------------

finalizar=function(nodo){
  solucion <- matrix(c(1,2,3,4,5,6,7,8,NA), nrow=3, ncol=3,byrow=TRUE);
  return(identical(nodo,solucion))
}

#-----------------------------------------------------------------------------------------------
#Rutina principal Modificada con el algoritmo DFS(busqueda en profundidad)
#-----------------------------------------------------------------------------------------------                        

# Función que indica si un elemento está en la lista pasada por parametro
en_lista <- function(item,lista){
  resp = FALSE
  for(itnodo in lista){
    if(identical(item,itnodo)){
      resp = TRUE
    }
  }
  return(resp)
}

# Función que crea un nuevo vector quitando el nodo dado de la lista
nuevo_vector <- function(nodo,lista){
  respuesta = list()
  for(item in lista){
    if(!identical(nodo,item)){
      respuesta[[length(respuesta)+1]] = item
    }
  }
  return(respuesta)
}

# Método que recorre el vector respuesta para llamar al método que grafica
visualizar_puzzle <- function(vector){
  for(i in 1:length(vector)){
    
    graph.puzzle(vector[[i]]);
    
    Sys.sleep(1)
    
  }
}

# Algoritmo recursivo de busqueda por profundidad
pasos = 0

dfs <- function(nodo,visitados,profundidad){
  pasos <<- pasos + 1
  print(pasos)
  resp = "NOT"
  profundidad = profundidad - 1
  if(profundidad>1){
    respuesta = finalizar(nodo)
    index = length(visitados)+1
    if(respuesta){
      visitados[[index]] = nodo
      print(nodo)
      print(visitados)
      visualizar_puzzle(visitados)
      resp = "OK"
      return(resp)
    }else{
      visitados[[index]] = nodo
      vecinos = puzzle.states(nodo)
      for(item in vecinos){
        if(resp != "OK"){
          if(!(en_lista(item,visitados))){
            resp = dfs(item,visitados,profundidad)
          }
        }
      }
      visitados = nuevo_vector(nodo,visitados)
    }
  }
  return(resp)
}

main <- function(){
  m <- matrix(c(5,1,2,NA,7,3,6,4,8), nrow=3, ncol=3,byrow=TRUE)
  visitados = list()
  graph.puzzle(m)
  dfs(m,visitados,22)
}

main()
