from random import randint

class Dataset:

    def get_mock_dataset(self, size):
        """  Mock 2D dataset for starters. """

        Points = []

        for i in range(size):
            point = {'x': randint(0,20), 'y': randint(0,20), 'color': 'black'}
            Points[i] = point

        return Points

