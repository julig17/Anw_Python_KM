
e_liste = [1,2,1]


#mehrdimensionale Liste
m_liste = ["Hi", "Hallo", [1,244,2, ["Das", "wird", "toll"]]]
#durch jedes Element durchlaufen und 
for element in m_liste:
    if type(element) == list:
        for inneres_element in element:
            print(inneres_element)
    else:
        print(element)
print(element)



mehrdimensionale_liste = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for zeile in mehrdimensionale_liste:
    ausgabe = ""
    for inneres_ele in zeile:
        ausgabe += str(inneres_ele) + "*"
    print(ausgabe)
    