zahl = 15
if zahl %2 == 0:
    print("gerade")
else:
    print("ungerade")
    if zahl%3 ==0:
        print("und durch drei teilbar")
    else:
        print("und?")


zahl = 15
if zahl %2 == 0:
    print("gerade")
elif zahl%3 ==0:
    print("ungerade \nund durch drei teilbar")

else:
    print("ungerade")
    print("und?")