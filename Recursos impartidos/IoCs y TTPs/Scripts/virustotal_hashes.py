#@creator Ivan Portillo & Claudia Sánchez-Girón - XVIII Jornadas STIC CCN-CERT
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
import json
import os
import time
from conf import API_VT


def search_hash(hash_id):

    headers = {
        "accept": "application/json",
        "x-apikey": API_VT
    }
	
    url = 'https://www.virustotal.com/api/v3/files/%s' %hash_id
	

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Convertir la respuesta a JSON
        data = response.json()
        nombre_fichero = 'hash_'+ hash_id +'.json'
        
        # Guardar el JSON en un archivo
        with open(nombre_fichero, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    else:
        print(f"Error en la solicitud: {response.status_code}")
        print(response.text)

def search_virustotal():

	hashes = []
	hashes_file = open('hashes.txt','r')

	for hash in hashes_file.read().split('\n'):
		if len(hash) == 0:
			#For drop a empty line in a List
			print("Drop empty line")
		else:
			print("--------------")
			hash_search = hash.split('\r' )[0]


			print("Hash analizado: "+ hash_search)
			dict_hashes = search_hash(hash_search)
			time.sleep(4)
		

	hashes_file.close()

if __name__ == '__main__':
	search_virustotal()