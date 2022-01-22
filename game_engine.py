from os import write
import config
from space_object import SpaceObject

class Engine:

    #   Class variables to store the objects imported and update game status

    spaceships = []
    asteroids = []
    upcoming_asteroids = []
    bullets = []
             
    game_width = 0
    game_height = 0
    spaceship_fuel = 0
    num_bullets = 0
    asteroids_current = 0
    asteroids_remaining = 0
    score = 0
    fuel_remaining = 0
    bullet_id = 0

    
    def __init__(self, game_state_filename, player_class, gui_class):
        
        self.import_state(game_state_filename)
        self.player = player_class()
        self.GUI = gui_class(self.width, self.height)

    #   Imports the game state data from a file

    def import_state(self, game_state_filename):

        # Enter your code here

        my_list =[]

        try:
            game_file = open(game_state_filename, "r")

            while True:

                line = game_file.readline()
            
                if not line:
                    break
                    
                my_list.append(line)

            if len(my_list) < 8:

                raise ValueError("Error: game state incomplete")
            
            for i in range(len(my_list)):

                new_line = my_list[i]

                new_line = new_line.rstrip("\n")
                
                new_line = new_line.split(" ")

                #if len(new_line) != 2:
                    
                    #raise ValueError("Error: expecting a key and value in line " + str(i + 1))
                
                if len(new_line) > 2:
                    
                    raise ValueError("Error: unexpected key: " + new_line[0] + " in line " + str(i + 1))
                
                elif len(new_line) == 1:
                    
                    raise ValueError("Error: unexpected key: " + new_line[0] + " in line " + str(i + 1))
                
                elif not isinstance(new_line[0], str):
                    
                    raise ValueError("Error: invalid data type in line " + str(i + 1))
                
                else:
                    
                    if new_line[0].lower() == "width" or new_line[0].lower() == "height" or new_line[0].lower() == "score" or new_line[0].lower() == "fuel" or new_line[0].lower() == "asteroids_count" or new_line[0].lower() == "bullets_count" or new_line[0].lower() == "upcoming_asteroids_count":
                        
                        if not new_line[1].isdigit():
                            
                            raise ValueError("Error: invalid data type in line " + str(i + 1))
                    
                    else:
                        
                        if not isinstance(new_line[1], str):
                            
                            raise ValueError("Error: invalid data type in line " + str(i + 1))
                        
                    #   Store key data variables and objects to be used in the run_game() method
                    
                    if new_line[0].lower() == "width":
                        
                        self.game_width += int(new_line[1])
                    
                    elif new_line[0].lower() == "height":
                        
                        self.game_height += int(new_line[1])
                        
                    elif new_line[0].lower() == "spaceship":

                        if not isinstance(new_line[1], str):
                            
                            raise ValueError("Error: unexpected key: " + spaceship_rep[0] + " in line " + str(i + 1))

                        spaceship_rep = new_line[1]
                        spaceship_rep = spaceship_rep.split(",")

                        if len(spaceship_rep) > 4:

                            raise ValueError("Error: unexpected key: " + spaceship_rep[0] + " in line " + str(i + 1))
                        
                        elif len(spaceship_rep) < 4:

                            raise ValueError("Error: invalid data type in line " + str(i + 1))
                        
                        else:

                            x = float(spaceship_rep[0])

                            y = float(spaceship_rep[1])

                            angle = float(spaceship_rep[2])

                            id = float(spaceship_rep[3])

                            spaceship = SpaceObject(x, y, self.game_width, self.game_height, angle, "spaceship", id)

                            self.spaceships.append(spaceship)
                    
                    elif new_line[0].lower() == "asteroid_small":

                        asteroid_small_rep = new_line[1]
                        asteroid_small_rep = asteroid_small_rep.split(",")

                        if len(asteroid_small_rep) > 4:

                            raise ValueError("Error: unexpected key: " + asteroid_small_rep[0] + " in line " + str(i + 1))
                        
                        elif len(asteroid_small_rep) < 4:

                            raise ValueError("Error: invalid data type in line " + str(i + 1))

                        else:
                        
                            x = float(asteroid_small_rep[0])

                            y = float(asteroid_small_rep[1])

                            angle = float(asteroid_small_rep[2])

                            id = float(asteroid_small_rep[3])

                            asteroid_small = SpaceObject(x, y, self.game_width, self.game_height, angle, "asteroid_small", id)

                            self.asteroids.append(asteroid_small)
                    
                    elif new_line[0].lower() == "asteroid_large":

                        asteroid_large_rep = new_line[1]
                        asteroid_large_rep = asteroid_large_rep.split(",")

                        if len(asteroid_large_rep) > 4:

                            raise ValueError("Error: unexpected key: " + asteroid_large_rep[0] + " in line " + str(i))
                        
                        elif len(asteroid_large_rep) < 4:

                            raise ValueError("Error: invalid data type in line " + str(i + 1))

                        else:

                            x = float(asteroid_large_rep[0])

                            y = float(asteroid_large_rep[1])

                            angle = float(asteroid_large_rep[2])

                            id = float(asteroid_large_rep[3])

                            asteroid_large = SpaceObject(x, y, self.game_width, self.game_height, angle, "asteroid_large", id)

                            self.asteroids.append(asteroid_large)
                
                    elif new_line[0].lower() == "upcoming_asteroid_small":

                        upcoming_asteroid_small_rep = new_line[1]
                        upcoming_asteroid_small_rep = upcoming_asteroid_small_rep.split(",")

                        if len(upcoming_asteroid_small_rep) > 4:

                            raise ValueError("Error: unexpected key: " + upcoming_asteroid_small_rep[0] + " in line " + str(i + 1))
                        
                        elif len(upcoming_asteroid_small_rep) < 4:

                            raise ValueError("Error: invalid data type in line " + str(i + 1))
                        
                        else:

                            x = float(upcoming_asteroid_small_rep[0])

                            y = float(upcoming_asteroid_small_rep[1])

                            angle = float(upcoming_asteroid_small_rep[2])

                            id = float(upcoming_asteroid_small_rep[3])

                            upcoming_asteroid_small = SpaceObject(x, y, self.game_width, self.game_height, angle, "asteroid_small", id)

                            self.upcoming_asteroids.append(upcoming_asteroid_small)
                    
                    elif new_line[0].lower() == "upcoming_asteroid_large":

                        upcoming_asteroid_large_rep = new_line[1]
                        upcoming_asteroid_large_rep = upcoming_asteroid_large_rep.split(",")

                        if len(upcoming_asteroid_large_rep) > 4:

                            raise ValueError("Error: unexpected key: " + upcoming_asteroid_large_rep[0] + " in line " + str(i + 1))
                        
                        elif len(upcoming_asteroid_large_rep) < 4:

                            raise ValueError("Error: invalid data type in line " + str(i + 1))
                        
                        else:

                            x = float(upcoming_asteroid_large_rep[0])

                            y = float(upcoming_asteroid_large_rep[1])

                            angle = float(upcoming_asteroid_large_rep[2])

                            id = float(upcoming_asteroid_large_rep[3])

                            upcoming_asteroid_large = SpaceObject(x, y, self.game_width, self.game_height, angle, "asteroid_large", id)

                            self.upcoming_asteroids.append(upcoming_asteroid_large)
                    
                    elif new_line[0].lower() == "fuel":
                        
                        self.spaceship_fuel += int(new_line[1])
                        self.fuel_remaining = self.spaceship_fuel

                    elif new_line[0].lower() == "bullets_count":
                        
                        self.num_bullets += int(new_line[1])

                    elif new_line[0].lower() == "asteroids_count":
                        
                        self.asteroids_current += int(new_line[1])

                    elif new_line[0].lower() == "upcoming_asteroids_count":
                        
                        self.asteroids_remaining += int(new_line[1])
                    
                    elif new_line[0].lower() == "score":
                        
                        self.score += int(new_line[1])

                    else:
                        
                        raise ValueError("Error: unexpected key: " + new_line[0] + " in line " + str(i + 1))
 
            game_file.close()

        except FileNotFoundError as fe:
            
            raise FileNotFoundError("Error: unable to open " + game_state_filename)


        self.width = self.game_width
        self.height = self.game_height

    #   Exports the game state data into a file

    def export_state(self, game_state_filename):
             
       # Enter your code here

        write_file = open(game_state_filename, "w")

        write_file.write("width " + str(self.game_width) + "\n")
        
        write_file.write("height " + str(self.game_height) + "\n")

        write_file.write("score " + str(self.score) + "\n")

        write_file.write(self.spaceships[0].__repr__() + "\n")

        write_file.write("fuel " + str(self.spaceship_fuel) + "\n")

        write_file.write("asteroids_count " + str(self.asteroids_current) + "\n")

        for i in range(len(self.asteroids)):

            new_asteroid = self.asteroids[i]
            write_file.write(new_asteroid.__repr__() + "\n")
        
        write_file.write("bullets_count " + str(self.num_bullets) + "\n")

        if self.num_bullets > 0:

            for i in range(len(self.bullets)):

                new_bullet = self.bullets[i]
                write_file.write(new_bullet.__repr__() + "\n")
        
        write_file.write("upcoming_asteroids_count " + str(self.asteroids_remaining) + "\n")

        if self.asteroids_remaining > 0:

            for i in range(len(self.upcoming_asteroids)):

                next_asteroid = self.upcoming_asteroids[i]

                if next_asteroid.obj_type.lower() == "asteroid_small":

                    write_file.write("upcoming_asteroid_small " + next_asteroid.__upcoming_asteroid_repr__() + "\n")
                
                else:

                    write_file.write("upcoming_asteroid_large " + next_asteroid.__upcoming_asteroid_repr__() + "\n")

        write_file.close()

    #   Runs the game

    def run_game(self):

        #   Variables to store each of the fuel thresholds

        threshold_prec_one = config.fuel_warning_threshold[0] / 100
        threshold_prec_two = config.fuel_warning_threshold[1] / 100
        threshold_prec_three = config.fuel_warning_threshold[2] / 100

        #   Booleans to determine when fuel thresholds are reached

        threshold_one = False
        threshold_two = False
        threshold_three = False

        #   Set values from the config file to be stored and used during gameplay

        fuel_threshold = config.shoot_fuel_threshold
        bullet_counter = config.bullet_move_count

        movement_fuel = config.spaceship_fuel_consumption
        bullet_fuel = config.bullet_fuel_consumption

        angle_turn = config.angle_increment

        #   Initialise a frame update

        #self.GUI.update_frame(self.spaceships[0], self.asteroids, self.bullets, self.score, self.fuel_remaining)

        #   Keep running game while set conditions are True

        while self.fuel_remaining > 0 and self.asteroids_remaining > 0:

            start = False

            spaceship = self.spaceships[0]

            #   Call in data from the bot

            new_tup = self.player.action(spaceship, self.asteroids, self.bullets, self.fuel_remaining, self.score)
            
            #   Update the frames each second

            fuel = self.fuel_remaining  
            self.GUI.update_frame(spaceship, self.asteroids, self.bullets, self.score, fuel)

            spaceship.move_left = new_tup[1]

            spaceship.move_right = new_tup[2]

            spaceship.bullet_ready = new_tup[3]

            if new_tup[0]:

                start = True

            if start:

                spaceship.start_spaceship()

            #   First determine the movement of the spaceship

            spaceship_speed = list(config.speed.values())[0]
            spaceship.set_movement_speed(spaceship_speed)
            
            spaceship_radius = list(config.radius.values())[0]
            spaceship.set_radius(spaceship_radius)

            if spaceship.get_move_left() and not spaceship.get_move_right():
                
                spaceship.turn_left()
                spaceship.moved_left()
        
            elif spaceship.get_move_right() and not spaceship.get_move_left():
                
                spaceship.turn_right()
                spaceship.moved_right()

            elif start:

                spaceship.move_forward()
            
            #   Update the position of each bullet currently stored in the list of bullets
            
            if self.num_bullets > 0:

                for new_bullet in self.bullets:

                    bullet_speed = list(config.speed.values())[1]
                    new_bullet.set_movement_speed(bullet_speed)

                    bullet_radius = list(config.radius.values())[1]
                    new_bullet.set_radius(bullet_radius)

                    new_bullet.increment_timer()

                    #   Remove bullets that have reached 5 frames

                    if new_bullet.get_bullet_timer() >= bullet_counter:
                        
                        self.bullets.remove(new_bullet)
                        self.num_bullets -= 1

                    else:

                        new_bullet.move_forward()
            
            self.fuel_remaining -= movement_fuel

            #   Launch a new bullet if instructed by bot
                    
            if spaceship.get_bullet_ready():

                #   Check if it is above minimum fuel threshold to launch bullet

                if self.fuel_remaining < fuel_threshold:
                    
                    print("Cannot shoot due to low fuel")
                    spaceship.bullet_fired()

                #   Create a new bullet object and store in list of bullets

                else:

                    bullet = SpaceObject(spaceship.x, spaceship.y, self.game_width, self.game_height, spaceship.angle, "bullet", self.bullet_id)
                    self.bullet_id += 1
                    self.num_bullets += 1
                    self.bullets.append(bullet)
                    spaceship.bullet_fired()
                    self.fuel_remaining -= bullet_fuel

            #   Update game status by printing out the thresholds for each of the fuel remaining

            if self.fuel_remaining <= threshold_prec_one * self.spaceship_fuel and not threshold_one:
                
                threshold_prec_one_rep = "{:.0f}".format(threshold_prec_one * 100)
                print(threshold_prec_one_rep + "% fuel warning: " + str(self.fuel_remaining) + " remaining")
                threshold_one = True

            if self.fuel_remaining <= threshold_prec_two * self.spaceship_fuel and not threshold_two:
                
                threshold_prec_two_rep = "{:.0f}".format(threshold_prec_two * 100)
                print(threshold_prec_two_rep + "% fuel warning: " + str(self.fuel_remaining) + " remaining")
                threshold_two = True
            
            if self.fuel_remaining <= threshold_prec_three * self.spaceship_fuel and not threshold_three:
                
                threshold_prec_three_rep = "{:.0f}".format(threshold_prec_three * 100)
                print(threshold_prec_three_rep + "% fuel warning: " + str(self.fuel_remaining) + " remaining")
                threshold_three = True
            
            #   Update the position of each asteroid

            for new_asteroid in self.asteroids:

                if new_asteroid.obj_type.lower() == "asteroid_small":

                    asteroid_speed = list(config.speed.values())[2]
                    new_asteroid.set_movement_speed(asteroid_speed)

                    asteroid_radius = list(config.radius.values())[2]
                    new_asteroid.set_radius(asteroid_radius)
                
                else:

                    asteroid_speed = list(config.speed.values())[3]
                    new_asteroid.set_movement_speed(asteroid_speed)

                    asteroid_radius = list(config.radius.values())[3]
                    new_asteroid.set_radius(asteroid_radius)
                    
                new_asteroid.move_forward()

                #Check if spaceship collides with an asteroid

                if (spaceship.collide_with(new_asteroid)):

                    self.asteroids_remaining -= 1
                    self.score += config.collide_score
                    self.asteroids.remove(new_asteroid)
                    
                    print("Score: " + str(self.score) + " \t [Spaceship collided with asteroid " + str(int(new_asteroid.id)) + "]")

                    if self.asteroids_remaining >= 0:

                        add_asteroid = self.upcoming_asteroids[0]
                        self.asteroids.append(add_asteroid)
                        self.upcoming_asteroids.remove(add_asteroid)
                        print("Added asteroid " + str(int(add_asteroid.id)))
                    
                    else:

                        print("Error: no more asteroids available")
                

                else:

                    if self.num_bullets > 0:
                        
                        for new_bullet in self.bullets:

                            #   Check if a bullet collides with an asteroid

                            if (new_bullet.collide_with(new_asteroid)):

                                self.player.rotated = False
                                self.player.bullet_fired = False
                                self.player.found_close = False
                                
                                self.num_bullets -= 1
                                self.bullets.remove(new_bullet)

                                self.asteroids_remaining -= 1
                                self.asteroids.remove(new_asteroid)

                                if new_asteroid.obj_type.lower() == "asteroid_small":
                                    
                                    self.score += config.shoot_small_ast_score
                                
                                else:

                                    self.score += config.shoot_large_ast_score
                                
                                print("Score: " + str(self.score) + " \t [Bullet " + str(new_bullet.id) + " has shot asteroid " + str(int(new_asteroid.id)) + "]")

                                if self.asteroids_remaining >= 0:

                                    add_asteroid = self.upcoming_asteroids[0]
                                    self.asteroids.append(add_asteroid)
                                    self.upcoming_asteroids.remove(add_asteroid)
                                    print("Added asteroid " + str(int(add_asteroid.id)))
                    
                                else:
                                    print("Error: no more asteroids available")


        #   Display the game status outcome at the end of the game
               
        self.GUI.finish(self.score)           


        #while True:
            # 1. Receive player input
            
            # 2. Process game logic

            # 3. Draw the game state on screen using the GUI class
            # self.GUI.update_frame(???)

            # Game loop should stop when:
            # - the spaceship runs out of fuel, or
            # - no more asteroids are available

            #break

        # Display final score
        # self.GUI.finish(???)

    # You can add additional methods if required
