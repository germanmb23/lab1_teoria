# -*- coding: utf-8 -*-
import re
import sys

#probando git

def programa(texto):
    # Implementar programa
    texto = re.sub(r"^\s*//.*\n", "", texto)
    texto = re.sub(r"\s*//.*", "", texto)
    texto = re.sub(r"^\s*[*]{3}.*[*]{3}\n", "", texto, flags=re.DOTALL)
    texto = re.sub(r"\s*[*]{3}.*[*]{3}", "", texto, flags=re.DOTALL)
    return texto

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
