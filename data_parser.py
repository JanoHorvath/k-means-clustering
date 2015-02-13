from random import randint

class Dataset:

    def get_mock_scattered_dataset(self, numberOf, x_upper_bound, y_upper_bound):
        """ Mock 2D dataset with scattered data points. """

        points = []

        for i in range(numberOf):
            point = [randint(0,x_upper_bound), randint(0,y_upper_bound), 'black']
            points.append(point)

        return points

    def get_mock_dataset(self, numberOf, x_upper_bound, y_upper_bound):
        """ Mock 2D dataset with clustered data points. """

        points = []
        clusters = []

        """ Creates between 2 to 10 cluster areas with random x/y values """
        for i in range(randint(2, 10)):
            cluster = [randint(0, x_upper_bound), randint(0, y_upper_bound)]
            clusters.append(cluster)

        """ Creates numberOf points each randomly assigned to one cluster area and random x/y values near that area """
        for i in range(numberOf):
            for i in range(randint(0, len(clusters))):
                point = [randint(0,30)+clusters[i][0], randint(0,30)+clusters[i][1], 'black']
                points.append(point)

        return points
