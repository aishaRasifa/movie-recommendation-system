
from recommender.movie_recommender import MovieRecommender

def main():

    recommender = MovieRecommender("data/movies.csv")

    print("Movie Recommendations")
    print("---------------------")

    print("\\nRecommendations for Genre='Sci-Fi', Language='English':")

    print(
        recommender.recommend(
            genre='Sci-Fi',
            language='English'
        )
    )

    print("\\nRecommendations for Genre='Drama':")

    print(
        recommender.recommend(genre='Drama')
    )

if __name__ == "__main__":
    main()
