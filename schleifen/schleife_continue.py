server = 0
while server < 5:
    server += 1
    if server == 3:
        print(f"Server {server}: Wartung – überspringen")
        continue   # aktueller Durchlauf wird übersprungen
    print(f"Server {server}: Status prüfen")
  
