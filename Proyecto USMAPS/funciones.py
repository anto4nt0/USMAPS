import networkx as nx
import folium 
from folium.plugins import MiniMap
import webbrowser
def leer_archivo(archivo):
    try:
        arch= open(archivo)
        return arch
    except OSError:
        print('problemas ', arch.name)
        raise

def idAubi(archivo,id):
    ubi=" "
    arch= leer_archivo(archivo)
    for linea in arch:
        datos= linea.strip().split('/')
        if id==datos[0]:
            ubi=(datos[1])
    return ubi

def ubiAid(archivo,ubi):
    id=" "
    arch= leer_archivo(archivo)
    for linea in arch:
        datos= linea.strip().split('/')
        if ubi==datos[1]:
            id=(datos[0])
    return id

def ubicacionAubi(archivo,ub):
    ubfun=""
    arch= leer_archivo(archivo)
    for linea in arch:
        datos= linea.strip().split('/')
        if ub in datos:
            ubfun=(datos[1])
    return ubfun



def uAu(archivo,ubi):
    arch= leer_archivo(archivo)
    x=' '
    for linea in arch:
        datos= linea.strip().split('/')
        if datos[1]==ubi:
            x=datos[-1]
    return x

def ubiAcoor(archi1,ubi):
    coor=[]
    arch= leer_archivo(archi1)
    for linea in arch:
        datos= linea.strip().split('/')
        if ubi==datos[0]:
            n=float(datos[4])
            m=float(datos[5])
            coor.append(m)
            coor.append(n)
    return coor
def algruta(ubi,des):

    G = nx.read_graphml('c.graphml')
    h=(list(G.nodes))
    lista=[]
    for i in h:
        r=idAubi('limitesPasillos.txt',i)
        lista.append(r)
    inicio=ubicacionAubi('limitesPasillos.txt',ubi)
    fin=ubicacionAubi('limitesPasillos.txt',des)

    archivo_graphml = "c.graphml"  # Reemplaza con la ruta a tu archivo GraphML
    nodo_inicio = ubiAid('limitesPasillos.txt',inicio)  # Reemplaza con tu nodo de inicio
    nodo_fin = ubiAid('limitesPasillos.txt',fin)  # Reemplaza con tu nodo de fin

# Encontrar la ruta más corta
    def encontrar_ruta_mas_corta(G, nodo_inicio, nodo_fin):

        try:
            ruta_mas_corta = nx.shortest_path(G, source=nodo_inicio, target=nodo_fin, weight='weight')
            return ruta_mas_corta
        except nx.NetworkXNoPath:
            print(f"No hay ruta disponible entre {nodo_inicio} y {nodo_fin}.")
            return None
        except nx.NodeNotFound as e:
            print(e)
        return None
    ruta_mas_corta = encontrar_ruta_mas_corta(G, nodo_inicio, nodo_fin)
    ruta=[]
    for i in ruta_mas_corta:
        s=idAubi('limitesPasillos.txt',i)
        ruta.append(s)
    la_ruta=[]
    for i in ruta:
        x=uAu('limitesPasillos.txt',i)
        la_ruta.append(x)

    rutacorta=[]
    for i in la_ruta:
        n=ubiAcoor('salaPasillo.txt',i)
        rutacorta.append(n)


    popuptext= '<b>ubicación</B>'
    popuptext2= '<b>destino</B>'
    edificioC= folium.Map(location=[-33.03598990, -71.5946348], zoom_start=22) 
    folium.plugins.AntPath(
        locations=rutacorta,
        color="#FF0000",
        weight=5,
        ).add_to(edificioC)
    web= edificioC.save('templates\edificioC.html')


    







