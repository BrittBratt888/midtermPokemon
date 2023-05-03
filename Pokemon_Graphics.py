import pygame

import time

import numpy as np

import sys

from pygame.locals import QUIT


# Delay printing

def delay_print(s):
    # print one character at a time

    for c in s:
        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(0.05)


# Create the class

class Pokemon:

    def __init__(self, game_instance, name, types, moves, EVs, health='=================='):
        # save variables as attributes

        self.name = name

        self.types = types

        self.moves = moves

        self.attack = EVs['ATTACK']

        self.defense = EVs['DEFENSE']

        self.health = health
        # Amount of health bars

        self.bars = 20
        self.game_instance = game_instance

    def update_screen(self, health):
        self.game_instance.display_images()
        pygame.draw.rect(self.game_instance.game_window, (0, 255, 0), [160, 180, len(health) * 10, 15])
        pygame.display.update()

    def fight(self, Pokemon2):
        # Allow two Pokemon to fight each other

        # Print fight information

        print('-----POKEMON BATTLE-----')

        print(f"\n{self.name}")

        print("TYPE/", self.types)

        print("Attack/", self.attack)

        print("DEFENSE/", self.defense)

        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))

        print("\nVS")

        print(f"\n{Pokemon2.name}")

        print("TYPE/", Pokemon2.types)

        print("Attack/", Pokemon2.attack)

        print("DEFENSE/", Pokemon2.defense)

        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages

        version = ['Fire', 'Grass', 'Water']

        for i, k in enumerate(version):

            if self.types == k:

                # Both are same type

                if Pokemon2.types == k:
                    string_1_attack = 'Its not very effective...'

                    string_2_attack = 'Its not very effective...'

                # Pokemon 2 is STRONG

                if Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon2.attack *= 2

                    Pokemon2.defense *= 2

                    self.attack /= 2

                    self.defense /= 2

                    string_1_attack = 'Its not very effective...\n'

                    string_2_attack = 'Its super effective!\n'

                # Pokemon2 is WEAK

                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2

                    self.defense *= 2

                    Pokemon2.attack /= 2

                    Pokemon2.defense /= 2

                    string_1_attack = 'Its super effective!\n'

                    string_2_attack = 'Its not very effective...\n'

        # Now for the actual fighting...
        # Continue while Pokemon still have health
        while (self.bars > 0) and (Pokemon2.bars > 0):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Print the health of both Pokemon
            print(f"{self.name}\t\tHEALTH\t{self.health}")

            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            self.update_screen(self.health)
            pygame.display.update()

            print(f"Go {self.name}!")

            for i, x in enumerate(self.moves):
                print(f"{i + 1}.", x)

            index = int(input('Pick a move: '))

            delay_print(f"{self.name} used {self.moves[index - 1]}!\n")

            time.sleep(1)

            delay_print(string_1_attack)

            # Determine damage

            Pokemon2.bars -= self.attack

            Pokemon2.health = ""

            # Add back bars plus defense boost

            for j in range(int(Pokemon2.bars + .1 * Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)

            print(f"{self.name}\t\tHEALTH\t{self.health}")

            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
            self.update_screen(self.health)
            pygame.display.update()
            time.sleep(.5)

            # Check to see if Pokemon fainted

            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')

                break

            # Pokemon2s turn
            print(f"Go {Pokemon2.name}!")

            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)

            index = int(input('Pick a move: '))

            delay_print(f"{Pokemon2.name} used {Pokemon2.moves[index - 1]}!\n")

            time.sleep(1)

            delay_print(string_2_attack)

            # Determine damage

            self.bars -= Pokemon2.attack

            self.health = ""

            # Add back bars plus defense boost

            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)

            print(f"{self.name}\t\tHEALTH\t{self.health}")

            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")
            self.update_screen(self.health)
            pygame.display.update()
            time.sleep(.5)

            # Check to see if Pokemon fainted

            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')

                break

        money = np.random.choice(5000)

        delay_print(f"Opponent paid you ${money}.")


class GameInstance:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.WIDTH = 800
        self.HEIGHT = 800
        self.game_window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.enemey_poke_pos = (450, 150)
        self.enemey_health = (140,150)
        self.poke_pos = (150, 350)
        self.poke_health = (340,350)
        self.pokemon = {
            'prinplup': {'path': 'assets/prinplup.png', 'size': (164, 164), 'pos': self.poke_pos},
            'grotle': {'path': 'assets/grotle.png', 'size': (164, 164), 'pos': self.enemey_poke_pos},
            'combusken': {'path': 'assets/combusken.png', 'size': (64, 64), 'pos': (0, 0)},
            'torchic': {'path': 'assets/torchic.png', 'size': (64, 64), 'pos': (0, 0)},
            'piplup': {'path': 'assets/piplup.png', 'size': (64, 64), 'pos': (0, 0)},
            'turtwig': {'path': 'assets/turtwig.png', 'size': (64, 64), 'pos': (0, 0)},
            'blaziken': {'path': 'assets/blaziken.png', 'size': (64, 64), 'pos': (0, 0)},
            'empoleon': {'path': 'assets/empoleon.png', 'size': (64, 64), 'pos': (0, 0)},
            'torterra': {'path': 'assets/torterra.png', 'size': (64, 64), 'pos': (0, 0)},

        }
        self.images = {
            'health_enemey': {'path': 'assets/health_bar.png', 'size': (240, 80), 'pos': self.enemey_health},
            'health_player': {'path': 'assets/health_bar.png', 'size': (240, 80), 'pos': self.poke_health},
        }
        pygame.display.set_caption('Pokemans')

        self.Prinplup = Pokemon(self, 'Prinplup', 'Water', ['Bubble Beam', 'Swagger', 'Fury Attack', 'Brine'],
                           {'ATTACK': 5, 'DEFENSE': 5})

        self.Grotle = Pokemon(self, 'Grotle', 'Grass', ['Curse', 'Bite', 'Mega Drain', 'Leech Seed'], {'ATTACK': 4, 'DEFENSE': 6})

    def game_loop(self):

        # Select pokemon
        pokemon = ('grotle', 'prinplup')
        for key, value in self.pokemon.items():
            if key in pokemon:
                self.images.update({key: value})

        while True:
            self.Grotle.fight(self.Prinplup)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def load_images(self):
        images = []
        for name, info in self.images.items():
            x = pygame.image.load(info['path'])
            x = pygame.transform.scale(x, info['size'])
            images.append({'surface': x, 'pos': info['pos']})
        return images

    def display_images(self):
        self.game_window.fill((255,255,255))
        for image in self.load_images():
            self.game_window.blit(image['surface'], image['pos'])


if __name__ == '__main__':

    GameInstance().game_loop()
