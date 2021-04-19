import csv

goalGenres = ["pop", "rock", "edm", "hip hop", "latin", "folk", "soul", "international pop"]

pop = ["barbadian pop", "candy pop"]
edm = ["dance pop", "electropop", "big room", "house", "permanent wave", "complextro", "electro", "metropopolis",
       "australian dance", "hollywood", "belgian edm", "electronic trap", "electro house", "brostep"]
rock = ["indie pop", "art pop", "boy band", "celtic rock", "escape room"]
hiphop = ["detroit hip hop", "hip pop", "atl hip hop", "chicago rap", "canadian hip hop", "australian hip hop",
          "canadian contemporary r&b", "alternative r&b"]
folk = ["neo mellow", "acustic pop", "baroque pop", "alaska indie", "acoustic pop", "folk-pop",
        "irish singer-songwriter", "downtempo", "contemporary country"]
interpop = ["canadian pop","australian pop", "colombian pop", "tropical house", "danish pop", "french indie pop",
            "canadian latin", "british soul", "moroccan pop"]

def findProbGenres(songList):
    problemGenres = []
    for song in songList:
        if song[15] not in goalGenres:
            if song[15] not in problemGenres:
                problemGenres.append(song[15])
    for genre in problemGenres:
        print(genre)

def simplifyGenres():
    opFile = open("top10s.csv", "r")
    csvReader = csv.reader(opFile)
    songList = list(csvReader)

    for song in songList:
        song.append(song[3])

    for song in songList:
        if song[15] in pop:
            song[15] = "pop"
        if song[15] in edm:
            song[15] = "edm"
        if song[15] in rock:
            song[15] = "rock"
        if song[15] in hiphop:
            song[15] = "hip hop"
        if song[15] in interpop:
            song[15] = "international pop"
        if song[15] in folk:
            song[15] = "folk"

    with open("nueTopTens.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(songList)