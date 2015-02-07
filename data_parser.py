from random import randint

class Dataset:

    def get_mock_dataset(self, size):
        """  Mock 2D dataset for starters. """

        points = []

        for i in range(size):
            point = [randint(0,20), randint(0,20), 'black']
            points.append(point)

        return points

