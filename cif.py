#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:58:09 2022

@author: imad
"""



from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifParser
query="mp-984"
Mapi_key="fbBViKxzZG36ESts"
mpr=MPRester(Mapi_key)
struct=mpr.get_structures(query)
print(struct)

struccif=mpr.get_data(query,data_type='',prop="cif").get("cif")
with open("{}.cif".format(query),"w") as output:
    output.write(struccif)
print(struccif)