from random import randint

class Dataset:

    def get_mock_dataset(self, number, x_upper_bound, y_upper_bound):
        """  Mock 2D dataset for starters. """

        points = []

        for i in range(number):
            point = [randint(0,x_upper_bound), randint(0,y_upper_bound), 'black']
            points.append(point)

        return points

