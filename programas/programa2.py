# -*- coding: utf-8 -*-
import re
import sys

from programa1 import programa as limpiar

def programa(texto):
    # Implementar programa
    texto = limpiar(texto)
    si = re.findall(r"\s+si\s", texto, re.DOTALL)
    para = re.findall(r"\s+para\s[^c][^a][^d][^a]", texto, re.DOTALL)
    paracada = re.findall(r"\s+para\scada\s", texto, re.DOTALL)
    mientras = re.findall(r"\s+mientras\s", texto, re.DOTALL)
    
    res = ""
    res += 'si: ' + str(len(si))
    res += "\npara: " + str(len(para))
    res += "\npara-cada: " + str(len(paracada))
    res += "\nmientras: " + str(len(mientras))
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
