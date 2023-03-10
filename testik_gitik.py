from tkinter import *

main_window = Tk()
main_window.title('Kube si zkousi Gitik')
main_window.geometry('320x320')
main_window.iconbitmap(main_window, 'znak_skoda.ico')
canvas = Canvas(main_window, width=320, height=240)
canvas.pack()
main_window.mainloop()


