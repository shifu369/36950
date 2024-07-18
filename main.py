import time

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
}

while True:
    time.sleep(1)
    print("Bienvenido al diccionario cibernético!")
    time.sleep(1)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    time.sleep(1)
    if word in meme_dict:
        print(meme_dict[word])
    else:
        print("La palabra no está disponible en el diccionario en este momento, estamos trabajando por usted.")
