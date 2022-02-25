""" code avec fonction yin_yang dessiné avec turtle """
import turtle

def yin_yang(rayon, color1='black', color2='white'):
    """ dessine un logo yin-yang de rayon rayon """

    def yang (rayon, couleur1, couleur2):
        """ dessin du yang à l'intérieur du yin (ou vice versa) """
        pass # code TODO

    def yin(rayon, couleur1, couleur2):
        """ dessine la moitié d'un yin-yang
            utilise la fonction yang """
        pass # code TODO

    #code de yin_yang
    turtle.reset()
    turtle.width(2)
    yin(rayon, color1, color2)
    yin(rayon, color2, color1)
    turtle.hideturtle()
    return

#code principal
yin_yang(200) #réalise le logo de rayon 200