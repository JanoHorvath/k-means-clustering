import math
import copy
from data_parser import Dataset
from random import randint
from graphics import *


class SortIntoClusters():
    dataset = Dataset()
    cluster_center = []
    size_of_graph = 500

    canvas = GraphWin()

    colors = ['red', 'blue', 'green', 'pink', 'brown', 'grey', 'gold', 'purple']

    Points = dataset.get_mock_dataset(size_of_graph)

    def initialize(self):
        number_of_clusters = int(raw_input('Enter number of clusters: '))

        """Initialize n cluster centers"""
        for n in range(number_of_clusters):
            self.cluster_center.append([randint(0, self.size_of_graph), randint(0, self.size_of_graph), self.colors[n]])

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
        old_centers = copy.deepcopy(self.cluster_center)

        for center in self.cluster_center:
            average = [[0] for _ in range(len(center))]

            """by getting all the points of the same color"""
            for point in filter(lambda p: p[-1] == center[-1], self.Points):
                for i in range(0, len(point)-1):average[i][0] += point[i]

            """and computing the average of all dimensions."""
            for i in range(0, len(center)-1):
                center[i] = average[i][0] / len(average)

        return old_centers == self.cluster_center


    def render(self):
        print('render')
        for point in self.Points:
            x = point[0]
            y = point[1]
            dot = Circle(Point(x,y), 2)
            dot.setFill(point[-1])
            dot.draw(self.canvas)

        for center in self.cluster_center:
            x = center[0]
            y = center[1]
            box = Rectangle(Point(x,y), Point(x+4,y+4))
            box.setFill(center[-1])
            box.draw(self.canvas)