import os
import re
path='clientes\\'
#Archivos: funciones que tienen directa relacion con los archivos
#******************************************************************************
#Nombre: lista_txt
#Parametros: String path (ruta donde se encuentran los documentos)
#Retorno: Lista de String ListaDocumentos (contiene una lista de documentos .dat)
#Descripcion: Busca todos los documentos .dat dentro de una determinada carpeta
def lista_txt(path):
	print path
	ListaDocumentos = []
	listaDirectorio = os.walk(path)
	for root, dirs, files in listaDirectorio:
	    for fichero in files:
	    	print fichero
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == ".dat"):
	            ListaDocumentos.append(nombreFichero+extension)
	            mostrar_lista('encontrado','\033[92m',ListaDocumentos,'Buscando...')

	mostrar_lista('encontrado','\033[92m',ListaDocumentos,'Busqueda Finalizada. '+'\033[91m'+str(len(ListaDocumentos))+'\033[0m'+' documentos encontrados')
	return ListaDocumentos

#Nombre: leer
#Parametros: String path (ruta donde se encuentran los documentos)
#Retorno: Boolean error (False si el documento esta correcto y True si contiene errores )
#Descripcion: leer un documento y comprueba si esta bien escrito
def leer(path):
	archivo = open(path, "r")
	error = False;
	for linea in archivo.readlines():
		forma=linea.split(': ')
		if (forma[0] == 'Nombre'):
			if (nombre(forma[1])):
				error=True
		elif (forma[0] == 'Rut'):
			if (rut(forma[1])):
				error=True
		elif (forma[0] == 'Fecha de Nacimiento'):
			if (fecha(forma[1])):
				error=True
		elif (forma[0] == 'Direccion'):
			if (direccion(forma[1])):
				error=True
		elif (forma[0] == 'Telefono'):
			if (telefono(forma[1])):
				error=True
		elif (forma[0] == 'E-Mail'):
			if (email(forma[1])):
				error=True
		
	archivo.close()
	if (comprobar_orden(path)):
		error=True
	return error

#Comprobar informacion: las siguientes funciones comprueban que un string este bien escrito segun los requisitos del sistema
#******************************************************************************
#Nombre: comprobar_orden
#Parametros: String path (ruta donde se encuentran los documentos)
#Retorno: Boolean error (False si el documento esta correcto y True si contiene errores )
#Descripcion: leer un documento y comprueba si el orden de los elementos se encuentra correcto
def comprobar_orden(path):
	archivo = open(path, "r")
	error = False;
	lineas=[]
	for linea in archivo.readlines():
		forma=linea.split(': ')
		lineas.append(forma[0])
	archivo.close()
	if (lineas[0] != 'Nombre'):
		error=True
	if (lineas[1] != 'Rut'):
		error=True
	if (lineas[2] != 'Fecha de Nacimiento'):
		error=True
	if (lineas[3] != 'Direccion'):
		error=True
	if (lineas[4] != 'Telefono'):
		error=True
	if (lineas[5] != 'E-Mail'):
		error=True
	return error


#Nombre: nombre
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo nombre del documento comprueba que esta este bien escrita
def nombre(inf):
	error = True
	if re.match('([A-Z]{1}[a-z]*\s)+([A-Z]{1}[a-z]*)',inf):
		error=False
	return error

#Nombre: rut
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo rut del documento comprueba que esta este bien escrita
def rut(inf):
	error = True
	if re.match('\d{1,2}[\.]\d{3}[\.]\d{3}[-][\d|k]',inf):
		error=False
	return error

#Nombre: fecha
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo fecha de nacimiento del documento comprueba que esta este bien escrita
def fecha(inf):
	error = True
	if re.match('\d{2}[/]\d{2}[/]\d{4}',inf):
		error=False
	return error

#Nombre: direccion
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo direccion del documento comprueba que esta este bien escrita
def direccion(inf):
	error = True
	if re.match('([A-Z]{1}[a-z]*\s)?([A-Z]{1}[a-z]*)[,]\s\d+[,]\s([A-Z]{1}[a-z]*\s)?([A-Z]{1}[a-z]*)[,]\s([A-Z]{1}[a-z]*\s)?([A-Z]{1}[a-z]*)',inf):
		error=False
	return error

#Nombre: telefono
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo telefono del documento comprueba que esta este bien escrita
def telefono(inf):
	error = True
	if re.match('\(\+\d{3}\)\d{3,}',inf):
		error=False
	return error

#Nombre: email
#Parametros: String inf (string a comprobar)
#Retorno: Boolean error (False si el string esta correcto y True si contiene errores )
#Descripcion: segun la informacion del campo e-mail del documento comprueba que esta este bien escrita
def email(inf):
	error = True
	if re.match('[a-z\.-_]+@[a-z-_]+\.[a-z]+',inf):
		error=False
	return error

#Reparar: las siguientes funciones modifican la informacion de cada campo para que se acomode a los requisitos del sistema 
#******************************************************************************
#Nombre: reparar
#Parametros: String path (ruta donde se encuentran los documentos)
#Retorno: -
#Descripcion: edita el documento para reparar tanto el orden y la informacion de los campos
def reparar(path):
	archivo = open(path,"r")
	for linea in archivo.readlines():
		forma=linea.split(': ')
		if (forma[0] == 'Nombre'):
			nombre=reparar_nombre(forma[1])
		elif (forma[0] == 'Rut'):
			rut=reparar_rut(forma[1])
		elif (forma[0] == 'Fecha de Nacimiento'):
			fecha=reparar_fecha(forma[1])
		elif (forma[0] == 'Direccion'):
			direccion=reparar_direccion(forma[1])
		elif (forma[0] == 'Telefono'):
			telefono=reparar_telefono(forma[1])
		elif (forma[0] == 'E-Mail'):
			email=reparar_email(forma[1])
	archivo.close()
	archivo =open(path,"w")
	archivo.write("Nombre: "+nombre)
	archivo.write("Rut: "+rut)
	archivo.write("Fecha de Nacimiento: "+fecha)
	archivo.write("Direccion: "+direccion)
	archivo.write("Telefono: "+telefono)
	archivo.write("E-Mail: "+email)
	archivo.close()


		
#Nombre: reparar_nombre
#Parametros: String inf (string a reparar)
#Retorno: String nombreReparado (string reparado)
#Descripcion: Repara el campo nombre segun los requerimientos entregados
def reparar_nombre(inf):
	nombre = inf.split(' ')
	#elimina espacios extras
	while (nombre.count('') != 0):
		nombre.remove('')
	#vuelve mayuscula la primera letra de cada palabre y el resto miniscula
	nombreReparado=[]
	for aux in nombre:
		nombreReparado.append(aux.capitalize())
	return ' '.join(nombreReparado)

#Nombre: reparar_rut
#Parametros: String inf (string a reparar)
#Retorno: String rutReparado (string reparado)
#Descripcion: Repara el campo rut segun los requerimientos entregados
def reparar_rut(inf):
	rutReparado =[]
	#elimina todo lo que no sea un numero en el rut
	for aux in inf:
		if (re.match('\d',aux)):
			rutReparado.append(aux)
	largo=len(rutReparado)
	rutReparado.insert(largo-1,'-')
	rutReparado.insert(largo-4,'.')
	rutReparado.insert(largo-7,'.')
	rutReparado.extend('\n')
	return ''.join(rutReparado)

#Nombre: reparar_fecha
#Parametros: String inf (string a reparar)
#Retorno: String fechaReparado (string reparado)
#Descripcion: Repara el campo fecha segun los requerimientos entregados
def reparar_fecha(inf):
	fechaReparada =[]
	fecha=[]
	#cambia la separacion por '/'
	for aux in inf:
		if (re.match('\d',aux)):
			fecha.append(aux)
		else:
			fecha.append('/')
	#elimina el '/' que se agrego remplazando '\n' y lo vuelve a remplazar por un '\n'
	fecha.pop(len(fechaReparada)-1)
	fecha.extend('\n')
	#se une la lista para, posteriormente dividirla por '/' y de este modo identificar dia, mes y ano
 	
	fecha = ''.join(fecha)
	fecha = fecha.split('/')
	for aux in fecha:
		if (len(aux)==1):
			fechaReparada.append('0'+aux)
		else:
			fechaReparada.append(aux)
	fechaReparada='/'.join(fechaReparada)
	return fechaReparada

#Nombre: reparar_direccion
#Parametros: String inf (string a reparar)
#Retorno: String direccionReparado (string reparado)
#Descripcion: Repara el campo direccion segun los requerimientos entregados
def reparar_direccion(inf):
	direccion = inf.split(', ')
	direccionReparada = []
	#se utiliza la funcion reparar_nombre para los nombres de la calle, ciudad y pais
	direccionReparada.append(reparar_nombre(direccion[0]))
	direccion[1] = direccion[1].split(' ')
	direccionReparada.append(''.join(direccion[1]))
	direccionReparada.append(reparar_nombre(direccion[2]))
	direccionReparada.append(reparar_nombre(direccion[3]))
	return ', '.join(direccionReparada)

#Nombre: reparar_telefono
#Parametros: String inf (string a reparar)
#Retorno: String telefonoReparado (string reparado)
#Descripcion: Repara el campo telefono segun los requerimientos entregados
def reparar_telefono(inf):
	telefonoReparado =[]
	#elimina todo lo que no sea un numero en el telefono
	for aux in inf:
		if (re.match('\d',aux)):
			telefonoReparado.append(aux)
	#se agregan los caracteres especiales al telefono
	telefonoReparado.insert(0,'(+')
	telefonoReparado.insert(4,')')
	telefonoReparado.extend('\n')
	return ''.join(telefonoReparado)

#Nombre: reparar_email
#Parametros: String inf (string a reparar)
#Retorno: String emailReparado (string reparado)
#Descripcion: Repara el campo e-mail segun los requerimientos entregados
def reparar_email(inf):
	return inf.lower()

	

#funciones auxiliares: funciones que muestran datos por pantalla o que no tienen directa relacion con los requerimientos, pero 
#******************************************************************************
#Nombre: clear
#Parametros: -
#Retorno: -
#Descripcion: escribe espacios en blanco para limpiar los textos en consola
def clear():
	contador = 0
	while contador < 100:
	   print '\n'
	   contador += 1
#Nombre: mostrar_lista
#Parametros: String accion, String pieDeLista, lista de String ( informacion que se muestra por pantalla), string color ( codigo del color del texto)
#Retorno: -
#Descripcion: escribe informacion en pantalla, puntualmente muestra las acciones y resultados de acciones realizadas sobre los documentos
def mostrar_lista(accion, color, lista, pieDeLista):
	clear()
	for elemento in lista:
		print ('['+color+accion+'\033[0m'+']	'+elemento)
	print pieDeLista


#se realizan llamados a funciones de encontrar los documentos y agrega los documentos con errores a una lista.
lista_txt=lista_txt(path)
clear()
errores=[]
for nombreTxt in lista_txt:
	if(leer(path+nombreTxt)):
		errores.append(path+nombreTxt)
		print ('['+'\033[91m'+'ERROR'+'\033[0m'+']    '+nombreTxt)
	else:
		print ('['+'\033[92m'+'OK'+'\033[0m'+']       '+nombreTxt)
#consulta si quiere reparar los documentos danado.
exit=False

if (len(errores)>0):

	while (not exit):

		respuesta = raw_input ('Desea reparar los errores encontrados? S/N ')
		#si la respuesta es 's' los repara y muestra mensaje 
		if (respuesta == 'S' or respuesta == 's'):
			exit=True
			for error in errores:
				nombreError =error.split('\\')
				print ('['+'\033[92m'+'Reparado'+'\033[0m'+'] '+nombreError[1])
				reparar(error)
		#si la respuesta es 'n' no realiza acciones
		elif (respuesta == 'N' or respuesta == 'n'):
			exit=True
			print ('Documentos no modificados')
		#cualquier otra respuesta es invalida
		else:
			print ('respuesta no valida')
else:
	print ('No se encontraron documentos con errores')
