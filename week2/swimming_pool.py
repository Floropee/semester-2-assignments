class SwimmingPool:
    def __init__(self,name,total_lanes,occupied_lanes=0):
        self._name=name
        self.total_lanes=total_lanes
        self.occupied_lanes=occupied_lanes
        
    @property
    def name(self):
        return self._name
    
    @property
    def total_lanes(self):
        return self._total_lanes
    
    @total_lanes.setter
    def total_lanes(self,value):
        if value<1:
            raise ValueError("Total lanes must be at least 1")
        self._total_lanes=value
        
    @property
    def occupied_lanes(self):
        return self._occupied_lanes
    
    @occupied_lanes.setter
    def occupied_lanes(self,value):
        if value<0:
            raise ValueError('Occupied lanes cannot be negative')
        if value>self._total_lanes:
            raise ValueError("Occupied lanes cannot exceed total lanes")
        self._occupied_lanes=value
    @property
    def free_lanes(self):
        return self._total_lanes-self._occupied_lanes
    
    @property
    def occupancy_rate(self):
        return round((self._occupied_lanes/self._total_lanes)*100,1)
    
    def assign(self,lanes):
        free_lanes=self.free_lanes
        if lanes<=0:
            raise ValueError('Number of lanes must be positive')
        if lanes>free_lanes:
            raise ValueError('Not enough free lanes')
        self._occupied_lanes+=lanes
        
    def release(self,lanes):
        if lanes<=0:
            raise ValueError('Number of lanes must be positive')
        if lanes>self._occupied_lanes:
            raise ValueError('Cannot release more than occupied')
        self._occupied_lanes-=lanes
        
p = SwimmingPool("Olympic", 8)
print(p.name, p.free_lanes, p.occupancy_rate)

p.assign(6)
print(p.occupied_lanes, p.occupancy_rate)

p.release(2)
print(p.free_lanes)

try:
    p.assign(5)
except ValueError as e:
    print(e)

try:
    p.name = "X"
except AttributeError:
    print("Cannot change pool name") 