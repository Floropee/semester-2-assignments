from dataclasses import dataclass,field
@dataclass
class Component:
    name: str
    units: float
    price_per_unit: float
    
    def total_price_com(self) -> float:
        return self.units * self.price_per_unit
@dataclass
class Assembly:
    title: str
    batch_size: int
    components: list[Component]=field(default_factory=list)
    total_price: float=field(init=False)
    
    def __post_init__(self):
        self._updating_total_price()
    def _updating_total_price(self):
        self.total_price=0
        for component in self.components:
            self.total_price+=component.total_price_com()
        return self.total_price
    def add_component(self, component: Component):
        self.components.append(component)
        self._updating_total_price()
    def price_per_item(self) -> float:
        return self.total_price / self.batch_size
    def scale(self, new_batch_size: int):
        ratio=new_batch_size/self.batch_size
        self.batch_size=new_batch_size
        for component in self.components:
            component.units*=ratio
        self._updating_total_price()
    def display(self) -> str:
        lines=[]
        lines.append(f'{self.title} ({self.batch_size} items):')
        for component in self.components:
            lines.append(f'  {component.name}: {component.units} units (${component.total_price_com()})')
        lines.append(f'Per item: ${self.price_per_item()}')
        return '\n'.join(lines)

a = Assembly("Drone", 8)
a.add_component(Component("Motor", 32.0, 15.0))
a.add_component(Component("Frame", 8.0, 45.0))
a.add_component(Component("Battery", 16.0, 25.0))

print(a.total_price)
print(a.price_per_item())
print(a.display())

a.scale(4)
print(a.display())