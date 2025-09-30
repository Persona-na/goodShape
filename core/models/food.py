class Food:
    def __init__(self, name, carbohydrates,protein,fat):
        self.name = name
        self.carbohydrates=carbohydrates
        self.protein=protein
        self.fat=fat
    def to_str(self):
        return self.name+','+self.carbohydrates+','+self.protein+','+self.fat