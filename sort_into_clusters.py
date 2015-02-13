import math, copy, time
from random import randint

from data_parser import Dataset


class SortIntoClusters():
    def __init__(self):
        self.cluster_center = []
        self.graph_height = 500
        self.graph_width = 500
        self.colors = ['red', 'dodger blue', 'green2', 'deep pink', 'brown', 'gray', 'gold', 'purple', 'cyan', 'green4']
        self.Points = []

    def initialize_data(self, canvas):
        """ Get info about canvas and initialize 20 points"""
        self.graph_height = canvas.winfo_reqwidth()-30
        self.graph_width = canvas.winfo_reqheight()-30
        self.cluster_center = []

        dataset = Dataset()
        self.Points = dataset.get_mock_dataset(20, self.graph_width, self.graph_height)

        canvas.delete('all')
        self.render(canvas)

    def initialize_cluster_centers(self, canvas, number_of_clusters):
        """Initialize n cluster centers"""
        self.cluster_center = []

        for n in range(number_of_clusters):
            self.cluster_center.append([randint(0, self.graph_height), randint(0, self.graph_width), self.colors[n]])

        self.render(canvas)
        print("Initialized " + str(len(self.cluster_center)) + " cluster centers.")

    def assign_points(self):
        """Assigns color to every point"""
        print('Assigning color to points.')

        for point in self.Points:
            distance = None

            """by computing distance to every cluster center"""
            for cluster in self.cluster_center:
                sum = 0
                for x in range(0, len(point) - 1):
                    sum += math.pow(point[x] - cluster[x], 2)

                """and finding the closest one."""
                new_distance = math.pow(sum, 0.5)
                if distance is None: distance = new_distance

                if new_distance <= distance:
                    point[-1] = cluster[-1]
                    distance = new_distance

    def recalibrate(self):
        """ Repositions cluster centers """
        old_centers = copy.deepcopy(self.cluster_center)

        for center in self.cluster_center:
            average = [0 for _ in range(len(center))]

            """by getting all the points of the same color"""
            points_of_same_color = filter(lambda p: p[-1] == center[-1], self.Points)
            for point in points_of_same_color:
                for i in range(0, len(point) - 1):
                    average[i] += point[i]

            """and computing the average of all dimensions."""
            for i in range(0, len(center) - 1):
                try:
                    center[i] = average[i]/len(points_of_same_color)
                except ZeroDivisionError:
                    pass


        print('Repositioned Cluster Centers')
        return old_centers == self.cluster_center

    def render(self, canvas):
        if len(self.Points[0]) <= 3:
            print('Rendering 2D.')

            canvas.delete('all')

            for point in self.Points:
                x = point[0]
                y = point[1]
                canvas.create_oval(x, y, x+5, y+5, fill=point[-1], width=0)

            for center in self.cluster_center:
                x = center[0]
                y = center[1]
                canvas.create_rectangle(x-4, y-4, x+4, y+4, fill=center[-1], width=0)
            canvas.update_idletasks()
        else:
            canvas.create_text(self.graph_width/2, self.graph_height/2, text="Data has more than 2 dimensions. Unable to render. yet.")


    def clusterize(self, canvas, number_of_clusters):
        """ Repeats k-means clustering until the cluster centers do not change coordinates between cycles """
        self.initialize_cluster_centers(canvas, number_of_clusters)

        finished = False
        while not finished:
            time.sleep(0.3)
            self.assign_points()
            self.render(canvas)
            time.sleep(0.3)
            finished = self.recalibrate()
            self.render(canvas)
            time.sleep(0.3)
            print('New cycle')

        print('Done')