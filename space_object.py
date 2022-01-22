import math
import config

class SpaceObject:

    #   Class variables which invoke conditions / parameters to be used in the methods

    move_left = False
    move_right = False
    movement_speed = 0
    turn_angle = config.angle_increment
    radius = 0
    bullet_timer = 0

    spaceship_start = False
    radius_set = False
    speed_set = False
    angle_set = False
    bullet_ready = False


    def __init__(self, x, y, width, height, angle, obj_type, id):
        
        # Enter your code here

        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.angle = angle
        self.obj_type = obj_type
        self.id = id

    #   Turns left if object is a spaceship

    def turn_left(self):
        
        # Enter your code here

        if self.obj_type.lower() == "spaceship":
            
            self.move_left = True

            #   If the angle exceeds 360 degrees, go back to a full revolution

            if self.angle + self.turn_angle >= 360:
                
                self.angle = self.angle + self.turn_angle - 360
            
            else:
                
                self.angle += self.turn_angle

    #   Turns right if object is a spaceship

    def turn_right(self):
        
        # Enter your code here

        if self.obj_type.lower() == "spaceship":
            
            self.move_right = True

            #   If the angle goes below 0 degrees, go forward a full revolution

            if self.angle - self.turn_angle < 0:

                self.angle = self.angle - self.turn_angle + 360
            
            else:
                
                self.angle -= self.turn_angle

    #   Method to move all of the objects currently in the frame

    def move_forward(self):
        
        # Enter your code here

        #   Retrieve all of the correct speeds according to object type

        if self.obj_type.lower() == "spaceship":

            self.movement_speed = list(config.speed.values())[0]

            #   Get the change in x-coordinate through the cosine function
                
            x_coord = self.movement_speed * math.cos(math.radians(self.angle))

            #   Get the change in y-coordinate through the sine function

            y_coord = -self.movement_speed * math.sin(math.radians(self.angle))

            #   If the object goes beyond map, return back a full cycle on the other side of the map

            if self.x + x_coord > self.width:

                self.x = self.x + x_coord - self.width
                
            elif self.x + x_coord < 0:

                self.x = self.x + x_coord + self.width

            else:

                self.x += x_coord
            
            if self.y + y_coord > self.height:

                self.y = self.y + y_coord - self.height
                
            elif self.y + y_coord < 0:

                self.y = self.y + y_coord + self.height
            
            else:

                self.y += y_coord
        
        #   Repeat movement logic for bullet

        elif self.obj_type.lower() == "bullet":

            self.movement_speed = list(config.speed.values())[1]
                
            x_coord = self.movement_speed * math.cos(math.radians(self.angle))
            y_coord = -self.movement_speed * math.sin(math.radians(self.angle))

            if self.x + x_coord > self.width:

                self.x = self.x + x_coord - self.width
                
            elif self.x + x_coord < 0:

                self.x = self.x + x_coord + self.width

            else:

                self.x += x_coord
            
            if self.y + y_coord > self.height:

                self.y = self.y + y_coord - self.height
                
            elif self.y + y_coord < 0:

                self.y = self.y + y_coord + self.height
            
            else:

                self.y += y_coord
        
        #   Repeat movement logic for small asteroid

        elif self.obj_type.lower() == "asteroid_small":

            self.movement_speed = list(config.speed.values())[2]
                
            x_coord = self.movement_speed * math.cos(math.radians(self.angle))
            y_coord = -self.movement_speed * math.sin(math.radians(self.angle))

            if self.x + x_coord > self.width:

                self.x = self.x + x_coord - self.width
                
            elif self.x + x_coord < 0:

                self.x = self.x + x_coord + self.width

            else:

                self.x += x_coord
            
            if self.y + y_coord > self.height:

                self.y = self.y + y_coord - self.height
                
            elif self.y + y_coord < 0:

                self.y = self.y + y_coord + self.height
            
            else:

                self.y += y_coord
        
        #   Repeat movement logic for large asteroid

        else:

            self.movement_speed = list(config.speed.values())[3]
            
            x_coord = self.movement_speed * math.cos(math.radians(self.angle))
            y_coord = self.movement_speed * math.sin(math.radians(self.angle))

            if self.x + x_coord > self.width:

                self.x = self.x + x_coord - self.width
                
            elif self.x + x_coord < 0:

                self.x = self.x + x_coord + self.width

            else:

                self.x += x_coord
            
            if self.y + y_coord > self.height:

                self.y = self.y + y_coord - self.height
                
            elif self.y + y_coord < 0:

                self.y = self.y + y_coord + self.height
            
            else:

                self.y += y_coord

    #   Returns the x-y coordinates of object as a tuple

    def get_xy(self):
        
        # Enter your code here

        return (self.x, self.y)

    #   Returns True if object collides with other object, False otherwise

    def collide_with(self, other):
        
        # Enter your code here

        #   First case check for direct overlap

        if self.x == other.x or self.y == other.y:

            return True
        
        #   Determine the appropriate radius of each object type

        if self.obj_type.lower() == "spaceship":

            self.radius = list(config.radius.values())[0]
        
        elif self.obj_type.lower() == "bullet":

            self.radius = list(config.radius.values())[1]
        
        elif self.obj_type.lower() == "asteroid_small":

            self.radius = list(config.radius.values())[2]
    
        else:

            self.radius = list(config.radius.values())[3]
        
        
        if other.obj_type.lower() == "spaceship":

            radius_other = list(config.radius.values())[0]
        
        elif other.obj_type.lower() == "bullet":

            radius_other = list(config.radius.values())[1]
        
        elif other.obj_type.lower() == "asteroid_small":

            radius_other = list(config.radius.values())[2]
    
        else:

            radius_other = list(config.radius.values())[3]
            
        #   Determine the minimum distance for the collision set from each individual object's radius
        
        min_distance = self.radius + radius_other

        if other.x - radius_other < 0 and self.x > other.x:

            horizontal_distance = other.x + self.width - self.x 
        
        elif self.x - self.radius < 0 and other.x > self.x:

            horizontal_distance = self.x + self.width - other.x 
        
        else:

            horizontal_distance = abs(self.x - other.x)
        
        if other.y - radius_other < 0 and self.y > other.y:

            vertical_distance = other.y + self.height - self.y
        
        elif self.y - self.radius < 0 and other.y > self.y:

            vertical_distance = self.y + self.height - other.y
        
        elif self.y + self.radius > self.height and other.y < self.y:

            vertical_distance = other.y + self.height - self.y
        
        elif other.y + other.radius > self.height and self.y < other.y:

            vertical_distance = self.y + self.height - other.y
        
        else:

            vertical_distance = abs(self.y - other.y)

        #   Calculate the actual distance between the objects using Euclidean distance

        true_distance = math.sqrt(horizontal_distance ** 2 + vertical_distance ** 2)

        if true_distance <= min_distance:

            return True 
      
        else:

            return False

    #   Returns a string representation of the object

    def __repr__(self):
        
        # Enter your code here

        line = ""

        line += self.obj_type

        line += " "

        x_format = "{:.1f}".format(self.x)

        line += x_format

        line += ","

        y_format = "{:.1f}".format(self.y)

        line += y_format

        line += ","

        angle_format = "{:.0f}".format(self.angle)

        line += angle_format

        line += ","

        id_format = "{:.0f}".format(self.id)

        line += id_format

        return line

    #   Sets the movement speed of the object

    def set_movement_speed(self, movement_speed):

        if not self.speed_set:
            
            self.movement_speed += movement_speed
            self.speed_set = True
    
    #   Sets the incrementing angle of the spaceship

    def set_angle(self, angle):

        if self.obj_type.lower() == "spaceship":

            if not self.angle_set:

                self.turn_angle += angle
                self.angle_set = True
        
    #   Sets the radius of the object

    def set_radius(self, radius):

        if not self.radius_set:
        
            self.radius += radius
            self.radius_set = True
    
    #   Returns the radius of the object

    def get_radius(self):

        return self.radius
    
    #   Increases the timer by 1 for the bullet to determine when it will expire

    def increment_timer(self):

        if self.obj_type.lower() == "bullet":

            self.bullet_timer += 1
    
    #   Return the track movement timer for the bullet

    def get_bullet_timer(self):

        return self.bullet_timer
    
    #   Initialises the forward motion of the spaceship

    def start_spaceship(self):

        if self.obj_type.lower() == "spaceship":

            self.spaceship_start = True
    
    #   Returns True if the spaceship has already moved left, False otherwise

    def moved_left(self):

        self.move_left = False
    
    #   Returns True if the spaceship has already moved right, False otherwise

    def moved_right(self):

        self.move_right = False
    
    #   Returns a string representation of an upcoming asteroid

    def __upcoming_asteroid_repr__(self):

        if self.obj_type.lower() == "asteroid_small" or self.obj_type.lower() == "asteroid_large":

            line = ""

            x_format = "{:.1f}".format(self.x)

            line += x_format

            line += ","

            y_format = "{:.1f}".format(self.y)

            line += y_format

            line += ","

            angle_format = "{:.0f}".format(self.angle)

            line += angle_format

            line += ","

            id_format = "{:.0f}".format(self.id)

            line += id_format

            return line
        
    #   Returns True if spaceship is moving left, False otherwise

    def get_move_left(self):
        
        return self.move_left
    
    #   Returns True if spaceship is moving right, False otherwise

    def get_move_right(self):

        return self.move_right
    
    #   Sets the spaceship to be ready to launch a bullet

    def launch_bullet(self):

        if self.obj_type.lower() == "spaceship":

            self.bullet_ready = True
    
    #   Returns True if the spaceship is ready to launch a bullet, False otherwise

    def get_bullet_ready(self):

        return self.bullet_ready
    
    #   Sets the spaceship to have already launched a bullet

    def bullet_fired(self):

        if self.obj_type.lower() == "spaceship":

            self.bullet_ready = False 

    #   Returns the Euclidean distance between one object and another

    def get_distance(self, other):

        x_diff = abs(self.x - other.x)
        y_diff = abs(self.y - other.y)

        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    # You can add additional methods if required

