import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import Canvas


class AlgorithmDialog:

    parent = ""

    def __init__(self, parent):
        print('>>> Show See Algorithm Dialog')

        self.explanation_text = "Masukan sistem adalah dokumen SKPL dalam Bahasa Indonesia. Dokumen\n" \
                                "Dokumen SKPL selanjutnya diekstraksi untuk diambil bagian spesifikasi\n" \
                                "kebutuhannya saja. Selanjutnya dilakukan pengolahan awal (preprocessing)\n" \
                                "terhadap kalimat kebutuhan. Preprocsesing dilakukan dengan mengubah\n" \
                                "semua kalimat kebutuhan menjadi bentuk huruf kecil semua (lower case),\n" \
                                "tujuannya adalah untuk menyiapkan data yang siap diolah oleh sistem. \n" \
                                "Proses selanjutnya yaitu deteksi ambiguitas pada kalimat kebutuhan. \n" \
                                "Deteksi dilakukan dengan menggunakan teknik berbasis aturan dengan \n" \
                                "memanfaatkan repositori aturan rekomendasi. Hasil dari tahap deteksi \n" \
                                "tersebut adalah justifikasi ambiguitas pada kalimat (ambigu atau tidak \n" \
                                "ambigu) beserta kata yang membuat kalimat tersebut menjadi ambigu. Tahap \n" \
                                "terakhir adalah pemberian rekomendasi terhadap kalimat kebutuhan yang \n" \
                                "ambigu. Pemberian rekomendasi menggunaakan teknik berbasis statistik, \n" \
                                "yaitu menggunakan model kalimat bigram. Hasil dari tahap pemberian \n" \
                                "rekomendasi rekomendasi perbaikan kalimat dengan urutan prioritas yang \n" \
                                "paling sesuai terlebih dahulu."

        self.explanation_text_1 = "Teknik berbasis aturan digunakan untuk menentukan mana kalimat yang \n" \
                                  "ambigu dan mana yang tidak. Cara kerjanya ada dengan mencocokkan setiap \n" \
                                  "kalimat kebutuhan dengan repositori aturan yang telah disusun oleh peneliti\n" \
                                  "Luaran dari proses ini adalah justifikasi kalimat kebutuhan ambigu atau\n" \
                                  "tidak beserta kata yang membuat kalimat tersebut menjadi ambigu.\n" \
                                  "Berikut adalah gambaran repositori aturan yang digunakan (format .XML)"

        self.explanation_text_2 = "Teknik berbasis statistik digunakan untuk memberikan rekomendasi perbaikan\n" \
                                  "kalimat kebutuhan secara urut mulai dari yang paling sesuai. Pada sistem ini\n" \
                                  "digunakan teknik bahasa bigram yang merupakan salah satu teknik dalam \n" \
                                  "natural language processing. Model bahasa bigram memecah sebuah kalimat\n" \
                                  "menjadi pecahan kalimat dimana setiap pecahan terdiri dari dua kata terurut\n" \
                                  "dari kalimat. Berikut adalah rumus untuk model bahasa bigram."

        self.explanation_text_3 = "Dalam penerapan model bahasa bigram, tidak menutup kemungkinan adanya\n" \
                                  "peluang sebuah bigram kata = 0. Jika terjadi hal demikian maka akan \n" \
                                  "menyebabkan nilai peluang kalimat menjadi 0. Untuk menanggulai hal tersebut\n" \
                                  "dapat menggunakan teknik smoothing. Teknik smoothing yang digunakan dalam\n" \
                                  "sistem ini adalah Add-One (Laplace) Estimation."

        self.images = []
        self.images.append(ImageTk.PhotoImage(file='Images\\Repositori-aturan.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\Rumus-bigram.png'))
        self.images.append(ImageTk.PhotoImage(file='Images\\Add-one-laplace.png'))

        self.titles = ['Teknik berbasis Aturan',
                       'Teknik berbasis Statistik',
                       'Teknik berbasis Statistik']

        self.text_captions = [self.explanation_text_1, self.explanation_text_2, self.explanation_text_3]

        self.images_number = -1
        self.explanation_text_number = -1

        self.parent = parent
        self.parent.geometry("1000x600")
        self.parent.resizable(width=False, height=False)
        self.parent.title("Algoritme Sistem")

        # make view focus in this dialog
        # prevent to open other view/dialog before close this dialog
        self.parent.grab_set()

        for r in range(11):
            self.parent.rowconfigure(r, weight=1)
        for c in range(6):
            self.parent.columnconfigure(c, weight=1)

        # set main frame: contain title of dialog
        self.frame1 = tk.Frame(self.parent)
        self.frame1.grid(row=0, column=0, columnspan=6, sticky='WENS')

        # set second frame: contain image flow chart that used in the system
        self.frame2 = tk.Frame(self.parent, bg="#FFFFFF")
        self.frame2.grid(row=1, column=0, rowspan=10, columnspan=3, sticky='WENS', padx=(20, 1), pady=(0, 20))

        # set third frame: contains slider description of algorithm used in the system
        self.frame3 = tk.Frame(self.parent, bg="#FFFFFF")
        self.frame3.grid(row=1, column=3, rowspan=10, columnspan=3, sticky='WENS', padx=(1, 20), pady=(0, 20))

        """Title of the Dialog: locate in Frame 1"""
        self.label_title = ttk.Label(self.frame1, text="Algoritme yang Digunakan dalam Sistem", font='Calibri 15 bold')
        self.label_title.place(relx=0.35, rely=0.2)

        # initialize for flow-chart image
        self.image_flow_chart = ImageTk.PhotoImage(file='Images\\flow-chart.png')
        # set canvas for show flow-chart image
        self.canvas_flow_chart = Canvas(self.frame2, bd=0)
        self.canvas_flow_chart.config(width=450, height=485)
        self.canvas_flow_chart.create_image(0, 0, image=self.image_flow_chart, anchor='nw')
        self.canvas_flow_chart.place(relx=0.03, rely=0.035)

        # set canvas for show flow-chart image
        self.canvas_formula = Canvas(self.frame3, bd=2)
        self.canvas_formula.config(width=425, height=250)
        self.image_on_canvas = self.canvas_formula.create_image(0, 0, image=self.images[0], anchor='nw')
        self.canvas_formula.place(relx=0.05, rely=0.32)
        self.canvas_formula.place_forget()

        self.label_explanation_title = ttk.Label(self.frame3, background='#FFFFFF', text='Keterangan', font='Calibri 13 bold')
        self.label_explanation_title.place(relx=0.4, rely=0.04)

        self.label_explanation_text = ttk.Label(self.frame3, background='#FFFFFF', text=self.explanation_text, font='Calibri 10')
        self.label_explanation_text.place(relx=0.05, rely=0.12)

        self.label_explanation_order = ttk.Label(self.frame3, background='#FFFFFF', text="1/4", font='Calibri 10 bold')
        self.label_explanation_order.place(relx=0.51, rely=0.83)

        self.button_next = ttk.Button(self.frame3, padding=1, text='Lanjut>>>', width=12, command=self.move_next)
        self.button_next.place(relx=0.55, rely=0.9)

        self.button_previous = ttk.Button(self.frame3, padding=1, text='<<<Kembali', width=12, command=self.move_previous)
        self.button_previous['state'] = 'disable'
        self.button_previous.place(relx=0.35, rely=0.9)

        # helper to show flow chart
        self.quit_button = ttk.Button(self.frame1, padding=1, text='OK', width=15, command=self.close_windows)
        self.quit_button.place(relx=0.8, rely=1)

    def move_next(self):
        self.images_number += 1
        self.explanation_text_number += 1

        if self.explanation_text_number == (len(self.images)-1):
            print(self.images_number)
            self.button_next['state'] = 'disable'
        else:
            print(self.images_number)
            self.button_previous['state'] = 'enable'

        self.label_explanation_text.configure(text=self.text_captions[self.explanation_text_number])
        self.canvas_formula.place(relx=0.05, rely=0.32)
        self.canvas_formula.itemconfigure(self.image_on_canvas, image=self.images[self.images_number])

        temp_numb = str(self.images_number + 2)
        numb = '%s/4' % temp_numb
        self.label_explanation_order.configure(text=numb)

    def move_previous(self):
        self.images_number -= 1
        self.explanation_text_number -= 1

        if self.explanation_text_number == -1:
            print(self.images_number)
            self.label_explanation_text.configure(text=self.explanation_text)
            self.button_previous['state'] = 'disable'
            self.canvas_formula.place_forget()
        else:
            print(self.images_number)
            self.label_explanation_text.configure(text=self.text_captions[self.explanation_text_number])
            self.canvas_formula.itemconfigure(self.image_on_canvas, image=self.images[self.images_number])
            self.button_next['state'] = 'enable'

        temp_numb = str(self.images_number + 2)
        numb = '%s/4' % temp_numb
        self.label_explanation_order.configure(text=numb)

    def close_windows(self):
        print('>>> Close See Algorithm Dialog\n')
        self.parent.destroy()


"""app = tk.Tk()
AlgorithmDialog(app)
app.mainloop()"""