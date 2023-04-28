from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __if_user_registered(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
        raise ValueError("This user does not exist!")

    def __if_movie_registered(self, movie):
        for m in self.movies_collection:
            if m == movie:
                return movie
        raise Exception(f"The movie {movie.title} is not uploaded!")

    def register_user(self, username: str, age: int):
        user = User(username, age)
        if user in self.users_collection:
            raise ValueError("User already exists!")

        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__if_user_registered(username)
        if not movie.owner == user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__if_user_registered(username)
        movie = self.__if_movie_registered(movie)
        if user.username == username:
            if movie not in user.movies_owned:
                raise Exception(f"{username} is not the owner of the movie {movie.title}!")
            for key, value in kwargs.items():
                if key == "title":
                    movie.title = value
                elif key == "year":
                    movie.title = value
                elif key == "age_restriction":
                    movie.title = value
            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__if_user_registered(username)
        movie = self.__if_movie_registered(movie)
        if movie in user.movies_owned:
            self.movies_collection.remove(movie)
            user.movies_owned.remove(movie)
            return f"{username} successfully deleted {movie.title} movie."
        else:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

    # @staticmethod
    # def __if_movie_not_owned_by_user(user, movie):
    #     if movie in user.movies_collection:
    #         raise Exception(f"{user.name} is the owner of the movie {movie.title}!")
    #     return movie

    def like_movie(self, username: str, movie: Movie):
        user = self.__if_user_registered(username)
        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__if_user_registered(username)
        if movie in user.movies_liked:
            movie.likes -= 1
            user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."
        raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        if len(self.movies_collection) < 1:
            return "No movies found."
        sorted_movies_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        i = len(sorted_movies_collection)
        ch = 0
        result = ''
        movies_str = []

        for movie in sorted_movies_collection:
            movies_str.append(movie.details())
        for string in movies_str:
            ch += 1
            if ch == i:
                result += string
            else:
                result += string
                result += '\n'
        return result

    def __str__(self):
        usernames = [user.username for user in self.users_collection]
        movie_titles = [movie.title for movie in self.movies_collection]
        if len(usernames) == 0:
            result = "All users: No users.\n"
        else:
            result = f"All users: {', '.join(usernames)}\n"
        if len(movie_titles) == 0:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(movie_titles)}"
        return result







