#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

# Const
from code.Const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')  # loading menu image
        self.rect = self.surf.get_rect(left=0, top=0)  #

    def run(self):
        # Music
        pygame.mixer.music.load('./asset/menu.mp3')  # menu music
        pygame.mixer.music.play(-1)  # (-1) - loop

        while True:
            # Window
            self.window.blit(source=self.surf, dest=self.rect)

            # Text menu
            self.menu_text(50, "City", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # Update the full display Surface to the screen
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # render image
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # rect
        self.window.blit(source=text_surf, dest=text_rect)  # draw image
