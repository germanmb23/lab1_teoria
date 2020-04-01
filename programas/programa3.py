# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    nombre = re.findall(r"funcion\s+(\w*)", texto)
    res = ""
    parametros = re.findall(r"funcion.*?\((.+?)\)", texto, re.S)
    tipo_salida = re.findall(r"funcion\s+.*?->\s*(.+?)\s*\{", texto)
    res += nombre[0]
    if parametros : res += f"\n{parametros[0]}"
    if tipo_salida : res += f"\n{tipo_salida[0]}"
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
