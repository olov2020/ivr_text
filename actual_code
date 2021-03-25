import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from tkinter import ttk


class Constants:
    def __init__(self, window, note):
        self.len = 3
        self.func = 0
        self.wind = window
        self.note = note

    def update_cur_func(self, cur_func):
        self.func = cur_func
        self.choose_func()

    def choose_func(self):
        if self.func == 0:
            home_func(self.wind, self.func, self.note)
        elif self.func == 1:
            xor_func(self.wind, self.func, self.note)
        elif self.func == 2:
            repl_func(self.wind, self.func, self.note)


def repl(_first_arg_label, _first_arg_entry, _second_arg_label, _second_arg_entry, _result_repl_label):
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
        messagebox.showwarning('Warning!', 'Incorrect number. Result if out of Unicode table')
        _second_arg_entry.delete(0, tk.END)
        return
    result_output = ''.join(result_repl)
    _result_repl_label.delete(0, tk.END)
    _result_repl_label.insert(0, result_output)
    # _result_repl_label.configure(text=f'The result of Replacement function is {result_output}')


def repl_func(window, const, note):
    header_label = tk.Label(
        window,
        text="Replacement with Unicode",
        pady=10,
    )
    first_arg_label = tk.Label(
        window,
        text="Write down text",
        pady=10,
    )
    first_arg_entry = tk.Entry(
        window,
        fg="white",
        bg="blue",
        width=40,
    )
    second_arg_label = tk.Label(
        window,
        text="Write down the number",
        pady=10,
    )
    second_arg_entry = tk.Entry(
        window,
        fg="white",
        bg="blue",
        width=40,
    )
    result_repl_label = tk.Entry(
        window,
        text='',
        width=100,
    )
    separate1 = tk.Label(
        window,
        pady=5,
        text='',
    )
    separate2 = tk.Label(
        window,
        pady=5,
        text='',
    )
    function = tk.Button(
        window,
        text="Calculate the result",
        command=lambda: repl(first_arg_label, first_arg_entry, second_arg_label, second_arg_entry, result_repl_label),
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
    result_repl_label.pack()

    window.mainloop()


def xor(_first_arg_label, _first_arg_entry, _second_arg_label, _second_arg_entry, _result_xor_label):
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
    first_arg_text = f"Your text is ~~{first_arg}~~"
    _first_arg_label.configure(text=first_arg_text)
    _first_arg_entry.delete(0, tk.END)
    second_arg_text = f"Your key is ~~{second_arg}~~"
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


def xor_func(window, const, note):
    header_label = tk.Label(
        window,
        text="XOR between 2 strings",
        pady=10,
    )
    first_arg_label = tk.Label(
        window,
        text="Write down text",
        pady=10,
    )
    first_arg_entry = tk.Entry(
        window,
        fg="white",
        bg="blue",
        width=40,
    )
    second_arg_label = tk.Label(
        window,
        text="Write down the key",
        pady=10,
    )
    second_arg_entry = tk.Entry(
        window,
        fg="white",
        bg="blue",
        width=40,
    )
    result_xor_label = tk.Entry(
        window,
        text='',
        width=100,
    )
    separate1 = tk.Label(
        window,
        pady=5,
        text='',
    )
    separate2 = tk.Label(
        window,
        pady=5,
        text='',
    )
    function = tk.Button(
        window,
        text="Calculate the result",
        command=lambda: xor(first_arg_label, first_arg_entry, second_arg_label, second_arg_entry, result_xor_label),
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
    result_xor_label.pack()

    window.mainloop()


def home_func(window, const, note):
    """
    notebook tkinter how to swich -> google
    """

    """
    :param window: 
    :param const: 
    :param note: 
    :return: 
    """

    # xor_on_page = ttk.Frame(note)
    # note.add(xor_on_page, text="XOR")
    # note.pack(expand=1, fill='both')
    hi_label = tk.Label(
        window,
        text='Hi, pupil!',
    )
    hi_label.config(font=("Courier", 32))
    hi_label.pack()


def start():
    window = tk.Tk()
    window.geometry("700x500")
    window.title("Добро пожаловать в приложение PythonRu")
    notes = ttk.Notebook(window)
    const = Constants(window, notes)
    menu = Menu(window)

    file = Menu(menu, tearoff=0)
    file.add_command(label='new')
    file.add_separator()
    file.add_command(label='change')

    some_codes = Menu(menu, tearoff=0)
    some_codes.add_command(label='Home', command=lambda: const.update_cur_func(0))
    some_codes.add_separator()
    some_codes.add_command(label='XOR', command=lambda: const.update_cur_func(1))
    some_codes.add_separator()
    some_codes.add_command(label='Replacement', command=lambda: const.update_cur_func(2))

    menu.add_cascade(label='File', menu=file)
    menu.add_cascade(label='Functions', menu=some_codes)
    window.config(menu=menu)

    window.mainloop()


def main():
    # print('Hello, world!')
    start()


if __name__ == '__main__':
    main()
