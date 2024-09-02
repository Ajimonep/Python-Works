movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

#q1 total_number_of_movies
# movie_count=0

# for film in movies:
#     if "title"!=None:
#         movie_count+=1

# print(movie_count)

movie_count=len(movies)
# print("numbers of movies=",movie_count)

#q2 movies with genre Drama

drama_genre=[film.get("title") for film in movies if "Drama" in film.get("genres")]
# print(drama_genre)

#q3 latest movie
def get_year(mov):
    return mov.get("year")

latest=max(movies,key=get_year)

latest_movie=[m.get("title") for m in movies if m.get("year")==latest.get("year")]
# print(latest_movie)

#q4 top movie (movie with higest rating)
def get_rating(mov):
    return mov.get("rating")

max_rate=max(movies,key=get_rating)
max_rating=[m.get("title") for m in movies if m.get("rating")==max_rate.get("rating")]
# print(max_rating)


# q5 movies with language malayalam

malayalam_movies=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)

# q6 movies released after year 2016
movies_after_2016=[m.get("title") for m in movies if m.get("year")>2016]
# print(movies_after_2016)

# q7 movie with lowest rating

low_rating=min(movies,key=get_rating)
lowest_rating=[m.get("title")for m in movies if m.get("rating")==low_rating.get("rating")]
# print(lowest_rating)

#q8 malayalam movies with genere Action
malayalam_action=[m.get("title") for m in movies if "Drama" in m.get("genres") and  m.get("language")=="Malayalam" ]
# print(malayalam_action) 

# q9 movies releasd in same years

movie_dictionary={}

for m in movies:

    release_year=m.get("year")

    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))

    else:
        movie_dictionary[release_year]=[m.get("title")]

# print(movie_dictionary)


# q10 oldest movie

old_movie=min(movies,key=get_year)
oldest_movie=[m.get("title") for m in movies if m.get("year")==old_movie.get("year")]
# print(oldest_movie)

# movie name with generes either Drama or Comedy
drama_comedy=[m.get("title")for m in movies if "Drama" in m.get("genres") or "Comedy" in m.get("genres")]
# print(drama_comedy)

#q11 number of movies relaesed in each year

years=[m.get("years")for m in movies]
# print(years)

year_count={y:years.count(y)for y in years}
# print(year_count)

# generes={g for m in movies for g in m.get("genres")}

# print(generes)

# generes=[]     

# for m in movies:
#     for g in m.get("genres"):
#         generes.append(g)

generes=[g for m in movies for g in m.get("genres")]

generes_count={g:generes.count(g)for g in generes }
# print(generes_count)

#q12  sort with title

sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))

sorted_movies_title=[m.get("title") for m in sorted_movies]

print(sorted_movies_title)







