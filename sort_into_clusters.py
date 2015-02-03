from data_parser import Dataset


class SortIntoClusters():
    number_of_clusters = raw_input('Enter number of clusters: ')

    Points = Dataset()

    Points.get_mock_dataset(Points, 50)



