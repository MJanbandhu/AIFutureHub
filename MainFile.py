# plot_graph.py
import matplotlib.pyplot as plt
import numpy as np

def display_graph():
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the graph
    plt.plot(x, y)
    plt.title("Simple Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Display the plot in the terminal
    plt.show()

if __name__ == "__main__":
   

 display_graph()