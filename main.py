import tkinter as tk
import socket
import threading
import sys
import uuid
import turtle
import json
import time
import random


#Fonction pour récuperer l'adresse MAC de la socket, elle servira d'identifiant
#@argument: string -> un mot, string -> le mot en underscore, string -> la lettre
#@return: string -> l'adresse MAC
def lettreTire(mot,motAct,lettre) :
  posi= giveIndex(mot, lettre)
  newWord= motAct
  for i in posi :
    newWord = newWord[:i]+lettre+newWord[(i+1):] 
  return newWord

#fonction pour transformer un temps en seconde en une date (custom)
#@argument: float -> un temp en seconde
#@return: string -> la date custom avec des tirets
def SecondeEnDate(time):
  day = str(int(time/86400))
  heure = str(int((time%86400)/3600))
  minute = str(int((time%3600)/60))
  seconde = str(int(time%60))
  return day+'-'+heure+'-'+minute+'-'+seconde    

#Fonction pour récuperer l'adresse MAC de la socket, elle servira d'identifiant
#@argument: 
#@return: string -> l'adresse MAC
def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

#Fonction pour copier dans le presse papier, pour copier l'ip
#@argument: string -> la variable a copier
#@return:
def copie(ip):
	app.clipboard_clear()
	app.clipboard_append(ip)

#Fonction pour simuler une connection et récupérer l'ip
#@argument: 
#@return: string -> l'ip
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

#Fonction pour afficher le dessin
#@argument: 
#@return: 
def printNextStep():
	global t
	global etape
	#function qui sert a afficher le pendu
	if terminal == '-t':
		#affichage terminal
		if etape == 1:
			print('''
			   ║
			   ║
			   ║
			   ║
			   ║
			   ║''')
		elif etape == 2:
			print('''
			   ║
			   ║
			   ║
			   ║
			   ║
			   ║
			═══╩═══════════''')
		elif etape == 3:
			print('''
			   ║  /
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 4:
			print('''
			═══╦═════════════╦
			   ║  /
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 5:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 6:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 7:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/            |
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 8:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 9:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 10:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║            /
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 11:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║            / \\
			  /║
			 / ║
			═══╩═══════════''')
		elif etape == 12:
			print('''
			═══╦═════════════╦     (dead)
			   ║  /          ║ . ¨
 			   ║ /           ○
			   ║/           /|\\
			   ║            / \\
			  /║
			 / ║
			═══╩═══════════''')

	else:
		#affichage tkinter
		if etape == 1:
			# Barre du sol
			t.penup()
			t.goto(-90,-250)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(180)
			t.fd(175)
			t.right(180)
			t.penup()
		elif etape == 2:
			# Barre vertical
			t.goto(-220,-250)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(90)
			t.fd(450)
			t.right(90)
			t.penup()
		elif etape == 3:
			#petit tchitchou
			t.goto(-160,-250)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(128)
			t.fd(90)
			t.right(128)
			t.penup()
		elif etape == 4:
			#poutre du  haut
			t.goto(-260,200)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(0)
			t.fd(400)
			t.right(0)
			t.penup()
		elif etape == 5:
			#corde
			t.goto(120,194)
			t.pendown()
			t.width(9)
			t.color("orange")
			t.left(-90)
			t.fd(65)
			t.right(-90)
			t.penup()
			t.goto(118,190)
			t.pendown()
			t.width(5)
			t.color("black")
			t.left(0)
			t.fd(5)
			t.right(0)
			t.penup()
			t.goto(118,175)
			t.pendown()
			t.width(5)
			t.color("black")
			t.left(0)
			t.fd(5)
			t.penup()
			t.goto(118,160)
			t.pendown()
			t.width(5)
			t.color("black")
			t.left(0)
			t.fd(5)
			t.right(0)
			t.penup()
			t.goto(118,145)
			t.pendown()
			t.width(5)
			t.color("black")
			t.left(0)
			t.fd(5)
			t.right(0)
			t.penup()
			t.goto(118,130)
			t.pendown()
			t.width(5)
			t.color("black")
			t.left(0)
			t.fd(5)
			t.right(0)
			t.penup()
		elif etape == 6:
			#tête
			t.goto(119,123)
			t.pendown()
			t.color("red")
			t.right(90)
			t.begin_fill()
			t.circle(20)
			t.end_fill()
			t.left(90)
			t.penup()
		elif etape == 7:
			#corps		
			t.goto(118,117)
			t.pendown()
			t.width(10)
			t.color("black")
			t.left(-90)
			t.fd(130)
			t.right(-90)
			t.penup()
		elif etape == 8:
			#bras droit
			t.goto(118,100)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-80)
			t.fd(75)
			t.right(-80)
			t.penup()
		elif etape == 9:
			#bras gauche
			t.goto(118,100)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-70)
			t.fd(70)
			t.right(-70)
			t.penup()
		elif etape == 10:
			#jambe droite
			t.goto(118,-13)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-80)
			t.fd(75)
			t.right(-33)
			t.fd(20)
			t.right(-47)
			t.penup()
		elif etape == 11:
			#jambe gauche
			t.goto(118,-13)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-97)
			t.fd(67)
			t.right(-30)
			t.fd(20)
			t.right(-60)
			t.penup()
		elif etape == 12:
			#mot de fin
			t.goto(-100,0)
			t.pendown()
			t.color("red")
			t.write("PENDU !",font=("Arial", 24, "normal"))
			t.penup()
	if etape == 12 :
		endGame()
	else:
		etape = etape + 1


#Fonction pour gérer la fin de jeu
#@argument: 
#@return: 
def endGame():
	global etape
	#TODO JULES afficher le temps qui est dans tab['param']
	etape = 0
	if terminal == '-t':
		choix = input('Que voulez-vous faire ?\n1->Rejouer\n2->Quitter\n')
		while(choix != '1' and choix != '2') :
			choix = input('Que voulez-vous faire ?\n1->Rejouer\n2->Quitter\n')
		if choix == 1:
			restartGame()
		elif choix ==2:
			pass
	else :
		app.saisi.destroy()
		app.button.destroy()
		app.button =  tk.Button(app, text="Rejouer", fg="blue", command=lambda : restartGame() )
		app.button.grid(row=3, column=1, columnspan=3)

#Fonction pour afficher le choix les lettres
#@argument: 
#@return: 
def displayLetters():
	global terminal
	global param
	global app
	global log
	try:
		if param != '':
			#fonction qui gere l'affichage des lettres
			if terminal == '-t':
				#affichage terminal
				pass
			else:
				try:
					for element in app.word : #TODO
						element.destroy()
				except :
					app.word = [] #TODO LE SUPPRIMER
				tabLetter = list(param)
				count = 0
				for letter in tabLetter :
					label = tk.Label(app.frame, text = letter, borderwidth = 2, relief="ridge", font=('Helvetica', 15))
					label.grid(row=0, column=count)
					#app.frame.append(label)
					app.word.append(label)
					count = count+1
	except Exception as e:
		if log:
			print(e)

#Fonction pour enlever les accents
#@argument: string -> mot
#@return: string -> mot sans accents
def Transform(mot):
	mot=mot.translate({ord('é'):'e', ord('à'):'a', ord('è'):'e', ord('ê'):'e', ord('ù'):'u', ord('ç'):'c', ord('ô'):'o', ord('î'):'i', ord('ï'):'i', ord('â'):'a'	})
	return mot

#Fonction pour connaitre l'index d'une lettre dans un mot
#@argument: string -> mot, string -> une lettre
#@return: bool -> True or False
def giveIndex(mot, lettre) :
	return [i for i, x in enumerate(mot) if x == lettre]


#Fonction pour checker l'input combinant adresse ip et port
#@argument: string -> combinaison 'ip:port'
#@return: bool -> True or False
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
		except Exception as e:
			print(e)
			return False
	else :
		return False

#TODO
def endGameConnection():
	global param
	if param == '':
		print('Le serveur n\'a pas répondu')

#choisi un mot random dans un dictionnaire
#argument: string -> name/path of the ditionnary
#@return: string -> a random word
def MotRandom(ficdico) :
	liste=open(ficdico,'rb')
	dico=liste.read().decode('utf-8')
	dicobon=dico.split("\r\n")
	mot=random.choice(dicobon)
	return mot

#transforme les lettres du mot en underscore
#argument: string -> word
#@return: string -> word in underscore
def changeWordInDash(word):
	string = ''
	for i in range(len(word)):
		string = string + '_'
	return string


#Fonction qui permet de créer le serveur en ouvrant une socket
#@argument: entier -> numero de PORT
#@return: 
def server(port):
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host_name = get_ip()
	sock.bind((host_name, port))
	sock.listen(5)
	client, address = sock.accept()
	print ("{} connected".format( address ))
	while True:
		response = client.recv(255).decode("utf-8")
		if log:
			print('Client->Server:')
			print(response)
		try:
			tab = json.loads(response)
			if 'MAC' in tab:
				macClient = tab['MAC']
				if 'command' in tab and tab['command'] == 'startGame':
					game[macClient] = {}
					#gérer les options ici
					temp=int(time.time())
					game[macClient] = {'mot': MotRandom('liste_francais.txt'), 'nbTry': 0, 'TimeStart': temp}
					print('le  mot est ' + game[macClient]['mot'])
					game[macClient]['fakeMot'] = changeWordInDash(game[macClient]['mot'])
					senderServer({'MAC':'SERVER', 'command': 'startGame', 'param': game[macClient]['fakeMot']}, client)
				else :
					if macClient in game and 'command' in tab:
						valeur = {}
						if tab['command'] == 'chooseWord':
							game[macClient]['mot'] = MotRandom('liste_francais.txt')
							valeur = {'MAC':'SERVER', 'command': 'chooseWord', 'param': 'ok'}
						elif tab['command'] == 'checkLetter':
							#le client demande de vérifier une lettre
							game[macClient]['nbTry'] = game[macClient]['nbTry'] + 1
							if tab['param'] in list(game[macClient]['mot']):
								##remplacer _ par lettre
								game[macClient]['fakeMot'] = lettreTire(game[macClient]['mot'], game[macClient]['fakeMot'], tab['param'])
								senderServer({'MAC':'SERVER', 'command': 'checkLetter', 'param': game[macClient]['fakeMot']}, client)
								if '_' not in game[macClient]['fakeMot']:
									game[macClient]['time'] = int(time.time()) - game[macClient]['TimeStart']
									valeur = {'MAC':'SERVER', 'command': 'win', 'param': SecondeEnDate(game[macClient]['time']) }
							else:
								valeur = {'MAC':'SERVER', 'command': 'checkLetter', 'param': 'ko'}
						elif tab['command'] == 'checkWord':
							#le client demande de vérifier un mot
							if tab['param'] == game[macClient]['mot'] :
								senderServer({'MAC':'SERVER', 'command': 'checkWord', 'param': game[macClient]['mot'] }, client)
								game[macClient]['time'] = int(time.time()) - game[macClient]['TimeStart']
								valeur = {'MAC':'SERVER', 'command': 'win', 'param': SecondeEnDate(game[macClient]['time']) }
							else:
								valeur = {'MAC':'SERVER', 'command': 'checkWord', 'param': 'ko' }
						if valeur != {}:
							senderServer(valeur, client)
					else:
						pass
		except Exception as e:
			print('Error')
			print(e)

#Une fonction pour envoyer selon un client
#@argument: object/dict -> les valeurs a envoyer, object client -> le client
#@return:
def senderServer(var, client):
	var['MAC'] = 'SERVER'
	toSend = json.dumps(var).encode()
	client.sendall(toSend)

#Une fonction pour envoyer au serveur
#@argument: object/dict -> les valeurs a envoyer
#@return:
def sender(var):
	var['MAC'] = id
	toSend = json.dumps(var).encode()
	try:	
		sock.sendall(toSend)
	except Exception as e:
		print('Error')
		print(e)



#Fonction qui permet de créer le client en ouvrant une socket
#@argument: string -> combinaison ip:port
#@return:
def client(chaine):
	global param
	global sock
	global log
	global terminal
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = chaine.split(':')[0]
	port = int(chaine.split(':')[1])
	try :
		if log :
			print('Essaie de connection avec : ' + address + ':' + str(port))
		sock.connect((address, port))
		if log :
			print('Connecté avec : ' + address + ':' + str(port))
		app.label.destroy()
	except Exception as e:
		if log :
			print(e)
	try:
		while True:
			response = sock.recv(255).decode("utf-8")
			if log :
				print('server->Client:')
				print(response)
			
				tab = json.loads(response)
				if 'command' in tab:
					macClient = tab['MAC']
					if tab['command'] == 'startGame' :
						if tab['param'] == 'ko':
							print('error')
						else:
							print(param)
							param = tab['param']
							if terminal != '-t':
								user_display(3)
							displayLetters()
					elif tab['command'] == 'checkLetter' :
						if tab['param'] == 'ko':
							app.saisi.delete(0, 'end')
							printNextStep()
						else:
							app.saisi.delete(0, 'end')
							param = tab['param']
							displayLetters()
					elif tab['command'] == 'checkWord' :
						if tab['param'] == 'ko':
							app.saisi.delete(0, 'end')
							printNextStep()
						else:
							param = tab['param']
							app.saisi.delete(0, 'end')
							displayLetters()
					elif tab['command'] == 'win' :
						print('WIN')
						endGame()
						
					else :
						pass
	except Exception as e:
		if log :
			print('Error socket :')
			print(e)



#Fonction qui fait l'affichage client (sert a relier le thread de socket avec le thread de tkinter
#@argument: entier -> l'étape
#@return:
def user_display(step):
	global param
	global t
	global app
	if terminal == '-t':
		if step == 1:
			print('Vous êtes désormais un joueur Suspensus')
			entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			while not verifIPport(entry):
				entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			thread = threading.Thread(target=client, args=([entry]) )
			thread.daemon = True
			thread.start()
			print('Choix Option')
			#Mettre les options de jeux ici
			entry = input('1->Commencer\n')
			while entry != '1' :
				entry = input('1->Commencer la partie\n')
			sender({'command': 'startGame', 'param': ''})
			while param == '':
				time.sleep(0.5)
			user_display(3)
		elif step == 3:
			print('Mot à choisir : '+ param )
			#TODO utiliser dispLetters
			entry = input('Veuillez saisir une lettre ou un mot :\n')
			if(' ' not in entry) :
				if len(entry) == 1:
					#il y a une seule lettre
					sender({'command': 'checkLetter', 'param': entry})
				elif len(entry) > 1:
					#il y a plusieurs lettre, c'est mot
					sender({'command': 'checkWord', 'param': entry})
				else : 
					entry = input('Veuillez saisir une lettre ou un mot :\n')
			else :
				entry = input('Veuillez saisir une lettre ou un mot :\n')

		elif step == 4:
			print('TO DO')
			
	#On veut tkinter, on va dans le else
	else:
		if step == 1:
			app.button_client.destroy()
			app.button_server.destroy()
			app.saisi_Client = tk.Entry(app, width=20)
			app.saisi_Client.grid(row=2, column=1)
			app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
			app.button_saisi.grid(row=2, column=3)
		elif step == 2:
			entry = app.saisi_Client.get()
			if not verifIPport(entry):
				app.saisi_Client.delete(0, 'end')
				app.label = tk.Label(app, text="Erreur dans l'adresse, veuillez saisir IP:Port", fg="red")
				app.label.grid(row=1, column=1, columnspan=3)
			else :
				app.button_saisi.destroy()
				app.saisi_Client.destroy()
				try :
					app.label['text'] = 'Connection à ' + entry
				except AttributeError:
					app.label = tk.Label(app, text='Connection à ' + entry)
					app.label.grid(row=1, column=1, columnspan=3)
				startThread(entry)
				#TODO ICI METTRE OTPION
				app.button_saisi = tk.Button(app, text="Commencer la partie", fg="blue", command=lambda : sender({'command': 'startGame', 'param': ''}) )
				app.button_saisi.grid(row=1, column=1, columnspan=3)
		elif step == 3:
			app.button_saisi.destroy()
			app.label.destroy()
			app.button =  tk.Button(app, text="Envoyer", fg="blue", command=lambda : user_display(4) )
			app.button.grid(row=3, column=3)
			app.saisi = tk.Entry(app, width=20 )
			app.saisi.grid(row=3, column=1)
			#On créer une frame pour le mot
			app.frame = tk.Frame(app, height = 50)
			app.frame.grid(row=2, column=1, columnspan=3)
			app.frame.grid_rowconfigure(0, weight=1)

			#On créer le canvas pour le dessin
			app.canvas = tk.Canvas(app, width = 600, height = 600)
			app.canvas.grid(row=1, column=1, columnspan=3)
			t = turtle.RawTurtle(app.canvas)
			t.hideturtle()
			t.speed("fast") # ou speed(0) pour instant draw
		elif step == 4:
			notFinish = True
			choix = app.saisi.get()
			if(' ' not in choix) :
				if len(choix) == 1:
					#il y a une seule lettre
					sender({'command': 'checkLetter', 'param': choix})
				elif len(choix) > 1:
					#il y a plusieurs lettre, c'est mot
					sender({'command': 'checkWord', 'param': choix})
			
#une fonction pour démarrer un thread
#@argument: combinaison ip:port
#@return:		
def startThread(entry) :
	thread = threading.Thread(target=client, args=([entry]) )
	thread.daemon = True
	thread.start()

				
#Fonction qui fait l'affichage serveur (sert a relier le thread de socket avec le thread de tkinter)
#@argument: entier -> l'étape
#@return:
def server_display(step):
	global user_choix
	global thread
	global terminal
	global app
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
			app.label.grid(row=2, column=1, columnspan=3)
			thread = threading.Thread(target=server, args=([port]))
			thread.daemon = True
			thread.start()
			app.button_saisi = tk.Button(app, text="Copier", fg="blue", command=lambda : copie(ip) )
			app.button_saisi.grid(row=1, column=1, columnspan=3)
		elif step == 2:
			pass


#Fonction qui fait l'affichage serveur pour le serveur
#@argument:
#@return:
def run():
	server_display(1)
	server_display(2)
	server_display(3)
	server_display(4)
	server_display(5)
	server_display(6)


###########################MAIN####################

#Option permetant de savoir si on veut un mode terminal ou non
global terminal
global nomJeu
global user_choix
global thread
global game
global id
global etape
global param
global sock
global log
try:
	
	if '-t' in sys.argv:
		terminal = '-t'
	else :
		terminal = ''
	if '-m' in sys.argv:
		var = sys.argv.index('-m')
		if sys.argv[(var+1)] != '':
			mode = sys.argv[(var+1)]
	else :
		mode = ''
	if '-log' in sys.argv:
		log = True
	else:
		log = False
except:
	terminal = 0
etape = 1
param = ''
id = get_mac()
game = {}
nomJeu = 'HANGMAN'
port= 1500
print('Bienvenue sur '+ nomJeu)
#terminal = '-t'
if terminal == '-t':
	if mode != '':
		if mode == 'server' :
			choix = '2'
		elif mode == 'client':
			choix = '1'
		else :
			choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
			while(choix != '2' and choix != '1') :
				choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
	else :
		choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
		while(choix != '2' and choix != '1') :
			choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
	if choix == '1':
		user_display(1)
	elif choix == '2':
		run()
else :
	global app
	app = tk.Tk()
	#app.geometry('200x100')
	app.title(nomJeu)
	app.quit = tk.Button(app, text="Quitter", fg="red", command=app.destroy)
	app.quit.grid(row=4, column=1,columnspan=3)
	app.button_server = tk.Button(app, text="Mode serveur", fg="blue", command=lambda :server_display(1))
	app.button_server.grid(row=2, column=1)
	app.button_client = tk.Button(app, text="Mode client", fg="blue", command=lambda :user_display(1))
	app.button_client.grid(row=2, column=3)
	if mode != '':
		if mode == 'server' :
			app.button_server.invoke()
		elif mode == 'client':
			app.button_client.invoke()
	app.mainloop()
		
try:
    sock.close()
except Exception as e:
    print(e)

	
print('Vous avez quitté ' + nomJeu + ", à bientôt\n")


 #https://www.geeksforgeeks.org/socket-programming-multi-threading-python/