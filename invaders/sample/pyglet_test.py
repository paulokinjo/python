"""shows the string '---o---', screen center should be on the 'o'
"""

from pyglet.gl import *
import pyglet
from pyglet.window import key


window = pyglet.window.Window(640, 480)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.has_exit = True

@window.event
def on_draw():
    window.clear()
    label.draw()

def update(dt):
    pass
pyglet.clock.schedule_interval(update, 1/30.)

label = pyglet.text.Label('---o---',
                          font_size=14,
                          x=window.width // 2, y=window.height // 2, 
                          anchor_x='center')

if __name__ == '__main__':
    pyglet.app.run()