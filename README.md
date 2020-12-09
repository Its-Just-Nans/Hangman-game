# Hangman-game
Project for DUT R&T


## Documentation :

You can use the program just with
```python
python3 main.py #on linux

py main.py #on windows
```

You can also add some options :
```python
python3 main.py [-t] [-log] [-m server|client]
```
> Legend :
> - `t` is used to activate terminal mode
> - `-log` show you the log, for example the data sent
> - `-m client|server` is used to start directly in the mode you selected
> - note that it is `-m client` OR `-m server`

The next step is to start the connection.
-> Server side, it's simple, we put a socket to listen, in a while loop, and with each connection, we will start a new thread

-> From the client side, we get our MAC address which will serve as an identifier for the server. 
```
get_mac() function
```

On the client, the client enters the @IP: Port combination, we check it, then if it is correct, we use it to connect to the servers
```
get_ip() function
verifIPport() function
```

Once this is verified, voila and the connection is initialized.

To simplify entering the server IP, a copy function to the IP clipboard has been implemented.
```
copie() function
```

For the client sends a first request, from 'StartGame', this request allows the server to choose a word and sends it to the client as an underscore

The client just has to enter his proposal to send the letter to the server which returns a response:

- either the letter of the word is false (false)
- either a letter that is filled (right)

If the number of tries has reached its maximum, the user loses.

Otherwise, he wins!!

It's your turn !!!

Attention to the player: a small easter egg is hidden  ; )

### Utility of the projet:

This module brought us different things,

First of all, we reused all the aspects and all the knowledge that we saw in tp (opening / writing a file,
how to make a web request, the random module, the threading)
But we also learned by ourselves (learning to tkinter)

Nans participated a lot, he also invested in the creation of a "virus" that we tried on maxence, but he also created "photo-copy"
a small program to easily retrieve photos, for example from a camera and store them in a folder where you can specify the name.


### Improvements:

In order to improve the program we had several ideas, we basically wanted to realize them before the presentation in order to show them to you but
First of all, we are aware that our program is not very secure and that it should be made more secure.
Also we were a little selfish and it only works in French, we could make dico of other languages ​​available but also of
translate each button / phrase by choosing a language at the start of the program.

Multiplayer is also an option that we had considered, it is not optimal / done for now.

### Difficulties:
we encountered several difficulties:
  drawing for the graphical interface and learning how to use Tkinter (maxence)

Have an identical rendering for both modes (terminals and graphics)

The use of server-side threads was also an additional difficulty