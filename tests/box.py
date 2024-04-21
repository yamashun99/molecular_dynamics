import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame


class GLFrame(OpenGLFrame):
    def initgl(self):
        self.nboxes = 1
        self.vertices = [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.0, 1.0, 1.0],
        ]
        self.faces = [
            [4, 5, 6, 7],
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7],
            [0, 1, 2, 3],
        ]
        self.normals = [
            [0.0, 0.0, -1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [-1.0, 0.0, 0.0],
            [0.0, -1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]

        glViewport(0, 0, self.width, self.height)
        glClearColor(0.5, 0.5, 0.5, 1.0)

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)

        for i in range(self.nboxes):
            glBegin(GL_QUADS)
            for j, face in enumerate(self.faces):
                glNormal3fv(self.normals[j])
                for k in face:
                    glVertex3fv(self.vertices[k])
            glEnd()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Box")
        self.glframe = GLFrame(self, width=640, height=480)
        self.glframe.pack(expand=True, fill=tk.BOTH)

        self.push_btn = tk.Button(self, text="Push", command=self.push_box)
        self.push_btn.pack(fill=tk.X)

        self.pop_btn = tk.Button(self, text="Pop", command=self.pop_box)
        self.pop_btn.pack(fill=tk.X)

    def push_box(self):
        self.glframe.nboxes += 1
        self.glframe._display()

    def pop_box(self):
        self.glframe.nboxes -= 1
        self.glframe._display()


App().mainloop()
