meme_dict={"CRINGE":"Garip ya da utandırıcı bir şey",
          "LOL": "Komik bir şeye verilen cevap",
          "ROFL": "Bir şakaya karşılık cevap",
          "SHEESH": " Onaylamak",
          "CREEPY":"Korkunç,ürkütücü",
          "AGGRO":"Agresifleşmek, sinirlenmek"}
word= input("Bilmediğiniz bir kelimeyi büyük harflerle yazınız.")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("bu kelime sözlükte yok")
