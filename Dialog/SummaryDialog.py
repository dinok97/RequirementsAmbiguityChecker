from tkinter import ttk
from SrsFile import SrsFile
import tkinter as tk
import tkinter.font as tkfont


class SummaryDialog:

    srs_file = SrsFile('', '', '')
    file_directory = ''
    correction_time = ''
    ambiguous_req = ''
    normal_req = ''
    total_req = ''
    detection_result = ''

    def __init__(self, parent, srs_file):
        print('\n>>> Show Summary Dialog')

        # set the parent window
        self.parent = parent
        self.parent.geometry("800x500")
        self.parent.resizable(width=False, height=False)
        self.parent.title("Kesimpulan")

        # make view focus in this dialog
        # prevent to open other view/dialog before close this dialog
        self.parent.grab_set()

        '''initialize all data to display in dialog'''
        self.srs_file = srs_file
        file_name = self.srs_file.get_file_name()
        self.file_directory = file_name[0:42]+". . ."
        self.correction_time = self.srs_file.get_correction_time()
        self.total_req = self.srs_file.get_total_req()
        self.normal_req = self.srs_file.get_normal_req()
        self.ambiguous_req = self.srs_file.get_ambiguous_req()
        self.detection_result = self.srs_file.get_detection_result()

        # set the grid size of parent window
        for r in range(20):
            self.parent.rowconfigure(r, weight=1)
        for c in range(25):
            self.parent.columnconfigure(c, weight=1)

        # help adjust the view
        space_1 = tk.Label(self.parent, text="-------------", fg="#f0f0f0")
        space_1.grid(row=0, column=1)
        space_2 = tk.Label(self.parent, text="-------------", fg="#f0f0f0")
        space_2.grid(row=6, column=1)

        """set the frame_1
        frame that contain information about SRS Document"""
        self.frame_1 = tk.Frame(self.parent, bg="white", highlightbackground="#2369B2", highlightthickness=2)
        self.frame_1.grid(row=1, column=1, rowspan=2, columnspan=11, sticky='WENS', padx=(20, 0))

        # frame_1 content
        # label that show information SRS directory
        self.label_file_name = ttk.Label(self.frame_1, text=('Direktori File    : %s' % self.file_directory), background='white', font='Calibri 10')
        self.label_file_name.place(relx=0.05, rely=0.15)

        # frame_1 content
        # label that show detection time of SRS
        self.label_detection_time = ttk.Label(self.frame_1, text=('Waktu Koreksi : %s' %self.correction_time), background='white', font='Calibri 10')
        self.label_detection_time.place(relx=0.05, rely=0.5)

        """set the frame_2
        frame that contain number of total requirements in SRS document"""
        self.frame_2 = tk.Frame(self.parent, bg="white", highlightbackground="#2369B2", highlightthickness=2)
        self.frame_2.grid(row=4, column=1, rowspan=2, columnspan=11, sticky='WENS', padx=(20, 0))

        # frame_2 content
        # label that show direction
        self.label_total_rec = ttk.Label(self.frame_2, text='Total Kebutuhan Sistem: ', background='white', font='Calibri 12')
        self.label_total_rec.place(relx=0.05, rely=0.25)

        # frame_2 content
        # label that show number of total requirements in SRS document (in blue color)
        self.label_number_rec = ttk.Label(self.frame_2, text=str(self.total_req), background='white', font='Calibri 30 bold')
        self.label_number_rec.configure(foreground='#2369B2')  # blue
        self.label_number_rec.place(relx=0.70, rely=0)

        """ set the frame_3
        frame that contain number of normal (non ambiguous) requirements """
        self.frame_3 = tk.Frame(self.parent, bg="white", highlightbackground="#2369B2", highlightthickness=2)
        self.frame_3.grid(row=1, column=13, rowspan=5, columnspan=5, sticky='WENS')

        # frame_3 content
        # label that show direction
        self.label_normal_rec = ttk.Label(self.frame_3, text='Kebutuhan tidak\n        ambigu: ', background='white', font='Calibri 10')
        self.label_normal_rec.grid(row=0, column=0)

        # frame_3 content
        # label that show number of normal (non ambiguous) requirements in SRS document (in green color)
        self.label_number_normal_rec = ttk.Label(self.frame_3, text=str(self.normal_req), background='white', font='Calibri 50 bold')
        self.label_number_normal_rec.configure(foreground='#16A345')  # green
        self.label_number_normal_rec.grid(row=1, column=0)

        # configure grid for frame_3
        self.frame_3.columnconfigure(0, weight=1)
        self.frame_3.rowconfigure(0, weight=1)
        self.frame_3.rowconfigure(1, weight=2)

        """ set the frame_4
        frame that contain number of ambiguous requirements """
        self.frame_4 = tk.Frame(self.parent, bg="white", highlightbackground="#2369B2", highlightthickness=2)
        self.frame_4.grid(row=1, column=19, rowspan=5, columnspan=5, sticky='WENS', padx=(0, 20))

        # frame_4 content
        # label that show direction
        self.label_ambiguous_rec = ttk.Label(self.frame_4, text='Kebutuhan ambigu: ', background='white',
                                             font='Calibri 10')
        self.label_ambiguous_rec.grid(row=0, column=0)

        # frame_4 content
        # label that show number of ambiguous requirements in SRS document (in red color)
        self.label_number_ambiguous_rec = ttk.Label(self.frame_4, text=str(self.ambiguous_req), background='white', font='Calibri 50 bold')
        self.label_number_ambiguous_rec.configure(foreground='#D3282D')  # red
        self.label_number_ambiguous_rec.grid(row=1, column=0, pady=(10, 0))

        # configure grid for frame_4
        self.frame_4.columnconfigure(0, weight=1)
        self.frame_4.rowconfigure(0, weight=1)
        self.frame_4.rowconfigure(1, weight=2)

        """label to show table name"""
        self.label_table_name = ttk.Label(self.parent, text='Tabel Kebutuhan Ambigu', font='Calibri 12 bold')
        self.label_table_name.grid(row=7, column=0, columnspan=25)

        """this is try data"""
        self.table_header = ['No.', 'Kode', 'Kalimat Kebutuhan', 'Ambiguitas', 'Pola Ambigu', 'Rekomendasi']
        self.car_list = [
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-'],
            ['1', 'FR-RAC-01-01',
             'Sistem dapat menampilkan data 10 pengguna dengan nilai tertinggi dalam rentang waktu 1 bulan', '-', '-',
             '-']
        ]

        self.tree = ttk.Treeview(self.parent, columns=self.table_header, show="headings")
        self.tree.column(self.table_header[0], minwidth=0, width=20, stretch=False)
        self.tree.column(self.table_header[1], minwidth=100, width=20, stretch=False)
        self.tree.column(self.table_header[2], minwidth=0, width=100, stretch=False)
        self.tree.column(self.table_header[3], minwidth=0, width=20, stretch=False)
        self.tree.column(self.table_header[4], minwidth=0, width=20, stretch=False)
        self.tree.column(self.table_header[5], minwidth=0, width=20, stretch=False)
        vsb = ttk.Scrollbar(self.parent, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.parent, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=8, column=1, rowspan=11, columnspan=23, sticky='NSEW', in_=self.parent, padx=(0, 15))
        vsb.grid(row=8, column=23, rowspan=11, sticky='NSE', in_=self.parent)
        hsb.grid(row=19, column=1, columnspan=23, sticky='NEW', in_=self.parent, padx=(0, 15))

        # setup table header
        for col in self.table_header:
            self.tree.heading(col, text=col.title())  # anchor=tk.W,
            # command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col, width=tkfont.Font().measure(col.title()))

        for item in self.detection_result:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(self.table_header[ix], width=None) < col_w:
                    self.tree.column(self.table_header[ix], width=col_w)
        self.tree.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        print('click')


'''data = [['kode', 'kalimat'], ['kode', 'kalimat']]
aa = SrsFile("Ini file", "Kamis", data)
app = tk.Tk()
SummaryDialog(app, aa)
app.mainloop()'''