from twython import TwythonStreamer
import pymongo
import os

# Connect to mongo
MONGO_HOST = os.environ['MONGO_HOST'] if 'MONGO_HOST' in os.environ else 'localhost'
mongo = pymongo.MongoClient(f"mongodb://root:password@{MONGO_HOST}:27017/")

# Select our target mongo collection
mongo_db = mongo['twitter']
mongo_collection = mongo_db['corona']

# Enter your keys/secrets as strings in the following fields
credentials = {}
credentials['app_key'] = "PQPqkWiyZxe7yHWhZ5rYAQ8ML"
credentials['app_secret'] = "9AzuzdjrttiRcvnPAe3tRpneWRzT2VvsWoZknh07fcnquqqDSn"
credentials['oauth_token'] = "1074243254-aJTdAiqQ1XuuQVbwz0oWrzqzKXyjn5WJA94Pnzv"
credentials['oauth_token_secret'] = "wpP8YkqKkscmUiIbCC3tfoa3p452BxlfDmC488oUhAiZP"


# Filter out unwanted data
def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['user'] = tweet['user']
    d['created_at']=tweet['created_at']
    d['geo']=tweet['geo']
    d['reply_count']=tweet['reply_count']
    d['retweet_count']=tweet['retweet_count']
    d['favorite_count']=tweet['favorite_count']
    d['id']=tweet['id_str']
    d['in_reply_to_status_id']=tweet['in_reply_to_status_id_str']
    d['in_reply_to_user_id_str']=tweet['in_reply_to_user_id_str']
    return d


# Create a class that inherits TwythonStreamer
class MyStreamer(TwythonStreamer):     

    count=0
    # Received data
    def on_success(self, data):

        # Only collect tweets in English
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_mongo(tweet_data)
            self.count += 1
            if(self.count%10==0):
                print("tweet received: "+str(self.count))

            # TODO: remove. Stop at 10
            if self.count > 100:
                self.disconnect()
            

    # Problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    # Save each tweet to csv file
    def save_to_mongo(self, tweet):
        mongo_collection.insert_one(tweet)
        print('saved ' + tweet['user']['name'] +'\'s tweet')


if __name__ == '__main__':
    print("Executing twython stream reader")

    stream = MyStreamer(**credentials)
    stream.statuses.filter(track='corona')

    
