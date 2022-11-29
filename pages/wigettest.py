import rebound
import streamlit as st
import matplotlib.pyplot as plt

st.write("hi")

sim = rebound.Simulation()
sim.add(m=1) # add a star
for i in range(10):
    sim.add(m=1e-3,a=0.4+0.1*i,inc=0.03*i,omega=5.*i) # Jupiter mass planets on close orbits
sim.move_to_com() # Move to the centre of mass frame

st.write(plt.plot(rebound.OrbitPlot(sim)))

sim.getWidget()
