# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:50:49 2022

@author: sp2di
"""

import os 
import pandas as pd

os.chdir(r"path")

df_indisponibilidade_aneel = pd.read_excel("BASE DE DADOS - 2017 a 2021 - ABERTURA TS.xlsx", sheet_name="INDISPONILIDADE")

os.chdir(r"path")

df_indisponibilidade_satra = pd.read_excel("BASE-DE-DADOS_INDISP-SATRA.xlsx")


filtro_consistencia = ['Consistido'] 
filtro_situacao = ['Fechado', 'Fechado e Processado', 'Reprocessado']
filtro_contab = ['OPV', 'PPV', 'DPB'] 
    
df_satra_filtrado = 0
# selecao de rows com base em valores 
df_satra_filtrado = df_indisponibilidade_satra.loc[df_indisponibilidade_satra['Consistencia_ONS'].isin(filtro_consistencia)]
df_satra_filtrado = df_indisponibilidade_satra.loc[df_indisponibilidade_satra['Situacao'].isin(filtro_situacao)]                                               
df_satra_filtrado = df_indisponibilidade_satra.loc[df_indisponibilidade_satra['Forma_Contabilizacao'].isin(filtro_contab)]                                                  
df_satra_filtrado = df_indisponibilidade_satra.loc[df_indisponibilidade_satra['Duracao_Real_Minutos'] != 0]   
df_satra_filtrado = df_indisponibilidade_satra[~df_indisponibilidade_satra['Duracao_Real_Minutos'].isnull()]


a = pd.to_numeric(df_satra_filtrado['Duracao_Real_Minutos'])
a = a.div(60).round(5)

df_satra_filtrado['Duracao_Real_Minutos'] = a

a = pd.to_numeric(df_satra_filtrado['Duracao_Ajustada_Minutos'])
a = a.div(60).round(5)

df_satra_filtrado['Duracao_Ajustada_minutoos'] =  a


#Tabela de Indisponibilidade Completa
df_indisponibilidade_satra

#Tabela Indisponibilidade Com Filtros
df_satra_filtrado

#Tabela de Indisponibilidade
df_indisponibilidade = df_satra_filtrado.groupby(['Agente','Contrato','IdAgente','Holding','Ano'], as_index= False).Duracao_Real_Minutos.sum()
