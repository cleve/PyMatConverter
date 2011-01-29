#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       transformador.py
#       
#       Copyright 2011 cleve <mauricio.cleveland@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import xlwt
import time

def formatear(linea):
	'''Elimino llave en ultimo elemento del vector'''
	
	for lista in linea:
		if '}' in lista[-1]:
			lista[-1] = lista[-1].split('}')[0]
	
	return linea

def complejo(numero):
	''' Sacar parte real del numero'''
	
	valor = numero
	pos = valor.index('I')
	
	while 1:
		if valor[pos] != ' ':
			pos-=1
		elif valor[pos] == ' ':
			#print valor[:pos-2]
			return valor[:pos-2]
			break
		
		elif pos==0:
			return 'no'
		
	
def limpiar(texto):
	''' Saco caracteres que no son numericos del texto completo'''
	if '{' in texto:
		
		texto = texto.replace('{','')
		
	
	if '\r\n' in texto:
		texto = texto.replace('\r\n','')

	return texto

def transformar(lista, nombre):
	try:
		linea_a_guardar = []
	
		'''
		Cargo escritor de archivos excel 2003
		'''
		
		#ws.write(0, 0, 'Test', style0)
		
		font0 = xlwt.Font()
		font0.name = 'Arial'
		

		style0 = xlwt.XFStyle()
		style0.font = font0

		style1 = xlwt.XFStyle()
		

		wb = xlwt.Workbook()
		ws = wb.add_sheet('Mediciones')
		
		
		columna_tempo = 0
		marca = True
		linea = ''
		texto = ''
		
		
		for ruta_archivo in lista:
			
			fil = 0
			col = columna_tempo
			
			archivo = open(ruta_archivo, 'r')
			
			texto = archivo.read()           #Archivo de texto completo
			
			texto = limpiar(texto)           #Limpiar de caracteres invalidos
			
			archivo.close()
			
			if '=' in texto:
				linea = texto.split('=')   #Separar lineas
			
			linea = linea[1:]
			
			for fila in linea:               #Obtengo filas
				linea_a_guardar.append(fila.split(','))
				
			linea_a_guardar = formatear(linea_a_guardar)
			
			for fila_numero in linea_a_guardar:
				
				for valor in fila_numero:		
					try:
						numero = float(valor)
						
					
					except:
						if 'I' in valor:
							
							numero = complejo(valor)
							numero = float(numero)
							
						
						elif '*^' in valor:
							
							numero = valor.replace('*^', 'e')
							numero = float(numero)
							
						
					
					ws.write(fil, col, numero, style0)
					col+=1
				
				
				fil+=1
				col = columna_tempo
			
			columna_tempo = columna_tempo + len(fila_numero) + 1
			linea_a_guardar = []
			
			
			wb.save(nombre)
					
		return 'ok'	

	except:
		return -1
