CRITICAL_MASS = 20

class Candy:
    def __init__(self, mass, uranium):
        self.mass = mass
        self.uranium = uranium

    def get_uranuium_quantity(self):
        return self.uranium * self.mass
    
    def get_mass(self):
        return self.mass
    

class Person:
    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position
    
    def set_position(self, position):
        self.position = position


class Kid(Person):
    def __init__(self, position, initiative):
        super().__init__(position)
        self.initiative = initiative
        self.basket = []

    def get_initiative(self):
        return self.initiative
    
    def add_candy(self, new_candy):
        self.basket.append(new_candy)

    def is_critical(self):  
        return sum(self.basket) > CRITICAL_MASS
    

class Host(Person):
    def __init__(self, position, candies):
        super().__init__(position)
        self.candies = candies

    def remove_candy(self, func):
        if len(self.candies) == 0:
            return None
        
        return func(self.candies)
    
    def get_candies_count(self, candies):
        return len(candies)
    
    def greater_distance(self, other_person):
        return ((self.get_position()[0] - other_person.get_position()[0]) ** 2 + (self.get_position()[1] - other_person.get_position()[1]) ** 2)
    

class FluxCapacitor:
    def __init__(self, participants):
        self.participants = participants
        self.kids = []
        self.hosts = []
        for participant in self.participants:
            if participant is Kid:
                self.kids.append(participant)
            elif participant is Host:
                self.hosts.append(participant)

        self.kids.sort(key=lambda x: x.get_initiative(), reverse = True)

        every_kid_hosts = {}
        for kid in self.kids:
            every_kid_hosts[kid] = self.hosts

    def remove_function(self, current_candies): 
        current_candies.sort(key=lambda x: x.mass, reverse = True)
        best_candy = current_candies.pop(0)
        return best_candy 

    def get_min_host(self, kid, hosts):
        return min(hosts, key=(lambda host:(host.greater_distance(kid), host.get_position()[0], host.get_position()[1])))

    def get_victim(self):
        victims = []

        while len(self.hosts) != 0:
            for kid in self.kids:
                best_host = self.get_min_host(kid, self.every_kid_hosts[kid])

                best_candy = best_host.remove_candy(self.remove_function(best_host.candies))
                kid.add_candy(best_candy)

                if kid.is_critical():
                    victims.append(kid)

                kid.set_position(best_host.get_position())

                for host in self.hosts:
                    if host.get_candies_count() == 0:
                        self.hosts.discard(host)

                self.every_kid_hosts[kid].discard(best_host)

            if len(victims) != 0:
                return victims

        return None