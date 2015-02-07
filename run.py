import time
from sort_into_clusters import SortIntoClusters

sort = SortIntoClusters()

sort.initialize()
while True:
    sort.assign_points()
    sort.render()
    time.sleep(1)
    print('Assigned')

    if sort.recalibrate():
        break
    sort.render()
    time.sleep(2)
    print('new cycle')

print('Done')