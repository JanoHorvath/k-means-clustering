import math
from data_parser import Dataset
from random import randint


class SortIntoClusters():
    dataset = Dataset()
    cluster_center = []
    size_of_graph = 500

    colors = ['red', 'blue', 'green', 'pink', 'brown', 'grey', 'gold', 'purple']

    Points = dataset.get_mock_dataset(dataset, 50)

    def initialize(self):
        number_of_clusters = raw_input('Enter number of clusters: ')
        self.size_of_graph = raw_input('Enter size of graph: ')

        """Initialize n cluster centers"""
        for n in number_of_clusters:
            self.cluster_center[n] = [randint(0, self.size_of_graph), randint(0, self.size_of_graph), self.colors[n]]

    def assign_points(self):
        """Assigns color to every point"""

        for point in self.Points:
            distance = self.size_of_graph*2

            """by computing distance to every cluster center"""
            for cluster in self.cluster_center:
                sum = 0
                for x in range(0, len(point)-1):
                    sum += math.pow(point[x]-cluster[x], 2)

                """and finding the closest one."""
                new_distance = math.pow(sum, 1/2)
                if new_distance < distance:
                    point[-1] = cluster[-1]

    def recalibrate(self):
        """ Repositions cluster centers """

        for center in self.cluster_center:
            average = []

            """by getting all the points of the same color"""
            for point in filter(lambda p: p[-1] == center[-1], self.Points):
                for i in range(0, len(point)-1):
                    average[i] += point[i]

            """and computing the average of all dimensions."""
            for i in range(0, len(center)-1):
                center[i] = average[i] / len(average)
