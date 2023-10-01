#!/usr/bin/env python
# coding: utf-8

# ## Q1. What does RGBA stand for?

# ### ANS1.  RGBA stands for red, green, blue, and alpha (transparency) in the color. An RGBA value is a tuple of 4 integers, each ranging from 0 to 255. The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.

# ## Q2. From the Pillow module, how do you get the RGBA value of any images?

# In[2]:


from PIL import ImageColor
ImageColor.getcolor('red', 'RGBA')


# ## Q3. What is a box tuple, and how does it work?

# ### ANS3. A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate,the width and the height, respectively.

# ## Q4. Use your image and load in notebook then, How can you find out the width and height of an Image object?

# In[6]:


from PIL import Image
pic = Image.open('pkt.jpg')
width,height = pic.size
width,height


# ## Q5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

# In[8]:


from PIL import Image
img = Image.open('pkt.jpg')
new_img = img.crop((0,50,50,50))


# ## Q6. After making changes to an Image object, how could you save it as an image file?

# In[10]:


from PIL import Image
pic = Image.open('pkt.jpg')
pic.save('pkt2.jpg')


# ## Q7. What module contains Pillow’s shape-drawing code?

# ### ANS7. Pillow's  `ImageDraw` module contains Shape drawing methods.

# ## Q8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

# ### ANS8. ImageDraw objects have shape-drawing methods such as `point()`, `line()` or `rectangle()`.They are returned by passing the Image object to the `ImageDraw.Draw()` function.
