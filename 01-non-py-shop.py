class chai:
    def __init__(self, sweetness,milk_level):
      self.sweetness = sweetness
      self.milk_level = milk_level

    def sip(self):
      print("Sipping the chai with sweetness level", self.sweetness, "and milk level", self.milk_level)

    def add_sugar(self, amount):
        self.sweetness += amount
        print("Added", amount, "sugar. New sweetness level is", self.sweetness)


my_chai = chai(sweetness=5, milk_level=8)

my_chai.sip()
my_chai.add_sugar(2)
my_chai.sip()
