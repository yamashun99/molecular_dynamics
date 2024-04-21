import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame
import numpy as np


class GLFrame(OpenGLFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.trajectory = []  # 球が移動する座標のリストを格納
        self.current_index = 0
        self.nframe = 0

    def initgl(self):
        glViewport(0, 0, self.width, self.height)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def redraw(self):
        self.nframe += 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height, 0.1, 100.0)
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Update current position based on the trajectory list
        if self.current_index >= len(self.trajectory):
            self.current_index = 0  # Reset index to loop the trajectory
        pos = self.trajectory[self.current_index]
        self.current_index += 1

        self.draw_sphere(mate=[0, 0.2, 0.8, 1.0], pos=pos, scale=[0.5, 0.5, 0.5])

    def draw_sphere(self, mate=[0, 0, 0.8, 1.0], pos=[0, 0, 0], scale=[1.0, 1.0, 1.0]):
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mate)
        glTranslated(*pos)
        glScaled(*scale)
        glRotated(self.nframe, 1, 1, 1)

        end = 2 * np.pi
        step = 20

        for itheta0 in range(step):
            theta0 = itheta0 * end / step
            theta1 = (itheta0 + 1) * end / step
            for iphi0 in range(step):
                phi0 = iphi0 * end / step
                phi1 = (iphi0 + 1) * end / step
                x1 = np.sin(theta0) * np.cos(phi0)
                y1 = np.sin(theta0) * np.sin(phi0)
                z1 = np.cos(theta0)

                x2 = np.sin(theta1) * np.cos(phi0)
                y2 = np.sin(theta1) * np.sin(phi0)
                z2 = np.cos(theta1)

                x3 = np.sin(theta1) * np.cos(phi1)
                y3 = np.sin(theta1) * np.sin(phi1)
                z3 = np.cos(theta1)

                x4 = np.sin(theta0) * np.cos(phi1)
                y4 = np.sin(theta0) * np.sin(phi1)
                z4 = np.cos(theta0)

                glNormal3d(x1, y1, z1)
                glBegin(GL_QUADS)

                glVertex3f(x1, y1, z1)
                glVertex3f(x2, y2, z2)
                glVertex3f(x3, y3, z3)
                glVertex3f(x4, y4, z4)

                glEnd()
        glPopMatrix()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animated Sphere on Trajectory")
        self.glframe = GLFrame(self, width=800, height=600)
        self.glframe.pack(fill=tk.BOTH, expand=True)
        self.glframe.animate = True
        # Set trajectory points directly in the GLFrame instance
        self.glframe.trajectory = [
            [0, 0, 0],
            [0.1, 0.1, 0.1],
            [0.2, 0.2, 0.2],
            [0.3, 0.3, 0.3],
            [0.4, 0.4, 0.4],
            [0.5, 0.5, 0.5],
            [0.6, 0.6, 0.6],
            [0.7, 0.7, 0.7],
            [0.8, 0.8, 0.8],
            [0.9, 0.9, 0.9],
            [1, 1, 1],
        ]


App().mainloop()
