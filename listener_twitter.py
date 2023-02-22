import socket
import tweepy

_HOST = 'localhost'
_PORT = 9008

s = socket.socket()
s.bind((_HOST,_PORT))
print(f'Aguardando conexão na porta {_PORT}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de {address}')

token = 'AAAAAAAAAAAAAAAAAAAAABlSlwEAAAAALptjUpuncbcqRdQHAJHoTHroADw%3DcsLSslg8hDvj7NTPnFKeAfFjNAdA3AxdZhsByU5Su5Wmg3Qfqh'
keyword = 'corinthians'

class Get_Tweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = Get_Tweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()