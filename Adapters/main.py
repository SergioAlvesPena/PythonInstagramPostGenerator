import openai
from dotenv import load_dotenv
import os

def openai_whisper_transcrever(caminho_audio, nome_arquivo, modelo_whisper, openai):
    print("Estou transcrevendo com whispers...")

    audio = open(caminho_audio, "rb")

    resposta = openai.Audio.transcribe(
        api_key = openai.api_key,
        model = modelo_whisper,
        file = audio
    )

    transcricao = resposta.text

    with open(f"texto_completo_{nome_arquivo}.txt", "w", encoding= 'utf-8') as arquivo_texto:
        arquivo_texto.write(transcricao)

    return transcricao

def main():
    load_dotenv()

    caminho_audio = "podcasts\manualdomundo.mp3"
    nome_arquivo = "manualdomundo"
    url_podcast = "https://www.youtube.com/watch?v=g6mJPl-E_UY"

    api_openai = os.getenv("API_KEY_OPENAI")

    openai.api_key = api_openai

    modelo_whisper = "whisper-1"

    transcricao_completa = openai_whisper_transcrever(caminho_audio, nome_arquivo, modelo_whisper,openai)

if __name__ == "__main__":
    main()