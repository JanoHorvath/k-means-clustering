from random import randint

class Dataset:

    def get_mock_dataset(self, size):
        """  Mock 2D dataset for starters. """

        Points = []

        for i in range(size):
            point = [randint(0,20), randint(0,20), 'black']
            Points[i] = point

        return Points

