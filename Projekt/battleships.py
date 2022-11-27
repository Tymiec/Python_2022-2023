import pygame
import time
from pygame.locals import *
from random import randrange
import pygame, sys
from pygame.locals import *
import button

YELLOW = (192, 192, 192)
BLUE = (0, 0, 255)
w = 300
h = 400
BG = pygame.image.load("assets_temp/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets_temp/font.ttf", size)




class Temtris () :
	
	def __init__ (self) : # miejsce na zmienne

		# podstawowe ustawienia
		self.fps = 60
		wysokośćObrazu = 224
		self.proporcjeObrazu = 1.142857142857143

        ## USELESS? 
		self.PX = 4 # szerokość piksela
		self.PY = 4 # wysokość piksela
		self.X = 32 # szerokość sprite
		self.Y = 32 # wysokość sprite
		
		# kontroler NES
		
		# gracz 1
		self.A1 = K_l
		self.B1 = K_k
		self.UP1 = K_UP
		self.DOWN1 = K_DOWN
		self.LEFT1 = K_LEFT
		self.RIGHT1 = K_RIGHT
		self.START1 = K_RETURN
		self.SELECT1 = K_RSHIFT
		
		# gracz 2
		self.A2 = K_x
		self.B2 = K_z
		self.UP2 = K_g
		self.DOWN2 = K_b
		self.LEFT2 = K_v
		self.RIGHT2 = K_n
		self.START2 = K_RETURN
		self.SELECT2 = K_RSHIFT

        ## USELESS ###################################################################

		# zmienne sterujące gry
		self.WyzerujZmienneSterujące ()
		self.klawisze = {self.A1: False, self.B1: False, self.UP1: False, self.DOWN1: False, self.LEFT1: False, self.RIGHT1: False, self.START1: False, self.SELECT1: False, self.A2: False, self.B2: False, self.UP2: False, self.DOWN2: False, self.LEFT2: False, self.RIGHT2: False, self.START2: False, self.SELECT2: False}
		self.poprzednieKlawisze = {self.A1: False, self.B1: False, self.UP1: False, self.DOWN1: False, self.LEFT1: False, self.RIGHT1: False, self.START1: False, self.SELECT1: False, self.A2: False, self.B2: False, self.UP2: False, self.DOWN2: False, self.LEFT2: False, self.RIGHT2: False, self.START2: False, self.SELECT2: False}
		
		# startujemy pygame
		pygame.init()


        # dopasowanie okna gry do monitora
		monitor = pygame.display.Info()
		i = 1
		while wysokośćObrazu * i < monitor.current_h * 0.8 :
			i += 1

		pygame.mixer.init ()
		self.zegar = pygame.time.Clock ()
		self.okno = pygame.display.set_mode ((int (wysokośćObrazu * i * self.proporcjeObrazu), wysokośćObrazu * i), HWSURFACE|DOUBLEBUF|RESIZABLE)
		pygame.display.set_caption("BATTLESHIPS")
		self.obraz = pygame.surface.Surface (self.okno.get_rect ().size)
		self.obraz.fill ((0, 0, 0))

		img = pygame.image.load('assets/aim.png')
		img.convert()
		rect = img.get_rect()

		# grafika
		hamulec = True
		while hamulec is True: #TODO: Remove me :D
			self.tłoMenu = pygame.image.load ("Assets/Grafika/menu.png")
			self.tłoGra = pygame.image.load ("Assets/Grafika/gra.png")
			self.tłoGra2Graczy = pygame.image.load ("Assets/Grafika/gra dwoch graczy.png")
			self.koniecGryKlatka1 = pygame.image.load ("Assets/Grafika/koniec gry klatka 1.png")
			self.koniecGryKlatka2 = pygame.image.load ("Assets/Grafika/koniec gry klatka 2.png")
			self.koniecGryKlatka2dwochGraczy = pygame.image.load ("Assets/Grafika/koniec gry klatka 2 dwoch graczy.png")
			
			self.introSprite = pygame.image.load ("Assets/Grafika/intro sprite.png")
			self.strzałkaSprite = pygame.image.load ("Assets/Grafika/strzalka.png")
			self.klockiSprite = pygame.image.load ("Assets/Grafika/klocki sprite.png").convert_alpha ()
			self.klockiSpriteGracz1 = pygame.image.load ("Assets/Grafika/klocki sprite gracz 1.png").convert_alpha ()
			self.klockiSpriteGracz2 = pygame.image.load ("Assets/Grafika/klocki sprite gracz 2.png").convert_alpha ()
			self.fragmentySprite = pygame.image.load ("Assets/Grafika/fragmenty sprite.png").convert_alpha ()
			self.rozbijanieLiniiSprite = pygame.image.load ("Assets/Grafika/rozbijanie linii sprite.png").convert_alpha ()
			self.cyfrySprite = pygame.image.load ("Assets/Grafika/cyfry sprite.png").convert_alpha ()
			
			self.pauzaSprite = pygame.image.load ("Assets/Grafika/pauza.png").convert_alpha ()
			self.czaszkaSprite = pygame.image.load ("Assets/Grafika/czaszka.png").convert_alpha ()
			self.koronaSprite = pygame.image.load ("Assets/Grafika/korona.png").convert_alpha ()

			## MOJE

			self.start_img = pygame.image.load('C:\Repo\Python_2022-2023\Projekt\concept_3\pygame_tutorials-main\Button\start_btn.png').convert_alpha()
			self.exit_img = pygame.image.load('C:\Repo\Python_2022-2023\Projekt\concept_3\pygame_tutorials-main\Button\exit_btn.png').convert_alpha()

			self.start_button = button.Button(100, 200, self.start_img, 0.8)
			self.exit_button = button.Button(450, 200, self.exit_img, 0.8)


			## MOJE
			hamulec = False
			
    
	def Start (self) :
		
		print ("############################################################")
		print ("                        BATTLE SHIPZ                        ")
		print ("############################################################")
		print ()

		self.Intro ()
		
		# główna pętla
		while True :
			
			self.Menu ()
			self.Gra ()
			self.KoniecGry ()

	def OdświeżOkno (self) :
		
		for event in pygame.event.get() :
			# naciśnięcie X na oknie
			if event.type == QUIT:
				pygame.quit ()
				exit ()
			elif event.type == VIDEORESIZE:
				self.okno = pygame.display.set_mode((event.size[1] * self.proporcjeObrazu, event.size[1]), HWSURFACE|DOUBLEBUF|RESIZABLE)
		
		klawisze = pygame.key.get_pressed ()
		for klawisz in self.klawisze :
			
			self.poprzednieKlawisze[klawisz] = self.klawisze[klawisz]
			self.klawisze[klawisz] = klawisze[klawisz]
		
		self.okno.blit (pygame.transform.scale (self.obraz, self.okno.get_rect ().size), (0, 0))
		pygame.display.update ()
		self.zegar.tick (self.fps)
		

	def Intro (self) :
		
		# if not self.CzekajLubPomiń (32) :
			# return
		# time.sleep(10)
		pygame.mixer.music.load ("Assets/Dzwiek/intro.ogg")
		pygame.mixer.music.play ()
		
		for i in range (0, 4) :
			
			# rysuj na ekranie logo
			self.obraz.blit(self.introSprite, Rect (6 * self.X, 11 * self.Y, 608, 320), Rect (0, i * 320, 608, 320))
			
			if not self.CzekajLubPomiń (32) :
				return
		
		if not self.CzekajLubPomiń (180) :
			return
			
		pygame.mixer.music.stop ()
	
	def Menu (self) :
		
		# wyzeruj zmienne sterujące grą
		# self.WyzerujZmienneSterujące ()
		
		# # załaduj tło menu
		
		
		# utwórz strzałkę wskazującą na gre dla 1 lub 2 graczy
		# wszystkieSprite = pygame.sprite.Group()
		
		# odtwarzaj muzykę w menu
		pygame.mixer.music.load ("Assets/Dzwiek/drunken_sailor_8_bit.ogg") # TODO:przyciszyć
		pygame.mixer.music.play (-1)
		
		self.OdświeżOkno ()
		
		while True :
			self.obraz.blit (self.tłoMenu, self.tłoMenu.get_rect())
			if self.start_button.draw(self.obraz):
				print('START')

				# self.obraz.blit(self.introSprite, Rect (6 * self.X, 11 * self.Y, 608, 320), Rect (0, 1 * 320, 608, 320))
			# self.SCREEN.fill("blue")
			# # START
			# if self.NaciśniętoKlawisz (self.START1) or self.NaciśniętoKlawisz (self.START2) :
			# 	return
			# # SELECT
			# elif self.NaciśniętoKlawisz (self.SELECT1) or self.NaciśniętoKlawisz (self.SELECT2) :
			# 	self.dwóchGraczy = not self.dwóchGraczy
				
			# 	# narysuj tło
				# self.obraz.blit (self.tłoMenu, self.tłoMenu.get_rect())
				
				# if self.dwóchGraczy :
				# 	strzałka.rect.y += self.Y
				# else :
				# 	strzałka.rect.y -= self.Y
				
				# wszystkieSprite.draw (self.obraz)

				
			self.OdświeżOkno ()
	
######################################################################
#       PRZYDATNE
######################################################################
	
	def Czekaj (self, klatki) :
		for _ in range (0, klatki) :
			self.OdświeżOkno ()
	
	def CzekajLubPomiń (self, klatki) :
		for _ in range (0, klatki) :
			
			if self.NaciśniętoKlawisz (self.START1) or self.NaciśniętoKlawisz (self.START2) :
				return False
				
			self.OdświeżOkno ()
		
		return True
		
	def NaciśniętoKlawisz (self, klawisz) :
		
		if self.klawisze[klawisz] and not self.poprzednieKlawisze[klawisz] :
			return True
		else :
			return False
	
	def WyzerujZmienneSterujące (self) :
		self.pauza = False
		self.poziom = 0
		self.liczbaLinii = [0, 0]
		self.liczbaLiniiCheems = [0, 0]
		self.liczbaLiniiDoge = [0, 0]
		self.liczbaLiniiBuffDoge = [0, 0]
		self.liczbaLiniiTemtris = [0, 0]
		self.liczbaPunktów = [0, 0]
		self.czasGry = 0
		self.dwóchGraczy = False
		self.obecnyGracz = 0
		self.zegarKontrolera = 10
		self.zegarKontroleraObrót = 10
		self.szybkośćOpadaniaKlocka = 60
		self.zegarOpadania = 60
		# self.plansza = self.Plansza (self)
	
def Main () :
	temtris = Temtris ()
	temtris.Start ()

if __name__ == "__main__" :
	Main ()
