import math, copy, time
from random import randint

from data_parser import Dataset


class SortIntoClusters():
    def __init__(self):
        self.cluster_center = []
        self.graph_height = 500
        self.graph_width = 500
        self.colors = ['red', 'dodger blue', 'green2', 'deep pink', 'brown', 'gray', 'gold', 'purple', 'cyan', 'green4']
        #'yellow', 'orange', 'salmon pink', 'light brown']
        self.Points = []

    def initialize_data(self, canvas):
        """ Get info about canvas and initialize 50 points"""
        self.graph_height = canvas.winfo_reqwidth()-30
        self.graph_width = canvas.winfo_reqheight()-30
        self.cluster_center = []

        number_of_points = 50
        dataset = Dataset()
        self.Points = dataset.get_mock_dataset(number_of_points, self.graph_width, self.graph_height)
        print("Initialized " + str(len(self.Points)) + " points.")

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

    def analyze(self, all_cluster_centers):
        """ Analyses the data, outputting the most frequent cluster center coordinates. """

        deviation = 5

        """ First merges centers close to each other counting how many were merged together, stripping color attribute"""
        final_cluster_centers = [all_cluster_centers[0][:-1]]
        final_cluster_centers[0].append(1)

        for cluster in all_cluster_centers:
            cluster[-1] = 1 #this will be the count of how many centers are merged to one (weight)
            duplicate = True
            for final_cluster in final_cluster_centers:
                for i in range(0, len(cluster)-2):
                    if (cluster[i] > (final_cluster[i] + deviation)) or (cluster[i] < (final_cluster[i] - deviation)):
                        duplicate = False
                        break
                    else:
                        duplicate = True
                if duplicate:
                    final_cluster[-1] += 1
                    break

            if not duplicate:
                final_cluster_centers.append(cluster)

        """ Compute mean weight of merged cluster centers """
        sum = 0
        all_the_weight = []
        for final_cluster in final_cluster_centers:
            sum += final_cluster[-1]
            all_the_weight.append(final_cluster[-1])
        mean_occurence = sum/len(final_cluster_centers)
        print ('Mean : ', mean_occurence)
        print ('All of them: ', all_the_weight)

        """ Filter out those cluster centers, which are greater than the popular threshold (weight) """
        popular_threshold = mean_occurence * 2
        final_cluster_centers = filter(lambda p: p[-1] > popular_threshold, final_cluster_centers)

        """  and reassign colors. """
        for n in range(0, len(final_cluster_centers)):
            final_cluster_centers[n].append(self.colors[n%10])
            print(final_cluster_centers[n][-2:])

        # """ Then compute the mean distance of a merged cluster to the points assigned to it"""

        return final_cluster_centers

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


    def clusterizeStep(self, canvas, number_of_clusters):
        """ Repeats k-means clustering until the cluster centers do not change coordinates between cycles """
        self.initialize_cluster_centers(canvas, number_of_clusters)

        finished = False
        while not finished:
            #time.sleep(0.3)
            self.assign_points()
            self.render(canvas)
            #time.sleep(0.3)
            finished = self.recalibrate()
            self.render(canvas)
            #time.sleep(0.3)
            print('New cycle')

        print('Done')

    def detectClusters(self, canvas, number_of_repetitions):
        """ Repeats the algorithm n times with 5-10 cluster centers """
        all_cluster_centers = []
        for i in range(5, 10):
            print('Starting with ' + str(i) + ' centers')
            for _ in range(0, int(number_of_repetitions)):
                self.clusterizeStep(canvas, i)
                for center in self.cluster_center:
                    all_cluster_centers.append(center)
            print('Ran the algorithm ' + str(number_of_repetitions) + ' times.')

        """ and then filters out the results. """
        final_cluster_centers = self.analyze(all_cluster_centers)
        print('Merged ' + str(len(all_cluster_centers)) + ' centers into ' + str(len(final_cluster_centers)) + ' new final centers.')

        self.cluster_center = final_cluster_centers
        self.assign_points()
        #self.cluster_center = [] #hack to hide cluster centers in the final.
        self.render(canvas)

        print('Done.')
