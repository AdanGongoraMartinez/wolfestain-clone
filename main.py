import sys

import pygame as pg

from settings import FPS, RESOLUTION


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps(): .1f}")

    def draw(self):
        self.screen.fill("black")

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
