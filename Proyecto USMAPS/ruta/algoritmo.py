
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









