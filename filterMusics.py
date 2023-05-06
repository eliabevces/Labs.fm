import json

f = open("historico.json", encoding="utf8")
historico = json.load(f)
f.close()


artista_dict = {"nome": [],"total": []} 
musica_dict = {"nome": [],"total": []} 

for video in historico:
    if video["header"] == "YouTube Music":
        if "subtitles" in video:
            if video["subtitles"][0]["name"] not in artista_dict["nome"]:
                artista_dict["nome"].append(video["subtitles"][0]["name"])
                artista_dict["total"].append(1)
            else:
                artista_dict["total"][artista_dict["nome"].index(video["subtitles"][0]["name"])] += 1

for video in historico:
    if video["header"] == "YouTube Music":
        if "title" in video:
            if video["title"] not in musica_dict["nome"]:
                musica_dict["nome"].append(video["title"])
                musica_dict["total"].append(1)
            else:
                musica_dict["total"][musica_dict["nome"].index(video["title"])] += 1

dict_final_art = sorted({artista_dict["nome"][i]: artista_dict["total"][i] for i in range(len(artista_dict["nome"]))}.items(), key=lambda x: x[1], reverse=True)
dict_final_music = sorted({musica_dict["nome"][i]: musica_dict["total"][i] for i in range(len(musica_dict["nome"]))}.items(), key=lambda x: x[1], reverse=True)

f = open("artistas.json", "w", encoding="utf8")
for i in dict_final_art:
    f.write(f"{i[0]}: {i[1]}\n")
f.close()

f = open("musicas.json", "w", encoding="utf8")
for i in dict_final_music:
    f.write(f"{i[0]}: {i[1]}\n")
f.close()        



