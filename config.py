import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
	exit('Не найдет файл .env')
else:
	load_dotenv()

	api_id = os.getenv('API_ID')
	api_hash = os.getenv('API_HASH')
	host = os.getenv('HOST')
	port = os.getenv("PORT")
	user_name = os.getenv('USER_NAME')
	password = os.getenv('PASSWORD')
	db_name = os.getenv('DATABASE')
	FROM_CHANNEL_ID = -1001551102382
	BOT_ID = 6912963846