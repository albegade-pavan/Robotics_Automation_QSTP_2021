# -*- coding: utf-8 -*-
"""QSTP_ROS_week1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19pkTk1JoU_mCaTzYb8nYOcpkY1u68ciK
"""

#! /usr/bin/python3
"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w)
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt
 
 
class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
 
        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]
 
        # print(self.x_points,self.y_points)
 
    def step(self, v: float, w: float, n: int):
        self.v = v
        self.w = w
        self.n = n
 
        self.dt=0.1
        # time = np.arange(0, self.dt)
        x = self.x
        y = self.y
        theta = self.theta
        time = self.dt
        for i in range(n):
            theta = theta+time * w 
            x =  x+v * np.cos(theta) * time 
            y =  y+v * np.sin(theta) * time 
 
            self.x_points.append(x)
            self.y_points.append(y)
 
 
        """
        Write the Kinematics model here
        Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose
        """
 
        #print(self.x_points,self.y_points)
        return self.x_points,self.y_points
        # return x, y, theta
 
    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
 
        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        #plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        plt.savefig(f"Unicycle_{v}_{w}.png")
 
 
 
 
if __name__ == "__main__":
    robot1 = Unicycle(0, 0, 0, 0.1)
    robot1.step(1, 0.5, 25)
    robot1.plot(1,0.5)

    robot2 = Unicycle(0, 0, 1.57, 0.2)
    robot2.step(0.5, 1, 10)
    robot2.plot(0.5,1)

    robot3 = Unicycle(0, 0, 0.77, 0.05)
    robot3.step(5, 4, 50)
    robot3.plot(5,4)


 
    print("Unicycle Model Assignment")
 
    # make an object of the robot and plot various trajectories