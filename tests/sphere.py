import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame
import numpy as np


class GLFrame(OpenGLFrame):
    def initgl(self):
        glViewport(0, 0, self.width, self.height)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        self.rotate = 0

    def torad(self, deg):
        return deg * np.pi / 180.0

    def redraw(self):
        self.rotate += 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height, 0.1, 100.0)
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(self.rotate, 1, 1, 0)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])

        end = 360
        step = 20

        for deg1 in range(0, end, step):
            arad1 = self.torad(deg1)
            arad2 = self.torad(deg1 + step)

            for deg2 in range(0, end, step):
                brad1 = self.torad(deg2)
                brad2 = self.torad(deg2 + step)

                x1 = np.sin(arad1) * np.cos(brad1)
                y1 = np.sin(arad1) * np.sin(brad1)
                z1 = np.cos(arad1)

                x2 = np.sin(arad2) * np.cos(brad1)
                y2 = np.sin(arad2) * np.sin(brad1)
                z2 = np.cos(arad2)

                x3 = np.sin(arad2) * np.cos(brad2)
                y3 = np.sin(arad2) * np.sin(brad2)
                z3 = np.cos(arad2)

                x4 = np.sin(arad1) * np.cos(brad2)
                y4 = np.sin(arad1) * np.sin(brad2)
                z4 = np.cos(arad1)

                glNormal3d(x1, y1, z1)
                glBegin(GL_QUADS)

                glVertex3f(x1, y1, z1)
                glVertex3f(x2, y2, z2)
                glVertex3f(x3, y3, z3)
                glVertex3f(x4, y4, z4)

                glEnd()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sphere")
        self.glframe = GLFrame(self, width=800, height=600)
        self.glframe.pack(fill=tk.BOTH, expand=True)
        self.glframe.animate = True


App().mainloop()
