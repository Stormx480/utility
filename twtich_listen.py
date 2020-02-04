import re
import socket
import time

# --------------------------------------------- Start Settings ----------------------------------------------------
HOST = "irc.twitch.tv"                          # Hostname of the IRC-Server in this case twitch's
PORT = 6667                                     # Default IRC-Port
CHAN = "#stormx480"                             # Channel name = #{Nickname}
NICK = ""                              # Nickname = Twitch username
PASS = ''   # www.twitchapps.com/tmi/ will help to retrieve the required authkey
# --------------------------------------------- End Settings -------------------------------------------------------

readbuffer = ""

server = socket.socket()
server.connect((HOST, PORT))
server.send(bytes('PASS ' + PASS + '\r\n', 'utf-8'))
server.send(bytes('NICK ' + NICK + '\r\n', 'utf-8'))
server.send(bytes('JOIN ' + CHAN + '\r\n', 'utf-8'))

server.send(bytes("CAP REQ :twitch.tv/commands\r\n", 'utf-8'))

print(server)

server.send(bytes('PRIVMSG #stormx480 :stormx480 heys' + '\r\n', 'utf-8'))

time.sleep(5)

server.send(bytes('PRIVMSG #stormx480 :.w stormx480 heys' + '\r\n', 'utf-8'))

while True:
    print(server.recv(2048))