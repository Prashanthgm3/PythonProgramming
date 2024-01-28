movies = []
MENU_PROMPT = "\nEnter 'a' to add movie \n'l' to list the movie \n'f' to find a movie by title \n 'q' to quit \n"

def add_movie():
    title = input("Enter the movie title")
    director = input("Enter the movie director name")
    year = input("Enter the movie release year")

    movies.append({

        'title': title,
        'director': director,
        'year': year
})
    
def list_movie():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def search_movie():
    search_title = input("Enter the movie title your looking for")
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": list_movie,
    "f": search_movie  #First class function in python
}
  

def user_menu():
    selection = input(MENU_PROMPT)
    while selection !='q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
             print("Unknown command, PLease try again")

        # if selection == 'a':
        #     add_movie()
        # elif selection == 'l':
        #     list_movie()
        # elif selection == 'f':
        #     search_movie() 
        # else:
           
        selection = input(MENU_PROMPT)          

user_menu()