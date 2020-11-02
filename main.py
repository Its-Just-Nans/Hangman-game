import tkinter as tk
import socket
import threading
import sys
import uuid
import turtle
import json


def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

 
def Transform(mot):
	mot=mot.translate({ord('é'):'e', ord('à'):'a', ord('è'):'e', ord('ê'):'e', ord('ù'):'u', ord('ç'):'c', ord('ô'):'o', ord('î'):'i', ord('ï'):'i', ord('â'):'a'	})
	return mot


def giveIndex(mot, lettre) :
	return [i for i, x in enumerate(mot) if x == lettre]


#
#Fonction qui permet de créer le serveur en ouvrant une socket
def server(port):
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host_name = get_ip()
	sock.bind((host_name, port))
	sock.listen(5)
	while True:
		client, address = sock.accept()
		print ("{} connected".format( address ))
		response = client.recv(255).decode("utf-8")
		print('Client->Server:')
		print(response)
		try:
			tab = json.loads(response)
			print('tab')
			print(tab)
			print(tab['MAC'])
			print(tab['command'])
			if 'getLetter' in response:
				print("il a l'attribut")
				valeur = {'MAC':'SERVEUR', 'command': 'getLetter', 'argument': MotRandom('liste_francais.txt') }
				print('Server->Client')
				sender(custom, valeur)
		except Exception as e:
			print(e)
		print('serveurSend ?')




def sender(varString, var):
	if varString == 'sendMAC' :
		valeur = json.dumps({'MAC': str(get_mac())}).encode()
		sock.send(valeur)
	elif varString == 'getLetter' :
		valeur = json.dumps({'MAC': str(get_mac()), 'command' : 'getLetter'}).encode()
		sock.send(valeur)
	elif varString == 'custom' :
		sock.send(var)
	else:
		pass
	print(valeur)



#Fonction pour checker l'input combinant adresse ip et port
def verifIPport(IPPort) :
	IPPort=IPPort.split(':')
	if len(IPPort) == 2 :
		try:
			if 1024 < int(IPPort[1]) < 65635 :
				ip=IPPort[0].split('.')
				if len(ip) == 4 :
					if  (0 < int(ip[0]) <= 255) and (0 < int(ip[1]) <= 255) and (0 < int(ip[2]) <= 255) and (0 < int(ip[3]) <= 255) :					
						return True
					else :
						return False
				else:
					return False
			else :
				return False
		except e:
			print(e)
			return False
	else :
		return False


def MotRandom(ficdico) :
	liste=open(ficdico,'rb')
	dico=liste.read().decode('utf-8')
	dicobon=dico.split("\n")
	mot=random.choice(dicobon)
	return mot

#
#Fonction qui permet de créer le client en ouvrant une socket
def client(chaine):
	global sock
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		address = chaine.split(':')[0]
		port = int(chaine.split(':')[1])
		print('Essaie de connection avec : ' + address + ':' + str(port))
		sock.connect((address, port))
		while True:
			response = sock.recv(255).decode("utf-8")
			print(response)
			response = json.loads(response)
			print(response)
			try:
				if hasattr(response, 'getLetter'):
					valeur = {'MAC':'SERVEUR', 'command': 'getLetter', 'argument': MotRandom('dico.txt') }
					send(valeur)
			except:
				pass
			if response != "":
				print('Client->Server:')
				print(response)
			else:
				return	
	except Exception as e:
		print(e)
		if hasattr(app, 'labelBug2'):
			app.labelBug2 = tk.Label(app, text = 'Connexion échouée', fg="red")
			app.labelBug2.pack()
		app.saisi_Client = tk.Entry(app, width=20)
		app.saisi_Client.pack(side="left")
		app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
		app.button_saisi.pack(side="right")
		app.label.destroy()


#
#Fonction qui fait l'affichage client (sert a relier le thread de socket avec le thread de tkinter
#Cette fonction varie en beaucoup en fonction de la valeur de la variable terminal
def user_display(step):
	global user_choix
	global thread
	global terminal
	if terminal == '-t':
		if step == 1:
			print('Vous êtes désormais un joueur Suspensus')
			entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			while not verifIPport(entry):
				entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			thread = threading.Thread(target=client, args=([entry]) )
			thread.daemon = True
			thread.start()
		elif step == 2:
			print('TO DO')
		elif step == 3:
			print('TO DO')
		elif step == 4:
			print('TO DO')
			
	#On veut tkinter, on va dans le else
	else:
		if step == 1:
			app.button_client.destroy()
			app.button_server.destroy()
			app.saisi_Client = tk.Entry(app, width=20)
			app.saisi_Client.pack(side="left")
			app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
			app.button_saisi.pack(side="right")
		elif step == 2:
			entry = app.saisi_Client.get()
			if not verifIPport(entry):
				try :
					app.labelBug.destroy()
				except :
					pass
				app.saisi_Client.destroy()
				app.button_saisi.destroy()
				if not hasattr(app, 'labelBug2'):
					app.labelBug = tk.Label(app, text = 'Mauvaise Ip veuillez recommencer', fg="red")
					app.labelBug.pack()
				app.saisi_Client = tk.Entry(app, width=20 )
				app.saisi_Client.pack(side="left")
				app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
				app.button_saisi.pack(side="right")
			else :
				try :
					app.labelBug.destroy()
					app.labelBug2.destroy()
				except :
					pass
				app.label = tk.Label(app, text= 'Connection à ' + entry +' ')
				app.label.pack(side="bottom")
				app.button_saisi.destroy()
				del app.button_saisi
				app.saisi_Client.destroy()
				thread = threading.Thread(target=client, args=([entry]) )
				thread.daemon = True
				thread.start()
				app.label.destroy()
				if not hasattr(app, 'button_saisi'):
					app.button_saisi = tk.Button(app, text="Commencer la partie", fg="blue", command=lambda : user_display(3) )
					app.button_saisi.pack()
		elif step == 3:
			app.button_saisi.destroy()
			app.label.destroy()
			canvas = tk.Canvas(app, width = 500, height = 500)
			canvas.pack()
			t = turtle.RawTurtle(canvas)
			t.speed("fast")
			print('Client->Server')
			sender('getLetter', '')
			#TODO afficher options de jeu
		elif step == 4:
			pass

def server_display(step):
	global user_choix
	global thread
	global terminal
	if terminal == '-t':
		if step == 1:
			print('Démarrage du serveur...')
			thread = threading.Thread(target=server, args=([port]))
			thread.daemon = True
			thread.start()
			host_name = get_ip()
			print('Serveur écoute en '+host_name+':'+str(port))
			print('Saisissez '+host_name+':'+ str(port) +' sur le client pour jouer')
		elif step == 2:
			print('taper exit pour quitter')
			while input() != 'exit':
				print('taper exit pour quitter')
			
	#On veut tkinter, on va dans le else
	else:
		if step == 1:
			app.button_client.destroy()
			app.button_server.destroy()
			ip =  get_ip() + ':' + str(port)
			app.label = tk.Label(app, text='Ip à saisir '+ ip, fg="blue" )
			app.label.pack(side="bottom")
			thread = threading.Thread(target=server, args=([port]))
			thread.daemon = True
			thread.start()
			app.button_saisi = tk.Button(app, text="Copier", fg="blue", command=lambda : copie(ip) )
			app.button_saisi.pack(side="bottom")
		elif step == 2:
			pass

def copie(ip):
	app.clipboard_clear()
	app.clipboard_append(ip)



def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except Exception:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

def run(state):
	if state == '2':
		server_display(1)
		server_display(2)
		server_display(3)
		server_display(4)
		server_display(5)
		server_display(6)
	elif state == '1':
		user_display(1)
		user_display(2)
		user_display(3)
		user_display(4)
		user_display(5)


###########################MAIN####################

#Option permetant de savoir si on veut un mode terminal ou non
global terminal
try:
	terminal = sys.argv[1]
except:
	terminal = 0
global nomJeu
global user_choix
global thread
nomJeu = 'S℧sℙ℈ℼd℧s'
port= 1500


if terminal == '-t':
	choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
	#TODO check error
	while(choix != '2' and choix != '1') :
		choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
	run(choix)
else : 
	global app
	app = tk.Tk()
	app.geometry('400x400')
	app.title(nomJeu)
	app.button_server = tk.Button(app, text="Mode serveur", fg="blue", command=lambda :server_display(1))
	app.button_server.pack(side="left")
	app.button_client = tk.Button(app, text="Mode client", fg="blue", command=lambda :user_display(1))
	app.button_client.pack(side="right")
	app.quit = tk.Button(app, text="Quitter", fg="red", command=app.destroy)
	app.quit.pack(side="bottom")
	app.mainloop()

print('Vous avez quitté ' + nomJeu + ', à bientôt')

#https://broux.developpez.com/articles/c/sockets/
