# 1.Setting Up Our Robot

"""Create a python class called DriveBot. Within this class, create instance variables for motor_speed,

sensor_range, and direction. All of these should be initialized to 0 by default. After setting up the class,

create an object from the class called robot_1. Set the motor_speed to 5, the direction to 90, and 

the sensor_range to 10. Use the provided print statements to check your work!"""

# Answer

# Define the DriveBot class here!
class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.sensor_range = 0
    self.direction = 0

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.sensor_range = 10
robot_1.direction = 90


print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# 2. Adding Robot Logic

"""In the DriveBot class, add a method called control_bot which accepts parameters: new_speed and new_direction.

These should replace the associated instance variables. Create another method called adjust_sensor which 

accepts a parameter called new_sensor_range which replaces the sensor_range instance variable. 

Afterwards, use these methods to rotate the robot 180 degrees at 10 miles per hour with a sensor range of 20 feet.

Use the provided print statements to check your code!"""

# Answer
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# 3. Enhanced Constructor

"""Upgrade the constructor in the DriveBot class in order to accept three optional parameters. 

The constructor can accept motor_speed (which defaults to 0 if not provided), direction (which defaults to 180 if not provided,

and sensor_range (which defaults to 10 if not provided). These parameters should replace the associated instance variables. 

Test out the upgraded constructor by initializing a new robot called robot_2 with a speed of 35, a direction of 75,

and a sensor range of 25."""

# Answer
class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
        
    def __repr__(self):
        return f"These are the robot's spesification: \n Speed: {self.motor_speed} \n Direction: {self.direction} \n Sensor range: {self.sensor_range}"
        
robot_1 = DriveBot(0, 0, 0)
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

test_bot_1 = DriveBot(10, 270)
test_bot_2 = DriveBot(sensor_range=20, motor_speed=45)
test_bot_3 = DriveBot(50)

print(test_bot_1)
print(test_bot_2)
print(test_bot_3)

robot_1 = DriveBot(0, 0, 0)
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot(35, 75, 25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

# Test the default value

# sensor_range defaults to 10
test_bot_1 = DriveBot(10, 270) 

# direction defaults to 180
test_bot_2 = DriveBot(sensor_range = 20, motor_speed = 45) 

# direction defaults to 180 and sensor_range defaults to 10
test_bot_3 = DriveBot(50) 

# all default values are used
test_bot_4 = DriveBot() 

# no default values are used
test_bot_5 = DriveBot(18, 95, 30)

print(test_bot_1)
print(test_bot_2)
print(test_bot_3)
print(test_bot_4)
print(test_bot_5)

# 4. Controlling Them All

"""Create a class variable called all_disabled which is set to False. Next, create two more class variables 

called latitude and longitude. Set both of those variables to equal -999999. A third robot has been created below

the first two robots. Set the latitude of all of the robots to -50.0 at once. Additionally, 

set the longitude of the robots to 50.0 and set all_disabled to True. 

You should be able to set those values using three lines of code."""

# Answer
class DriveBot:
  # Create the class variables!
    all_disabled = False
    latitude = -999999
    longitude = -999999

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

# Change the latitude, longitude, and all_disabled values for all three robots using only three lines of code!

DriveBot.latitude = -50.0
DriveBot.longitude = 50.0
DriveBot.all_disabled = True

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# 5. Identifying Robots

"""Within the DriveBot class, create an instance variable called id which will be assigned to the robot when 

the object is created. Every time a robot is created, increment a counter (stored as a class variable) so that 

the next robot will have a different id. For example, if three robots were created: first_robot, next_robot, and last_robot;

first_robot will have an id of 1 next_robot will have an id of 2 and last_robot will have an id of 3."""

# Answer
class DriveBot:
  # Create a counter to keep track of how many robots were created
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        # Assign an `id` to the robot when it is constructed by incrementing the counter and assigning the value to `id`
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

