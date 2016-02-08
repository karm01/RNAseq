#!/usr/bin/env python
data = {}
cepas = []
FH = open ("names.txt", "r")
for renglon in FH:
  CFH = open ("%s/abundance.tsv" % renglon.strip())
  cepas.append(renglon.strip()) #se hace el arreglo con el nombre de las cepas
  for linea in CFH: #rellena el diccionario con los genes y los conteos
    items = line.strip().split("\t")
    if items[0] in data:
      data[items[0]].append(int(items[3]))
    else:
      data[items[0]] = [int(items[3])]
OUT = open ("conteos-totales.tsv", "w+")
OUT.write("id\t")
for cepa in cepas:
  OUT.write("%s\t" % cepa)
OUT.write("\n")
for key, values in data.iteritems():
  OUT.write("%s\t" % key)
  for value in values:
    OUT.write("%s\t" % values)
  OUT.write("\n")


  


    
