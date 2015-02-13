import Tkinter

from sort_into_clusters import SortIntoClusters


window = Tkinter.Tk()
sort = SortIntoClusters()

canvas = Tkinter.Canvas(window, height=500, width=500)
canvas.grid(row=0, column=0, rowspan=10)

label_scale = Tkinter.Label(window,
                            text="1) Initialize data points \n" +
                                 "2) Choose # of cluster centers using slider \n" +
                                 "3) Run algorithm to detect clusters",
                            justify='left').grid(row=0, column=1, sticky='s')

initialize_random_button = Tkinter.Button(window,
                                          text="Initialize data points",
                                          command=lambda: sort.initialize_data(canvas)).grid(row=1,column=1)

scale = Tkinter.Scale(window, orient='horizontal', from_=0, to=10)
scale.grid(row=2, column=1, sticky='n')

run_loop_button = Tkinter.Button(window,
                                 text="Run algorithm",
                                 command=lambda: sort.clusterize(canvas, scale.get())).grid(row=3, column=1, sticky='n')

window.mainloop()
