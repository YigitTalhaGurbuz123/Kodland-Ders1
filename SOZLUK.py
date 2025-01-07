import time

while True:
    meme_dict = {
                "LOL": "Komik bir şeye verilen cevap",
                "CRINGE": "garip ya da utandırıcı bir şey",
                "AGGRO": "agresifleşmek/sinirlenmek",
                "CREEPY": "korkunç",
                "ROFL": "bir şakaya karşılık cevap",
                "SHEESH": "onaylamamak"
                }
    
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
        print(".")
        print(".")
        print(".")
    else:
        print("Bu kelime yok :(")
        print(".")
        print(".")
        print(".")

    time.sleep(0.6)


    