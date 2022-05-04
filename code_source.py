from PIL import Image
from IPython.display import display
import urllib.request

#Espace dédié aux images proposées
print("Choisissez une image à déformer parmi cette liste d'images libres de droit !")
print("- 1 : régiment de bananes \n- 2 : la Terre \n- 3 : pastèque \n- 4 : 'La Laitière' \n- 5 : drapeau du Brésil \n- 6 : 'La nuit étoilée' - Van Gogh\n- 7 : 'La Grande Vague de Kanagawa' - Hokusai\n- 8 : logo de IKEA\n- 9 : aurore boréale\n- 10 : le Laure des Grottes à Kyiv\n- 11 : taxi new-yorkais\n- 12 : cerf\n- 13 : Vinicunca\n- 14 : poisson-mandarin\n- 15 : Jaws (spot de surf)\n- 16 : Kensuke Koike")
numero = input("Entrez le numéro de l'image que vous souhaitez modifier \n")

if numero == "1" :
    lien = "http://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Bananas_white_background_DS.jpg/1280px-Bananas_white_background_DS.jpg"

if numero == "2" : 
    lien = "https://upload.wikimedia.org/wikipedia/commons/d/d9/Earth_by_the_EPIC_Team_on_21_April_2018.png"

if numero == "3" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wassermelone_%2827769857845%29.jpg/1280px-Wassermelone_%2827769857845%29.jpg"

if numero == "4" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Johannes_Vermeer_-_Het_melkmeisje_-_Google_Art_Project.jpg/913px-Johannes_Vermeer_-_Het_melkmeisje_-_Google_Art_Project.jpg"

if numero == "5" :
    lien = "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Flag_of_Brazil.svg/1280px-Flag_of_Brazil.svg.png"

if numero == "6" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/2560px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

if numero == "7" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tsunami_by_hokusai_19th_century.jpg/2560px-Tsunami_by_hokusai_19th_century.jpg"

if numero == "8" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Ikea_logo.svg/2560px-Ikea_logo.svg.png"

if numero == "9" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/a/aa/Polarlicht_2.jpg"

if numero == "10" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/%D0%9B%D0%B0%D0%B2%D1%80%D0%B0.jpg/2560px-%D0%9B%D0%B0%D0%B2%D1%80%D0%B0.jpg"

if numero == "11" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/New_York_Taxi.JPG/2560px-New_York_Taxi.JPG"

if numero == "12" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Cervus_unicolor_2.jpg"

if numero == "13" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/1/1e/Rainbow_Mountain_Peru.jpg"

if numero == "14" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Synchiropus_splendidus_2_Luc_Viatour.jpg/2560px-Synchiropus_splendidus_2_Luc_Viatour.jpg"

if numero == "15" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/4/45/Maggie_Hallahan_Jaws_Hawaii.jpg"

if numero == "16" :
    lien = "https://upload.wikimedia.org/wikipedia/commons/f/fe/Kensuke_Koike_ritratto.png"

im  = Image.open(urllib.request.urlopen(lien))


#Espace dédié au modification proposée

print("Il existe plusieurs modifications possibles, elles sont les suivantes :")
print("- entrez 1 pour l'extraction de carrés dans l'image")
print("- entrez 2 pour le découpage en bandelettes")
print("- entrez 3 pour l'extension")
print("- entrez 4 pour le quadrillage")
print("- entrez 5 pour l'inversion")
print("- entrez 6 pour la séparation en 4 images")
print("- entrez 7 pour le pixelisateur")
reponse = input("Quelles modifications aimeriez vous apporter à votre image ?\n Attendre quelques secondes pour le résultat...")

#Espace dédié au fonctions pour modifier l'image

def carre_blanc():
    '''
    Cette modification extrait des carrés de l'image laissant des troues blanc. Ces carrés sont par la suite réunis pour créer une plus petite image.
    Vidéo de Kensuke koike: https://www.youtube.com/watch?v=U1KiC0AXhHg
    '''
    width, height = im.size
    im_new = Image.new("RGB", (240, 320), (250, 250, 250))
    ecart = (width-40 -12*20)//11
    ecart_y = (height-40 - 16*20)//15
    pointeur_y_deb = -20 - ecart_y
    pointeur_y_fin = - ecart_y
    x_new = -1
    y_new = 0
    for loop in range(16):
        pointeur_y_deb += ecart_y + 20
        pointeur_y_fin += ecart_y + 20
        pointeur_x_fin = - ecart
        pointeur_x_deb = -20 - ecart
        x_new = -1
        y_new += 20
        for loop in range(12):
            pointeur_x_deb += ecart + 20
            pointeur_x_fin += ecart + 20
            for x in range(pointeur_x_deb, pointeur_x_fin):
                x_new +=1
                y_new -= 20
                for y in range(pointeur_y_deb, pointeur_y_fin):
                    pixel = im.getpixel((x+20,y+ 20))
                    im_new.putpixel((x_new,y_new), pixel)
                    im.putpixel((x+20,y+20), (255, 255, 255))
                    y_new += 1
                    
    return display(im, im_new)



def bande():
    '''
    Cette modification sépare en bande l'image et déplace ces bandes selon un effet de mirroir. La première bande passera en dernière, la seconde passera avant-dernière etc.
    Modification basé sur la début de cette vidéo de Kensuke Koike: https://www.youtube.com/watch?v=As2KMSOad08
    '''
    width, height = im.size
    im_new = Image.new("RGB", (width, height), (250, 250, 250))
    x = -1
    nb_bande = 18
    while width%nb_bande != 0:
        nb_bande += 1
    if nb_bande == width:
        nb_bande = 18
        while width%nb_bande > 1: 
            nb_bande += 1
    taille_bande = width // nb_bande 
    x_new = width + taille_bande
    for loop in range(nb_bande):
        x_new -= taille_bande*2
        for loop in range(taille_bande):
            x += 1
            x_new += 1
            for y in range(height):
                pixel = im.getpixel((x, y))
                im_new.putpixel((x_new -1, y), pixel)
    return display(im_new)



def extension():
    '''
    Cette modification coupe l'image en 2 et décale les deux images. Pour finir, le vide est comblé par le pixel adéquat
    Modification inspiré de cette vidéo de Kensuke koike: https://www.youtube.com/watch?v=BGEQymHBQX0
    '''
    width, height = im.size
    im_new = Image.new("RGB", (width*2 - width//2, height), (250, 250, 250))
    for x in range(width):
        for y in range(height):
            pixel = im.getpixel((x,y))
            if x< width//2:
                im_new.putpixel((x,y), pixel) 
            else:
                im_new.putpixel((x+width//2, y), pixel)
    x = width//2
    for y in range(height):
        pixel = im.getpixel((x,y))
        for x_new in range(width//2, width):
            im_new.putpixel((x_new,y), pixel)  
    return display(im_new)



def quadrillage():
    '''
    Cette modification utilise la fonction 'bande' mais le répète 2 fois: dans la longueur puis dans la largeur. Cela permet de créer un effet de quadrillage avec plein de carrés mélangé et dans le mauvais sens.
    Modificartion basé sur cette vidéo dee Kensuke Koike: https://www.youtube.com/watch?v=As2KMSOad08
    '''
    width, height = im.size
    im_new = Image.new("RGB", (width, height), (250, 250, 250))
    x = -1
    nb_bande = 18
    while width%nb_bande != 0:
        nb_bande += 1
    if nb_bande == width:
        nb_bande = 18
        while width%nb_bande > 5: 
            nb_bande += 1
    taille_bande = width // nb_bande 
    x_new = width + taille_bande
    for loop in range(nb_bande):
        x_new -= taille_bande*2
        for loop in range(taille_bande):
            x += 1
            x_new += 1
            for y in range(height):
                pixel = im.getpixel((x, y))
                im_new.putpixel((x_new -1, y), pixel)
    y = -1
    nb_bande = 18
    while height%nb_bande != 0:
        nb_bande += 1
    if nb_bande == height:
        nb_bande = 18
        while height%nb_bande > 5: 
            nb_bande += 1
    taille_bande = height // nb_bande 
    y_new = height + taille_bande
    for loop in range(nb_bande):
        y_new -= taille_bande*2
        for loop in range(taille_bande):
            y += 1
            y_new += 1
            for x in range(width):
                pixel = im_new.getpixel((x, y))
                im.putpixel((x, y_new -1 ), pixel)
    return display(im)



def inversion():
    '''
    Cette modification permet de renversé une partie de l'image. 
    Cette modification à été inventé par notre groupe.
    '''
    x_new=0
    y_new=0
    compteur = 0
    width, height = im.size
    img_new = Image.new("RGB", (width, height), (250, 250, 250))
    for x in range (width):
        for y in range(height):
            pixel = im.getpixel((x,y))
            img_new.putpixel((x,y), pixel)
    position_y_1 = (height)//3
    position_y_2= ((height)//3)*2
    hauteur = position_y_2 + 1
    position_y_fin = width
    for y in range(position_y_1, position_y_2):
        hauteur -= 1 
        compteur += 1
        for x in range(position_y_fin):
            pixel = im.getpixel((x, y ))
            img_new.putpixel((x,hauteur), pixel)
    
    return display(img_new)


def quatre_image():
    '''
    Cette modification sépare l'image choisis en carreaux et déplace les carreaux dans 4 différentes images. 
    Modifiation basé sur cette vidéo de Keensuke Koike: https://www.youtube.com/watch?v=f1fXCRtSUWU
    '''
    width, height = im.size
    im_new_1 = Image.new("RGB", (width//2, height), (250, 250, 250))
    im_new_2 = Image.new("RGB", (width//2, height), (250, 250, 250))
    x_new_1 = 0
    x_new_2 = 0
    taille_bande = width//20
    pointeur_x = 0 - taille_bande
    compteur = 0
    nb_bande = 0
    for loop in range(20):
        nb_bande += 1
        pointeur_x += taille_bande
        if nb_bande%2 == 0:
            compteur -= taille_bande*2
        for x in range(pointeur_x, pointeur_x + taille_bande):
            compteur += 1
            if nb_bande%2 == 0:
                x_new_2 += 1
            else:
                x_new_1 += 1
            for y in range(height):
                pixel = im.getpixel((x,y))
                if compteur > 0:
                    im_new_1.putpixel((x_new_1 -1, y), pixel)
                else:
                    im_new_2.putpixel((x_new_2 -1, y), pixel) 
    im_new_1_1 = Image.new("RGB", (width//2, height//2), (250, 250, 250))
    im_new_1_2 = Image.new("RGB", (width//2, height//2), (250, 250, 250))
    y_new_1 = 0
    y_new_2 = 0
    taille_bande = height//20
    pointeur_y = 0 - taille_bande
    compteur = 0
    nb_bande = 0
    for loop in range(20):
        nb_bande += 1
        pointeur_y += taille_bande
        if nb_bande%2 == 0:
            compteur -= taille_bande*2
        for y in range(pointeur_y, pointeur_y + taille_bande):
            compteur += 1
            if nb_bande%2 == 0:
                y_new_2 += 1
            else:
                y_new_1 += 1
            for x in range(width//2):
                pixel = im_new_1.getpixel((x,y))
                if compteur > 0:
                    im_new_1_1.putpixel((x, y_new_1 -1), pixel)
                else:
                    im_new_1_2.putpixel((x, y_new_2 -1), pixel) 
    im_new_2_1 = Image.new("RGB", (width//2, height//2), (250, 250, 250))
    im_new_2_2 = Image.new("RGB", (width//2, height//2), (250, 250, 250))
    y_new_1 = 0
    y_new_2 = 0
    pointeur_y = 0 - taille_bande
    compteur = 0
    nb_bande = 0
    for loop in range(20):
        nb_bande += 1
        pointeur_y += taille_bande
        if nb_bande%2 == 0:
            compteur -= taille_bande*2
        for y in range(pointeur_y, pointeur_y + taille_bande):
            compteur += 1
            if nb_bande%2 == 0:
                y_new_2 += 1
            else:
                y_new_1 += 1
            for x in range(width//2):
                pixel = im_new_2.getpixel((x,y))
                if compteur > 0:
                    im_new_2_1.putpixel((x, y_new_1 -1), pixel)
                else:
                    im_new_2_2.putpixel((x, y_new_2 -1), pixel)
    width, height = im_new_1_1.size 
    x = width 
    pixel = im_new_1_1.getpixel((x -1,1))
    while pixel == (250, 250, 250):
        x -= 1
        pixel = im_new_1_1.getpixel((x -1,1))
    y = height
    pixel = im_new_1_1.getpixel((1,y -1))
    while pixel == (250, 250, 250):
        y -= 1
        pixel = im_new_1_1.getpixel((1,y -1))  
    liste_image1 =[]
    liste_image1.append(im_new_1_1)
    liste_image1.append(im_new_1_2)
    liste_image1.append(im_new_2_1)
    liste_image1.append(im_new_2_2)
    liste_image2 = []
    for compteur in range(4):
        new_im = Image.new("RGB", (x, y), (250, 250, 250))
        for x1 in range(x):
            for y1 in range(y):
                pixel = liste_image1[compteur].getpixel((x1, y1))
                new_im.putpixel((x1, y1), pixel)
        liste_image2.append(new_im)
    width, height = liste_image2[0].size 
    im_final = Image.new("RGB", (width*4, height), (250, 250, 250))
    compteur = -1
    x_new = 0 - width -1
    for loop in range(4):
        compteur += 1
        for x in range(width):
            x_new += 1
            for y in range(height):
                pixel = liste_image2[compteur].getpixel((x, y))
                im_final.putpixel((x_new, y), pixel)

    return display(im_final)


def pixeliser():
    '''
    Cette modification rend une image en basse définition. cela permet de ccomprendre l'oeuvre sans voir les détails.
    Modification inventé par notre groupe.
    '''
    width, height = im.size
    im_new = Image.new("RGB", (width, height), (250, 250, 250))
    carre_x = width//60
    carre_y = height//60  
    position_moitie_x= carre_x//2
    position_moitie_y= carre_y//2
    pointeur_y = 0 - carre_y
    for loop in range(60):
        pointeur_y += carre_y
        pointeur_x = 0 - carre_x
        for loop in range(60):
            pointeur_x += carre_x
            for y in range(pointeur_y, pointeur_y + carre_y):
                for x in range(pointeur_x, pointeur_x + carre_x):
                    pixel = im.getpixel((position_moitie_x + pointeur_x, position_moitie_y + pointeur_y))
                    im_new.putpixel((x,y), pixel)
    x = width 
    pixel = im_new.getpixel((x -1,1))
    while pixel == (250, 250, 250):
        x -= 1
        pixel = im_new.getpixel((x -1,1))
    y = height
    pixel = im_new.getpixel((1,y -1))
    while pixel == (250, 250, 250):
        y -= 1
        pixel = im_new.getpixel((1,y -1)) 
    im_new2 = Image.new("RGB", (x, y), (250, 250, 250))
    for x1 in range(x):
        for y1 in range(y):
            pixel = im_new.getpixel((x1, y1))
            im_new2.putpixel((x1, y1), pixel) 

    return display(im_new2)


#Appel des fonctions

if reponse == "1":
    carre_blanc()

if reponse == "2": 
    bande()

if reponse == "3":
    extension()

if reponse == "4" :
    quadrillage()

if reponse == "5" :
    inversion()

if reponse == "6" :
    quatre_image()

if reponse == "7":
    pixeliser()
