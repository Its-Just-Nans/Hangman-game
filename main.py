import tkinter as tk
import socket
import threading
import sys
import uuid
import turtle
import json
import time
import random



def lettreTire(mot,motAct,lettre) :
  posi= giveIndex(mot, lettre)
  newWord= motAct
  for i in posi :
    newWord = newWord[:i]+lettre+newWord[(i+1):] 
  return newWord

def SecondeEnDate(time):
  day = str(int(time/86400))
  heure = str(int((time%86400)/3600))
  minute = str(int((time%3600)/60))
  seconde = str(int(time%60))
  return day+'-'+heure+'-'+minute+'-'+seconde    

def get_mac():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
  return mac

def copie(ip):
	app.clipboard_clear()
	app.clipboard_append(ip)

def inWord(word, letter) :
	if letter in list(word):
		return True
	else:
		return False

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
	etape = etape + 1
 
def displayLetters():
	try:
		global param
		global app
		if param != '':
			#fonction qui gere l'affichage des lettres
			if terminal == '-t':
				#affichage terminal
				pass
			else:
				try:
					tab = app.frame
					for element in tab :
						element.destroy()
				except Exception as e:
					print(e)
				tabLetter = list(param)
				count = 0
				for letter in tabLetter :
					app.frame.label[count] = tk.Label(app.frame, text = letter, borderwidth = 6, relief="ridge")
	except Exception as e:
		print(e)


def Transform(mot):
	mot=mot.translate({ord('é'):'e', ord('à'):'a', ord('è'):'e', ord('ê'):'e', ord('ù'):'u', ord('ç'):'c', ord('ô'):'o', ord('î'):'i', ord('ï'):'i', ord('â'):'a'	})
	return mot


def giveIndex(mot, lettre) :
	return [i for i, x in enumerate(mot) if x == lettre]


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

def endGameConnection():
	global param
	if param == '':
		print('Le serveur n\'a pas répondu')

def MotRandom(ficdico) :
	liste=open(ficdico,'rb')
	dico=liste.read().decode('utf-8')
	dicobon=dico.split("\r\n")
	mot=random.choice(dicobon)
	return mot

def changeWordInDash(word):
	#transforme les lettres du mot en tirets
	string = ''
	for i in range(len(word)):
		string = string + '_'
	return string

#
#Fonction qui permet de créer le serveur en ouvrant une socket
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
							if inWord(game[macClient]['mot'], tab['param']):
								##remplacer -_ par lettre
								game[macClient]['fakeMot'] = lettreTire(game[macClient]['mot'], game[macClient]['fakeMot'], tab['param'])
								valeur = {'MAC':'SERVER', 'command': 'checkLetter', 'param': game[macClient]['fakeMot']}
								
							else:
								valeur = {'MAC':'SERVER', 'command': 'checkLetter', 'param': 'ko'}
						elif tab['command'] == 'checkWord':
							#le client demande de vérifier un mot
							if tab['param'] == game[macClient]['mot'] :
								game[macClient]['time'] = int(time.time()) - game[macClient]['TimeStart']
								valeur = {'MAC':'SERVER', 'command': 'checkWord', 'param': SecondeEnDate(game[macClient]['time']) }
							else:
								valeur = {'MAC':'SERVER', 'command': 'checkWord', 'param': 'ko' }
						if valeur != {}:
							senderServer(valeur, client)
					else:
						pass
		except Exception as e:
			print('Error')
			print(e)

def senderServer(var, client):
	var['MAC'] = 'SERVER'
	toSend = json.dumps(var).encode()
	client.sendall(toSend)

def sender(var):
	var['MAC'] = id
	toSend = json.dumps(var).encode()
	try:	
		sock.sendall(toSend)
	except Exception as e:
		print('Error')
		print(e)


#
#Fonction qui permet de créer le client en ouvrant une socket
def client(chaine):
	global param
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = chaine.split(':')[0]
	port = int(chaine.split(':')[1])
	try :
		print('Essaie de connection avec : ' + address + ':' + str(port))
		sock.connect((address, port))
		while True:
			response = sock.recv(255).decode("utf-8")
			print('server->Client:')
			print(response)
			try:
				tab = json.loads(response)
				if 'command' in tab:
					macClient = tab['MAC']
					if tab['command'] == 'startGame' :
						if tab['param'] == 'ko':
							print('error')
						else:
							print(param)
							param = tab['param']
							#affichier les mots
							if terminal != '-t':
								user_display(3)
							
					elif tab['command'] == 'checkLetter' :
						if tab['param'] == 'ko':
							app.saisi.delete(0, 'end')
							printNextStep()
						else:
							#bonne lettre, on verifie s'il a trouvé le mot
							if '_' in tab['param'] :
								#changer l'affichage
								pass
							else :
								print('WINN')
					elif tab['command'] == 'checkWord' :
						if tab['param'] == 'ok':
							print('wiiiiiiiiiiiinnnnnnnnnnnnnnnnnnn')
						else:
							app.saisi.delete(0, 'end')
							printNextStep()
					else :
						pass
			except Exception as e:
				print('Error')
				print(e)
	except Exception as e:
		print(e)
		# if hasattr(app, 'labelBug2'):
		# 	app.labelBug2 = tk.Label(app, text = 'Connexion échouée', fg="red")
		# 	app.labelBug2..grid(row=1, column=1, columnspan=3)
		# app.saisi_Client = tk.Entry(app, width=20)
		# app.saisi_Client.pack(side="left")
		# app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
		# app.button_saisi.pack(side="right")
		# app.label.destroy()


#
#Fonction qui fait l'affichage client (sert a relier le thread de socket avec le thread de tkinter
#Cette fonction varie en beaucoup en fonction de la valeur de la variable terminal
def user_display(step):
	global param
	global t
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
			entry = input('Veuillez saisir une lettre ou un mot :\n')
			#TODO Faire fonction de vérif le choix
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
				try :
					app.labelBug.destroy()
				except :
					pass
				app.saisi_Client.destroy()
				app.button_saisi.destroy()
				if 'labelBug2' not in app:
					app.labelBug = tk.Label(app, text = 'Mauvaise Ip veuillez recommencer', fg="red")
					app.labelBug.grid(row=1, column=1, columnspan=3)
				app.saisi_Client = tk.Entry(app, width=20 )
				app.saisi_Client.grid(row=2, column=1)
				app.button_saisi = tk.Button(app, text="Se connecter", fg="blue", command=lambda : user_display(2) )
				app.button_saisi.grid(row=2, column=3)
			else :
				try :
					app.labelBug.destroy()
					app.labelBug2.destroy()
				except :
					pass
				app.label = tk.Label(app, text= 'Connection à ' + entry +' ')
				app.label.grid(row=1, column=1, columnspan=3)
				app.button_saisi.destroy()
				del app.button_saisi
				app.saisi_Client.destroy()
				thread = threading.Thread(target=client, args=([entry]) )
				thread.daemon = True
				thread.start()
				app.label.destroy()
				if not hasattr(app, 'button_saisi'):
					app.button_saisi = tk.Button(app, text="Commencer la partie", fg="blue", command=lambda : sender({'command': 'startGame', 'param': ''}) )
					app.button_saisi.grid(row=1, column=1, columnspan=3)
		elif step == 3:
			app.button_saisi.destroy()
			app.label.destroy()
			app.button =  tk.Button(app, text="Envoyer", fg="blue", command=lambda : user_display(4) )
			app.button.grid(row=3, column=3)
			app.saisi = tk.Entry(app, width=20 )
			app.saisi.grid(row=3, column=1)
			app.frame = tk.Frame(app, height = 50)
			displayLetters()
			#app.geometry('600x600')
			canvas = tk.Canvas(app, width = 600, height = 600)
			canvas.grid(row=1, column=1, columnspan=3)
			t = turtle.RawTurtle(canvas)
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
except:
	terminal = 0
global nomJeu
global user_choix
global thread
global game
global id
global etape
etape = 1
global param
global sock
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
			#TODO check error
			while(choix != '2' and choix != '1') :
				choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
	else :
		choix = input('Que voulez-vous faire ?\n1->Jouer à ' + nomJeu + '\n2->Démarrer un serveur de jeu ' + nomJeu + '\n')
			#TODO check error
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
	app.mainloop()
	if mode != '':
		if mode == 'server' :
			server_display(1)
		elif mode == 'client':
			user_display(1)
	else :
		app.button_server = tk.Button(app, text="Mode serveur", fg="blue", command=lambda :server_display(1))
		app.button_server.grid(row=2, column=1)
		app.button_client = tk.Button(app, text="Mode client", fg="blue", command=lambda :user_display(1))
		app.button_client.grid(row=2, column=3)
try:
    sock.close()
except Exception as e:
    print(e)

	
print('Vous avez quitté ' + nomJeu + ', à bientôt')

#https://broux.developpez.com/articles/c/sockets/


# >>> import datetime
# >>> first_time = datetime.datetime.now()
# >>> later_time = datetime.datetime.now()
# >>> difference = later_time - first_time
# >>> seconds_in_day = 24 * 60 * 60
# datetime.timedelta(0, 8, 562000)
# >>> divmod(difference.days * seconds_in_day + difference.seconds, 60)
# (0, 8) 