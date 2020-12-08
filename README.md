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