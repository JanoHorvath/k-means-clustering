import math
from data_parser import Dataset
from random import randint


class SortIntoClusters():
    number_of_clusters = raw_input('Enter number of clusters: ')
    size_of_graph = raw_input('Enter size of graph: ')

    dataset = Dataset()
    cluster_center = []
    colors = ['red', 'blue', 'green', 'pink', 'brown', 'grey', 'gold', 'purple']

    Points = dataset.get_mock_dataset(dataset, 50)

    """Initialize n cluster centers"""
    for n in number_of_clusters:
        cluster_center[n] = [randint(0, size_of_graph), randint(0, size_of_graph), colors[n]]

    """Assign color to every point"""
    for point in Points:
        distance = size_of_graph*2

        """by computing distance to every cluster center"""
        for cluster in cluster_center:
            sum = 0
            for x in range(0, len(point)-1):
                sum += math.pow(point[x]-cluster[x], 2)

            """and finding the closest one."""
            new_distance = math.pow(sum, 1/2)
            if new_distance < distance:
                point[-1] = cluster[-1]