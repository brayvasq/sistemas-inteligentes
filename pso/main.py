#!/usr/bin/env python

import random, sys ,math

################################################################################

number_of_variables = 2
# the minimum possible value x or y can take
min_value = -500
# the maximum possible value x or y can take
max_value = 500
# the number of particles in the swarm
number_of_particles = 6
# number of times the algorithm moves each particle in the problem space
number_of_iterations = 2000

w = 0.4    # inertia
c1 = 1.49 # cognitive (particle)
c2 = 1.49 # social (swarm)

################################################################################

class Particle:

    def __init__(self, number_of_variables, min_value, max_value):

        # init x and y values
        self.positions = [0.0 for v in range(number_of_variables)]
        # init velocities of x and y
        self.velocities = [0.0 for v in range(number_of_variables)]

        for v in range(number_of_variables):
            # update x and y positions
            self.positions[v] = ((max_value - min_value) * random.random()
                                + min_value)
            # update x and y velocities
            self.velocities[v] = ((max_value - min_value) * random.random()
                                + min_value)

        # current fitness after updating the x and y values
        self.fitness = Fitness(self.positions)
        # the current particle positions as the best fitness found yet
        self.best_particle_positions = list(self.positions)
        # the current particle fitness as the best fitness found yet
        self.best_particle_fitness = self.fitness

def Fitness(x):
    #                 x -            y + 7
    #return positions[0] - positions[1] + 7
    d = len(x)
    suma = 0
    for i in range(d):
        suma += x[i] * math.sin(math.sqrt(abs(x[i])))
    return 418.9829 * d - suma

def calculate_new_velocity_value(particle, v):

    # generate random numbers
    r1 = random.random()
    r2 = random.random()

    # the learning rate part
    part_1 = (w * particle.velocities[v])
    # the cognitive part - learning from itself
    part_2 = (c1 * r1 * (particle.best_particle_positions[v] - particle.positions[v]))
    # the social part - learning from others
    part_3 = (c2 * r2 * (best_swarm_positions[v] - particle.positions[v]))

    new_velocity = part_1 + part_2 + part_3

    return new_velocity

def desviacionx(swarm):
    media = 0
    for part in swarm:
        media += part.positions[0]

    media = media / len(swarm)

    suma = 0
    for part in swarm:
        suma += (part.positions[0] - media)**2
    
    var = math.sqrt( (1/(len(swarm)-1)) * suma )
    print("Desviacion X : ",var)
    return var

def desviaciony(swarm):
    media = 0
    for part in swarm:
        media += part.positions[1]

    media = media / len(swarm)

    suma = 0
    for part in swarm:
        suma += (part.positions[1] - media)**2
    
    var = math.sqrt( (1/(len(swarm)-1)) * suma )
    print("Desviacion Y : ",var)
    return var

def desviacion(swarm):
    x = desviacionx(swarm)
    print("Desviacion x : ",x)
    y = desviaciony(swarm)
    print("Desviacion y : ",y)
    resp = False
    if x <= 1.5 and y <= 1.5:
        resp = True
    return resp

################################################################################

# create the swarm
swarm = [Particle(number_of_variables, min_value, max_value)
                    for __x in range(number_of_particles)]

######################################### best particle error and positions ####

best_swarm_positions = [0.0 for v in range(number_of_variables)]
best_swarm_fitness = sys.float_info.max

for particle in swarm: # check each particle
    if particle.fitness < best_swarm_fitness:
        best_swarm_fitness = particle.fitness
        best_swarm_positions = list(particle.positions)

################################################################################
num = 0
converge = False
while not converge:
    num += 1
    print("Iteracion ",num)
    for particle in swarm:
        # start moving/updating particles to calculate new fitness

        # compute new velocities for each particle
        for v in range(number_of_variables):

            particle.velocities[v] = calculate_new_velocity_value(particle, v)

            if particle.velocities[v] < min_value:
                particle.velocities[v] = min_value
            elif particle.velocities[v] > max_value:
                particle.velocities[v] = max_value

        # compute new positions using the new velocities
        for v in range(number_of_variables):
            particle.positions[v] += particle.velocities[v]

            if particle.positions[v] < min_value:
                particle.positions[v] = min_value
            elif particle.positions[v] > max_value:
                particle.positions[v] = max_value

        # compute the fitness of the new positions
        particle.fitness = Fitness(particle.positions)

        # are the new positions a new best for the particle?
        if particle.fitness < particle.best_particle_fitness:
            particle.best_particle_fitness = particle.fitness
            particle.best_particle_positions = list(particle.positions)

        # are the new positions a new best overall?
        if particle.fitness < best_swarm_fitness:
            best_swarm_fitness = particle.fitness
            best_swarm_positions = list(particle.positions)

    if(desviacionx(swarm) < 1 and desviaciony(swarm) <1):
        converge = True
    
    if num == number_of_iterations:
        converge = True


################################################################################
for particle in swarm:
    print(particle.positions)

desviacionx(swarm)
desviaciony(swarm)

print(best_swarm_positions)
print(Fitness(best_swarm_positions))