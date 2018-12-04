#Break Statement

list = ["cat", "dog", "bird", "mouse"]
 
i = 0
while i < len(list):
      element = list[i]
      i += 1
 
      # Test for this element.
      if element == "bird":
         break
 
      # Display element.
      print("Love", element)


#The Continue Statement

list = ["cat", "dog", "bird", "mouse"]
 
i = 0
while i < len(list):
      element = list[i]
      i += 1
 
      # Test for this element.
      if element == "bird":
         continue
 
      # Display element.
      print("Love", element)

#The Pass Statement

list = ["cat", "dog", "bird", "mouse"]
 
i = 0
while i < len(list):
      element = list[i]
      i += 1
 
      # Test for this element.
      if element == "bird":
         pass
 
      # Display element.
      print("Love", element)