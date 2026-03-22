def log_action(func):
    def wrapper(*args,**kwargs):
        print(f"[ACTION] {func.__name__} executed")
        return func(*args,**kwargs)
    return wrapper
class Chef:
    _total_chefs=0
    def __init__(self,name,license_no):
        self.name=name
        self.license_no=license_no
        self._recipes={}
        Chef._total_chefs += 1
    @log_action
    def submit_recipe(self,recipe_name,rating):
        recipe_name=recipe_name.upper()
        self._recipes[recipe_name]=rating
        return f"{self.name} submitted {recipe_name} rated {rating}"
    def avg_rating(self):
        return round(sum(rating for rating in self._recipes.values())/len(self._recipes), 1) if self._recipes else 0.0
    def best_recipe(self):
        if not self._recipes:
            return "No recipes"
        highest_r=0
        best_name=''
        for name,rating in self._recipes.items():
            if rating>highest_r:
                highest_r=rating
                best_name=name
                return best_name
    @classmethod
    def from_enrollment(cls, data):
        name,license= data.split('-')
        return cls(name,int(license))
    @staticmethod
    def is_valid_license(license_no):
        return len(license_no)==7 and sum(1 for c in license_no if '0' <= c <= '9') ==7
    
    @classmethod
    def total_chefs(cls):
        return cls._total_chefs
    
    
c1 = Chef("Zulfiya", "7701001")
c1.submit_recipe("plov", 93)
c1.submit_recipe("lagman", 87)
c1.submit_recipe("shashlik", 79)

c2 = Chef.from_enrollment("Otabek-7701002")
c2.submit_recipe("Somsa", 96)
c2.submit_recipe("manti", 85)

print(f"{c1.name}: Avg = {c1.avg_rating()}, Best = {c1.best_recipe()}")
print(f"{c2.name}: Avg = {c2.avg_rating()}, Best = {c2.best_recipe()}")

print(f"Valid license '7701001': {Chef.is_valid_license('7701001')}")
print(f"Valid license '77Z': {Chef.is_valid_license('77Z')}")
print(f"Total chefs: {Chef.total_chefs()}")