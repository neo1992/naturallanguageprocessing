from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import newsentimentmod as nsm


#consumer key, consumer secret, access token, access secret.
ckey= "5r7c191hnjtmIl8QDAtpfJmGQ"
csecret= "JRgp5lHJXG1cbjAU2iwKSrJZNrgCg60w8lGDslK9pOM2y9mOg3"
atoken= "1265437226-litt6I7DS2T0GGdxGbhk2aFLBFsqomyBNlTpyv3"
asecret= "FZYnXjelpUWjaAgn7SRnvYDTF5KTjNHrl1V6pQgd1lTOb"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = nsm.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter_out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        time.sleep(0.3)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Infinity War"])