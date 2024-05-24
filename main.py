import random 
fry_up_question = input("would you like fry up  ")# prompts the user to answer the question 
fry_up_options = "samosas", "spring-rolls", "half-moons", "bread-rolls", "nuggets"# these are the options that are availble 
fry_up = "" # this varaible value will be updated 
if fry_up_question =="yes":
  for a in range (1): # this will run the code once 
    fry_up = random.choice(fry_up_options)# this wil update the value of fry_up with a random choice from the list fry_up_options 
  print ("your fry up meunu is: " + fry_up   )
else:
  for b in range(1):
    print("")
 
  
  
  # this is for the main menue 
type = input("would you like english or indian food")
Indian_main_dish_options= "butter chicken", "dhar chawal", 
"aqni", "mug", "indian veg "
main_menue = ""
if type == "indian":
  for x in range (1):
      main_menue += random.choice(Indian_main_dish_options)
  print(main_menue  )
else: # this filters out all the ther options 
  english_main_menue = "sherperds pie ", "pasta ", "pizza"
  main_menue2 = ""
  for y in range(1):
    main_menue2 += random.choice(english_main_menue) # this updates the valuveof mai_ menue2 by chosig a radnom option form english_main_Menue
    print(main_menue2  
         )