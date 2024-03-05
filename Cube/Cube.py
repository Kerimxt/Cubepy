import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def draw_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Küpün köşe noktaları
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    z = [0, 0, 0, 0, 1]

    # Köşe noktalarını çiz
    ax.plot(x, y, z, color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def main():
    root = tk.Tk()
    root.title("3D Kırmızı Küp")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    draw_button = tk.Button(root, text="Küpü Çiz", command=draw_cube)
    draw_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
