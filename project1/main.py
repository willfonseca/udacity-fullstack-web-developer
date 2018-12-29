import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story 3",
                        "Toy Story 3 is a 2010 American 3D computer-animated"
                        "comedy-drama film produced by Pixar Animation"
                        "Studios for Walt Disney Pictures. It is the third "
                        " installment in Pixar's Toy Story series, "
                        " to 1999's Toy Story 2.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://youtu.be/CHA3Kss72Ro")

hurt_locker = movie.Movie("Hurt Locker",
                          "The Hurt Locker é um filme americano,"
                          " do genero drama, lançado em 2008, dirigido por"
                          " Kathryn Bigelow e escrito pelo ex-correspondente"
                          " na Guerra do Iraque Mark Boal",
                          "https://upload.wikimedia.org/wikipedia/pt/8/82/Hurt_locker.jpg",
                          "https://www.youtube.com/watch?v=AIbFvqFYRT4")

terminator2 = movie.Movie("Terminator 2",
                          "Terminator 2: Judgment Day is a 1991 American "
                          "science-fiction action film co-written, produced, "
                          "directed by James C. Staring Arnold Schwarzenegger"
                          ", Linda Hamilton, Robert Patrick, "
                          "and Edward Furlong as its principal cast."
                          "It is the sequel to the 1984 film "
                          "The Terminator, as well as the second installment"
                          " in the Terminator franchise.",
                          "https://upload.wikimedia.org/wikipedia/pt/8/85/Terminator2poster.jpg",
                          "https://www.youtube.com/watch?v=HgV7-MJwUBw")

the_godfather = movie.Movie("The Godfather",
                            "The Godfather is a 1972 American crime "
                            "film directed by Francis Ford Coppola"
                            " and produced by Albert S. Ruddy, based "
                            "on Mario Puzo's best-selling novel"
                            "of the  same name. It stars"
                            "Marlon Brando and Al Pacino as the leaders"
                            "of a fictional New York crime family.",
                            "https://upload.wikimedia.org/wikipedia/pt/7/71/Chef%C3%A3o.jpg",
                            "https://youtu.be/sY1S34973zA")

the300 = movie.Movie("300",
                     "300 is a 2006 American epic war film based"
                     " on the 1998 comic series of the same name by Frank"
                     " Miller and Lynn Varley.  Both are fictionalized "
                     "retellings of the Battle of Thermopylae"
                     "within the Persian Wars.",
                     "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
                     "https://youtu.be/UrIbxk7idYA")

batman_dark_knight = movie.Movie("Batman - The Dark Knight",
                                 "The Dark Knight is a 2008 superhero  "
                                 "film directed, co-produced, and co-written  "
                                 "by Christopher Nolan. Based on the "
                                 "DC Comics character Batman, the film  "
                                 "is the second part of Nolan's The Dark  "
                                 "Knight Trilogy and a sequel to 2005's"
                                 "Batman Begins.",
                                 "https://upload.wikimedia.org/wikipedia/pt/d/d1/The_Dark_Knight.jpg",
                                 "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# creating a list of films to pass to fresh_tomatoes function
movies = [toy_story, hurt_locker, terminator2,
          the_godfather, the300, batman_dark_knight]

# showing list of movies with fresh_tomatoes function
fresh_tomatoes.open_movies_page(movies)
