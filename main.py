meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado"
            "SLAY" : "icónico, genial"
            "GHOSTING" : "ignorar a alguien"
            "DEMURE" : "recatado o modesto"
            }
print("Bienvenido, te ayudamos a comprender el mundo actual con nuestro diccionario moderno")

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(word + "="+ meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esta palabra no está en el diccionario")
