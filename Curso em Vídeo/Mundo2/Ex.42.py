l1 = float(input("Digite o comprimento do lado 1: ")); 
l2 = float(input("Digite o comprimento do lado 2: ")); 
l3 = float(input("Digite o comprimento do lado 3: ")); 

if(l1 + l2 > l3):
    if(l1 + l2 > l3):
        if(l1 + l2 > l3):

            if(l1 == l2 == l3):
                print("\033[0;31;47mÉ possível formar um triângulo equilátero.\033[m");      
            elif(l1 == l2 or l1 == l3 or l2 == l3):
                print("\033[0;31;47mÉ possível formar um triângulo isóceles.\033[m");      
            else:
                print("\033[0;31;47mÉ possível formar um triângulo escaleno.\033[m");      
        else:
            print("É impossível formar um triângulo."); 
    else:
        print("É impossível formar um triângulo."); 
else:
    print("É impossível formar um triângulo."); 
