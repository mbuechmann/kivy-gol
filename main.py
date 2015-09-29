import kivy
kivy.require('1.4.1')

from kivy.config import Config
Config.read('gol.ini')
Config.set('graphics', 'width', '256')
Config.set('graphics', 'height', '256')


from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window

from board_widget import BoardWidget
from population import Population

class GameOfLifeApp(App):

    _board = None
    _population = None


    def build(self):
        self._population = Population(cols=256, rows=256)
        self._board = BoardWidget(width=256, height=256, population = self._population)
        Clock.schedule_interval(self.callback, 0.1)
        return self._board

    def callback(self, dt):
        self._population.evolve() 
        self._board.update_graphics()

if __name__ == '__main__':
    GameOfLifeApp().run()
