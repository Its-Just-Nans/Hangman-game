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
-> Server side, it's simple, we put a socket to listen, in a while loop, and with for each new connection, the server start a new thread.
The server display is own IP (know with the function `get_ip()`)

On the client, you enter the @IP and port combination of the server, then, the program check your entry with the function `verifIPport()`, then if it's correct, we connect us to the server

To simplify entering the server IP, a copy function to the IP clipboard has been implemented.
`copie()`

After the connection start, the client can send requests to the server. To identify the client, the client need to send the combination of is `MAC` address (the function `get_mac` return the MAC) and the port used.

For the client sends a first request, from 'StartGame', this request allows the server to choose a word and sends it to the client as an underscore

The client just has to enter his proposal (it can be a word or a letter), then send it to the server which returns a response:

- either the letter of the word is false (false)
- either a letter that is filled (right)

If the number of tries has reached its maximum, the user loses.

Otherwise, he wins !

### Utility of the projet:

This module brought us different things,

First of all, we reused all the aspects and all the knowledge that we saw in TP :
- opening / writing in a file
- make a web request
- the `random` module
- the `threading` module
But we also learned by ourselves (learning to `tkinter` and `turtle`)

@Its-Just-Nans participated a lot, he also invested in the creation of some programs that you can found in his Github

### Improvements:

- First of all, we are aware that our program is not very secure and that it should be made more secure.
- Also we were a little selfish and it only works in French, we could make a `lang` options at the start of the program (to translate each button or sentence in the program)
- Multiplayer is also an option but it's experimental (you  can found it in the branch `multi`)

### Difficulties:

We encountered several difficulties:
- drawing for the graphical interface and learning how to use Tkinter
- Both mode (terminal and graphic) can do the same exact thing
- The use of server-side threads was also an additional difficulty
