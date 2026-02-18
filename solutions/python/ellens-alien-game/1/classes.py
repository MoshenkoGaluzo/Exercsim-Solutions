"""Solution to Ellen's Alien Game exercise."""


class Alien:

    total_aliens_created = 0
    
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        self.health = 3
        Alien.total_aliens_created += 1
        
    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health < 1:
            return False   
        return True

    def teleport(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        pass

    def collision_detection(self, other_object):
        pass


    
    pass

def new_aliens_collection(alien_start_positions):
    result = []
    for pos in alien_start_positions:
        result.append(Alien(pos[0], pos[1]))
    return result

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
