import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import tkinter.filedialog as fd
import rsa
import os


def choose_directory():
    filetypes = (("Текстовый файл", "*.txt"),
                 ("Изображение", "*.jpg *.gif *.png"),
                 ("Любой", "*"))
    my_file = fd.askopenfile(title="Открыть файл", initialdir="/ИВР",
                             filetypes=filetypes)  # here you can type path to your directory
    if my_file:
        # working with file
        # print(*my_file.readlines())
        my_file.close()


def xor_function(_first_arg_label, _first_arg_entry, _second_arg_label, _second_arg_entry, _result_xor_label):
    """

    :param _first_arg_label:
    :param _first_arg_entry:
    :param _second_arg_label:
    :param _second_arg_entry:
    :param _result_xor_label:
    :return:
    """
    first_arg = _first_arg_entry.get()
    if len(first_arg) != 0:
        try:
            first_arg = str(first_arg)
        except ValueError:
            messagebox.showwarning('Warning!', 'Please, type your text')
            _first_arg_entry.delete(0, tk.END)
            return
    else:
        messagebox.showwarning('Warning!', 'Please, type your text')
        _first_arg_entry.delete(0, tk.END)
        return
    second_arg = _second_arg_entry.get()
    if len(second_arg) != 0:
        try:
            second_arg = str(second_arg)
        except ValueError:
            messagebox.showwarning('Warning!', 'Please, type your key')
            _second_arg_entry.delete(0, tk.END)
            return
    else:
        messagebox.showwarning('Warning!', 'Please, type your key')
        _second_arg_entry.delete(0, tk.END)
        return
    first_arg_text = f"Your text is <{first_arg}>"
    _first_arg_label.configure(text=first_arg_text)
    _first_arg_entry.delete(0, tk.END)
    second_arg_text = f"Your key is <{second_arg}>"
    _second_arg_label.configure(text=second_arg_text)
    _second_arg_entry.delete(0, tk.END)
    result_xored = []
    for i in range(len(first_arg)):
        # additional check print(hex(ord(first_arg[i % len(first_arg)])))
        xored_arg = ord(first_arg[i % len(first_arg)]) ^ ord(
            second_arg[i % len(second_arg)])  # additional check ^ ord(second_arg[i % len(second_arg)])
        result_xored.append(hex(xored_arg)[2:])
    result_output = ' '.join(result_xored)
    _result_xor_label.delete(0, tk.END)
    _result_xor_label.insert(0, result_output)
    # _result_xor_label.configure(text=f'The result of XOR function is {result_output}')


def replacement_function(_first_arg_label, _first_arg_entry, _second_arg_label, _second_arg_entry,
                         _result_repl_label):
    """
    :param _first_arg_label:
    :param _first_arg_entry:
    :param _second_arg_label:
    :param _second_arg_entry:
    :param _result_repl_label:
    :return:
    """
    first_arg = _first_arg_entry.get()
    if len(first_arg) != 0:
        try:
            first_arg = str(first_arg)
        except ValueError:
            messagebox.showwarning('Warning!', 'Please, type your text')
            _first_arg_entry.delete(0, tk.END)
            return
    else:
        messagebox.showwarning('Warning!', 'Please, type your text')
        _first_arg_entry.delete(0, tk.END)
        return
    second_arg = _second_arg_entry.get()
    if len(second_arg) != 0:
        try:
            second_arg = int(second_arg)
        except ValueError:
            messagebox.showwarning('Warning!', 'Please, type your number')
            _second_arg_entry.delete(0, tk.END)
            return
    else:
        messagebox.showwarning('Warning!', 'Please, type your number')
        _second_arg_entry.delete(0, tk.END)
        return
    first_arg_text = f"Your text is ~~{first_arg}~~"
    _first_arg_label.configure(text=first_arg_text)
    _first_arg_entry.delete(0, tk.END)
    second_arg_text = f"Your number is ~~{second_arg}~~"
    _second_arg_label.configure(text=second_arg_text)
    _second_arg_entry.delete(0, tk.END)
    result_repl = []
    check = False
    for i in range(len(first_arg)):
        repl_arg = ord(first_arg[i]) + int(second_arg)  # Adding given number to the unicode number of each symbol
        if repl_arg < 0 or repl_arg > 917999:
            check = True
            break
        result_repl.append(chr(repl_arg))
    if check:
        messagebox.showwarning('Warning!', 'Incorrect number. Result is out of Unicode table')
        _second_arg_entry.delete(0, tk.END)
        return
    result_output = ''.join(result_repl)
    _result_repl_label.delete(0, tk.END)
    _result_repl_label.insert(0, result_output)
    # _result_repl_label.configure(text=f'The result of Replacement function is {result_output}')


def swap_texts(message, result):
    crypto = result['text']  # .get(1.0, tk.END)
    message.delete(1.0, tk.END)
    message.insert(1.0, crypto)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # settings for the window
        self.title('Cryptography')
        self.geometry('700x500+10+10')
        self.protocol("WM_DELETE_WINDOW", lambda: self.exit_function())

        # some variables
        self.function_number = -1
        self.status = 1

        # generating keys
        (pubkey, privkey) = rsa.newkeys(512)
        self.pubkey = pubkey
        self.privkey = privkey

        # creating menu
        menu = tk.Menu(self)

        # different tabs
        # file tab
        file = Menu(menu, tearoff=0)
        file.add_command(label='Uploading file', command=lambda: choose_directory())
        file.add_separator()
        file.add_command(label='Exit', command=lambda: self.exit_function())  # add messagebox to exit

        # choose function tab
        choosing_function = Menu(menu, tearoff=0)
        choosing_function.add_command(label='Home', command=lambda: self.update_current_function(0))
        choosing_function.add_separator()
        choosing_function.add_command(label='XOR', command=lambda: self.update_current_function(1))
        choosing_function.add_separator()
        choosing_function.add_command(label='Replacement', command=lambda: self.update_current_function(2))
        choosing_function.add_separator()
        choosing_function.add_command(label='RSA', command=lambda: self.update_current_function(3))
        choosing_function.add_separator()
        choosing_function.add_command(label='Табличный алгоритм', command=lambda: self.update_current_function(4))

        # adding tabs to menu
        menu.add_cascade(label='File', menu=file)
        menu.add_cascade(label='Choose function', menu=choosing_function)

        # adding menu to window
        self.config(menu=menu)

        # running program
        self.mainloop()

    def exit_function(self):
        try:
            os.remove('Keys.txt')  # your working directory
            self.destroy()
        except FileNotFoundError:
            self.destroy()

    def update_current_function(self, _function_number):
        if self.function_number != _function_number:
            self.destroy_everything()
            self.function_number = _function_number
            if self.function_number == 0:
                self.home_show()
            elif self.function_number == 1:
                self.xor_show()
            elif self.function_number == 2:
                self.replacement_show()
            elif self.function_number == 3:
                self.rsa_show()
            elif self.function_number == 4:
                self.table_algorithm_show()

    def destroy_everything(self):
        for widget in self.winfo_children():
            if widget.winfo_name() != '!menu':
                widget.destroy()
                # print(widget.winfo_name())

    def upload_file(self):
        btn_dir = tk.Button(self, text="Выбрать папку",
                            command=choose_directory)
        btn_dir.pack()

    def home_show(self):
        welcome = tk.Label(
            self,
            text='Hello, world!\n'
                 'Welcome to my application for Cryptography :)\n'
                 'Here you can have some practise in it...',
        )

        welcome.pack()

    def xor_show(self):
        header_label = tk.Label(
            self,
            text="XOR between 2 strings",
            pady=10,
        )
        first_arg_label = tk.Label(
            self,
            text="Write down text",
            pady=10,
        )
        first_arg_entry = tk.Entry(
            self,
            fg="white",
            bg="blue",
            width=80,
        )
        second_arg_label = tk.Label(
            self,
            text="Write down the key",
            pady=10,
        )
        second_arg_entry = tk.Entry(
            self,
            fg="white",
            bg="blue",
            width=80,
        )
        result_label = tk.Entry(
            self,
            text='',
            width=80,
        )
        separate1 = tk.Label(
            self,
            pady=5,
            text='',
        )
        separate2 = tk.Label(
            self,
            pady=5,
            text='',
        )
        function = tk.Button(
            self,
            text="Calculate the result",
            command=lambda: xor_function(first_arg_label, first_arg_entry, second_arg_label, second_arg_entry,
                                         result_label),
        )

        header_label.pack()
        first_arg_entry.focus()
        first_arg_label.pack()
        first_arg_entry.pack()
        second_arg_label.pack()
        second_arg_entry.pack()
        separate1.pack()
        function.pack()
        separate2.pack()
        result_label.pack()

    def replacement_show(self):
        header_label = tk.Label(
            self,
            text="Replacement with Unicode",
            pady=10,
        )
        first_arg_label = tk.Label(
            self,
            text="Write down text",
            pady=10,
        )
        first_arg_entry = tk.Entry(
            self,
            fg="white",
            bg="blue",
            width=80,
        )
        second_arg_label = tk.Label(
            self,
            text="Write down the number",
            pady=10,
        )
        second_arg_entry = tk.Entry(
            self,
            fg="white",
            bg="blue",
            width=80,
        )
        result_label = tk.Entry(
            self,
            text='',
            width=80,
        )
        separate1 = tk.Label(
            self,
            pady=5,
            text='',
        )
        separate2 = tk.Label(
            self,
            pady=5,
            text='',
        )
        function = tk.Button(
            self,
            text="Calculate the result",
            command=lambda: replacement_function(first_arg_label, first_arg_entry, second_arg_label,
                                                 second_arg_entry,
                                                 result_label),
        )

        header_label.pack()
        first_arg_entry.focus()
        first_arg_label.pack()
        first_arg_entry.pack()
        second_arg_label.pack()
        second_arg_entry.pack()
        separate1.pack()
        function.pack()
        separate2.pack()
        result_label.pack()

    def rsa_show(self):
        header_label = tk.Label(
            self,
            text='Rsa encryption',
            pady=10,
        )
        button_generating_keys = tk.Button(self, text='Сгенерировать пару ключей',
                                           command=lambda: self.generating_keys(button_generating_keys))

        header_label.pack()
        button_generating_keys.pack()

    def generating_keys(self, button_generating_keys):
        button_generating_keys['state'] = 'disable'

        self.working_with_keys()
        # pubkey and privkey in console
        # print(pubkey_pem)
        # print(privkey_pem)

    def working_with_keys(self):
        keys_file = open("Keys.txt", "w+")
        keys_file.write(
            f"Это твой публичный ключ. Поделись им с друзьями :)\n{self.pubkey.save_pkcs1()}\n"
            f"\nЭто твой приватный ключ. Сохрани его в секрете\n{self.privkey.save_pkcs1()}\n")
        keys_file.close()
        explanation_label = tk.Label(
            self,
            text='Теперь у тебя есть открытый и закртый ключи.\n'
                 'Они сохранились в папку, из которой была запущена эта программа.\n'
                 'Найди и открой этот файл, он тебе понадобится.',
            pady=10,
        )
        message_label = tk.Label(
            self,
            text='Введите сообщение которое хотите зашифровать / расшифровать',
            pady=5
        )
        message_text = tk.Text(
            self,
            width=40,
            height=7,
        )
        drop_down_encryption_list = [
            "Зашифровать",
            "Расшифровать",
        ]

        # result_text = tk.Text(
        #     self,
        #     width=40,
        #     height=7,
        # )

        def callback(*args):
            result_label.configure(text=f'Результутат команды {variable.get()}')
            # print(variable.get())
            if variable.get() == 'Зашифровать':
                self.encryption(message_text.get(1.0, tk.END), result)
            elif variable.get() == 'Расшифровать':
                self.decryption(message_text.get(1.0, tk.END), result)

        result_label = tk.Label(self, pady=5, text=f'Здесь будет твой ответ')
        result = tk.Label(self, pady=5, text=f'Some text')
        variable = tk.StringVar(self)
        variable.set(drop_down_encryption_list[0])  # default value
        variable.trace("w", callback)

        drop_down_encryption_menu = tk.OptionMenu(self, variable, *drop_down_encryption_list)
        result_button = tk.Button(self, text='Поменять',
                                  command=lambda: swap_texts(message_text, result))

        scroll = tk.Scrollbar(command=message_text.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)

        message_text.config(yscrollcommand=scroll.set)

        explanation_label.pack()
        message_label.pack()
        message_text.pack()
        drop_down_encryption_menu.pack()
        result_label.pack()
        # result_text.pack()
        result.pack()
        result_button.pack()

    def encryption(self, message, result):
        message = message.encode()
        crypto = rsa.encrypt(message, self.pubkey)
        print(crypto)
        # result.delete(1.0, tk.END)
        # result.insert(1.0, crypto)
        result.configure(text=f'{crypto}')

    def decryption(self, crypto, result):  # not working for now
        crypto = crypto.encode()  # need fix
        message = rsa.decrypt(crypto, self.privkey)
        message = message.decode()
        # result.delete(1.0, tk.END)
        # result.insert(1.0, message)
        result.configure(text=f'{message}')

    def table_algorithm_show(self):
        header_label = tk.Label(
            self,
            pady=5,
            text='Это табличный алгоритм',
        )
        main_text_label = tk.Label(
            self,
            pady=5,
            text='Исходный текст',
        )
        separate1 = tk.Label(
            self,
            text='',
        )
        main_text_entry = tk.Entry(self, width=60)
        key_label = tk.Label(self, pady=5, text='Ключ')
        key_entry = tk.Entry(self, width=20)
        canvas = tk.Canvas(self)
        canvas.create_rectangle(
            250, 60, 430, 240,
            outline="#aaf", fill="#aaf"
        )
        result_entry = tk.Entry(self, bg='#aaf', width=60)
        result_button = tk.Button(self, text='Получить результат',
                                  command=lambda: self.working_with_table_algorithm(main_text_entry.get(),
                                                                                    key_entry.get(), result_entry,
                                                                                    canvas_numbers_list,
                                                                                    canvas_symbols_list,
                                                                                    canvas))

        # horizontal lines
        canvas.create_line(250, 59, 430, 59)
        canvas.create_line(250, 241, 430, 241)
        canvas.create_line(250, 90, 430, 90)
        canvas.create_line(250, 120, 430, 120)
        canvas.create_line(250, 150, 430, 150)
        canvas.create_line(250, 180, 430, 180)
        canvas.create_line(250, 211, 430, 211)
        canvas_numbers_list = [0 for j in range(6)]  # key numbers
        canvas_symbols_list = [[0 for j in range(6)] for i in range(6)]  # main text symbols
        for i in range(6):
            canvas_numbers_list[i] = canvas.create_text(265 + i * 30, 50, text=f'{i + 1}')
            for j in range(6):
                canvas_symbols_list[i][j] = canvas.create_text(265 + j * 30, 75 + i * 30, text='a')

        # vertical lines
        canvas.create_line(249, 50, 249, 240)
        canvas.create_line(280, 50, 280, 240)
        canvas.create_line(310, 50, 310, 240)
        canvas.create_line(340, 50, 340, 240)
        canvas.create_line(370, 50, 370, 240)
        canvas.create_line(400, 50, 400, 240)
        canvas.create_line(431, 50, 431, 240)

        header_label.pack()
        main_text_label.pack()
        main_text_entry.pack()
        key_label.pack()
        key_entry.pack()
        canvas.pack(fill=tk.BOTH)
        result_button.pack()
        separate1.pack()
        result_entry.pack()

    def working_with_table_algorithm(self, main_text, key, result, canvas_numbers_list, canvas_symbols_list, canvas):
        result_str = ''
        for i in range(6):
            canvas.itemconfigure(canvas_numbers_list[i], text=int(key[i]))
            for j in range(6):
                if len(main_text) > i * 6 + j:
                    canvas.itemconfigure(canvas_symbols_list[i][j], text=main_text[i * 6 + j])
                else:
                    canvas.itemconfigure(canvas_symbols_list[i][j], text=' ')
        for i in range(6):
            t = 0
            for j in range(6):
                if int(key[j]) - 1 == i:
                    t = j
                    break
            for j in range(6):
                if len(main_text) > t + j * 6:
                    result_str += main_text[t + j * 6]
        result.delete(0, tk.END)
        result.insert(0, result_str)


if __name__ == '__main__':
    MainWindow()
