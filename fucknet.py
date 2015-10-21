# *-* encoding: utf-8 *-*
import urllib
import time

from subprocess import call

class Fucker(object):
	def __init__(self):
		self.range = "192.168.151."
		self.start = 1
		self.end = 254
		self.current_ip = 1
		self.log = "index.txt"
		self.url_test = "http://facebook.com"
		self.locked = True
		self.ip_full = self.range+str(self.current_ip)
		self.if_name = "wlan0"
		self.key = "checkpoint"
		self.ips_ok = [] # Ips con permisos
		self.ips_free = []  # Ips con permisos que no están siendo usadas

	def test_url(self):
		try:
			urllib.urlretrieve(self.url_test, filename=self.log)
			archivo 	= open(self.log)
			contenido 	= archivo.read()
			if self.key in contenido or "ERR_CONNECTION_RESET" in contenido:
				return False
			else:
				return True
		except Exception:
			print "No se pudo conectar con "+self.url_test+", parece haber problemas con la conexión. Verifique con sudo ifconfig "
			return False

	def change_ip(self):
		if self.current_ip <= self.end:
			ip_comm =str(self.range)+str(self.current_ip) 
			call(["ifconfig", self.if_name, ip_comm, "netmask", "255.255.255.0", "broadcast", self.range+"255"])
			print "Configurando interface a "+self.if_name+" a "+ip_comm
			self.current_ip = self.current_ip+1
			new_ip = str(self.range)+str(self.current_ip)
			self.ip_full = new_ip
		else:
			return False

	def run(self):
		print "Comenzando pruebas de red, por favor espere...."
		while (self.current_ip<=self.end):
			time.sleep(3)
			test = self.test_url()
			if test:
				print "   *** FUNCIONA "+str(self.url_test)+" CON "+str(self.ip_full)
				self.ips_ok.append(str(self.ip_full))
			self.change_ip()


		if len(self.ips_ok)>0:
			print "Las ips sin restricciones a la url "+self.url_test+" son: "
			for x in self.ips_ok:
				print x
		else:
			print "Lo lamento, no pude encontrar IPS sin restricciones :("
		
######################################################################################################
##
## 										VAMOS A PROBAR
## 
######################################################################################################		
fuck = Fucker()
fuck.run()