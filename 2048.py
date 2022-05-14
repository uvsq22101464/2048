import tkinter as tk
import random
racine = tk.Tk()

##############################
#Variables

taille = 4
WIDTH = 500
HEIGHT = 500
quitter = 0
matrice = []
matrice_verif = []
cpt = 0
score = 0
dico_bg = {0 : "dimgray", 2 : "lightyellow", 4 : "lemonchiffon", 8 : "lightsalmon", 16 : "salmon", 32 : "darkorange", 64 : "orangered", 128 : "skyblue", 256 : "cornflowerblue",\
     512 : "royalblue", 1024 : "mediumblue", 2048 : "darkblue", 4096 : "black", 8192 : "black", 16384 : "black", 32768 : "black", 65536 : "black", 131072 : "black"}
dico_chiffres = {0 : "dimgray", 2 : "silver", 4 : "silver", 8 : "silver", 16 : "silver", 32 : "silver", 64 : "silver", 128 : "darkred", 256 : "darkred",\
     512 : "darkred", 1024 : "darkred", 2048 : "darkred", 4096 : "white", 8192 : "white", 16384 : "white", 32768 : "white", 65536 : "white", 131072 : "white"}
move = ""
for i in range(taille) :
    matrice.append([])
    for j in range(taille) :
        matrice[i].append(0)
random_ligne = random.randint(0, taille)
random_colonne = random.randint(0, taille)
#print(matrice)
##############################
#fonctions :

def droite(event) :
    execution("droite")


def gauche(event) :
    execution("gauche")

def haut(event) :
    execution("haut")

def bas(event) :
    execution("bas")

def calcul(pos) :
    global matrice, score
    if pos == "droite" :
        for i in range(taille) :
            for j in range(taille-1, -1, -1) :
                if j-1 < 0 :
                    continue
                if matrice[i][j] == matrice[i][j-1] and matrice[i][j] != 0 and matrice[i][j-1] != 0 :
                    matrice[i][j] = matrice[i][j] + matrice[i][j-1]
                    matrice[i][j-1] = 0
                    score += matrice[i][j] + matrice[i][j-1]
    if pos == "gauche" :
        for i in range(taille) :
            for j in range(taille) :
                if j+1 >= taille :
                    continue
                if matrice[i][j] == matrice[i][j+1] and matrice[i][j] != 0 and matrice[i][j+1] != 0 :
                    matrice[i][j] = matrice[i][j] + matrice[i][j+1]
                    matrice[i][j+1] = 0
                    score += matrice[i][j] + matrice[i][j+1]
    if pos == "haut" :
        for i in range(taille) :
            for j in range(taille) :
                if i+1 >= taille :
                    continue
                if matrice[i][j] == matrice[i+1][j] and matrice[i][j] != 0 and matrice[i+1][j] != 0 :
                    matrice[i][j] = matrice[i][j] + matrice[i+1][j]
                    matrice[i+1][j] = 0
                    score += matrice[i][j] + matrice[i+1][j]
    if pos == "bas" :
        for i in range(taille-1, -1, -1) :
            for j in range(taille-1, -1, -1) :
                if i-1 < 0 :
                    continue
                if matrice[i][j] == matrice[i-1][j] and matrice[i][j] != 0 and matrice[i-1][j] != 0 :
                    matrice[i][j] = matrice[i][j] + matrice[i-1][j]
                    matrice[i-1][j] = 0
                    score += matrice[i][j] + matrice[i-1][j]
    return matrice, score
    
def mouvement(move) :
    global matrice, taille
    if move == "droite" or move == "gauche" :
        for i in range(taille) :
            for j in range(taille) :
                while 0 in matrice[i] :
                    matrice[i].remove(0)
        if move == "droite" :
            for i in range(taille) :
                while len(matrice[i]) != taille :
                    matrice[i].insert(0, 0)
        if move == "gauche" :
            for i in range(taille) :
                while len(matrice[i]) != taille :
                    matrice[i].append(0)
    if move == "haut" :
        for i in range(taille) :
            while len(matrice[i]) != taille :
                    matrice[i].append(0)
        for k in range(taille-1) :
            for i in range(taille) :       
                for j in range(taille) :
                    if i+1 >= taille :
                        continue
                    if matrice[i][j] == 0 and matrice[i+1][j] != 0 :
                        matrice[i][j] = matrice[i+1][j] 
                        matrice[i+1][j] = 0
    if move == "bas" :
        for i in range(taille) :
            while len(matrice[i]) != taille :
                    matrice[i].append(0)
        for k in range(taille-1) :
            for i in range(taille) :       
                for j in range(taille) :
                    if i-1 < 0 :
                        continue
                    if matrice[i][j] == 0 and matrice[i-1][j] != 0 :
                        matrice[i][j] = matrice[i-1][j] 
                        matrice[i-1][j] = 0
    return matrice

def case_fin_tour() :
    """permet d'ajouter un 2 ou un 4 à la fin de chaque tour"""
    global matrice
    proba = 1
    random_ligne = random.randint(0, taille - 1)
    random_colonne = random.randint(0, taille - 1)
    random_2_ou_4 = random.randint(proba, proba * 9)
    while matrice[random_ligne][random_colonne] > 0 :
        random_ligne = random.randint(0, taille - 1)
        random_colonne = random.randint(0, taille - 1)
    if matrice[random_ligne][random_colonne] == 0 :
        if random_2_ou_4 == proba :
            matrice[random_ligne][random_colonne] = 4
        else :
            matrice[random_ligne][random_colonne] = 2
    print(random_ligne, random_colonne)
    return matrice

def defeat() :
    global cpt
    cpt, cpt_0 = 0, 0
    for i in range(taille) :
        if 0 not in matrice[i] :
            cpt_0 += 1
        if cpt_0 == taille :
            for i in range(taille) :
                for j in range(taille) :
                    if i == 0 and j == 0 :                      # coin haut gauche
                        if matrice[i][j] != matrice[i+1][j] and matrice[i][j] != matrice[i][j+1] :
                            cpt += 1
                    if i == 0 and j == taille-1 :               # coin haut droit
                        if matrice[i][j] != matrice[i+1][j] and matrice[i][j] != matrice[i][j] != matrice[i][j-1] :
                            cpt += 1
                    if i == taille-1 and j == 0 :               # coin bas gauche
                        if matrice[i][j] != matrice[i-1][j] and matrice[i][j] != matrice[i][j+1] :
                            cpt += 1
                    if i == taille-1 and j == taille-1 :        # coin bas droit
                        if matrice[i][j] != matrice[i-1][j] and matrice[i][j] != matrice[i][j-1] :
                            cpt += 1
                    if i == 0 and 0 < j < taille-1 :            # ligne haut
                        if matrice[i][j] != matrice[i+1][j] and matrice[i][j+1] != matrice[i][j] and matrice[i][j-1] != matrice[i][j] :
                            cpt += 1
                    if i == taille-1 and 0 < j < taille-1 :     # ligne bas
                        if matrice[i][j] != matrice[i-1][j] and matrice[i][j+1] != matrice[i][j] and matrice[i][j-1] != matrice[i][j] :
                            cpt += 1
                    if j == 0 and 0 < i < taille-1 :            # colonne gauche
                        if matrice[i][j] != matrice[i+1][j] and matrice[i-1][j] != matrice[i][j] and matrice[i][j+1] != matrice[i][j] :
                            cpt += 1
                    if j == taille-1 and 0 < i < taille-1 :     # colonne droite
                        if matrice[i][j] != matrice[i+1][j] and matrice[i][j-1] != matrice[i][j] and matrice[i-1][j] != matrice[i][j] :
                            cpt += 1
                    else :                                      # le milieu
                        cpt += 1
    print(cpt)
    if cpt >= (taille**2 + (3*(taille-1))) :        # petite formule de maths je sais pas pk ça fait ça mais bon vive les maths
        #racine.destroy()
        pass
    return cpt

def execution(direction) :
    defeat()
    if cpt != (taille**2 + (3*(taille-1))) :
        mouvement(direction)
        calcul(direction)
        mouvement(direction)
        
        case_fin_tour()
        for i in range(len(matrice)) :
            print(matrice[i])
        affichage()
    else :
        affichage_defaite()

def affichage_defaite() :
    zone_jeu.create_text(WIDTH//2, HEIGHT//2, text="Défaite, votre score est de : " + str(score), font=("helvetica", "20"), fill="black",)









##############################
#widgets :

zone_jeu = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg='black')
quitter = tk.Button(racine, text="quitter", command= lambda : racine.destroy())

##############################
#placements des widgets :

zone_jeu.grid()
quitter.grid(row=1)

##############################
#le reste :


#matrice = [[1, 2, 3, 8], [8, 16, 4, 9], [5, 6, 7, 10], [11, 12, 13, 14]] #matrice de test
#matrice = [[128, 256, 512, 2048], [16, 64, 32, 16], [2, 16, 16, 8], [4, 2, 4, 2]] ## bug de défaite

chiffres = []
couleurs = []
print(matrice)
racine.bind("<Right>", droite)
racine.bind("<Left>", gauche)
racine.bind("<Up>", haut)
racine.bind("<Down>", bas)

# création de l'interface de base
for i in range(taille) :
    chiffres.append([])
    couleurs.append([])
    for j in range(taille) :
        couleurs[i].append(zone_jeu.create_rectangle(i*(WIDTH//taille), j*(HEIGHT//taille), i*(WIDTH//taille)+WIDTH//taille, j*(HEIGHT//taille)+HEIGHT//taille, fill=dico_chiffres[2]))
        chiffres[i].append(zone_jeu.create_text(WIDTH/taille * i + HEIGHT//taille//2, HEIGHT/taille * j + WIDTH//taille//2,\
            text=matrice[i][j] if matrice[i][j] != 0 else None, font=("helvetica", "40"), fill="white"))
            
def affichage() :
    
    for i in range(taille) :
        for j in range(taille) :
            
            zone_jeu.itemconfigure(couleurs[j][i], fill=dico_bg[matrice[i][j]])
            zone_jeu.itemconfigure(chiffres[j][i], text=matrice[i][j], fill=dico_chiffres[matrice[i][j]])


case_fin_tour()           # position de départ       
affichage()

racine.mainloop()