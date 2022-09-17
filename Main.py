import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as mbox
from datetime import datetime
from FileExtraction import ExtractFile
from FileSaving import ExportFile
from Dialog.SystemGuideDialog import SystemGuideDialog
from Dialog.AlgorithmDialog import AlgorithmDialog
from Dialog.SummaryDialog import SummaryDialog
from Dialog.DetailRequirementsDialog import DetailRequirementsDialog
from Detection import *

LARGE_FONT = ("Verdana", 12)
FONT_STYLE_HEADER = "Helvetica 18 bold"
FONT_STYLE_NORMAL = "Helvetica 12 bold"
FONT_STYLE_DIRECTORY = "Helvetica 10"

doc_flag = 0
file_name = "tidak ada berkas SKPL"


class MainController(tk.Tk):

    srs_file = SrsFile
    file_name = ''

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        self.geometry("1200x650")
        self.title("Requrements Ambiguity Checker")

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomeView, MainView):
            self.frame = F(container, self)
            self.frames[F] = self.frame
            self.frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomeView)

    def show_frame(self, cont):
        self.frame = self.frames[cont]
        self.frame.tkraise()
        if cont == MainView:
            self.frame.setup_menu()
            self.show_directory()
            self.change_status_bar("  Main  |   Silahkan Ekstrak Dokumen SKPL Anda")

    def open_file(self):
        global file_name
        global doc_flag
        self.file_name = FileDialog.askopenfilename(title="Pilih Dokumen SKPL", filetypes=(("doc files", "*.doc*"), ("docx files", "*.docx*")))
        file_name = self.file_name

        if file_name != '':
            self.show_directory()
            self.change_status_bar("  Main  |   Silahkan Ekstrak Dokumen SKPL Anda")
        else:
            self.set_warning_message("Tidak ada dokumen SKPL yang dipilih")

    def extract_file(self):
        global file_name
        extract_file = ExtractFile(file_name)
        extract_file.start_extraction()
        extraction_result = extract_file.get_extraction_result()

        if extraction_result != "table not found":
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y - %H:%M:%S")

            self.srs_file = SrsFile(file_name, date_time, extraction_result)
            requirement_list = self.srs_file.get_detection_result()
            self.insert_data_to_table(requirement_list)
            self.change_status_bar("  Main  |   Ekstraksi berhasil. Silahkan mulai deteksi")

        else:
            self.frame.clear_table_data()
            self.set_error_message("Tabel spesifikasi kebutuhan tidak ditemukan dalam dokumen. Pastikan dokumen yang inputkan adalah dokumen SKPL dan ditulis dalam bahasa Indonesia")
            self.set_warning_message("Tabel spesifikasi kebutuhan tidak ditemukan dalam dokumen")

    def detection(self):
        # if file is still default
        if self.srs_file == SrsFile:
            self.set_warning_message("Lakukan ekstraksi dokumen SKPL terlebih dahulu untuk mendapatkan daftar kalimat kebutuhan perangkat lunak")
        else:
            t_start = datetime.now()
            rule_base = RuleBaseDetection(self.srs_file.get_detection_result())
            rule_base.set_rule('Rule\\rule_real.xml')
            rule_base.start_detection()
            rule_base_result = rule_base.get_detection_result()

            self.change_status_bar("Deteksi sedang berlangsung. . .")

            statistical_base = StatisticalBaseRecommendation(rule_base_result)
            statistical_base.set_corpus("Corpus\\leipzig_indonesia.txt")
            statistical_base.start_recommendation()
            statistical_base_result = statistical_base.get_recommendation_result()

            self.srs_file.update_detection_result(statistical_base_result)
            self.insert_data_to_table(self.srs_file.get_detection_result())
            self.frame.show_success_message("Deteksi Selesai")

            t_finish = datetime.now()
            det_time = (t_finish - t_start) // 1000
            det_time = det_time.microseconds // 1000
            self.change_status_bar("  Home  |  Deteksi selesai -- Waktu deteksi: %s detik" % det_time)

    def export_file(self):
        save_file_name = FileDialog.asksaveasfilename(title="Pilih Lokasi Penyimpanan File", filetypes=(("docx files", "*.docx*"), ("pdf files", "*.pdf")))
        if save_file_name != "":
            print("Direktori File: %s" % save_file_name)
            export_file = ExportFile(save_file_name, self.srs_file)
            export_file.start_export_file()
            export_file.save_file()
            self.set_success_message("File berhasil disimpan di" + save_file_name)

        else:
            print("Cancel Export File")
            self.set_warning_message("Anda Tidak menulis nama fiel")
            return

    def insert_data_to_table(self, requirement_list):
        self.frame.build_table(requirement_list)

    def set_error_message(self, message):
        self.frame.show_error_message(message)

    def set_success_message(self, message):
        self.frame.show_success_message(message)

    def set_warning_message(self, message):
        self.frame.show_warning_message(message)

    def show_directory(self):
        self.frame.show_directory()

    def change_status_bar(self, status):
        self.frame.show_status_bar(status)


class HomeView(tk.Frame):

    file_name = ''

    label_title = ''
    label_doc_name = ''
    button_browse_doc = ''
    button_next = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button_style = ttk.Style()
        button_style.map("C.TButton", foreground=[('pressed', 'black'), ('active', 'blue')],
                         background=[('pressed', '!disabled', 'blue'), ('active', 'blue')])

        self.label_title = ttk.Label(self, text="Requirements Ambiguity Checker", font=FONT_STYLE_HEADER)
        self.label_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label_doc_name = ttk.Label(self, text="-Belum ada dokumen yang dipilih-")
        self.label_doc_name.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.button_browse_doc = ttk.Button(self, padding=6, style="C.TButton", text="Pilih Berkas", command=self.open_file, width=20)
        self.button_browse_doc.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.button_next = ttk.Button(self, padding=5, style="C.TButton", text="Lanjutkan>>", command=lambda: controller.show_frame(MainView), width=20)
        self.button_next.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.button_next["state"] = "disable"

    def open_file(self):
        global file_name
        global doc_flag

        self.file_name = FileDialog.askopenfilename(title="Pilih Dokumen SKPL", filetypes=(("doc files", "*.doc*"), ("docx files", "*.docx*")))
        file_name = self.file_name

        if file_name != '':
            doc_flag = 1
            self.button_next["state"] = "enable"
        else:
            doc_flag = 0
            mbox.showwarning("Perhatian", "Tidak ada dokumen SKPL yang dipilih")
        self.change_label_doc_name()

    def change_label_doc_name(self):
        if doc_flag:
            doc_name = "Dokumen yang Anda pilih: " + file_name
        else:
            doc_name = "- Pilih dokumen SKPL terlebih dahulu -"
        self.label_doc_name.config(text=doc_name)


class MainView(tk.Frame):

    parent = ""
    controller = ""
    table_header = []
    table_content = []
    menu_bar = ""
    tree_table = ""

    label_title = ""
    label_error = ""
    label_directory = ""
    entry_directory = ""
    entry_error = ""

    button_show_directory = ""
    button_extract_file = ""
    button_run_detection = ""
    button_generate_conclution = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # initialize file name
        self.file_name = ''

        # initialize the Frame
        self.parent = parent

        # initialize the controller
        self.controller = controller

        # initialize table header
        self.table_header = ['No.', 'Kode', 'Kalimat Kebutuhan', 'Ambiguitas', 'Pola Ambigu', 'Rekomendasi Perbaikan']

        # initialize table
        self.init_table()

        self.label_title = ttk.Label(self, text="Requirements Ambiguity Checker", font=FONT_STYLE_HEADER)
        self.label_title.grid(column=0, row=0, columnspan=3)

        self.label_directory = ttk.Label(self, text="Direktori File: ", font=FONT_STYLE_NORMAL)
        self.label_directory.grid(column=0, row=1, sticky="E")

        self.entry_directory = ttk.Entry(self, font=FONT_STYLE_DIRECTORY, width=85)
        self.entry_directory.grid(column=1, row=1)

        self.button_show_directory = ttk.Button(self, padding=3, text="Lihat Direktori", width=20, command=self.show_directory)
        self.button_show_directory.grid(column=2, row=1, sticky="W")

        self.button_extract_file = ttk.Button(self, padding=3, text="Ekstrak Dokumen", width=20, command=lambda: controller.extract_file())
        self.button_extract_file.grid(column=0, row=2, sticky="E")

        self.button_run_detection = ttk.Button(self, padding=3, text="Mulai Deteksi", width=20, command=lambda: controller.detection())
        self.button_run_detection.grid(column=1, row=2)

        self.button_generate_conclution = ttk.Button(self, padding=3, text="Rangkuman", width=20, command=self.show_summary)
        self.button_generate_conclution.grid(column=2, row=2, sticky="W")

        self.label_error = ttk.Label(self, text="Pesan Eror", font=FONT_STYLE_NORMAL)
        self.label_error.grid(column=0, row=5, sticky="WNS", padx=25)

        self.entry_error = ttk.Entry(self, text="Pesan Eror", width=100)
        self.entry_error.grid(column=0, row=6, columnspan=3, sticky="NSEW", padx=25, pady=(0, 20))

        self.status_bar = Label(self.controller, text="  Home  |   Silahkan Pilih Dokumen SKPL Anda", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=5)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=2)

    def show_directory(self):
        global file_name
        self.entry_directory.delete(0, 'end')
        self.entry_directory.insert(0, file_name)
        # self.entryDirectory["state"] = "disable"

    def setup_menu(self):
        self.menu_bar = Menu(self)
        file_menu = Menu(self.menu_bar)
        file_menu.add_command(label="Buka Berkas SKPL", command=lambda: self.controller.open_file())
        file_menu.add_command(label="Riwayat", command=self.print_hello)
        file_menu.add_separator()
        file_menu.add_command(label="Rilis Hasil Deteksi", command=lambda: self.controller.export_file())
        self.menu_bar.add_cascade(label="Utama", menu=file_menu)

        help_menu = Menu(self.menu_bar)
        help_menu.add_command(label="Panduan Pengguna", command=self.show_system_guide)
        help_menu.add_command(label="Lihat Algoritme", command=self.show_system_algorithm)
        help_menu.add_separator()
        help_menu.add_command(label="Keluar", command=self.print_hello)
        self.menu_bar.add_cascade(label="Bantuan", menu=help_menu)

        self.controller.config(menu=self.menu_bar)

    def show_system_guide(self):
        new_window = tk.Toplevel(self.controller)
        SystemGuideDialog(new_window)

    def show_system_algorithm(self):
        new_window = tk.Toplevel(self.controller)
        AlgorithmDialog(new_window)

    def show_detail_requirements(self, data):
        new_window = tk.Toplevel(self.controller)
        DetailRequirementsDialog(new_window, data)

    def show_summary(self):
        new_window = tk.Toplevel(self.controller)
        SummaryDialog(new_window, self.controller.srs_file)

    def init_table(self):
        self.tree_table = ttk.Treeview(self, columns=self.table_header, show="headings")
        self.tree_table.column(self.table_header[0], minwidth=0, width=20, stretch=False)
        self.tree_table.column(self.table_header[1], minwidth=100, width=20, stretch=False)
        self.tree_table.column(self.table_header[2], minwidth=0, width=100, stretch=False)
        self.tree_table.column(self.table_header[3], minwidth=0, width=20, stretch=False)
        self.tree_table.column(self.table_header[4], minwidth=0, width=20, stretch=False)
        self.tree_table.column(self.table_header[5], minwidth=0, width=20, stretch=False)
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree_table.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree_table.xview)
        self.tree_table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_table.grid(column=0, row=3, columnspan=3, sticky='NSEW', in_=self, padx=(25, 35), pady=(20, 0))
        vsb.grid(column=2, row=3, sticky='NSE', in_=self, padx=(0, 20), pady=(20, 0))
        hsb.grid(column=0, row=4, columnspan=3, sticky='NEW', in_=self, padx=(25, 40))

        # setup table header
        for col in self.table_header:
            self.tree_table.heading(col, text=col.title())  # anchor=tk.W,
            # command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree_table.column(col, width=tkfont.Font().measure(col.title()))

    def build_table(self, data_list):
        self.table_content = data_list

        '''print('table contents %s' % self.table_content)
        print('normal req %s' % self.srs_file.get_normal_req())
        print('amb req %s' % self.srs_file.get_ambiguous_req())
        print('total req %s' % self.srs_file.get_total_req())'''

        x = self.tree_table.get_children()
        for item in x:
            self.tree_table.delete(item)

        for item in self.table_content:
            self.tree_table.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self.tree_table.column(self.table_header[ix], width=None) < col_w:
                    self.tree_table.column(self.table_header[ix], width=col_w)
        self.tree_table.bind("<Double-1>", self.on_item_double_click)

    def clear_table_data(self):
        self.tree_table.delete(*self.tree_table.get_children())

    @staticmethod
    def show_success_message(message):
        mbox.showinfo("Informasi", message)

    @staticmethod
    def show_warning_message(message):
        mbox.showwarning("Perhatian", message)

    def show_error_message(self, message):
        self.entry_error.delete(0, 'end')
        self.entry_error.insert(0, message)

    def show_status_bar(self, status):
        self.status_bar.config(text=status)
        self.status_bar.update_idletasks()

    def on_item_double_click(self, event):
        data = []
        item = self.tree_table.selection()

        for i in item:
            print("\nuser clicked on", self.tree_table.item(i, "values")[0])
            j = int(self.tree_table.item(i, "values")[0])
            data = self.controller.srs_file.get_detection_result(j)
            print(self.controller.srs_file.get_detection_result(j))

        self.show_detail_requirements(data)

    # to remove
    @staticmethod
    def print_hello():
        print("Hello")


if __name__ == '__main__':
    app = MainController()
    app.mainloop()
