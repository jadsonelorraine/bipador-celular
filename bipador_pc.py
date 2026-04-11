import keyboard
import requests

url = "https://script.google.com/macros/s/AKfycbxShUtv5yMcNi2qvQiC_TH-5kbqKVekt-1GuAVhRxoXrgSVtMEUoHsuk79UUhEyTi3qng/exec"

codigo = ""
enviados = set()

print("Bipador ativo...")

def enviar(cod):

    if cod not in enviados:

        enviados.add(cod)

        try:

            requests.post(url, data={"codigo": cod})

            print("enviado:", cod)

        except:

            print("erro")

while True:

    evento = keyboard.read_event()

    if evento.event_type == keyboard.KEY_DOWN:

        if evento.name == "enter":

            if codigo != "":

                enviar(codigo)

                codigo = ""

        elif len(evento.name) == 1:

            codigo += evento.name
