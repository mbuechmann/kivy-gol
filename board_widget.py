import kivy
kivy.require('1.4.1')

from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.graphics.texture import Texture

class BoardWidget(Widget):

    _population = None
    _texture = None
    
    def __init__(self, **kwargs):
        super(BoardWidget, self).__init__(**kwargs)
        if kwargs.has_key('population'):
            self._population = kwargs['population']
        self._texture = Texture.create(size=(self.width, self.height), colorfmt='rgb')
        self.update_graphics()

    def update_graphics(self, *largs):
        self.canvas.clear()
        a = []
        for row in range(self._population.rows):
            for col in range(self._population.cols):
                if self._population.cells[col][row]:
                    a.extend([255, 255, 255])
                else:
                    a.extend([0, 0, 0])

        buf = ''.join(map(chr, a)) 
        self._texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        with self.canvas:      
            Rectangle(pos=(0, 0), size=self.size, texture=self._texture)
