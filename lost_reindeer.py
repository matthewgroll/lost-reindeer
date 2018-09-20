from arcade import *
import os

SPRITE_SCALING = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Player setup
        self.score = 0
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None

    def setup(self):
        # Set up the game
        self.all_sprites_list = SpriteList()
        self.wall_list = SpriteList()

        self.score = 0
        self.player_sprite = Sprite("images/deer.png", SPRITE_SCALING)

        # Set up the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.all_sprites_list.append(self.player_sprite)

        def create_walls(bottom, top, freq, axis, align):
            for j in range(bottom, top, freq):
                wall = Sprite("images/gift_box.png", SPRITE_SCALING)
                if axis == 'x':
                    wall.center_x = j
                    wall.center_y = align
                if axis == 'y':
                    wall.center_x = align
                    wall.center_y = j
                self.all_sprites_list.append(wall)
                self.wall_list.append(wall)

        # middle column
        create_walls(273, 600, 100, 'y', 465)

        # right most column
        create_walls(250, 600, 80, 'y', 550)

        # left most column
        create_walls(240, 600, 50, 'y', 200)

        # horizontal middle row
        create_walls(173, 650, 48, 'x', 200)

        self.physics_engine = PhysicsEngineSimple(self.player_sprite,
                                                  self.wall_list)

        # Background color
        set_background_color(color.ANTIQUE_BRONZE)

    def on_draw(self):
        # Render the screen
        start_render()

        # Draw sprites
        self.wall_list.draw()
        self.player_sprite.draw()

    def on_key_press(self, val, modifiers):
        # Called when a key is pressed

        if val == key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif val == key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif val == key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif val == key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, val, modifiers):
        # Called when a key is released

        if val == key.UP or val == key.DOWN:
            self.player_sprite.change_y = 0
        elif val == key.LEFT or val == key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):

        self.physics_engine.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    run()


if __name__ == "__main__":
    main()



