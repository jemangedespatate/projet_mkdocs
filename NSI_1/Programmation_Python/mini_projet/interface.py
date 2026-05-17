import pygame
import sys
import time
from pendu import *

class PenduGame:
    def __init__(self):
        pygame.init()

        self.width, self.height = 400, 400
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Jeu du Pendu")

        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

        self.pendu = 0
        self.mot_a_trouver = choix_mot("pendu_dico.txt").upper()
        self.mot_cache = cacher_mot(self.mot_a_trouver)

        self.guessed_letters = set()

        self.x_start = 175
        self.y_start = 350
        self.beam_length = 100
        self.crossbar_length = 100
        self.line_thickness = 5
        self.x_corde = self.x_start + self.crossbar_length // 1.5
        self.y_corde = self.y_start - self.beam_length + self.line_thickness

    def draw_potence(self):
        pygame.draw.rect(self.screen, self.black, (self.x_start - self.line_thickness // 2, self.y_start - self.beam_length, self.line_thickness, self.beam_length))
        pygame.draw.rect(self.screen, self.black, (self.x_start, self.y_start - self.beam_length, self.crossbar_length // 1.5, self.line_thickness))
        pygame.draw.rect(self.screen, self.black, (self.x_start - self.crossbar_length // 2, self.y_start, self.crossbar_length, self.line_thickness))
        pygame.draw.rect(self.screen, self.black, (self.x_corde, self.y_corde - self.line_thickness, self.line_thickness, 20))

    def draw_pendu(self):
        if self.pendu > 0:
            pygame.draw.circle(self.screen, self.black, (self.x_corde + self.line_thickness // 2, self.y_corde + 20), 10, width=5)
        if self.pendu > 1:
            pygame.draw.rect(self.screen, self.black, (self.x_corde, self.y_corde + 30, self.line_thickness, 30))
        if self.pendu > 2:
            pygame.draw.polygon(self.screen, self.black, [(self.x_corde, self.y_corde + 30),
                                                           (self.x_corde, self.y_corde + 35),
                                                           (self.x_corde - 10, self.y_corde + 55),
                                                           (self.x_corde - 10, self.y_corde + 50)])
        if self.pendu > 3:
            pygame.draw.polygon(self.screen, self.black, [(self.x_corde + self.line_thickness, self.y_corde + 30),
                                                           (self.x_corde + self.line_thickness, self.y_corde + 35),
                                                           (self.x_corde + 10 + self.line_thickness, self.y_corde + 55),
                                                           (self.x_corde + 10 + self.line_thickness, self.y_corde + 50)])
        if self.pendu > 4:
            pygame.draw.polygon(self.screen, self.black, [(self.x_corde, self.y_corde + 30 + 25),
                                                           (self.x_corde, self.y_corde + 35 + 25),
                                                           (self.x_corde - 10, self.y_corde + 55 + 25),
                                                           (self.x_corde - 10, self.y_corde + 50 + 25)])
        if self.pendu > 5:
            pygame.draw.polygon(self.screen, self.black, [(self.x_corde + self.line_thickness, self.y_corde + 30 + 25),
                                                           (self.x_corde + self.line_thickness, self.y_corde + 35 + 25),
                                                           (self.x_corde + 10 + self.line_thickness,
                                                            self.y_corde + 55 + 25),
                                                           (self.x_corde + 10 + self.line_thickness,
                                                            self.y_corde + 50 + 25)])

    def draw_guessed_letters(self):
        guessed_text = self.font_small.render("Guessed Letters: " + ", ".join(sorted(self.guessed_letters)), True, self.black)
        self.screen.blit(guessed_text, (self.width // 2 - guessed_text.get_width() // 2, 10))

    def draw_word(self):
        word_text = self.font_large.render(self.mot_cache, True, self.black)
        self.screen.blit(word_text, (self.width // 2 - word_text.get_width() // 2, 100))

    def run(self):

        while True:
            self.screen.fill((255, 255, 255))  # Set alpha for screen surface

            self.draw_potence()
            self.draw_pendu()
            self.draw_guessed_letters()
            self.draw_word()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key >= pygame.K_a and event.key <= pygame.K_z:
                        caractere = chr(event.key).upper()
                        if caractere not in self.guessed_letters:
                            self.guessed_letters.add(caractere)
                            if verifier_lettre(self.mot_a_trouver, caractere):
                                self.mot_cache = lettre(self.mot_a_trouver, self.mot_cache, caractere)
                            else:
                                self.pendu = nb_erreur(self.pendu)

            pygame.display.flip()
            self.clock.tick(30)

            if self.pendu == 6:
                self.screen.fill((255 , 255 , 255 , 220))
                result_text = "Perdu ! Le mot était : " + self.mot_a_trouver
                word_text = self.font_small.render(result_text, True, self.black)
                self.screen.blit(word_text, (self.width // 2 - word_text.get_width() // 2, 200))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                sys.exit()
            elif "_" not in self.mot_cache:
                self.screen.fill((255, 255, 255,150))
                result_text = "Bravo ! Vous avez trouvé le mot : " + self.mot_a_trouver
                word_text = self.font_small.render(result_text, True, self.black)
                self.screen.blit(word_text, (self.width // 2 - word_text.get_width() // 2, 200))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    pendu_game = PenduGame()
    pendu_game.run()
