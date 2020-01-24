import tweepy
import time
import json

# Toda a baboseira da api só que em json
def get_credentials():
    t = open("config/credentials.json")
    j = json.loads(t.read())
    t.close()
    return j

# Fazendo o post assim que encontrar os bagulho ai
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: tweepy.Status):
        auth = tweepy.OAuthHandler(get_credentials()['consumer_key'], get_credentials()['consumer_secret'])
        auth.set_access_token(get_credentials()['access_token'], get_credentials()['access_token_secret'])
        self.api = tweepy.API(auth)
        content = "Foda-se"
        self.api.update_status(content, status.id, auto_populate_reply_metadata=True)
        print(f"[**] Novo post: {content}")

# Criando o stream e o filtro de palavras
def create_stream(api: tweepy.API):
    print("[--] Stream iniciado [--]")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["LoL", "CBLOL", "League of Legends", "League of Legends Brasil"])
