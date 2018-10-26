import tweepy
consumer_key="8iPkUy4FXkAbBYR3FWiCy6881"
consumer_secret="japsNktgZ0fHOWZTAGAsKMHOpOiXWrWS4TOotyokFHVt4zwExy"
access_token="1007167772797759490-Abvq7PCf3SfaEY0hin9BgObeeLN4O3"
access_token_secret="7TKMQE8X2qxKojmdFCO2V4ikpomoM5QTqIJqUWJ6TMNwH"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)  
auth.set_access_token(access_token,access_token_secret) 
api=tweepy.API(auth)
api.update_status(status="hello everyone")
