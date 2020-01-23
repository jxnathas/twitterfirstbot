# -*- coding: utf-8 -*-
import random, os, sys
import tweepy

text_file = open("palavras.txt", "r")       #Abrimos a lista de palavras
palavras = text_file.readlines()        #E convertemos numa lista

consumer_secret = ""
consumer_key = ""           #Credencias do twitter dev
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)          #Logando 

numero = int(palavras[0])  #A palavra atual esta salvo no indice 0 da lista

texto = "Foda-se " + palavras[numero]
#postando o texto

    
api.update_status(status=texto) #Então postamos no twitter o texto gerado

palavras[0] = str(numero + 1) + '\n'     #Incrementos o contador

with open('palavras.txt', 'w') as file:
    file.writelines(palavras)       #E salvamos devolta no arquivo
