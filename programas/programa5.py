# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    regex = re.compile(r"(\s[a-z][a-z, A-Z, \_, 0-9]*:.*=[a-z, \_, 0-9][a-z, A-Z, \_, 0-9,\(, \)]*([\-, \/, \*, \+ ]*[a-z, \_, 0-9][a-z, A-Z, \_, 0-9,\(, \)]*)*)", flags = 0)
    all_match = regex.findall( texto )
    res = ""
    if all_match:
        regex1 = re.compile(r"\s*:.*=\s*", flags = 0)
        regex2 = re.compile(r"\spara\s", flags = 0) 
        ultimo = len(all_match)
        for m in all_match:
            maux1 = regex1.sub(",", m[0])
            maux2 = regex2.sub("", maux1)
            maux3 = re.sub(r"^\s", "", maux2)
            maux4 = re.sub(r"\s*$", "", maux3)
            if ultimo == 1 :
                res += "(" + maux4 + ")"
            else:
                 res += "(" + maux4 + ")\n"
            ultimo =  ultimo - 1  
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
