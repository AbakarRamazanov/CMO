import cocos
import pyglet


class DisplayPurpleRect(cocos.layer.Layer):

    background_sprite = 0
    house = 0

    def __init__(self):
        super(DisplayPurpleRect, self).__init__()
        self.house = cocos.sprite.Sprite('img/ex2.png', anchor=(0.0, 0.0))
        self.house.scale = 0.5
        self.background_sprite = cocos.sprite.Sprite(pyglet.image.load_animation('img/space1.gif'), anchor=(0.0, 0.0))
        self.background_sprite.position = (0, 0)
        self.background_sprite.rotation = 0
        self.add(self.background_sprite, z=0)
        self.add(self.house, z=5)


    def set_size_background(self, width, heigth):
        self.background_sprite.scale_x = width / self.background_sprite.width
        self.background_sprite.scale_y = heigth / self.background_sprite.height
        pass

    def set_position_house(self, width, height):
        self.house.position = width/2 - self.house.width/2, 0





Dwidth = 800
Dheight = 800
cocos.director.director.init(width=Dwidth, height=Dheight, caption="Hello World", fullscreen=False)

display = DisplayPurpleRect()
display.set_size_background(Dwidth, Dheight)
display.set_position_house(Dwidth, Dheight)

main_scene = cocos.scene.Scene(display)
cocos.director.director.run(main_scene)
