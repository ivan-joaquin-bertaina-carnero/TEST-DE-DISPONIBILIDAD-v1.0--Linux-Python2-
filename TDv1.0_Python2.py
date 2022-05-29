#-----------------------------------------------------------------------------------------------
# -*- coding: latin-1 -*-
#-----------------------------------------------------------------------------------------------

from datetime import datetime
import threading    
import socket       
import os
import time
import random
id_nro_prueba=0
lista=[]
archivo_urls_ips="urls_ips.txt"

#-----------------------------------------------------------------------------------------------

semilla=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_aleatorio_1=random.randint(0, int(len(semilla)-1))
num_aleatorio_2=random.randint(0, int(len(semilla)-1))
num_aleatorio_3=random.randint(0, int(len(semilla)-1))
num_aleatorio_4=random.randint(0, int(len(semilla)-1))


#-----------------------------------------------------------------------------------------------

def generar_id_sesion():
	id_sesion = str(semilla[num_aleatorio_1])+str(semilla[num_aleatorio_2])+str(semilla[num_aleatorio_3])+str(semilla[num_aleatorio_4])
	return id_sesion

id_s_actual=generar_id_sesion()

#-----------------------------------------------------------------------------------------------

def limpiar_pantalla():
	command = 'clear'
	if os.name in ('nt', 'dos'): 
		command = 'cls'           
	os.system(command)

#-----------------------------------------------------------------------------------------------

def separador():
	print (chr(27)+"[1;36m"+"-------------------------------------------------------------------------------"+chr(27)+"[0;37m")

#-----------------------------------------------------------------------------------------------

def pantalla_principal():
    limpiar_pantalla()
    print(chr(27)+"[1;36m")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # #                                       # # # # # # # # # #")
    print(" # # # # # # # # # #      TEST DE DISPONIBILIDAD V1.0      # # # # # # # # # #")
    print(" # # # # # # # # # #                                       # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(chr(27)+"[1;37m")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #") 
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(chr(27)+"[1;36m")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # #                                       # # # # # # # # # #")
    print(" # # # # # # # # # #    I.J.B. - ARGENTINA - 30/04/2022    # # # # # # # # # #")
    print(" # # # # # # # # # #                                       # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(" # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print(chr(27)+"[0;37m")

#-----------------------------------------------------------------------------------------------

def titulo(texto):
	print(chr(27)+"[1;33;40m"+texto)
	print('\033[0;m')
	

#-----------------------------------------------------------------------------------------------

def esta_disponible(url_o_ip,intentos):
	resultado1 = os.system("fping -r "+str(intentos)+" -q " + url_o_ip + " >/dev/null")
	mensaje1 = resultado1
	try:
		resultado2 = os.system("curl --connect-timeout 1 --max-time 2 -f -I -sS "+ url_o_ip + " >/dev/null")
		mensaje2 = resultado2
	except:
		pass
	if resultado1==0:
		resultado1='True'
	else:
		resultado1='False'
	if resultado2==0:
		resultado2='True'
	else:
		resultado2='False'
	if resultado1=='True' or resultado2=='True':
		print(chr(27)+"[1;37m"+marca_de_tiempo(0)+chr(27)+"[0;37m"+" -> "+url_o_ip+" -> "+chr(27)+"[1;32m"+"PERFECTO!!!"+chr(27)+"[0;37m")
		reporte=generar_reporte(url_o_ip+'.csv','a')
		reporte.write(id_s_actual+","+str(id_nro_prueba)+","+marca_de_tiempo(1)+","+url_o_ip+",EN LINEA,"+str(mensaje1)+","+str(mensaje2)+"\n")
		time.sleep(1)
		reporte.close()
		r_general=generar_reporte('Resultados.csv','a')
		r_general.write(id_s_actual+","+str(id_nro_prueba)+","+marca_de_tiempo(1)+","+url_o_ip+",EN LINEA,"+str(mensaje1)+","+str(mensaje2)+"\n")
		r_general.close()
	else:
		print(chr(27)+"[1;37m"+marca_de_tiempo(0)+chr(27)+"[0;37m"+" -> "+url_o_ip+" -> "+chr(27)+"[1;31m"+"NO RESPONDE!!!"+chr(27)+"[0;37m")
		reporte=generar_reporte(url_o_ip+'.csv','a')
		reporte.write(id_s_actual+","+str(id_nro_prueba)+","+marca_de_tiempo(1)+","+url_o_ip+",NO RESPONDE,"+str(mensaje1)+","+str(mensaje2)+"\n")
		reporte.close()
		r_general=generar_reporte('Resultados.csv','a')
		r_general.write(id_s_actual+","+str(id_nro_prueba)+","+marca_de_tiempo(1)+","+url_o_ip+",NO RESPONDE,"+str(mensaje1)+","+str(mensaje2)+"\n")
		r_general.close()	

#-----------------------------------------------------------------------------------------------

def agregar_cero(numero):
	if numero<10:
		texto = "0"+str(numero)
	else:
		texto = str(numero)
	return(texto)

#-----------------------------------------------------------------------------------------------

def generar_reporte(nombre, modo):
  try:
    reporte = open(nombre, modo)
    return reporte
  except OSError as err:
    print("Error: {0}".format(err))
  return

#-----------------------------------------------------------------------------------------------

def cargar_urls_ips(nombre, modo):
  try:
    archivo_urls_ips = open(nombre, modo)
    return archivo_urls_ips
  except OSError as err:
    print("Error: {0}".format(err))
  return

#-----------------------------------------------------------------------------------------------

def marca_de_tiempo(tipo_de_salida):
	fecha_y_hora = datetime.now()
	dia = agregar_cero(fecha_y_hora.day)
	mes = agregar_cero(fecha_y_hora.month)
	anio = agregar_cero(fecha_y_hora.year)
	hora = agregar_cero(fecha_y_hora.hour)
	minutos = agregar_cero(fecha_y_hora.minute)
	segundos = agregar_cero(fecha_y_hora.second)
	microsegundos = str(fecha_y_hora.microsecond)
	if(tipo_de_salida==1):
		m_d_t = dia + "/" + mes + "/" + anio + "," + hora + "," + minutos + "," + segundos + "," + microsegundos 
	else:
		m_d_t = "[" + dia + "/" + mes + "/" + anio + "-" + hora + ":" + minutos + ":" + segundos + "]"
	
	return(m_d_t)

#-----------------------------------------------------------------------------------------------

r_general=generar_reporte('Resultados.csv','a')
r_general.write("SESION,NRO_PRUEBA,FECHA,HORA,MINUTOS,SEGUNDOS,MICROSEGUNDOS,URL_O_IP_DESTINO,ESTADO,PING,CURL"+"\n")
r_general.close()

while(1):
	archivo=cargar_urls_ips(archivo_urls_ips, "r")
	for linea in archivo:
		lista.append(linea[0:-1])
	pantalla_principal()
	separador()
	print(chr(27)+"[1;37m"+"["+id_s_actual+"] Se cargaron "+str(len(lista))+" elementos desde el archivo "+archivo_urls_ips+chr(27)+"[0;37m")
	separador()
	time.sleep(1)
	x=int(len(lista))
	for elemento in range(0,x):
		item=str(lista[elemento])
		esta_disponible(item,1)
		separador()
		id_nro_prueba=id_nro_prueba+1
		
	while(len(lista)):
		item=str(lista[0])
		#print("Eliminando elemento [0] del array -> "+item)
		#time.sleep(1)
		lista.pop(0)
	time.sleep(1)




