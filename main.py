from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 50
PROMISED_UP = 50

Bot = InternetSpeedTwitterBot()
current_speed= Bot.get_internet_speed()

if current_speed['down_speed']<PROMISED_DOWN or current_speed['up_speed']<PROMISED_UP:
   Bot.tweet_at_provider()
