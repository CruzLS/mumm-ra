# -*- coding: utf-8 -*-

class Edades(object):

	def __init__(self):
		self.respuesta = ""

	def respuesta_edad(self):
		return self.respuesta	

	def edadX(self, anios):
		if(anios <= 0):
			self.respuesta = "No existes"
		elif(anios < 13):
			self.respuesta = "Eres nino"
		elif(anios < 18):	
			self.respuesta = "Eres fluorescent adolescent"
		elif(anios < 65):	
			self.respuesta = "Eres adulto"
		elif(anios < 120):	
			self.respuesta = "Eres adulto mayor"
		else:	
			self.respuesta = "Eres Mumm-Ra"		