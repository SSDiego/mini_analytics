# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:27:22 2022

@author: sp2di
"""


#
import requests
import io
from zipfile import ZipFile

url = "https://antigo.aneel.gov.br/web/guest/tomadas-de-subsidios?p_p_id=participacaopublica_WAR_participacaopublicaportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=1&_participacaopublica_WAR_participacaopublicaportlet_ideDocumento=47189&_participacaopublica_WAR_participacaopublicaportlet_tipoFaseReuniao=fase&_participacaopublica_WAR_participacaopublicaportlet_jspPage=%2Fhtml%2Fpp%2Fvisualizar.html"




r = requests.get(url)
z = ZipFile(io.BytesIO(r.content))
z.extractall("/path/to/destination_directory")



  
# specifying the zip file name
file_name = "BASES-DE-DADOS.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
  
    # extracting all the files
   
    zip.extract('BASES DE DADOS/BASE DE DADOS - 2017 a 2021 - ABERTURA TS.xlsx')
    print('Done!')
    
    


archive = ZipFile("BASES-DE-DADOS.zip", 'r')
xlfile = archive.open('BASES-DE-DADOS\BASE DE DADOS - 2017 a 2021 - ABERTURA TS.xlsx')
df = pd.read_excel(xlfile)
zip.extract('BASES DE DADOS/BASE DE DADOS - 2017 a 2021 - ABERTURA TS.xlsx')
