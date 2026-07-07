from threading import Timer

def hallo():
    print("Hallo")

Timer(5, hallo).start()


hallo()
