
import pandas as pd

class MovieRecommender:

    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, genre=None, language=None):

        result = self.data

        if genre:
            result = result[
                result['genre'].str.lower() == genre.lower()
            ]

        if language:
            result = result[
                result['language'].str.lower() == language.lower()
            ]

        return result['movie'].tolist()
