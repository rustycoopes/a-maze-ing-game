import pygame

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
 
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet     
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey((0,0,0))
 
        # Return the image
        return image


    
def create_sprites(cell_size):
    """ Loads required images for games, to make an appropriately sized set of images available to the painter
    """

    ss = SpriteSheet('images/players.png')
    sprite_size_H = 80
    sprite_size_W = 80
    player_sprites= {pygame.K_RIGHT: ss.get_image(  1 * sprite_size_W, 0  * sprite_size_H,  sprite_size_W, sprite_size_H), 
         pygame.K_LEFT: ss.get_image( 10 * sprite_size_W, 2  * sprite_size_H,  sprite_size_W, sprite_size_H), 
         pygame.K_UP: ss.get_image(  1 * sprite_size_W, 5  * sprite_size_H,  sprite_size_W, sprite_size_H), 
         pygame.K_DOWN: ss.get_image(  6 * sprite_size_W, 5  * sprite_size_H,  sprite_size_W, sprite_size_H)}
    player_sprites[pygame.K_RIGHT] =  pygame.transform.scale(player_sprites[pygame.K_RIGHT], (int(cell_size * 0.5), int(cell_size * 0.5)))
    player_sprites[pygame.K_LEFT] =  pygame.transform.scale(player_sprites[pygame.K_LEFT], (int(cell_size * 0.5), int(cell_size * 0.5)))
    player_sprites[pygame.K_UP] =  pygame.transform.scale(player_sprites[pygame.K_UP], (int(cell_size * 0.5), int(cell_size * 0.5)))
    player_sprites[pygame.K_DOWN] =  pygame.transform.scale(player_sprites[pygame.K_DOWN], (int(cell_size * 0.5), int(cell_size * 0.5)))
    return player_sprites

def create_finish(cell_size):
    finish = pygame.image.load('images/finish.png')
    finish = pygame.transform.scale(finish, (cell_size -2, cell_size -2))
    return finish

