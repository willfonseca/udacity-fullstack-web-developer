import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story 3",
                        "Toy Story 3 is a 2010 American 3D computer-animated comedy-drama film produced by Pixar Animation Studios for Walt Disney Pictures. It is the third installment in Pixar's Toy Story series,[2] and the sequel to 1999's Toy Story 2. It was directed by Lee Unkrich, the editor of the first two films and the co-director of Toy Story 2, written by Michael Arndt, while Unkrich wrote the story along with John Lasseter and Andrew Stanton, respectively director and co-writer of the first two films.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://youtu.be/CHA3Kss72Ro")

hurt_locker = movie.Movie("Hurt Locker",
                            "The Hurt Locker (bra: Guerra ao Terror; prt: Estado de Guerra) é um filme americano, do gênero drama, lançado em 2008, dirigido por Kathryn Bigelow e escrito pelo ex-correspondente na Guerra do Iraque Mark Boal",
                            "https://upload.wikimedia.org/wikipedia/pt/8/82/Hurt_locker.jpg",
                            "https://www.youtube.com/watch?v=AIbFvqFYRT4")

terminator2 = movie.Movie("Terminator 2",
                          "Terminator 2: Judgment Day (often shortened to Terminator 2 or T2) is a 1991 American science-fiction action film[4] co-written, produced, and directed by James Cameron. The film stars Arnold Schwarzenegger, Linda Hamilton, Robert Patrick, and Edward Furlong as its principal cast. It is the sequel to the 1984 film The Terminator, as well as the second installment in the Terminator franchise. Terminator 2 follows Sarah Connor (Hamilton) and her ten-year-old son John (Furlong) as they are pursued by a new, more advanced Terminator: the liquid metal, shapeshifting T-1000 (Patrick), sent back in time to kill John Connor and prevent him from becoming the leader of the human resistance. A second, less advanced Terminator (Schwarzenegger) is also sent back in time to protect John.",
                          "https://upload.wikimedia.org/wikipedia/pt/8/85/Terminator2poster.jpg",
                          "https://www.youtube.com/watch?v=HgV7-MJwUBw")

the_godfather = movie.Movie("The Godfather",
                            "The Godfather is a 1972 American crime film directed by Francis Ford Coppola and produced by Albert S. Ruddy, based on Mario Puzo's best-selling novel of the same name. It stars Marlon Brando and Al Pacino as the leaders of a fictional New York crime family. The story, spanning 1945 to 1955, chronicles the family under the patriarch Vito Corleone (Brando), focusing on the transformation of Michael Corleone (Pacino) from reluctant family outsider to ruthless mafia boss.",
                            "https://upload.wikimedia.org/wikipedia/pt/7/71/Chef%C3%A3o.jpg",
                            "https://youtu.be/sY1S34973zA")

the300 = movie.Movie("300",
                     "300 is a 2006 American epic war film based on the 1998 comic series of the same name by Frank Miller and Lynn Varley. Both are fictionalized retellings of the Battle of Thermopylae within the Persian Wars. The film was directed by Zack Snyder, while Miller served as executive producer and consultant. It was filmed mostly with a super-imposition chroma key technique, to help replicate the imagery of the original comic book.",
                     "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
                     "https://youtu.be/UrIbxk7idYA")

batman_dark_knight = movie.Movie("Batman - The Dark Knight",
                                 "The Dark Knight is a 2008 superhero film directed, co-produced, and co-written by Christopher Nolan. Based on the DC Comics character Batman, the film is the second part of Nolan's The Dark Knight Trilogy and a sequel to 2005's Batman Begins, starring an ensemble cast including Christian Bale, Michael Caine, Heath Ledger, Gary Oldman, Aaron Eckhart, Maggie Gyllenhaal and Morgan Freeman. In the film, Bruce Wayne / Batman (Bale), Police Lieutenant James Gordon (Oldman) and District Attorney Harvey Dent (Eckhart) form an alliance to dismantle organized crime in Gotham City, but are menaced by an anarchist mastermind known as the Joker (Ledger), who seeks to undermine Batman's influence and turn the city to chaos.",
                                 "https://upload.wikimedia.org/wikipedia/pt/d/d1/The_Dark_Knight.jpg",
                                 "https://www.youtube.com/watch?v=EXeTwQWrcwY")

# creating an array of movie instancies
movies = [toy_story, hurt_locker, terminator2, the_godfather, the300, batman_dark_knight]

# showing list of movies with fresh_tomatoes function
fresh_tomatoes.open_movies_page(movies)
