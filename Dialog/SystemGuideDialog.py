import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
from tkinter import Canvas


class SystemGuideDialog:

    parent = ""

    def __init__(self, parent):
        print('>>> show System Guide')

        self.images = []
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-1.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-2.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-3.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-4.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-5.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-6.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\langkah-7.png'))

        self.text_guide = ['Tekan tombol \"Pilih Berkas\" pada Halaman Beranda',
                           'Pilih berkas SKPL yang ingin Anda analisa',
                           'Tekan tombol \"Lanjutkan\" pada Halaman Beranda',
                           'Sistem beralih ke Halaman Utama',
                           'Tekan tombol \"Lihat Direktori\" untuk menampilkan lokasi file SKPL',
                           'Tekan tombol \"Ekstrak Dokumen\" untuk menampilkan daftar kebutuhan ke monitor',
                           'Tekan tombol \"Mulai Deteksi\"'
                           ]

        self.image_number = 0
        self.text_guide_number = 0

        self.parent = parent
        self.parent.geometry("750x500")
        self.parent.resizable(width=False, height=False)
        self.parent.title("Panduan Pengguna")

        # make view focus in this dialog
        # prevent to open other view/dialog before close this dialog
        self.parent.grab_set()

        # initialize frame
        self.frame = tk.Frame(self.parent)
        self.frame.pack(side="top", fill="both", expand=True)

        for r in range(12):
            self.frame.rowconfigure(r, weight=1)
        for c in range(10):
            self.frame.columnconfigure(c, weight=1)

        # initialize for side image
        self.photo = ImageTk.PhotoImage(file='Images\\tech.png')

        # set canvas for show side image
        self.canvas_side = Canvas(self.frame, bd=0, bg='white')
        self.canvas_side.config(width=100, height=500)
        # self.canvas_side.create_image(0, 0, image=self.photo, anchor='nw')
        self.canvas_side.grid(row=0, column=0, rowspan=12, sticky='nw')

        # set canvas for show guide image
        self.canvas_guide = Canvas(self.frame, bd=1, bg='white')
        self.canvas_guide.config(width=545, height=320)
        self.image_on_canvas = self.canvas_guide.create_image(0, 0, image=self.images[self.image_number], anchor='nw')
        self.canvas_guide.place(relx=0.2, rely=0.05)

        self.label_text_guide = ttk.Label(self.frame, text=self.text_guide[self.text_guide_number], font='Calibri 12')
        self.label_text_guide.grid(row=9, column=1, columnspan=8, sticky='S')

        self.label_guide_order = ttk.Label(self.frame, text="1/7", font='Calibri 12 bold')
        self.label_guide_order.grid(row=10, column=1, columnspan=8, sticky='N')

        self.button_quit = ttk.Button(self.frame, padding=3, text='OK', width=12, command=self.close_windows)
        self.button_quit.place(relx=0.85, rely=0.9)

        self.button_next = ttk.Button(self.frame, padding=3, text='Lanjut>>>', width=12, command=self.move_next)
        self.button_next.place(relx=0.57, rely=0.9)

        self.button_previous = ttk.Button(self.frame, padding=3, text='<<<Kembali', width=12,
                                          command=self.move_previous)
        self.button_previous['state'] = 'disable'
        self.button_previous.place(relx=0.45, rely=0.9)

    def move_next(self):

        self.image_number += 1
        self.text_guide_number += 1

        if self.image_number == (len(self.images)-1):
            self.button_next['state'] = 'disable'
        else:
            self.button_previous['state'] = 'enable'

        self.canvas_guide.itemconfigure(self.image_on_canvas, image=self.images[self.image_number])
        self.label_text_guide.configure(text=self.text_guide[self.text_guide_number])
        temp_numb = str(self.image_number+1)
        numb = '%s/7' % temp_numb
        self.label_guide_order.configure(text=numb)

    def move_previous(self):

        self.image_number -= 1
        self.text_guide_number -= 1

        if self.image_number == 0:
            self.button_previous['state'] = 'disable'
        else:
            self.button_next['state'] = 'enable'

        self.canvas_guide.itemconfigure(self.image_on_canvas, image=self.images[self.image_number])
        self.label_text_guide.configure(text=self.text_guide[self.text_guide_number])
        temp_numb = str(self.image_number + 1)
        numb = '%s/7' % temp_numb
        self.label_guide_order.configure(text=numb)

    def close_windows(self):
        print('>>> close System Guide\n')
        self.parent.destroy()


"""app = tk.Tk()
SystemGuideDialog(app)
app.mainloop()"""
