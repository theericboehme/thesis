#!/usr/bin/env python
# coding: utf-8

# In[15]:


#import libraries

#essential
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import pylab as pl
import seaborn as sns
from sklearn.linear_model import LinearRegression
import datetime as dt
import scipy as sp
import statsmodels.api as sm

from yahoofinancials import YahooFinancials

from tqdm import tqdm_notebook as tqdm

#scraping
from bs4 import BeautifulSoup
import requests

import time

import webbrowser


#defs - output must be dataframe with index "date" and column "close"
def import_dax():
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/DAX_historisch.csv")
    df["Datum"] = pd.to_datetime(df["Datum"])
    df["Schlusskurs"]=df["Schlusskurs"].astype(float)
    df.rename(columns = {"Schlusskurs":"close"}, inplace = True)
    df = df[::-1]
    df.rename(columns = {"Datum":"date"}, inplace = True)
    df.set_index("date", inplace = True)
    return df

def import_ftse_mib():
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/FTSE_MIB_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_aex():
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/AEX_historisch.csv")
    df = df[["Date","Close"]]
    df.rename(columns = {"Date":"date","Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_atx():
    df = pd.read_excel("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/ATX_historisch.xlsx")
    df = df[["Datum","Schlusspreis<sup>4</sup>"]]
    df.rename(columns = {"Datum":"date","Schlusspreis<sup>4</sup>":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_ftse_jse():
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/FTSEJSE_All_Share_Index_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_rtsi():
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/RTSI_historisch.csv")
    df = df[["Date","Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date","Close":"close"}, inplace = True)
    df.set_index("date", inplace = True)
    return df

# ------------ just added ----------------------------
#def import_sse(): #Shanghai Stock Index (China)
#    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/SSE_historisch.csv")
#    df = df[["Date"," Close"]]
#    df = df[::-1]
#    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
#    df["date"] = pd.to_datetime(df["date"])
#    df.set_index("date", inplace = True)
#    return df

def import_klse(): #Kuala Lumpur Stock Index (Malaysia)
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/KLSE_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_psei(): #Philippines
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/PSEi_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_bse(): #India
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/S&PBSE_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_kospi(): #Kuala Lumpur Stock Index (Malaysia)
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/KOSPI_historisch.csv")
    df = df[["Date"," Close"]]
    df = df[::-1]
    df.rename(columns = {"Date":"date"," Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df

def import_sse(): #Shanghai Stock Index (China)
    df = pd.read_csv("C:/Users/eric_/Dropbox/Studium/Bachelorarbeit/Data/historische Preise/SSE_historisch2.csv")
    df = df[["Date","Close"]]
    df.rename(columns = {"Date":"date","Close":"close"}, inplace = True)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace = True)
    return df
    
    #change format
    new_index = []
    for i in df.index:
        i = i.split(".")
        i = "{}-{}-{}".format(i[-1],i[1],i[0])
        new_index.append(i)
    df.index = new_index
    df.index = pd.to_datetime(df.index)
    return df