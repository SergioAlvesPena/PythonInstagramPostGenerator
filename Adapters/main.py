import openai
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    caminho_audio = "podcasts\podcast.mp3"
    nome_arquivo = "podcast"
    url_podcast = "https://www.youtube.com/watch?v=pKCE07D_WSQ"

    api_openai = os.getenv("API_KEY_OPENAI")

    openai.api_key = api_openai


if __name__ == "__main__":
    main()