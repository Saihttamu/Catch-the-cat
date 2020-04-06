# CATCH THE CAT Game
# by Saihttamu or Amistath


import random, pygame, sys
from pygame.locals import *


# Définition des variables importantes

# VARIABLES DU JEU

#global FPS, speed

FPS = 30
speed = 5  # en pixels par FPS


LARGEUR = 1110
HAUTEUR = 625
gap = 15


# COULEURS
#        ( R    G    B )
BLANC  = (255, 255, 255)
NOIR   = (  0,   0,   0)
ROUGE  = (255,   0,   0)
BLEU   = (  0,   0, 255)
VERT   = (  0, 255,   0)
GRIS   = (100, 100, 100)
JAUNE  = (255, 255,   0)
VIOLET = (255,   0, 255)
CYAN   = (  0, 255, 255)

ALLCOLORS = (BLANC, NOIR, ROUGE, BLEU, VERT, GRIS, JAUNE, VIOLET, CYAN)
COULEUR = BLANC
FONT = NOIR

#def main():
#global FPSCLOCK, DISPSURF, catImage
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPSURF = pygame.display.set_mode((LARGEUR, HAUTEUR), 0, 32)
pygame.display.set_caption('Catch the Cat!')


titreObj = pygame.font.Font('freesansbold.ttf', 64)
titreSurfObj = titreObj.render('Catch the cat!', False, BLANC, NOIR)
titreRectObj = titreSurfObj.get_rect()
titreRectObj.center = (LARGEUR/2, HAUTEUR/2 - 5*gap)
 
comptObj = pygame.font.Font('freesansbold.ttf', 50)

viesObj = pygame.font.Font('freesansbold.ttf', 50)

coulObj = pygame.font.Font('freesansbold.ttf', 50)
coulSurfObj = coulObj.render('COULEUR', False, NOIR, BLANC)
coulRectObj = coulSurfObj.get_rect()
coulRectObj.center = (LARGEUR/2, titreRectObj.bottom + 2*gap + 6*int(coulRectObj.height/2))

goObj = pygame.font.Font('freesansbold.ttf', 70)
goSurfObj = goObj.render('GAME OVER', False, NOIR, BLANC)
goRectObj = goSurfObj.get_rect()
goRectObj.center = (LARGEUR/2, HAUTEUR/2)

catImage = pygame.image.load('cat.png')

catx = 10  # position de départ du chat
caty = 10
catL = catImage.get_width()
catH = catImage.get_height()

catLimH = 10 # en y
catLimD = LARGEUR - 10 - catL # en x
catLimB = HAUTEUR - 10 - catH # en y
catLimG = 10 # en x
    
direction = 'droite'
    
mousex = 0
mousey = 0
# mouseClicked = False
compteur = 0
vies = 5

gameover = False


def catClicked():
    return ((catx <= mousex <= (catx + catL)) and (caty <= mousey <= (caty + catH)))

 
def coulClicked():
    return ((coulRectObj.left <= mousex <= coulRectObj.right) and (coulRectObj.top <= mousey <= coulRectObj.bottom))
    
while True: # main game loop
    
    
    comptSurfObj = comptObj.render('Clicks : ' + str(compteur), False, FONT, COULEUR)
    comptRectObj = comptSurfObj.get_rect()
    comptRectObj.center = (LARGEUR/2, titreRectObj.bottom + gap + int(comptRectObj.height/2))    
    
    viesSurfObj = viesObj.render('Vies restantes : ' + str(vies), False, FONT, COULEUR)
    viesRectObj = viesSurfObj.get_rect()
    viesRectObj.center = (LARGEUR/2, comptRectObj.bottom + gap + int(viesRectObj.height/2))
    
    DISPSURF.fill(COULEUR)
    
    if not gameover:
        DISPSURF.blit(titreSurfObj, titreRectObj)
        DISPSURF.blit(comptSurfObj, comptRectObj)
        DISPSURF.blit(viesSurfObj, viesRectObj)
        DISPSURF.blit(coulSurfObj, coulRectObj)
    else:
        DISPSURF.blit(goSurfObj, goRectObj)
    
    
    if direction == 'droite':
        if catx + speed < catLimD:
            catx += speed
        else:
            catx = catLimD
            direction = 'bas'
        
    elif direction == 'bas':
        if caty + speed < catLimB:
            caty += speed
        else:
            caty = catLimB
            direction = 'gauche'
             
    elif direction == 'gauche':
        if catx - speed > catLimG:
            catx -= speed
        else:
            catx = catLimG
            direction = 'haut'  
        
    elif direction == 'haut':
        if caty - speed > catLimH:
            caty -= speed
        else:
            caty = catLimH
            direction = 'droite'
                
        
    DISPSURF.blit(catImage, (catx, caty))
    
    
    for event in pygame.event.get():
        
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        
#        elif event.type == MOUSEMOTION:
#            mousex, mousey = event.pos
        
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            if gameover:
                speed = 5
                compteur = 0
                vies = 5
                gameover = False
            elif catClicked():
                compteur += 1
                speed += 5
            elif coulClicked():
                COULEUR = ALLCOLORS[random.randint(0, len(ALLCOLORS)-1)]
                if COULEUR == NOIR:
                    FONT = BLANC
                else:
                    FONT = NOIR
            else:
                vies -= 1
                if vies == 0:
                    gameover = True
            
        
#        elif event.type == MOUSEBUTTONDOWN and gameover:
#            speed = 5
#            compteur = 0
#            vies = 10
#            gameover = False
                
    
    
            
        
    pygame.display.update()
        
    FPSCLOCK.tick(FPS)
        
#if __name__ == '__main__':
#    main()
    
