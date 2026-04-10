import time 
def bajar ():
    piso = int(input("Que piso esta usted? 1, 2, 3, 4, 5: "))
    if piso == 5:
        print("Estoy en el piso", piso ,",el siguiente paso es bajar al 4")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 4,",el siguiente paso es bajar al 3")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 3 ,",el siguiente paso es bajar al 2")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 2 ,",el siguiente paso es bajar al 1")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 1 ,",Ya llegamos a lo mas abajo")

    elif piso == 4:
        print("Estoy en el piso", piso ,",el siguiente paso es bajar al 3")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 3,",el siguiente paso es bajar al 2")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 2 ,",el siguiente paso es bajar al 1")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 1 ,",Ya llegamos a lo mas abajo")

    elif piso == 3:
        print("Estoy en el piso", piso ,",el siguiente paso es bajar al 2")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 3,",el siguiente paso es bajar al 1")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 1 ,",Ya llegamos a lo mas abajo")
    elif piso == 2:
        print("Estoy en el piso", piso ,",el siguiente paso es bajar al 1")
        print("Bajando")
        time.sleep(5)
        print("Estoy en el piso", 1 ,",Ya llegamos a lo mas abajo")
    elif piso == 1:
        print("Ya estas en lo mas bajo")    

bajar()