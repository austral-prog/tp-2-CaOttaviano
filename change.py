def change():
    expense = 23.75
    money = 100
    print (f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n")
    print (f"Vuelto\n\nPesos:\n{int((money-expense)//1)}\nCentavos:\n{int(((money-expense)%1)*100)}")
