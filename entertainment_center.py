#!/usr/bin/env python

import media
import fresh_tomatoes

# Movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",  # noqa
                        "G",
                        "1995",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "http://media2.fdncms.com/boiseweekly/imager/disney-announces-toy-story-4-for-2017/u/original/3345916/342369.jpg?dl=1"  # noqa
                        )

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=uA8SG4Yea7s",
                     "PG-13",
                     "2009",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     "http://www.hdwallpapers.in/walls/neytiri__jake_sully_avatar-wide.jpg?dl=1"  # noqa
                     )

maze_runner = media.Movie("The Maze Runner",
                          "Stuck in a Maze with no memory of the past," +
                          " everyday is a fight for your life",
                          "http://ia.media-imdb.com/images/M/MV5BMjUyNTA3MTAyM15BMl5BanBnXkFtZTgwOTEyMTkyMjE@._V1_SX214_AL_.jpg",  # noqa
                          "https://www.youtube.com/watch?v=64-iSYVmMVY",  # noqa
                          "PG-13",
                          "2014",
                          "Dylan O'Brien, Kaya Scodelario, Will Poulter",
                          "http://images6.fanpop.com/image/photos/37600000/The-Maze-Runner-the-maze-runner-37604286-1920-1200.jpg?dl=1"  # noqa
                          )

interstellar = media.Movie("Interstellar",
                           "One man's travels through space and time" +
                           " on a quest to save humanity",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",  
                           "PG-13",
                           "2014",
                           "Matthew McConaughey, Anne Hathaway, "+
                           "Jessica Chastain",
                           "http://www.hdwallpapers.in/download/matthew_mcconaughey_in_interstellar-1920x1200.jpg?dl=1"  # noqa
                           )

fifth_element = media.Movie("The Fifth Element",
                            "Taxi driver saves the planet",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/6/65/Fifth_element_poster_%281997%29.jpg/220px-Fifth_element_poster_%281997%29.jpg",  # noqa
                            "https://www.youtube.com/watch?v=VkX7dHjL-aY",
                            "PG-13",
                            "1997",
                            "Bruce Willis, Milla Jovovich, Gary Oldman, " +
                            "Chris Tucker",
                            "http://megawallpapershd.com/wallpapers/l/1920x1200/84/gary_oldman_milla_jovovich_the_fifth_element_1920x1200_83775.jpg?dl=1"  # noqa
                            )

martian = media.Movie("The Martian",
                      "An astronaut's attempt to survive in a hostile " +
                      "martian climate",
                      "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=ej3ioOneTy8",
                      "PG-13",
                      "2015",
                      "Matt Damon, Jessica Chastain, Kristen Wiig",
                      "http://www.hdwallpapersimages.com/wp-content/uploads/2015/09/The-Martian-Matt-Damon-As-Mark-Watney-Images-6310.jpg?dl=1"  # noqa
                      )

mask = media.Movie("The Mask",
                   "A magical mask changes a mans life forever",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/The_Mask_%28film%29_poster.jpg/220px-The_Mask_%28film%29_poster.jpg",  # noqa
                   "https://youtu.be/lcjN7zkgELM",
                   "PG-13",
                   "1994",
                   "Jim Carrey, Cameron Diaz, Peter Riegert",
                   "http://images-cdn.moviepilot.com/images/c_limit,h_540,w_960/t_mp_quality/dqgbffrbobbj1jxjykye/5-day-recommendation-challenge-the-perfect-90-s-comedy-628414.jpg?dl=1"  # noqa
                   )

home_alone = media.Movie("Home Alone",
                         "Clever kid  left at home proves that " +
                         "he can take care of himself",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Home_alone.jpg/220px-Home_alone.jpg",  # noqa
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0",
                         "PG",
                         "1990",
                         "Macaulay Culkin, Joe Pesci, Daniel Stern",
                         "http://cdn.mtlblog.com/uploads/2015/11/home-alone.jpg?dl=1"  # noqa
                         )

harry_potter = media.Movie("Harry Potter",
                           "An orphan and his magical life",
                           "http://ia.media-imdb.com/images/M/MV5BMTYwNTM5NDkzNV5BMl5BanBnXkFtZTYwODQ4MzY5._V1_SY317_CR8,0,214,317_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=PbdM1db3JbY",
                           "PG",
                           "2001",
                           "Daniel Radcliffe, Rupert Grint, Richard Harris",
                           "http://pcwallart.com/images/harry-potter-and-the-sorcerers-stone-logo-wallpaper-2.jpg?dl=1"  # noqa
                           )

blankman = media.Movie("Blankman",
                       "A simpleton inventor becomes a superhero with a " +
                       "bulletproof costume and a low budget",
                       "http://ia.media-imdb.com/images/M/MV5BMTQyNDc4OTA5OF5BMl5BanBnXkFtZTcwOTI1NzMyMQ@@._V1_SX214_AL_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=GSFaU4cN-qI",
                       "PG-13",
                       "1994",
                       "Damon Wayans, David Alan Grier, Robin Givens",
                       "https://wallpaperscraft.com/image/blankman_1994_darryl_walker_damon_wayans_99871_3840x2400.jpg?dl=1"  # noqa
                       )

rush_hour = media.Movie("Rush Hour",
                        "Two cops team up to get back a kidnapped daughter",
                        "http://ia.media-imdb.com/images/M/MV5BMjAyMzAyNzY5N15BMl5BanBnXkFtZTcwNjU3MTc0MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE",
                        "PG-13",
                        "1998",
                        "Jackie Chan, Chris Tucker, Ken Leung",
                        "http://images7.alphacoders.com/336/336247.jpg?dl=1"
                        )

total_recall = media.Movie("Total Recall",
                           "When a man goes for virtual vacation memories " +
                           "of the planet Mars, an unexpected and harrowing " +
                           "series of events forces him to go to the planet " +
                           "for real, or does he?",
                           "http://ia.media-imdb.com/images/M/MV5BMTc2MTU4ODI5MF5BMl5BanBnXkFtZTcwODI2MzAyOA@@._V1_SY317_CR7,0,214,317_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=WFMLGEHdIjE",
                           "R",
                           "1990",
                           "Arnold Schwarzenegger, Sharon Stone, " +
                           "Michael Ironside",
                           "https://georgespigot.files.wordpress.com/2015/08/total-rekall-01.jpg?dl=1"  # noqa
                           )

leprechaun = media.Movie("Leprechaun",
                         "When a man goes for virtual vacation memories " +
                         "of the planet Mars, an unexpected and harrowing " +
                         "series of events forces him to go to the planet " +
                         "for real, or does he?",
                         "http://ia.media-imdb.com/images/M/MV5BMTU4NjE2MjgwN15BMl5BanBnXkFtZTcwMjEyMTMyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=0xD8AE8ZcpA",
                         "R",
                         "1993",
                         "Warwick Davis, Jennifer Aniston, Ken Olandt",
                         "http://image.tmdb.org/t/p/w1920/zYbm9EL6h6LtXCJwIcMskiRpiP7.jpg?dl=1"  # noqa
                         )

# Array of all movies to be displayed
movies = [toy_story, avatar, maze_runner, interstellar, fifth_element, martian,
          mask, home_alone, harry_potter, blankman, rush_hour, leprechaun
          ]

fresh_tomatoes.open_movies_page(movies)
