# Example file for working with classes

class foodItem():
  """
  foodItem(foodName,calories)

  Class that stores the food name and calories of food.

  Parameters
  ----------
  foodName : str
    Name of food item.
  calories : int
    Calories of food item.
  
  Attributes
  ----------
  foodName : str
  calories : int

  Methods
  -------
  show()
    Print to the terminal the food item name and calories
  change(newInsert,categories)
    Changes an attribute of the foodItem instance

  See Also
  --------
  foodItemNoCal : For food items with no calories (e.g. water)

  Notes
  -----  
  29/08/20 : Created
  Nicholas Butterly

  Examples
  --------
  >>> f1 = foodItem("Bacon Burger",3250)
  >>> f1.show()
  Bacon Burger --- 3250

  """
  def __init__(self,foodName,calories):
    self.foodName = foodName
    self.calories = calories
  def show(self):
    print(self.foodName," -- ",self.calories)
  def change(self,newInsert,category):
    if(category == "f"): self.foodName = newInsert
    elif(category == "c"): self.calories = newInsert
    else:
      print("Category must be \"f\" for foodName or \"c\" for calories")

class foodItemNoCal(foodItem):
  def __init__(self,foodName):
    self.foodName = foodName
    self.calories = 0
  def change(self,newInsert):
    super().change(self,newInsert,"f")

def main():
  f1 = foodItemNoCal("Chicken Burger")
  f1.show()
  foodItemNoCal.show(f1)
  
if __name__ == "__main__":
  main()

# Use [instance].__dict__ to return all attributes of a class instance
# Use __init__ to initialise the instance of the class
# For an instance of foodItemNoCal named `f1` with a method .show(),   `f1.show()` is equivalent to `foodItemNoCal.show(f1)`
# classes can inherit all methods of a superclass, with the superclass methods being called as super().method1()