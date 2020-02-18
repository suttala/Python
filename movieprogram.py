import movie_show

# A function to read an integer with exception handling.

def read_integer():
    int_ok = False
    while not int_ok:
        try:
            luku = int(input())
            int_ok = True
            return luku
        except ValueError:
            print("Invalid integer. Enter a new intetger!")


# The function prints the menu of the possible actions and returns
# the number of the action chosen by the user.
        
def menu():
    print()
    print("Menu:")
    print("1. Add a new show")
    print("2. Print the reservation map")
    print("3. Reserve a seat")
    print("4. Reserve several seats")
    print("5. Find available seats")
    print("6. Print show info")
    print("7. Quit")
    choice = read_integer()
    return choice


# The function outputs the list of the shows available and returns
# the number of the show chosen by the user. If the user's choice is
# not valid, the function returns -1.

def choose_show(showlist):
    if len(showlist) == 0:
        print("No show info available.")
        print("This action is not possible.")
        return -1
    else:
        print("Enter the number of the show:")
        i = 0
        while i < len(showlist):
            print("{:d}. {:s}".format(i + 1, str(showlist[i])))
            i += 1
        show_no = read_integer()
        if 1 <= show_no <= len(showlist):
            return show_no - 1
        else:
            print("The number of the show is not valid!")
            return -1

        
# The function asks the user to enter the information about a show,
# creates a new MovieShow objects and appends it to the list given
# as a parameter.

def add_show(showlist):
    print("Give information about the show to be added.")
    title1 = input("Movie title:\n")
    time1 = input("Show time:\n")
    theater1 = input("Theater:\n")
    print("Number of rows in the theater:")
    rows1 = read_integer()
    print("Number of seats in one row:")
    seats1 = read_integer()
    new_show = movie_show.MovieShow(title1, time1, theater1, rows1, seats1)
    showlist.append(new_show)
    
    
# The function outputs the reservation map of the show chosen be the user.
# The parameter is the list containg the MovieShow objects of the available
# shows.

def print_reservation_map(showlist):
    show_index = choose_show(showlist)
    if show_index != -1:
        print(showlist[show_index].get_reservation_map())

# The function reserves one seat in the show chosen by the user.
# The parameter is the list containg the MovieShow objects of the available
# shows.

def reserve_one_seat(showlist):
    show_index = choose_show(showlist)
    if show_index != -1:
        print("Enter the row of the seat:")
        row_no = read_integer()
        print("Enter the number of the seat to be reserved:")
        seat_no = read_integer()
        if showlist[show_index].reserve_seat(row_no, seat_no):
            print("Seat reserved.")
        else:
            print("It is not possible to reserve that seat.")

            
# The function reserves several adjacent seats in the show chosen by the user.
# The parameter is the list containg the MovieShow objects of the available
# shows.

def reserve_several_seats(showlist):
    show_index = choose_show(showlist)
    if show_index != -1:
        print("Enter the number of the row.")
        row_no = read_integer()
        print("Enter the number of the first seat to be reserved.")
        seat_no1 = read_integer()
        print("Enter the number of the last seat to be reserved.")
        seat_no2 = read_integer()
        if showlist[show_index].reserve_seats(row_no, seat_no1, seat_no2):
            print("Seats reserved.")
        else:
            print("It is not possible to reserve those seats.")


# The function finds several adjacent available seats from the show 
# chosen by the user. The parameter is the list containg the MovieShow 
# objects of the available shows.
           
def find_adjacent_seats(showlist):
    show_index = choose_show(showlist)
    if show_index != -1:
        number_of_seats = -1
        while number_of_seats <= 0:
            print("How many available seats do you want to find?")
            number_of_seats = read_integer()
        result = showlist[show_index].find_available_seats(number_of_seats)
        if result == movie_show.MovieShow.NOT_AVAILABLE:
            print("It is not possible to find {:d} adjacent seats available.".\
                  format(number_of_seats))
        else:
            row_no = result[0]
            seat_no = result[1]
            print("{:d} adjacent seats available in row {:d} starting from seat {:d}".\
                  format(number_of_seats, row_no, seat_no))
            
            
            
# The function output information on the shows available.
# The parameter is the list containg the MovieShow objects of the available
# shows.

def print_show_info(showlist):
    if len(showlist) == 0:
        print("No movie shows available.")
    else:
        print("The movie shows:")
        i = 0
        while i < len(showlist):
            print("{:d}. {:s}".format(i + 1, str(showlist[i])))
            i += 1
    
    
def main():    
    shows = []
    action = menu()
    while action != 7:
        if action == 1:
            add_show(shows)
        elif action == 2:
            print_reservation_map(shows)
        elif action == 3:
            reserve_one_seat(shows)
        elif action == 4:
            reserve_several_seats(shows)
        elif action == 5:
            find_adjacent_seats(shows)
        elif action == 6:
            print_show_info(shows)
        action = menu()
            
            
main()