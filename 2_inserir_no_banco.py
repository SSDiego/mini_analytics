# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:51:50 2022

@author: sp2di
"""

import os
import sqlite3
import pandas as pd

os.chdir(r"path")

conn = sqlite3.connect('bd_indisponibilidade')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS tabela_ind (Agente text, Contrato text, IdAgente number, Ano number, Ruracaoo_Real_Minutos number)')
conn.commit()

df = df_indisponibilidade

df.to_sql('tabela_ind', conn, if_exists='replace', index = False)