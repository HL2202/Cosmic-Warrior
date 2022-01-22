import math
from os import close
import config

class Player:

    #   Class variables to determine when the spaceship has rotated sufficiently, a bullet is already fired and whether an asteroid can be destroyed without the need for movement

    rotated = False
    bullet_fired = False
    found_close = False


    def __init__(self):
        
        # Enter your code here
        
        pass

    def action(self, spaceship, asteroid_ls, bullet_ls, fuel, score):
        
        # Enter your code here

        fuel -= 1
                
        thrust = False
        left = False
        right = False
        bullet = False

        lowest_dist = 0
        closest_ast = 0

        #   First check the vicinity of the spaceship to see if any asteroids can be reached by only turning and not moving

        for new_asteroid in asteroid_ls:

            dist = spaceship.get_distance(new_asteroid)

            #   If the spaceship has not already been turned sufficiently to be in the same direction as the asteroid, continue turning the spaceship left/right

            if not self.rotated:

                #   Method to calculate the angle of inclination using the arctan() formula
                                            
                angle_diff = math.degrees(math.atan((new_asteroid.y - spaceship.y) / (spaceship.x - new_asteroid.x)))


                if angle_diff < 0:

                    if spaceship.x - new_asteroid.x < 0:

                        angle_diff += 360
                
                    else:

                        angle_diff += 180

                #First check if any asteroid can be reached in the vicinity without moving

                #   If spaceship requires less than 6 turns (< 90 degrees) left or right to reach the asteroid

                if abs(spaceship.angle - angle_diff) <= 90 and dist <= 120:

                    if angle_diff < spaceship.angle and not self.rotated: 
                    
                        #   Turn right

                        right = True
                        revolution = False

                        if spaceship.angle - config.angle_increment < 0:

                            adj_angle = spaceship.angle - config.angle_increment + 360
                            revolution = True
                    
                        else:

                            adj_angle = spaceship.angle - config.angle_increment

                        if adj_angle < angle_diff or revolution:

                            self.rotated = True
                
                    elif angle_diff > spaceship.angle and not self.rotated:
                    
                        #   Turn left

                        left = True
                        revolution = False

                        if spaceship.angle - config.angle_increment >= 360:

                            adj_angle = spaceship.angle + config.angle_increment - 360
                            revolution = True 
                    
                        else:

                            adj_angle = spaceship.angle + config.angle_increment

                        if adj_angle > angle_diff or revolution:

                            self.rotated = True

                #   If spaceship requires more than 6 turns (> 90 degrees) left or right to reach the asteroid

                elif abs(spaceship.angle - angle_diff) <= 180 and dist <= 100 and not self.rotated:

                    if angle_diff < spaceship.angle and not self.rotated: 
                    
                        #   Turn right

                        right = True
                        revolution = False

                        if spaceship.angle - config.angle_increment < 0:

                            adj_angle = spaceship.angle - config.angle_increment + 360
                            revolution = True
                    
                        else:

                            adj_angle = spaceship.angle - config.angle_increment

                        if adj_angle < angle_diff or revolution:

                            self.rotated = True
                
                    elif angle_diff > spaceship.angle and not self.rotated:
                    
                        #   Turn left

                        left = True
                        revolution = False

                        if spaceship.angle - config.angle_increment >= 360:

                            adj_angle = spaceship.angle + config.angle_increment - 360
                            revolution = True 
                    
                        else:

                            adj_angle = spaceship.angle + config.angle_increment

                        if adj_angle > angle_diff or revolution:

                            self.rotated = True
            

            
        #If there is an asteroid nearby, then start to turn in the direction of the asteroid and fire bullet when the angles align

            if self.rotated:
            
                my_asteroid = asteroid_ls[int(closest_ast)]

                #   Large asteroids have a larger readius so bullet can be fired sooner

                if dist <= 120 and not self.bullet_fired and my_asteroid.obj_type.lower() == "asteroid_large":

                    bullet = True
                    self.bullet_fired = True
                
                #   Small asteroids have a smaller radius so spaceship needs to be closer to ensure bullet hits asteroid
                
                elif dist <= 90 and not self.bullet_fired and my_asteroid.obj_type.lower() == "asteroid_small":

                    bullet = True
                    self.bullet_fired = True
            
                else:
                    
                    #   Check if existing bullets collide with asteroids

                    if len(bullet_ls) > 0:
                
                        for new_bullet in bullet_ls:

                            if new_bullet.collide_with(my_asteroid):

                                self.rotated = False 
                                self.bullet_fired = False
                
                    #   Check if existing bullets expire each frame

                    elif len(bullet_ls) == 0 and self.bullet_fired:

                        self.bullet_fired = False

        #If there are no asteroids nearby, scan the map for the nearest asteroid

        if not self.found_close:

            for i in range(len(asteroid_ls)):

                new_asteroid = asteroid_ls[i]

                dist = spaceship.get_distance(new_asteroid)
                
                #   Set the lowest asteroid to its index position int he list

                if lowest_dist == 0:

                    lowest_dist += dist
                    closest_ast += i
                
                elif dist < lowest_dist:

                    lowest_dist = 0
                    lowest_dist += dist
                    closest_ast = 0
                    closest_ast += i   

            my_asteroid = asteroid_ls[int(closest_ast)]

            #   Method to get angle of inclination

            angle_diff =  math.degrees(math.atan((spaceship.y - my_asteroid.y) / (spaceship.x - my_asteroid.x)))

            set_down = False

            if abs(spaceship.x - my_asteroid.x) < 10:

                set_down = True
            
            if set_down:

                angle_diff = 270

            #   Determine which quadrant the asteroid is in: this method is important for determining the correct angle the spaceship should move towards in order to reachasteroid

            if angle_diff < 0 and not set_down:

                if spaceship.x - my_asteroid.x < 0 and spaceship.y - my_asteroid.y < 0 and (abs(spaceship.x - my_asteroid.x) > 20 or abs(spaceship.y - my_asteroid.y) > 20):

                    angle_diff += 360
                
                elif spaceship.x - my_asteroid.x > 0 and spaceship.y - my_asteroid.y < 0 and (abs(spaceship.x - my_asteroid.x) > 20 or abs(spaceship.y - my_asteroid.y) > 20):

                    if 85 < angle_diff < 90:

                        angle_diff += 180

                    else:

                        angle_diff += 270
                
                elif spaceship.x - my_asteroid.x < 0 and spaceship.y - my_asteroid.y > 0 and (abs(spaceship.x - my_asteroid.x) > 20 or abs(spaceship.y - my_asteroid.y) > 20):

                    angle_diff = - angle_diff
                
                else:

                    angle_diff += 180
            
            elif spaceship.x > my_asteroid.x and spaceship.y > my_asteroid.y and angle_diff > 0 and (abs(spaceship.x - my_asteroid.x) > 20 or abs(spaceship.y - my_asteroid.y) > 20) and not set_down:

                angle_diff = 180 - angle_diff
            
            elif spaceship.x < my_asteroid.x and spaceship.y < my_asteroid.y and angle_diff > 0 and (abs(spaceship.x - my_asteroid.x) > 20 or abs(spaceship.y - my_asteroid.y) > 20) and not set_down:

                if 85 < angle_diff < 90:

                    angle_diff += 180

                else:

                    angle_diff = 360 - angle_diff
            
            #   Update the movement each frame to determine if the spaceship's path has deviated from asteroid motion, in which case adjust the spaceship's direction of movement
            
            if self.rotated:

                if my_asteroid.obj_type.lower() == "asteroid_large":

                    if abs(spaceship.angle - angle_diff) > 15:

                        self.rotated = False
                
                else:
                    
                    if abs(spaceship.angle - angle_diff) > 5:

                        self.rotated = False

            if angle_diff < spaceship.angle and not angle_diff < spaceship.angle - 180 and not self.rotated: 
                    
                #   Turn right
                right = True
                revolution = False

                if spaceship.angle - config.angle_increment < 0:

                    adj_angle = spaceship.angle - config.angle_increment + 360
                    revolution = True
                    
                else:

                    adj_angle = spaceship.angle - config.angle_increment

                if adj_angle < angle_diff or revolution:

                    self.rotated = True
                
            elif angle_diff > spaceship.angle and not angle_diff > spaceship.angle + 180 and not self.rotated:
                    
                #   Turn left
                left = True
                revolution = False

                if spaceship.angle - config.angle_increment >= 360:

                    adj_angle = spaceship.angle + config.angle_increment - 360
                    revolution = True 
                    
                else:

                    adj_angle = spaceship.angle + config.angle_increment

                if adj_angle > angle_diff or revolution:

                    self.rotated = True
            
            elif angle_diff < spaceship.angle - 180 and not self.rotated:

                #   Turn left
                left = True
                revolution = False

                if spaceship.angle - config.angle_increment >= 360:

                    adj_angle = spaceship.angle + config.angle_increment - 360
                    revolution = True 
                    
                else:

                    adj_angle = spaceship.angle + config.angle_increment

                if adj_angle > angle_diff or revolution:

                    self.rotated = True

            elif angle_diff > spaceship.angle + 180 and not self.rotated:

                #   Turn right
                right = True
                revolution = False

                if spaceship.angle - config.angle_increment < 0:

                    adj_angle = spaceship.angle - config.angle_increment + 360
                    revolution = True
                    
                else:

                    adj_angle = spaceship.angle - config.angle_increment

                if adj_angle < angle_diff or revolution:

                    self.rotated = True 

            #Start moving in the direction of the nearest asteroid and turn accordingly

            if self.rotated:

                thrust = True

                dist = spaceship.get_distance(my_asteroid)

                #   Determine whether to fire bullet for large asteroid

                if dist <= 120 and not self.bullet_fired and my_asteroid.obj_type.lower() == "asteroid_large":

                    bullet = True
                    self.bullet_fired = True

                #   Determine whether to fire bullet for small asteroid
                
                elif dist <= 90 and not self.bullet_fired and my_asteroid.obj_type.lower() == "asteroid_small":

                    bullet = True
                    self.bullet_fired = True
            
                else:
                
                    if len(bullet_ls) > 0:
                
                        for new_bullet in bullet_ls:

                            if new_bullet.collide_with(my_asteroid):

                                self.rotated = False 
                                self.bullet_fired = False
                
                    elif len(bullet_ls) == 0 and self.bullet_fired:

                        self.bullet_fired = False

        return (thrust, left, right, bullet)

    # You can add additional methods if required
