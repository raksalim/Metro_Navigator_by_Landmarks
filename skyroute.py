from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# stations under construction to be taken out of dfs and bfs vertexes
stations_under_construction = ["Olympic Village"]

landmark_string = ""
for letter, landmark in landmark_choices.items():
    if (letter in stations_under_construction) or (landmark_choices[letter] in stations_under_construction):
        landmark_string += "CLOSED FOR CONSTRUCTION: [{} - {}]\n".format(
            letter, landmark)
    else:
        landmark_string += "{} - {}\n".format(letter, landmark)


######################################

# Print Greeting

def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


################################
# takes in None/landmark_choice keys and puts out landmarks
def start_and_end(start_point=None, end_point=None):
    # if user wants to change start_point or end_point or both
    if start_point and end_point:

        print("\n\nYour current path is\n\nFROM: {}\nTO: {}\n".format(
            landmark_choices[start_point], landmark_choices[end_point]))

        change_point_str = "What would you like to change?\n\nYou can enter 'o' for 'origin',\n'd' for 'destination'\n'b' for 'both', or\n'n' for neiter.\n-> "
        valid_choices_list = ["o", "d", "b", "n"]

        change_point = get_valid_input(change_point_str, valid_choices_list)

        # control flow to change user's input
        if change_point == "n":

            return start_point, end_point

        else:
            if change_point == "o":
                start_point = get_start()
            elif change_point == "d":
                end_point = get_end()
            elif change_point == "b":
                start_point = get_start()
                end_point = get_end()
            # making sure
            return start_and_end(start_point, end_point)

    # if neither
    else:
        # get start and end for the None input values
        if (start_point == None) and (end_point == None):
            start_point = get_start()
            end_point = get_end()
        elif (end_point == None):
            print("I see you're starting from {}.".format(
                landmark_choices[start_point]))
            end_point = get_end()
        else:
            print("I see you're heading to {}.".format(
                landmark_choices[end_point]))
            start_point = get_start()

        # making sure
        return start_and_end(start_point, end_point)


###################################

# Gets starting Point from user
def get_start():

    start_pointer_letter = input(
        "\nWhere are you coming from?\nType in the corresponding letter: ").lower()

    while start_pointer_letter not in landmark_choices.keys():
        print("""
  Sorry, that's not a landmark we have data on. 
  Let's try this again...""")
        return get_start()

    return start_pointer_letter


#########################

# gets desired destination point from user

def get_end():

    end_pointer_letter = input(
        "\nWhere are you heading to\nType in the corresponding letter: ").lower()

    while end_pointer_letter not in landmark_choices.keys():
        print("""
  Sorry, that's not a landmark we have data on. 
  Let's try this again...""")
        return get_end()

    return end_pointer_letter


#########################################

# validate user input given the input and
# a list of valid inputs
def get_valid_input(input_str, valid_input_list):

    user_input = input(input_str)

    valid_choices_str = ""
    for i in valid_input_list:
        valid_choices_str += "'{}'  ".format(i)
    # validation while loop
    while user_input.lower() not in valid_input_list:
        user_input = input("\nPlease choose from the following letters:\n{}\n".format(
            valid_choices_str)).lower()

    return user_input


##########################################
# finding new Routes given a start and an end
def new_route(start_point=None, end_point=None):

    if start_point == None or end_point == None:
        # starting and endling landmark_choices dict values
        start_point, end_point = start_and_end(start_point, end_point)

    start_station, end_station = landmark_choices[start_point], landmark_choices[end_point]

    # display shortest route
    all_routes = get_route(start_station, end_station)

    if all_routes == None:
        print("Appoligies, this route is not possible due to construction. Please try again with a different starting and ending point.")
        new_route()

    shortest_route = min(all_routes, key=len)

    if shortest_route:
        shortest_route_str = "\n".join(shortest_route)

        print("The shortest route from {0} to {1}:\n{2}\n".format(
            start_station, end_station, shortest_route_str))

    else:
        print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(
            start_point, end_point))

    # ask if user would like a new route
    again_input_str = "Would you like to see another route? Enter y/n: "
    again = get_valid_input(again_input_str, ["y", "n"])

    while again == "y":
        num_routes_shown = 0

        while num_routes_shown < len(all_routes) and again == "y":

            curr_route = all_routes[num_routes_shown]
            curr_route_str = "\n".join(curr_route)
            print("Route #{0} from {1} to {2}:\n{3}\n".format(
                num_routes_shown, start_station, end_station, curr_route_str))
            num_routes_shown += 1
            again = get_valid_input(again_input_str, ["y", "n"])

        if again == "y":
            exhaused_options_again_str = "All possible routes have been printed. Would you like to restart to list of possible routes? Enter y/n "
            again = get_valid_input(exhaused_options_again_str, ["y", "n"])

        if again == "y":
            again = get_valid_input(again_input_str, ["y", "n"])
        if again == "n":
            return

    return


#############################################
# gets the route user wishes to take
def get_route(start_point, end_point):

    # define start and end locations
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]

    # initiate route list
    all_routes = []

    # updated metro system with stations under construction
    metro_system = get_active_stations() if stations_under_construction else vc_metro

    # check to see if stations_under construction
    # make it immposible for travel from one
    # location to anothe
    for ss in start_stations:
        for es in end_stations:
            possible_route = dfs(metro_system, ss, es)
            if possible_route:
                if possible_route not in all_routes:
                    all_routes.append(possible_route)

    if possible_route == None:
        return None

    # itterating through all posible start stations
    # nearest landmarks
    for start_station in start_stations:
        for end_station in end_stations:

            route = bfs(vc_metro, start_station, end_station)

            if route not in all_routes:
                all_routes.append(route)

    return all_routes

#########################################
# show the landmarks corespoinding with the
# station


def show_landmarks():
    see_landmarks_str = "Would you like to see the list of landmarks again? Enter y/n: "
    see_landmarks = get_valid_input(see_landmarks_str, ["y", "n"])

    if see_landmarks == "y":
        print(landmark_string)

    return

#######################################
# closing function


def goodbye():
    print("\nThank you for using SkyRoute!\nCome Again!\n")


####################################
# get all stations and routes that are
# unaffected by station closures
def get_active_stations():
    updated_metro = vc_metro
    for closed_station in stations_under_construction:
        for current_station, neighboring_stations in vc_metro.items():
            if current_station != closed_station:
                updated_metro[current_station] -= set(
                    stations_under_construction)
            else:
                updated_metro[current_station] = set()

    return updated_metro

###################################


# wrapper function
def skyroute():

    # start off with a greeting
    greet()

    new_route()

    goodbye()


skyroute()
