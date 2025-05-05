#Colegio republica de chillan
#necesitamos gestionar el proceso de matriculas, además del pago
#de centro de padres y mensualidades
#1) se paga solo una vez la matrícula, pero puede pagar mas de 1 mensualidad.
#2)entre 3 a 5 mens, 6%dcto. entre 6-12 10%. Si paga todo junto 20%
#se pide programa que permita determinar el total a pagar.
# el menú debe presentar los valores
#1)el pago determina el total, y si es que tiene descuento
#2)se despliega el total y emite gracias por confiar en nosotros
#3)anular compra y volver a mostrar el menú desde 0
#4)salir del programa
#TODOS los descuentos se aplican al total a pagar.
import os
def cls():
    os.system("cls")
mat_eb=0
mat_em=0
cdp=0
cant_mens=0
total_mens=0
cant_mat_em=0
cant_mat_eb=0

plop=False
ciclo=True
while ciclo:
    cls()
    print("Bienvenido a las Matrículas 2026 República de Chillán")
    print("1.- Pagos")
    print("2.- Total compra")
    print("3.- Anular compra")
    print("4.- Salir")
    op=int(input("Seleccione una opción entre 1-4: "))
    cls()
    match op:
        case 1:
            print("Pagos")
            print('''   
                    1.-Matrícula Ed. Básica
                    2.-Matrícula Ed. Media
                    3.-Centro de Padres
                    4.-Mensualidad
                    5.-Salir"
                ''')
            op2=int(input("Seleccione una opción entre 1-5: "))
            cls()
            if op2 >=1 and op2 <=4:
                plop=True
                match op2:
                    case 1:
                        cant_mat_eb=int(input("Cuantas matrículas quiere?: "))
                        mat_eb=cant_mat_eb*45000
                    case 2:
                        cant_mat_em=int(input("Cuantas matrículas quiere?: "))
                        mat_em=cant_mat_em*67000
                    case 3:
                        cdp=10000
                    case 4:
                        cant_mens=int(input("Cuantos meses quiere pagar? 1-12: "))
                        total_mens = (cant_mens*30000)
                    case 5:
                        plop = False
                    case __:
                        print("Error")        
        case 2:
            cls()
            if plop:
                print("Total de Compra")
                descuentos = 0
                subTotal=mat_eb+mat_em+cdp+total_mens
                if cant_mens == 12 and cant_mat_eb >0 and cant_mat_em>0:
                    descuento = subTotal * 0.2                 
                    total = subTotal - descuento 
                    print("Tiene un descuento del 20%") 
                elif cant_mens >= 6 and cant_mens <= 12:
                    descuento = subTotal * 0.1
                    total = subTotal - descuento
                    print("Tiene un descuento del 10%")
                elif cant_mens >= 3 and cant_mens <= 5:
                    descuento = subTotal * 0.06
                    total = subTotal - descuento
                    print("Tiene un descuento del 5%")
                else:
                    descuento = 0
                    total = subTotal
            if mat_eb>0:
                    print(f"Paga {cant_mat_eb} Matrículas Básica. Total: {mat_eb}")
            if mat_em>0:           
                    print(f"Paga {cant_mat_em} Matrículas Media.  Total: {mat_em}")
            if cdp>0:            
                    print(f"Subtotal Centro de Padres:                   {cdp}")
            if total_mens>0:            
                    print(f"Paga {cant_mens} Mensualidades.       Total: {total_mens}")

                    print(f"Su Total es:                                 {subTotal}" )
                    print(f"Su Descuento es de:                          {descuento}")
                    print(f"Su Total Final de compra es:                 {total}") 
                    print("Gracias por Confiar en Nosotros")        
                    x=input("Presione una tecla para continuar: ") 
        case 3:
            cls()
            mat_eb=0
            mat_em=0
            cdp=0
            cant_mens=0
            total_mens=0
            plop=False
            salir=input("Anulado!, presione una tecla para continuar: ")  
        case 4:
            cls()
            ciclo=False
            print("Hasta Pronto!")
