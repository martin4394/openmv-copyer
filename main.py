import ttkbootstrap as ttk
import subprocess

def save_program():
	subprocess.run(["cp", "-r", f"{pathentry.get()}.", "/media/robi/OPENMV"], shell=False)


window = ttk.Window(themename='superhero')
window.title('OpenMV Copyer')
window.geometry('440x300')
window.resizable(False, False)

pathentry = ttk.Entry(window, text="Nummer")
pathentry.place(x=20, y=20, width=400)
pathentry.insert(0, "/home/robi/Dokumente/OpenMV/LineTest/")

btn = ttk.Button(window, text='Upload', command=save_program)
btn.place(x=20, y=70, width=400)


window.mainloop()
