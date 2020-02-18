def read_names():
    laskulista = {}
    print("Input the names of the participants.")
    print("Stop by entering an empty line.")
    nimi = input()
    laskulista[nimi] = 0.0
    while nimi != "":
        nimi = input()
        laskulista[nimi] = 0.0
    del laskulista[""]
    return laskulista
def add_costs(nimilista):
    print("Next, the information about costs are added.")
    print("Stop by entering an empty line as a name.")
    print("Enter the name of the participant.")
    nimi = input()
    if nimi == "":
        None
    if nimi not in nimilista and nimi != "":
        print("This name is not among the participants.")
    if nimi in nimilista:
        print("Enter the amount to be added.")
        raha = float(input())
        if raha < 0:
            print("Negative amounts are not added.")
        else:
            nimilista[nimi] += raha
    while nimi != "":
        print("Enter the name of the participant.")
        nimi = input()
        if nimi == "":
            None
        if nimi not in nimilista and nimi != "":
            print("This name is not among the participants.")       
        if nimi in nimilista:
            print("Enter the amount to be added.")
            raha = float(input())
            if raha < 0:
                print("Negative amounts are not added.")
            else:
                nimilista[nimi] += raha
    print("Information about costs stored.")
    return nimilista
def calculate_average(nimilista):
    if len(nimilista) == 0:
        return 0.0
    else:
        summa = 0.0
        for nimi in nimilista:
            summa += float(nimilista[nimi])
        keskiarvo = summa / (len(nimilista))
        return keskiarvo
def list_totals(nimilista):
    avaimet = sorted(nimilista)
    print("Total sums paid:")
    for nimi in avaimet:
        print("{:15} {:8.2f} eur.".format(nimi, float(nimilista[nimi])))
    print("\n")
def list_debts(nimilista):
    ka = float(calculate_average(nimilista))
    avaimet = sorted(nimilista)
    for nimi in avaimet:
        maksut = float(nimilista[nimi])
        if maksut >= ka:
            hinta = maksut - ka
            print(nimi,"should receive {:.2f} eur.".format(hinta))
        else:
            hinta = ka - maksut 
            print(nimi,"should pay {:.2f} eur.".format(hinta))
def main():
    nimet = read_names()
    nimet1 = add_costs(nimet)
    list_totals(nimet1)
    list_debts(nimet1)
    print("The program ends.")
main()
        