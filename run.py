import Tkinter
from sort_into_clusters import SortIntoClusters


window = Tkinter.Tk()
sort = SortIntoClusters()

canvas = Tkinter.Canvas(window, height=500, width=500)
canvas.pack()

scale = Tkinter.Scale(window, from_=0, to=10)
scale.pack()

initialize_random_button = Tkinter.Button(window, text="Init", command=lambda: sort.initialize_data(canvas))
initialize_random_button.pack()

run_loop_button = Tkinter.Button(window, text="Run algorithm", command=lambda: sort.clusterize(canvas, scale.get()))
run_loop_button.pack()

window.mainloop()
