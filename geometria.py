import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def line_between(a, b): 
    x = [a[0], b[0]] 
    y = [a[1], b[1]] 
    return x, y

def line_slope(a, b):
    dy = a[1] - b[1]
    dx = a[0] - b[0]
    if dx == 0:
        print("slope is infinite!\n")
        return np.nan
    else:
        m = dy/dx
        return m

def line_coeffs(a, b):
    A = b[1] - a[1]
    B = b[0] - a[0]
    C = a[0]*A - a[1]*B
    return A, B, C

def intersection(a, b, c, d):
    a1, b1, c1 = line_coeffs(a, b)
    a2, b2, c2 = line_coeffs(c, d)
    detM = a1*b2 - a2*b1
    if detM == 0:
        print("lines are parallel!")
        return np.nan, np.nan
    else:
        x_intersect = (c1*b2 - c2*b1)/detM
        y_intersect = -(a1*c2 - a2*c1)/detM
        return x_intersect, y_intersect

def plot_line(a, b, wdth = 1.5):
    x_vals, y_vals = line_between(a, b)
    plt.plot(x_vals, y_vals, linewidth = wdth)

def plot_intersect(a, b, c, d):
    x_intersect, y_intersect = intersection(a, b, c, d)
    plt.plot(x_intersect, y_intersect, 'o')

def construzione_legittima(p1, p2, a, b, iterations = 100): 
    # primero, juntamos los puntos de fuga con los vértices
    # y calculamos el punto de fuga de las diagonales veritcales:

    p3 = intersection(p1, p2, a, b)
    plot_line(p1, p2)
    plot_line(p1, a) 
    plot_line(p2, a) 
          
    # luego, encontrar la intersección de la lineas 
    # que unen P1, P2 con B con las lineas que unen 
    # P1, P2 con A. 
     
    a1 = intersection(p1, b, p2, a)
    plot_line(p1, a1)
    
    for i in range(iterations):
        b1 = intersection(p3, a1, p2, b)
        a1 = intersection(p1, b1, p2, a)
        plot_line(p1, a1, 1.5 - i/iterations)

    a2 = intersection(p2, b, p1, a)
    plot_line(p2, a2)
    for i in range(iterations):
        b2 = intersection(p3, a2, p1, b)
        a2 = intersection(p2, b2, p1, a)
        plot_line(p2, a2, 1.5 - i/iterations)
     
    plt.show()

def mandelbrot(p):
     z = complex(0,0)
     for i in range(10):
         z = z*z + p
         if abs(z) >= 2:
             return i
             break
     return i

def plot_mandelbrot(width = 1, grain = 100): 
     cmap = cm.get_cmap('viridis', 10) 
     p_x = np.linspace(-width, width, grain) 
     p_y = np.linspace(-width, width, grain) 
     lwidth = 2*width/grain 
     for i in range(grain): 
         for j in range(grain): 
             p = complex(p_x[i], p_x[j]) 
             m = mandelbrot(p) 
             plt.plot(p_x[i], p_y[j], 'o', color = cmap(m/9), linewidth = lwidth, alpha = 0.5 ) 
     plt.show() 
