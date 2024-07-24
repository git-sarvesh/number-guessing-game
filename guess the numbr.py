import random
top_of_range = input('enter a number you like:) :  ')
if top_of_range.isdigit():
    top_of_range =    int(top_of_range)
    if top_of_range<=0:
       print('please enter a number larger than 0 next time. ')
       quit()
else:
  print('please ente a number next time thankyou! ')
  quit()

random_numbe = random.randint(0,top_of_range)

while True:
   user_guss=input('makea guss:  ')
   if user_guss.isdigit():
    user_guss = int(user_guss)
    if user_guss<=0:
       print('please enter a number larger than 0 next time. ')
   else:
        print('please ente a number next time thankyou! ')
        
        continue

   if user_guss== random_numbe:
      print('yeaaa yo got it correct!:)')
      break
   else:
        print('ouppsss you got it wrong better luck next time')