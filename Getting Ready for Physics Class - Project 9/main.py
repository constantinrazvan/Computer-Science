def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

train_mass = 22680
train_acceleration = 10

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force." )

bomb_mass = 1

def get_energy(mass, C=3 * 10**8):
    return mass * C**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")
train_distance = 100

def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")

time = "3pm"
mood = "good"
 
def report():
  print("The current time is " + time)
  print("The mood is " + mood)
 
print("Beginning of report")
 
report()