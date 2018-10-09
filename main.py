import cocos

class DisplayPurpleRect(cocos.layer.Layer):
    def __init__(self):
        super(DisplayPurpleRect, self).__init__()
        sprite = cocos.sprite.Sprite('img/ex2.png')
        sprite.position = 320,240
        sprite.scale = 0.5
        self.add(sprite)

cocos.director.director.init( width=800, height=600, caption="Hello World", fullscreen=False)
display_purple = DisplayPurpleRect()
main_scene = cocos.scene.Scene(display_purple)
cocos.director.director.run(main_scene)
