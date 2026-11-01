from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)  # This line prints the value of the api_key variable to the console, which is retrieved from the environment variable "API_KEY" defined in the .env file.