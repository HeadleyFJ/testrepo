import streamlit as st
import streamlit.components.v1 as components

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 

def func(t, line):
    t = np.arange(0,t,0.1)
    y = np.sin(t)
    line.set_data(t, y)
    return line
 
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-1.2, 1.22))
redDots = plt.plot([], [], 'ro')
line = plt.plot([], [], lw=2)
 

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=np.arange(1,100,0.1), fargs=(line), interval=100, blit=False)
#line_ani.save(r'Animation.mp4')
 
 

#HtmlFile = line_ani.to_html5_video()
with open("myvideo.html","w") as f:
  print(line_ani.to_html5_video(), file=f)
  
HtmlFile = open("myvideo.html", "r")
#HtmlFile="myvideo.html"
source_code = HtmlFile.read() 
components.html(source_code, height = 900,width=900)
