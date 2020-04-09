# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    op_booleanas = re.findall(r"([^<>&=\-\(]|\s|[a-z, A-Z, 0-9,\_])([><]|(&&)|(>=)|(<=)|(==)|(=&&))([^<>&=\-\), A-Z]|\s|[a-z, 0-9, \_])", texto, flags = 0)
    op = re.findall(r"[^\/\*\-+<>][\/\*\-+][^\/\*\-+<>]", texto, flags = 0)  
    res = ""
    res += "booleanas: " + str(len(op_booleanas))
    res += "\nno booleanas: " + str(len(op))
    return res 

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
