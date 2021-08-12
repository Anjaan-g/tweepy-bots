from decouple import config
import tweepy
import logging
# from logging.handlers import FileHandler

logger = logging.getLogger('info')
# logging.basicConfig(format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s', filename = "info.log", datefmt =  "%Y-%m-%d-%H-%M-%S")


def create_api():
    consumer_key = config("CONSUMER_KEY")
    consumer_secret = config("CONSUMER_SECRET")
    access_token = config("ACCESS_TOKEN")
    access_token_secret = config("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        logging.error("Error creating API", exc_info=True)
        raise e
    logging.info("API created")
    print("authenticated")
    return api
