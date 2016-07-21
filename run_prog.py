""" Run the program with a GUI. """

import docx_to_xlsx
import os, sys
import tkinter as tk
from tkinter import filedialog, Frame, BOTH, Button, RIGHT, RAISED


class TrendGUI(Frame):

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        # saved reference to parent widget. "Tk root window"
        self.parent = parent
        self._workbook = None
        self._file_path = None
        self._folder_path = None

        self.frame_1 = Frame(self, relief=RAISED)
        self.run_button = Button(self, text='Run', width=10,
                                 command=self.run_program)
        self.workbook_button = Button(self.frame_1, text='Select Workbook',
                                      width=15, command=self.get_workbook)
        self.file_button = Button(self.frame_1, text='Select File',
                                  width=15, command=self.get_file)
        self.folder_button = Button(self.frame_1, text='Select Folder',
                                    width=15, command=self.get_folder)
        self.close_button = Button(self, text='Close', width=10,
                                   command=self.quit)

        self.init_gui()

    def init_gui(self):
        """ Create the GUI. """
        # set title of root window
        self.parent.title('Trending Analysis Program')
        # fill frame to take up whole of root window
        self.pack(fill=BOTH, expand=True)
        self.frame_1.pack(fill=BOTH, expand=True)

        # Buttons
        self.folder_button.pack(side=RIGHT, padx=5)
        self.file_button.pack(side=RIGHT, pady=5)
        self.workbook_button.pack(side=RIGHT, padx=5, pady=5)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)
        self.run_button.pack(side=RIGHT, pady=5)

    def get_file(self):
        self._file_path = filedialog.askopenfilename()
        self.file_button.config(text='File Selected')
        self.folder_button.destroy()

    def get_folder(self):
        self._folder_path = filedialog.askdirectory()
        self.folder_button.config(text='Folder Selected')
        self.file_button.destroy()

    def get_workbook(self):
        self._workbook = filedialog.askopenfilename()
        self.workbook_button.config(text='Workbook Selected')

    def run_program(self):
        # user selected one CAPA
        if self._folder_path is None:
            docx_to_xlsx.main(self._file_path)
        # user selected a folder of CAPA's
        elif self._file_path is None:
            pass


def main():

    root = tk.Tk()
    root.geometry("350x100+300+300")
    app = TrendGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
