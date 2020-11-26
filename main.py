import sys
import socket
import threading
import uuid
import json
import time
import random
import webbrowser


global info
info = {}
global nomJeu
global game
global sock
#check si c'est en terminal
if '-t' in sys.argv:
	info['terminal'] = True
else :
	info['terminal'] = False
if not info['terminal']:
	import tkinter as tk
	import turtle
	global app # tkinter
	global t # la turtle



#Fonction pour sauvergarder les stats
#@argument: dict/object -> valeurs a sauvegarder
#@return: 
def statsWrite (donnees):
	with open("stats.json", "w") as file:
		json.dump(donnees, file)

#Fonction pour charger les stats
#@argument: string -> id
#@return: dict/object -> stats de l'id
def statsRead(identifant):
	with open("stats.json", "r") as read_file:
		data = json.load(read_file)
		if identifant in data:
			return data[identifant]

#Fonction pour récuperer l'adresse MAC de la socket, elle servira d'identifiant
#@argument: string -> un mot, string -> le mot en underscore, string -> la lettre
#@return: string -> l'adresse MAC
def lettreTire(mot,motAct,lettre) :
  posi = giveIndex(mot, lettre)
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
		ip = s.getsockname()[0]
	except Exception:
		ip = '127.0.0.1'
	finally:
		s.close()
	return ip

#Fonction pour afficher le dessin
#@argument: 
#@return: 
def printNextStep():
	global info
	global t
	#function qui sert a afficher le pendu
	if info['terminal']:
		#affichage terminal
		print('-----------------------------------------')
		if info['etape'] == 1:
			print('''
			   ║
			   ║
			   ║
			   ║
			   ║
			   ║''')
		elif info['etape'] == 2:
			print('''
			   ║
			   ║
			   ║
			   ║
			   ║
			   ║
			═══╩═══════════''')
		elif info['etape'] == 3:
			print('''
			   ║  /
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 4:
			print('''
			═══╦═════════════╦
			   ║  /
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 5:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 6:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 7:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/            |
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 8:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 9:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 10:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║            /
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 11:
			print('''
			═══╦═════════════╦
			   ║  /          ║
			   ║ /           ○
			   ║/           /|\\
			   ║            / \\
			  /║
			 / ║
			═══╩═══════════''')
		elif info['etape'] == 12:
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
		if info['etape'] == 1:
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
		elif info['etape'] == 2:
			# Barre vertical
			t.goto(-220,-250)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(90)
			t.fd(450)
			t.right(90)
			t.penup()
		elif info['etape'] == 3:
			#petit tchitchou
			t.goto(-160,-250)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(128)
			t.fd(90)
			t.right(128)
			t.penup()
		elif info['etape'] == 4:
			#poutre du  haut
			t.goto(-260,200)
			t.pendown()
			t.width(10)
			t.color("brown")
			t.left(0)
			t.fd(400)
			t.right(0)
			t.penup()
		elif info['etape'] == 5:
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
		elif info['etape'] == 6:
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
		elif info['etape'] == 7:
			#corps		
			t.goto(118,117)
			t.pendown()
			t.width(10)
			t.color("black")
			t.left(-90)
			t.fd(130)
			t.right(-90)
			t.penup()
		elif info['etape'] == 8:
			#bras droit
			t.goto(118,100)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-80)
			t.fd(75)
			t.right(-80)
			t.penup()
		elif info['etape'] == 9:
			#bras gauche
			t.goto(118,100)
			t.pendown()
			t.width(8)
			t.color("black")
			t.left(-70)
			t.fd(70)
			t.right(-70)
			t.penup()
		elif info['etape'] == 10:
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
		elif info['etape'] == 11:
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
		elif info['etape'] == 12:
			#mot de fin
			t.goto(-100,0)
			t.pendown()
			t.color("red")
			t.write("PENDU !",font=("Arial", 24, "normal"))
			t.penup()
	if info['etape'] == 12 :
		info['fini'] = True
		if not info['terminal']:
			endGame()
	else:
		info['etape'] = info['etape'] + 1


#Fonction pour gérer la fin de jeu
#@argument: 
#@return: 
def endGame():
	global info
	#TODO JULES afficher le temps qui est dans tab['param']
	info['etape'] = 0
	info['mot'] = ''
	if info['terminal']:
		choix = input('Que voulez-vous faire ?\n1->Rejouer\n2->Quitter\n')
		while(choix != '1' and choix != '2') :
			choix = input('Que voulez-vous faire ?\n1->Rejouer\n2->Quitter\n')
		if choix == '1':
			restartGame()
		elif choix == '2':
			pass
	else :
		app.saisi.destroy()
		app.button.destroy()
		app.button =  tk.Button(app, text="Rejouer", fg="blue", command=lambda : restartGame() )
		app.button.grid(row=4, column=1)
		app.quit.grid(row=4, column=2)
		app.quitAndURL = tk.Button(app, text="Quitter Et sortir", fg="red", command=lambda :destroyTkinter(True))
		app.quitAndURL.grid(row=4, column=3)

#Fonction pour afficher le choix les lettres
#@argument: 
#@return: 
def displayLetters():
	global info
	global app
	try:
		if info['mot'] != '':
			#fonction qui gere l'affichage des lettres
			if info['terminal']:
				print('Le mot est : ' + str(' '.join(list(info['mot']))))
			else:
				try:
					if app.word:
						tabLetter = list(info['mot'])
						count = 0
						for element in app.word :
							element['text'] = tabLetter[count]
							count = count+1
					#TODO TEST
				except :
					app.word = []
					tabLetter = list(info['mot'])
					count = 0
					for letter in tabLetter :
						label = tk.Label(app.frame, text = letter, borderwidth = 2, relief="ridge", font=('Helvetica', 15))
						label.grid(row=0, column=count)
						#app.frame.append(label)
						app.word.append(label)
						count = count+1
	except Exception as e:
		if info['log'] :
			print(type(e).__name__)
			print(e.__class__.__name__)
			print(e.__class__.__qualname__)
			print(e)

#Fonction pour enlever les accents
#@argument: string -> mot
#@return: string -> mot sans accents
def transform(mot):
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
	if ' ' in IPPort:
		return False
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
			if info['log'] :
				print(type(e).__name__)
				print(e.__class__.__name__)
				print(e.__class__.__qualname__)
				print(e)
			return False
	else :
		return False

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
def server(tab):
	global sock
	global game
	client = tab[0]
	addr = tab[1]
	try:
		while True:
			try :
				response = client.recv(255).decode("utf-8")
			except ConnectionResetError:
				if info['log']:
					print('Client '+ addr[0] +' -> déconnecté')
				break
			except KeyboardInterrupt:
				print('Vous avez quitté')
				break
			if info['log'] and response:
				print('Client->Server:')
				print(response)
			try:
				if response:
					tab = json.loads(response)
				else:
					if info['log']:
						print('-----------------------------------')
						print('la réponse reçue du client ' + addr[0] + ':' + str(addr[1]) + ' est incorrect')
						print('le client a été donc déconnecté')
						print('-----------------------------------')
					break
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
			except KeyboardInterrupt:
				print('Vous avez quitté')
				break
			except ConnectionAbortedError:
				pass
			except Exception as e:
				if info['log'] :
					print(type(e).__name__)
					print(e.__class__.__name__)
					print(e.__class__.__qualname__)
					print(e)
	except KeyboardInterrupt:
		print('Vous avez quitté')
		

#Une fonction pour envoyer selon un client
#@argument: object/dict -> les valeurs a envoyer, object client -> le client
#@return:
def senderServer(var, client):
	var['MAC'] = 'SERVER'
	toSend = json.dumps(var).encode()
	client.send(toSend)

#Une fonction pour envoyer au serveur
#@argument: object/dict -> les valeurs a envoyer
#@return:
def sender(var):
	#sender ne gère pas les erreurs, il faut le mettre en try: except:
	global info
	var['MAC'] = info['id']
	toSend = json.dumps(var).encode()
	sock.send(toSend)



#Fonction qui permet de créer le client en ouvrant une socket
#@argument: string -> combinaison ip:port
#@return:
def client(chaine):
	global sock
	global info
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sock.settimeout(60)
	address = chaine.split(':')[0]
	port = int(chaine.split(':')[1])
	try :
		if info['log'] :
			print('Essaie de connection avec : ' + address + ':' + str(port))
		sock.connect((address, port))
		portClient = sock.getsockname()[1]
		if info['log'] :
			print('Connecté à : ' + address + ':' + str(port) + ' avec le port ' + str(portClient))
		info['id'] = info['id'] + ':' + str(portClient)
		if info['terminal']:
			setOptions()
			info['mot'] = ''
			mot = info['mot']
		else:
			app.label.destroy()
	except TimeoutError:
			print('Erreur de connexion')
			sys.exit(500)
	except ConnectionAbortedError:
		print('Erreur de connexion')
		sys.exit(300)
	except ConnectionResetError:
		print('Erreur de connexion')
		sys.exit(200)
	except ConnectionRefusedError:
		print('Erreur de connexion')
		sys.exit(100)
	except Exception as e:
		if info['log'] :
			print(type(e).__name__)
			print(e.__class__.__name__)
			print(e.__class__.__qualname__)
			print(e)
	try:
		while True:
				try:
					response = sock.recv(255).decode("utf-8")
				except ConnectionAbortedError:
					break
				if info['log'] :
					print('server->Client:')
					print(response)
				tab = json.loads(response)
				if 'command' in tab:
					if tab['command'] == 'startGame' :
						if tab['param'] == 'ko':
							print('error')
						else:
							info['mot'] = tab['param']
							if info['terminal']:
								user_display(2)
							else :
								user_display(3)
								displayLetters()
					elif tab['command'] == 'checkLetter' :
						if tab['param'] == 'ko':
							if info['terminal']:
								printNextStep()
								user_display(2)
							else:
								app.saisi.delete(0, 'end')
								printNextStep()
								app.button['state'] = 'normal'
						else:
							info['mot'] = tab['param'] #on actualise le mot
							if info['terminal']:
								user_display(2)
							else:
								app.saisi.delete(0, 'end')
								displayLetters()
								app.button['state'] = 'normal'
					elif tab['command'] == 'checkWord' :
						if tab['param'] == 'ko':
							if info['terminal']:
								printNextStep()
								user_display(2)
							else:
								app.saisi.delete(0, 'end')
								printNextStep()
								app.button['state'] = 'normal'
						else:
							info['mot'] = tab['param'] #on actualise le mot
							if info['terminal']:
								user_display(2)
							else:
								app.saisi.delete(0, 'end')
								displayLetters()
								app.button['state'] = 'normal'
					elif tab['command'] == 'win' :
						print('WIN')
						info['fini'] = True
						info['mot'] = ''
						if not info['terminal']:
							endGame()
					else :
						pass
	except TimeoutError:
			print('Erreur de connexion')
			sys.exit(500)
	except ConnectionAbortedError:
		print('Erreur de connexion')
		sys.exit(300)
	except ConnectionResetError:
		print('Erreur de connexion')
		sys.exit(200)
	except ConnectionRefusedError:
		print('Erreur de connexion')
		sys.exit(100)
	except Exception as e:
		if info['log'] :
			print('Error socket :')
			print(type(e).__name__)
			print(e.__class__.__name__)
			print(e.__class__.__qualname__)
			print(e)



#Fonction qui fait l'affichage client (sert a relier le thread de socket avec le thread de tkinter
#@argument: entier -> l'étape
#@return:
def user_display(step):
	global param
	global info
	global app
	global t
	if info['terminal']:
		if step == 1:
			print('Vous êtes désormais un joueur Suspensus')
			entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			while not verifIPport(entry):
				entry = input('Veuillez saisir la combinaison adresseIP:Port\n')
			try:
				client(entry)
			except KeyboardInterrupt:
				pass
			endGame()
		elif step == 2:
			displayLetters()
			motInArray = list(info['mot'])
			if '_' in motInArray:
				entry = input('Veuillez saisir une lettre ou un mot :\n')
				if ' ' not in entry:
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
				app.frameOption = tk.Frame(app, height = 50)
				app.frameOption.grid(row=2, column=1, columnspan=3)
				app.frameOption.grid_rowconfigure(0, weight=1)
				#TODO afficher OPTION
				app.button_saisi = tk.Button(app, text="Commencer la partie", fg="blue", command=lambda : setOptions() )
				app.button_saisi.grid(row=3, column=1, columnspan=3)
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
			if not info['terminal']:
				app.button['state'] = 'disabled'
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

#une fonction pour gérer les options
#@argument:
#@return:		
def setOptions() :
	global game
	global app
	game['option'] = {}
	try :
		if info['terminal']:
			#TODO gérer les options pour le terminal
			entry = input('1->Commencer la partie\n')
			while entry != '1' :
				entry = input('1->Commencer la partie\n')
		else:
			if app.optionSaveLetter.get() == True:
				game['option']['saveLetter'] = True
			if app.optionLinkDict.get() == True:
				game['option']['dict'] = app.optionLinkDict.get()
			if app.optionMulti.get() == True:
				game['option']['multi'] = True
			app.frameOption.destroy()
	except Exception as e:
		pass
	
	sender({'command': 'startGame', 'param': game['option']})


#Fonction qui fait l'affichage serveur (sert a relier le thread de socket avec le thread de tkinter)
#@argument: entier -> l'étape
#@return:
def server_display():
	global thread
	global info
	global app
	global sock
	port = 1500
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.1)
	host_name = get_ip()
	sock.bind((host_name, port))
	sock.listen(5)
	text = 'Saisissez '+host_name+':'+ str(port) +' sur le client pour jouer'
	#AFFICHAGE
	if info['terminal']:
		print('Démarrage du serveur...')
		print('Serveur écoute en '+host_name+':'+str(port))
		serverWaiting(text)
	#On veut tkinter, on va dans le else
	else:
		app.button_client.destroy()
		app.button_server.destroy()
		ip =  host_name + ':' + str(port)
		app.label = tk.Label(app, text='Ip à saisir '+ ip, fg="blue" )
		app.label.grid(row=2, column=1, columnspan=3)
		app.button_saisi = tk.Button(app, text="Copier", fg="blue", command=lambda : copie(ip) )
		app.button_saisi.grid(row=1, column=1, columnspan=3)
		threadWaiter = threading.Thread(target=serverWaiting, args=([text]) )
		threadWaiter.daemon = True
		threadWaiter.start()
	
		

def serverWaiting(text) :
	global info
	global sock
	threadForClient = []
	if info['terminal']:
		print('------------------------------------------------------')
		print(text)
		print('------------------------------------------------------')
	try:
		while True:
			try:
				# a chaque connection, le serveur démarre un thread
				client, addr = sock.accept()
				if info['log'] :
					print('Client '+ addr[0] + ':' + str(addr[1]) + '-> connecté')
				threadForClient = threading.Thread(target=server, args=([ [client, addr] ]))
				threadForClient.daemon = True
				threadForClient.start()
				if info['terminal']:
					print('------------------------------------------------------')
					print(text)
					print('------------------------------------------------------')
			except KeyboardInterrupt:
				print('Vous avez quitté')
				break
			except socket.timeout:
				pass
	except KeyboardInterrupt:
		print('Vous avez quitté')
		pass
	except Exception as e:
		pass



#Convertis la date noté j-h-m-s en : Vous avez mis : j jours h heures m minutes et s secondes
#@arguments date noté j-h-m-s
#@return : string -> date
def ConvertDateIntoLetters(date):
  liste_date = date.split('-')
  return 'Vous avez mis : '+liste_date[0] + ' jours ' + liste_date[1]+ ' heures '+ liste_date[2] + ' minutes ' +'et '+ liste_date[3] + ' secondes'

def destroyTkinter(openUrl):
	global app
	global sock
	if openUrl:
		webbrowser.open_new('https://media.interieur.gouv.fr/deplacement-covid-19/')
	try:
		sock.close()
	except Exception as e:
		pass
	app.quit()
	

###########################MAIN####################

try:
	#check si il y a un mode
	if '-m' in sys.argv:
		var = sys.argv.index('-m')
		if sys.argv[(var+1)] != '':
			info['mode'] = sys.argv[(var+1)]
	else :
		info['mode'] = ''
	#check si il y a un mode
	if '-log' in sys.argv:
		info['log'] = True
	else:
		info['log'] = False
except:
	info['terminal'] = False
	info['log'] = False
	info['mode'] = ''
info['etape'] = 1
info['fini'] = False
info['param'] = ''
info['id'] = get_mac()
game = {}
nomJeu = 'HANGMAN'
info['port'] = 1500
print('Bienvenue sur '+ nomJeu)
#terminal = '-t'
if info['terminal']:
	if info['mode'] != '':
		if info['mode'] == 'server' :
			choix = '2'
		elif info['mode'] == 'client':
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
		server_display()
else :
	global app
	app = tk.Tk()
	app.rowconfigure(0, weight=1)
	app.rowconfigure(1, weight=1)
	app.columnconfigure(0, weight=1)
	app.columnconfigure(1, weight=1)
	app.geometry('200x100')
	app.title(nomJeu)
	app.quitter = tk.Button(app, text="Quitter", fg="red", command=lambda:destroyTkinter(False))
	app.quitter.grid(row=1, column=0, columnspan=2)
	app.button_server = tk.Button(app, text="Mode serveur", fg="blue", command=lambda :server_display())
	app.button_server.grid(row=0, column=0, sticky="nesw")
	app.button_client = tk.Button(app, text="Mode client", fg="blue", command=lambda :user_display(1))
	app.button_client.grid(row=0, column=1, sticky="nesw")
	if info['mode'] != '':
		if info['mode'] == 'server' :
			app.button_server.invoke()
		elif info['mode'] == 'client':
			app.button_client.invoke()
	app.mainloop()
	app.destroy()
try:
	sock.close()
except Exception as e:
    #print(e)
	pass

	
print('Vous avez quitté ' + nomJeu + ", à bientôt")
sys.exit(0)