# Todd Nelson
# Student ID: 10106136
# Assignment 3 Complex Data structures


### Function to obtain name and student ID information
def get_name_and_student_id(data):
    
    full_name = data["name"]            #Stores the full name string from data structure in main()
    first_name = full_name.split()[0]   #Grabs full name string into a list of words, then stores the first word represented by [0]
    student_id = data["student ID"]     #Stores Student ID integer from data structure in main()

    print1 = f"My name is {full_name}, but you can call me Sir {first_name}"    #Sentence building
    print2 = f"My student ID is {student_id}."                                  #Sentence building

    return f"{print1}\n{print2}"    #Returns both sentences to be joined in order with a new line

### Function to obtain pizza topping information
def get_pizza_toppings(data):

    print3 = ["My favourite pizza toppings are:"]   #Stores sentence as header for list of toppings to follow
    for topping in data ["pizza toppings"]:         #Loop through each topping
        print3.append(f' - {topping}')              #Add each "-" in front of each topping from the loop

    return "\n".join(print3)    #Returns the list of toppings in bullet point form, each on their own line

### Function to add pizza toppings
def add_pizza_toppings(data, toppings):

    for topping in toppings:                    #Loop through each topping
        data["pizza toppings"].append(topping)  #Append each topping to the pizza toppings list

    data["pizza toppings"].sort()                                           #Sort alphabetically
    data["pizza toppings"] = [t.lower() for t in data["pizza toppings"]]    #Convert all to lowercase
    
    return 

### Function to get movie genres
def get_movie_genres(data):

    genres = [movie["genre"] for movie in data["movies"]] #Builds a list of genre strings for each movie in the data set

    if len(genres)>1:
        genres2 = ", ".join(genres[:-1]) + ", and " + genres[-1] ##Joins all but the last with commas and appends "and" for the last genre

    else:
        genres2 = genres[0] #Uses the genres as is if only one genre is used

    return f"I like to watch {genres2} movies." #Returns the genres in an f-string for printing

### Function to get movie titles
def get_movie_titles(movie_list):

    titles = [movie["title"].title() for movie in movie_list] #Loop through each movie

    if len(titles)>1:
        titles2 = ", ".join(titles[:-1]) + ", and " + titles[-1] ##Joins all but the last with commas and appends "and" for the last movie

    else:
        titles2 = titles[0] #Uses titles as is if only one title is used

    return f"Some of my favourite movies are {titles2}!" #Returns the titles in an f-string for printing

### Function to add movie to the list
def add_movie(data, title, genre):
    
    data["movies"].append({"title": title, "genre": genre}) #Build new movie dictionary and append it to the movie list.

    return

def main():
    ### Complex Data Structure
    myinfo = {
        "name":"Todd Nelson",
        "student ID":10106136,
        "pizza toppings":["RED ONION","PEPPERONI","GREEN PEPPER"],
        "movies":[{"title": "arrival", "genre": "sci-fi"},
                  {"title": "fall guy", "genre": "comedy"},
        ]
    }

    ### Start by printing the student information
    print(get_name_and_student_id(myinfo))
    ### Next, print the favourite pizza toppings as a bullet point list in all caps
    print(get_pizza_toppings(myinfo))
    ### Then, store new toppings to be called later
    new_toppings = ("bacon", "sausage")
    ### Call the function to add the new toppings to the "pizza toppings" list
    add_pizza_toppings(myinfo, new_toppings)
    ### Then, print the new list of pizza toppings as a bullet point list, this time in alphabetical order and lowercase
    print(get_pizza_toppings(myinfo))
    ### Next, we call the function to add a movie to our dictionary, "title": "Interstellar", "genre": "fantasy"
    add_movie(myinfo, "interstellar", "fantasy")
    ### Finally, we print the genres from our dictionary
    print(get_movie_genres(myinfo))
    ### Then, we print the movies from our dictionary
    print(get_movie_titles(myinfo["movies"]))

    

if __name__ == "__main__":
    main()