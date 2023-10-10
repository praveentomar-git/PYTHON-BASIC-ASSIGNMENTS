#!/usr/bin/env python
# coding: utf-8

# ## Q1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?

# In[3]:


class Thing:
    pass
print(Thing)
example=Thing()
print(example)


# ### Printed values are not same, it prints, class and object details.

# ## Q2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.

# In[6]:


class Thing2:
    letters="abc"
Thing2.letters


# ## Q3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?

# In[8]:


class Thing3:
    def __init__(self):
        self.letters='xyz'


# In[13]:


# Yes, we have to make an instance (object) from the Thing3 class.
obj = Thing3()
obj.letters


# ## Q4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.

# In[15]:


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
obj=Element( 'Hydrogen', 'H',  1)
obj.symbol


# ## Q5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.

# In[21]:


dictionary={'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen=Element(**dictionary)
print(hydrogen.name, hydrogen.symbol, hydrogen.number, sep='\t')


# ## Q6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.

# In[22]:


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def dump(self):
        print(self.name,self.symbol,self.number)
hydrogen=Element('Hydrogen','H',1)
hydrogen.dump()


# ## Q7. Call print(hydrogen). In the definition of Element, change the name of method dump to `__str__`, create a new hydrogen object, and call print(hydrogen) again.

# In[23]:


print(hydrogen)


# In[30]:


class Element:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def __str__ (self):
        return f'{self.name} {self.symbol} {self.number}'
Hydrogen=Element('Hydrogen','H',1)
print(Hydrogen)


# ## Q8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.

# In[33]:


class Element:
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number
    @property
    def name(self):
        return(self.__name)
    @property
    def symbol(self):
        return(self.__symbol)
    @property
    def number(self):
        return(self.__number)    
hydrogen=Element('Hydrogen','H',1)
hydrogen.symbol


# ## Q9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.

# In[59]:


class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'
# Creating objects from each class
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print("Bear eats:", bear.eats())
print("Rabbit eats:", rabbit.eats())
print("Octothorpe eats:", octothorpe.eats())


# ## Q10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.

# In[64]:


class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        print (self.laser.does(),self.claw.does(),self.smartphone.does())
robot=Robot()
robot.does()

