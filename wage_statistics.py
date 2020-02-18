'''
Created on 13.10.2018

@author: alariksutter
'''
def calculate_daily_pay(daily_hours, hourly_wages):
    if daily_hours <= 8:
        palkka = daily_hours * hourly_wages
    if 8 < daily_hours <= 10:
        palkka = (8 * hourly_wages) + ((daily_hours - 8 )*hourly_wages*1.5)
    if daily_hours > 10:
        palkka = (8 * hourly_wages) + (2*1.5*hourly_wages) + (daily_hours-10)*hourly_wages*2    
    return palkka
def read_hours():
    lista_tunnit = []
    print("Enter the working hours. Stop by giving a negative value.")
    tunnit = float(input("Enter the working hours of the 1st worker:\n"))
    if tunnit >= 0:
        lista_tunnit.append(tunnit)
        while tunnit >= 0:
            tunnit = float(input("Enter the working hours of the next worker:\n"))
            if tunnit >= 0:
                lista_tunnit.append(tunnit)
    else:
        None
    return lista_tunnit
def calculate_wages(lista_tunnit, hourly_wages):
    lkm = len(lista_tunnit)
    lista_palkat = [0.0] * lkm
    i = 0
    while i != lkm:
        daily_hours = lista_tunnit[i]
        lista_palkat[i] = calculate_daily_pay(daily_hours, hourly_wages)
        i += 1
    return lista_palkat
def calculate_average(lista_palkat):
    average = (sum(lista_palkat)) / (len(lista_palkat))
    return average
def wages_out_of_interval(lista_palkat, alaraja, ylaraja):
    i = 0
    x = 0
    while i != len(lista_palkat):
        if alaraja <= lista_palkat[i] <= ylaraja:
            None
        else:
            x += 1
        i += 1
    return x
def output_wages(lista_palkat):
    print("Wages:")
    i = 0
    while i != len(lista_palkat):
        print("{:.2f} eur".format(lista_palkat[i]))
        i += 1
def main():
    tuntipalkka = float(input("Enter the hourly wages in euros:\n"))
    tunnit_lista = read_hours()
    if len(tunnit_lista) == 0:
        print("No working hours were entered.")
    else:
        palkat_lista = calculate_wages(tunnit_lista, tuntipalkka)
        ka = calculate_average(palkat_lista)
        alaraja = ka * 0.75
        ylaraja = ka * 1.25
        ulkona = wages_out_of_interval(palkat_lista, alaraja, ylaraja)
        output_wages(palkat_lista)
        print("The average wage is {:.2f} eur.".format(ka))
        print("The number of the wages that differs over 25 % from the average is {:d}.".format(ulkona))
main()