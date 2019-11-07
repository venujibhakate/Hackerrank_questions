page = input("Enter your page no.")
needed_page = input("enter the page")
position_page = raw_input("left or right")
total = page/2
if position_page == "left":
   print (needed_page/2)
else:
    print (total-needed_page/2)