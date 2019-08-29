from tkinter import ttk
from tkinter import Canvas
import tkinter as tk


class DetailRequirementsDialog:

    parent = ""
    id_req = ""
    requirement = ""
    ambiguity = ""
    ambiguity_location = ""
    recommendation = ""

    def __init__(self, parent, req_data):
        print('\n>>> Show Detail Requirements Dialog')

        # set the parent window
        self.parent = parent
        self.parent.geometry("600x400")
        self.parent.resizable(width=False, height=False)
        self.parent.title("Detail Hasil Deteksi")

        # make view focus in this dialog
        # prevent to open other view/dialog before close this dialog
        self.parent.grab_set()

        # initialize all data to display
        if req_data[3] == '-':
            req_data[3] = 'Tidak Ambigu'
        self.id_req = req_data[1]
        self.requirement = req_data[2]
        self.ambiguity = req_data[3]
        self.ambiguity_location = req_data[4]
        self.recommendation = req_data[5]

        ''' field 1
        show the label and data about requirements ID'''
        self.label_id_req = ttk.Label(self.parent, text='Kode Kebutuhan :', font='Calibri 12')
        self.label_id_req.place(relx=0.05, rely=0.05)

        self.text_id_req = ttk.Label(self.parent, text=self.id_req, font='Calibri 12 bold')
        self.text_id_req.configure(foreground='#2369B2')  # blue
        self.text_id_req.place(relx=0.05, rely=0.1)

        canvas = Canvas(parent, width=540, height=1, borderwidth=0, highlightthickness=0, bg="grey")
        canvas.place(relx=0.05, rely=0.17)

        ''' field 2
        show the label and data about requirements sentences'''
        self.label_req_sentences = ttk.Label(self.parent, text='Kalimat Kebutuhan :', font='Calibri 12')
        self.label_req_sentences.place(relx=0.05, rely=0.2)

        self.text_rec_sentences = tk.Text(parent, height=3, width=67, bg='#f0f0f0', font='Calibri 12 bold', fg='#2369B2')
        self.text_rec_sentences.place(relx=0.05, rely=0.26)
        self.text_rec_sentences.insert(tk.END, self.requirement)

        ''' field 3
        show the label and data about is ambiguous or not'''
        self.label_ambiguity = ttk.Label(self.parent, text='Ambiguitas :', font='Calibri 12')
        self.label_ambiguity.place(relx=0.05, rely=0.45)

        self.text_ambiguity = ttk.Label(self.parent, text=self.ambiguity, font='Calibri 12 bold')
        self.text_ambiguity.configure(foreground='#2369B2')  # blue
        self.text_ambiguity.place(relx=0.05, rely=0.5)

        canvas = Canvas(parent, width=540, height=1, borderwidth=0, highlightthickness=0, bg="grey")
        canvas.place(relx=0.05, rely=0.57)

        '''field 4
        show the label and data about word that cause ambiguous to the requirements'''
        self.label_ambiguity_location = ttk.Label(self.parent, text='Letak Ambiguitas :', font='Calibri 12')
        self.label_ambiguity_location.place(relx=0.05, rely=0.6)

        self.text_ambiguity_location = ttk.Label(self.parent, text=self.ambiguity_location, font='Calibri 12 bold')
        self.text_ambiguity_location.configure(foreground='#2369B2')  # blue
        self.text_ambiguity_location.place(relx=0.05, rely=0.65)

        canvas = Canvas(parent, width=540, height=1, borderwidth=0, highlightthickness=0, bg="grey")
        canvas.place(relx=0.05, rely=0.72)

        '''field 5
        show the label and data about recommendation to fix the ambiguous'''
        self.label_recommendation = ttk.Label(self.parent, text='Rekomendasi Perbaikan :', font='Calibri 12')
        self.label_recommendation.place(relx=0.05, rely=0.75)

        self.text_recommendation = tk.Text(parent, height=3, width=67, bg='#f0f0f0', font='Calibri 12 bold', fg='#2369B2')
        self.text_recommendation.place(relx=0.05, rely=0.81)
        self.text_recommendation.insert(tk.END, self.recommendation)


'''data = [['kode', 'kalimat'], ['kode', 'kalimat ini kalimat untuk percobaan saja']]
aa = SrsFile("Ini file", "Kamis", data)
bb = aa.get_detection_result(2)
app = tk.Tk()
DetailRequirementsDialog(app, bb)
app.mainloop()'''