import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import tkinter.filedialog as fd
import rsa
import os

"""
Done
1) XOR works well now
2) Replacement works well now
3) RSA need some fixes
4) Table algorithm:
    showing works well
    result works well
    (4, 5, 6) works well
5) Full commented code
    
Need to do:
1) Design
2) Cheats for table
3) Files for table
4) Home page
5) My page
"""


def choose_directory():  # uploading file
    filetypes = (("Текстовый файл", "*.txt"),
                 ("Любой", "*.png"))
    my_file = fd.askopenfile(title="Открыть файл", initialdir="/TestApp",
                             filetypes=filetypes)  # here you can type path to your directory
    if my_file:  # if file is open
        # working with file
        # print(*my_file.readlines())
        return my_file.read()
    return ''


def xor_function(_first_arg_entry, _second_arg_entry, _result_entry):  # working on xor result
    first_arg = _first_arg_entry.get()
    second_arg = _second_arg_entry.get()

    # all necessary checks
    if first_arg == '':
        messagebox.showwarning('Warning!', 'Please, type your text')
        _first_arg_entry.delete(0, tk.END)
        _first_arg_entry.focus()
        return
    if second_arg == '':
        messagebox.showwarning('Warning!', 'Please, type your text')
        _second_arg_entry.delete(0, tk.END)
        _second_arg_entry.focus()
        return
    result_list = []
    for i in range(len(first_arg)):
        xored_arg = ord(first_arg[i % len(first_arg)]) ^ ord(second_arg[i % len(second_arg)])
        # additional check ^ ord(second_arg[i % len(second_arg)])
        result_list.append(f'{hex(xored_arg)} ')  # result in hex format for unicode, not ascii!
    result_output = ''.join(result_list)
    _result_entry.delete(0, tk.END)
    _result_entry.insert(0, result_output)


def replacement_function(_first_arg_entry, _second_arg_entry, _third_arg_entry, _result_repl_label):
    # working on replacement result
    all_changes = {}
    first_arg = _first_arg_entry.get()
    second_arg = _second_arg_entry.get()
    third_arg = _third_arg_entry.get()
    first_list = []
    second_list = []
    third_list = []

    # all necessary checks
    if first_arg == '':
        messagebox.showwarning('Warning!', 'Please, write some text')
        _first_arg_entry.delete(0, tk.END)
        _first_arg_entry.focus()
        return
    if second_arg == '':
        messagebox.showwarning('Warning!', 'Please, write some text')
        _second_arg_entry.delete(0, tk.END)
        _second_arg_entry.focus()
        return
    if third_arg == '':
        messagebox.showwarning('Warning!', 'Please, write some text')
        _third_arg_entry.delete(0, tk.END)
        _third_arg_entry.focus()
        return
    if len(first_arg) != len(second_arg):
        messagebox.showwarning('Warning!', 'Please, write valid lines')
        if len(first_arg) > len(second_arg):
            _first_arg_entry.delete(0, tk.END)
            _first_arg_entry.focus()
        elif len(first_arg) < len(second_arg):
            _second_arg_entry.delete(0, tk.END)
            _second_arg_entry.focus()
        return

    for i in range(len(third_arg)):
        t = 0
        for j in range(len(first_arg)):
            if first_arg[j] == third_arg[i]:
                t += 1
        if t != 1:
            messagebox.showwarning('Warning!', 'Please, write valid text')
            _third_arg_entry.delete(0, tk.END)
            _third_arg_entry.focus()
            return
        third_list.append(third_arg[i])
    for i in range(len(first_arg)):
        for j in range(len(first_list)):
            if first_arg[i] == first_list[j]:
                messagebox.showwarning('Warning!', 'Please, write different symbols')
                _first_arg_entry.delete(0, tk.END)
                _first_arg_entry.focus()
                return
            if second_list[j] == second_arg[i]:
                messagebox.showwarning('Warning!', 'Please, write different symbols')
                _second_arg_entry.delete(0, tk.END)
                _second_arg_entry.focus()
                return
        first_list.append(first_arg[i])
        second_list.append(second_arg[i])
    for i in range(len(first_list)):
        all_changes[first_list[i]] = second_list[i]
    # print(all_changes)

    result = ''
    for i in range(len(third_list)):
        result += all_changes.get(third_list[i])
    _result_repl_label.delete(0, tk.END)
    _result_repl_label.insert(0, result)


def swap_texts(message, result):  # related to rsa function
    # use this instead of copying text
    crypto = result.get(1.0, tk.END)
    message.delete(1.0, tk.END)
    message.insert(1.0, crypto)


def working_with_files(file_text, main_text_entry, key_entry):
    xor_text = "Игровые смартфоны сейчас в тренде, а уж модели ASUS всегда привлекали внимание и получали" \
               " одобрение аудитории. Сегодня на обзоре — геймерский телефон линейки Republic of Gamers нового" \
               " поколения, оснащённый по последнему слову мобильной техники. Протестируем новинку всесторонне." \
               " Индивидуальность во всём. В дизайне ROG Phone 5 видна манера ASUS: рубленные линии, цепляющие" \
               " глаз яркие элементы. С первых минут использования замечаешь увесистость модели (целых 238 грамм)" \
               " и чрезвычайно скользкую поверхность, главным образом из-за качественного олеофобного покрытия" \
               " с обеих сторон. Так что лучше сразу облачить устройство в комплектный чехол. Заодно чехол скроет" \
               " слегка выступающий из корпуса блок камер, а небольшие бортики над дисплеем уберегут стекло" \
               " Gorilla Glass Victus от повреждений. У кейса есть и недостатки — он не защищает правый торец" \
               " аппарата, а через две недели использования начинает люфтить. Под стеклом на тыльной стороне" \
               " смартфона — логотип ROG c RGB-подсветкой. Отметим, что в версиях Pro и Ultimate вместо него" \
               " установлен небольшой PMOLED-дисплей. Рамка аппарата выполнена из алюминия, помогающего отводить" \
               " тепло от компонентов при интенсивной работе. На левом торце — дополнительный разъём USB Type-C" \
               " и контактная площадка из пяти пинов для подключения внешнего кулера. Если в них нет необходимости," \
               " они прикрываются резиновой заглушкой, которая легко слетает даже при обычном хвате телефона." \
               " Велика вероятность её потерять. Ниже находится лоток для двух симок, так что возможности расширить" \
               " память нет. Геймерские аксессуары. Какой игровой телефон сегодня можно представить без активной" \
               " системы охлаждения? У ROG Phone 5 есть внешний вентилятор — он может быть или отсутствовать" \
               " в комплекте в зависимости от версии устройства. Чтобы прикрепить кулер к смартфону, аппарат не" \
               " обязательно вынимать из чехла. Достаточно совместить контакты на корпусе гаджета и вентилятора," \
               " затем надавить на телефон до характерного щелчка. Проделать это с первого раза удаётся не всегда," \
               " к тому же кажется, что так можно поцарапать алюминиевую рамку корпуса. Уж лучше бы производитель" \
               " сохранил более удачные крепления кулера от предшественника. Из плюсов — на корпусе вертушки" \
               " красуются две дополнительные настраиваемые кнопки, удобная ножка-подставка и собственная" \
               " RGB-подсветка. Эффективность работы вентилятора мы решили продемонстрировать с помощью двух" \
               " бенчмарков. Ещё из геймерских аксессуаров производитель представил вакуумные наушники" \
               " ROG Centa II. Подключаются они через старый добрый аудиоджек. «Уши» могут похвастать технологией" \
               " активного шумоподавления и большим разнообразием комплектных амбушюр, среди которых каждый найдёт" \
               " вариант себе по размеру. В остальном затычки ничем не выделяются. Безупречный дисплей. Экран" \
               " ROG Phone 5 представлен 6,78-дюймовой матрицей AMOLED с разрешением FHD+. К углам обзора не" \
               " придраться, максимальной яркости хватает, чтобы отчётливо видеть информацию даже под прямыми" \
               " лучами солнца. С цветопередачей всё в порядке, более того, панель поддерживает технологию HDR10+." \
               " ШИМ незаметен, но на всякий случай есть функция DC Dimming. Частота опроса сенсорного слоя" \
               " составляет 300 раз в секунду, поддерживаются варианты развёртки в 60, 120 и 144 Гц. Радует, что" \
               " ASUS не стала делать в дисплее вырезы. Фронтальную камеру спрятали в небольшую рамку над матрицей," \
               " а снизу есть симметричный отступ того же размера, поэтому перфекционисты могут спать спокойно." \
               " Для индикации пропущенных уведомлений используется маленький светодиод, расположенный над экраном," \
               " или функция Always on Display. Для безопасной разблокировки гаджета под дисплеем разместился" \
               " быстрый сканер отпечатков пальцев, работающий, за редким исключением, без ошибок. Максимальная" \
               " производительность и специальный софт. В ROG Phone 5 установили новый топовый восьмиядерный" \
               " 5-нанометровый чипсет Qualcomm Snapdragon 888. Максимальная частота большого ядра достигает" \
               " 2,84 ГГц. За графику отвечает ускоритель Adreno 660. Тестовый экземпляр получил 16 ГБ оперативной" \
               " памяти типа LPDDR5 и 256 ГБ постоянного хранилища стандарта UFS 3.1. Аппарат функционирует под" \
               " управлением ОС Android 11 с оболочкой ROG UI. При первой настройке прошивка предлагает выбрать" \
               " одну из двух тем оформления: фирменный лончер или интерфейс чистой версии Android. Из" \
               " предустановленного софта выделим специализированное ПО Armoury Crate, возможности которого" \
               " рассмотрим на скриншотах. Далее мы приступили к тестированию игр. Каждое приложение запускали" \
               " с наилучшими графическими настройками. Аппарат всегда работал в режиме «X»" \
               " (максимальная производительность) с подключённым кулером. Замеры fps осуществлялись с помощью" \
               " утилиты PerfDog. Универсальный набор камер. Прошлогодний ROG Phone 3, будучи геймерским" \
               " смартфоном, всё-таки удивил своими способностями по части фото и видео. Поэтому в ASUS решили" \
               " не изобретать велосипед и оснастили новинку аналогичным с предшественником блоком камер из трёх" \
               " модулей. Основной объектив представлен сенсором Sony IMX686 на 64 Мп со светосилой f/1.8. Его" \
               " дополняют ширик на 13 Мп со 125-градусным углом обзора и макросенсор на 5 Мп. Предлагаем" \
               " ознакомиться с примерами снимков. ROG Phone 5 способен снимать 4K-видео на 60 fps. В таком режиме" \
               " прекрасно себя демонстрирует электронная стабилизация — тряска практически незаметна. Четыре" \
               " микрофона здорово отсекают шум сильного морского ветра. Автофокус за редкими исключениями" \
               " срабатывает корректно и быстро. Производительности гаджета достаточно, чтобы снимать ускоренные" \
               " 4K-видео. Надо лишь установить смартфон на штатив и оставить его на несколько минут. Съёмка" \
               " 8K-видео доступна только на 30 fps. В таком случае отключается стабилизация, но автофокус остаётся" \
               " моментальным. Передовые технологии на каждый день. Скоростной интернет в ROG Phone 5" \
               " обеспечивается модулем Wi-Fi 6E, а на будущее заложена поддержка сетей 5G. Также есть NFC-чип" \
               " для бесконтактной оплаты. Смартфон способен улавливать спутники GPS, Glonass, Galileo и BeiDou," \
               " так что с ним вы точно не потеряетесь. Для меломанов станут полезными встроенный" \
               " ЦАП ESS SABRE ES9280AC, кодек Bluetooth aptX и аудиоджек. Насладиться прослушиванием любимых" \
               " композиций или просмотром контента помогут едва ли не лучшие стереодинамики в классе. Звучат они" \
               " громко, чисто и басовито. Ещё понравился приятный вибромоторчик, который выводит ощущения от" \
               " использования гаджета на новый уровень. Из интересных функций в прошивке выделим возможность" \
               " дублирования приложений, что особенно удобно, если у вас несколько аккаунтов в одном сервисе." \
               " Доступна настройка различных жестов, например, двойного постукивания для пробуждения смартфона" \
               " и рисования символов на заблокированном экране для запуска определённых задач. А в холодное" \
               " время года станет незаменимым режим работы в перчатках. Двойная батарея. Аппарат оборудован двумя" \
               " аккумуляторами по 3000 мАч. На автономность сильно влияют выбранные режимы работы дисплея и" \
               " производительности. При активации «сверхустойчивого» пресета функционирования ЦП частота обновления" \
               " дисплея блокируется на 60 Гц. Так смартфон с лёгкостью выдержит полтора дня активной эксплуатации." \
               " Тогда как в режиме «X» и с развёрткой 144 Гц проценты будут таять на глазах. Тестовый ролик Full HD" \
               " на среднем уровне яркости в авиарежиме ROG Phone 5 непрерывно крутит 20 часов. Практически" \
               " аналогичный результат получился и при воспроизведении 1080p-видео на YouTube. Играть в Genshin" \
               " Impact с подключённым вентилятором и режимом максимальной производительности можно всего 2 часа," \
               " а в этой же игре без кулера и в «Динамичном» режиме смартфон проработал 3 часа. В комплекте с" \
               " устройством поставляется блок питания на 65 Вт. Заряжать новинку можно через любой разъём, но не" \
               " одновременно. Гаджет поддерживает быструю зарядку: первые 25% восполняются за 7 минут, до 50%" \
               " ROG Phone 5 подпитывается за 16 минут, а 75% он набирает за 29 минут. Таким образом до 100% аппарат" \
               " заряжается всего за 53 минуты. Батарея при этом нагревается до 41 градуса. Итоги. ROG Phone 5" \
               " — универсальный флагман с широкими возможностями для гейминга и повседневного использования." \
               " Смартфон вместил в себя всё, чего только можно хотеть сегодня: топовое железо, способное тянуть" \
               " любую игру на максимальных настройках графики, а также передовые технологии вроде Wi-Fi 6E," \
               " скоростной зарядки, стереодинамиков и отличного дисплея. Аппарат порадовал способностями по части" \
               " съёмки фото и видео, а также фирменным софтом. Из недостатков выделим разве что быстрый разряд в" \
               " определённых режимах работы, неудобный способ крепления вентилятора к корпусу и отсутствие" \
               " влагозащиты. Но эти недочёты меркнут в сравнении с преимуществами новинки."
    trash_text = file_text.split('/')

    # working with trash text
    result_list = []
    for i in range(len(trash_text)):
        xored_arg = ord(chr(int(trash_text[i % len(trash_text)], 16))) ^ ord(xor_text[i % len(xor_text)]) \
            # ^ ord(xor_text[i % len(xor_text)]) - for check
        result_list.append(f'{chr(int(hex(xored_arg), 16))}')  # (f'{chr(int(hex(xored_arg), 16))}') - for check
    result_output = ''.join(result_list)

    # finding main text
    s1 = result_output.find('$')
    s2 = result_output.rfind('$')
    main_text = result_output[s1 + 1:s2]

    # finding key text
    s1 = result_output.find('&')
    s2 = result_output.rfind('&')
    key_text = result_output[s1 + 1:s2]

    # additional printing
    # print(result_output)
    # print(main_text)
    # print(key_text)

    main_text_entry.insert(0, main_text)
    main_text_entry['state'] = 'disable'
    key_entry.insert(0, key_text)


def working_with_table_algorithm(main_text_entry, key_entry, result, canvas_key_list, canvas_symbols_list,
                                 canvas_fill_squares_list, canvas, typo_algorithm):
    # all checks for valid key and text
    main_text = main_text_entry.get()
    key = key_entry.get()
    if main_text == '':
        messagebox.showwarning('Warning!', 'Please, enter your text')
        return
    if key == '':
        messagebox.showwarning('Warning!', 'Please, enter your key')
        return
    check_len_key = 0
    for i in range(len(key)):
        if key[i].isdigit():
            check_len_key += 1
            if key[i] == '0' or key[i] == '7' or key[i] == '8' or key[i] == '9':
                messagebox.showwarning('Warning!', 'Please, enter valid key')
                key_entry.delete(0, tk.END)
                key_entry.focus()
                return
        # *key_not_digit*
        # else:
        #     check_len_key -= 1
    if check_len_key != 6:  # *key_not_digit* and check_len_key != -6:
        messagebox.showwarning('Warning!', 'Please, enter valid key')
        key_entry.delete(0, tk.END)
        key_entry.focus()
        return
    key_list = []
    for i in range(6):
        for j in range(len(key_list)):
            if int(key[i]) == key_list[j]:
                messagebox.showwarning('Warning!', 'Please, enter valid key')
                key_entry.delete(0, tk.END)
                key_entry.focus()
                return
        key_list.append(int(key[i]))

    if typo_algorithm == 4:  # зашифровать
        # filling table (canvas) by adding key and text
        result_str = ''
        for i in range(6):
            canvas.itemconfigure(canvas_key_list[i], text=key_list[i])
            for j in range(6):
                if len(main_text) > i * 6 + j:
                    canvas.itemconfigure(canvas_symbols_list[i][j], text=main_text[i * 6 + j])
                else:
                    canvas.itemconfigure(canvas_symbols_list[i][j], text='')

        # showing the result
        for i in range(6):
            t = 0
            if check_len_key == 6:
                for j in range(6):
                    if key_list[j] - 1 == i:
                        t = j
                        break
            # *key_not_digit*
            # in case we want to see letter symbols in the key
            # elif check_len_key == -6:
            #     for j in range(5):
            #         if key_list[j + 1] < key_list[t]:
            #             t = j + 1
            #     key_list[t] = 'яя'
            for j in range(6):
                if len(main_text) > t + j * 6:
                    result_str += main_text[t + j * 6]
        result.delete(0, tk.END)
        result.insert(0, result_str)
        # separator
    elif typo_algorithm == 5:  # расшифровать
        # filling table (canvas) by adding key and text
        result_str = ''
        result_list = []
        for i in range(6):
            prom_res = []
            canvas.itemconfigure(canvas_key_list[i], text=key_list[i])
            t = 0
            for j in range(6):
                if key_list[j] - 1 == i:
                    t = j
            for j in range(6):
                if len(main_text) > i * 6 + j:
                    canvas.itemconfigure(canvas_symbols_list[j][t], text=main_text[i * 6 + j])
                    prom_res.append(main_text[i * 6 + j])
                else:
                    canvas.itemconfigure(canvas_symbols_list[j][t], text='')
                    prom_res.append('')
            result_list.append(prom_res)

        # showing the result
        for i in range(6):
            for j in range(6):
                result_str += result_list[key_list[j] - 1][i]
        result.delete(0, tk.END)
        result.insert(0, result_str)
        # separator
    elif typo_algorithm == 6:  # дешифровать
        check_fill = 0
        result_str = ''
        result_list = []
        for i in range(6):
            prom_res = []
            canvas.itemconfigure(canvas_key_list[i], text=key_list[i])
            t = 0
            for j in range(6):
                if key_list[j] - 1 == i:
                    t = j
            for j in range(6):
                # a = (j + check_fill) % 6
                # b = (t + (j + check_fill) // 6) % 6
                c = i * 6 + j - check_fill
                if len(main_text) > c:
                    if canvas_fill_squares_list[j][t] == 1:
                        check_fill += 1
                        prom_res.append('')
                    elif canvas_fill_squares_list[j][t] == 0:
                        canvas.itemconfigure(canvas_symbols_list[j][t], text=main_text[c])
                        prom_res.append(main_text[c])
                else:
                    if canvas_fill_squares_list[j][t] == 1:
                        check_fill += 1
                        prom_res.append('')
                    elif canvas_fill_squares_list[j][t] == 0:
                        canvas.itemconfigure(canvas_symbols_list[j][t], text='')
                    prom_res.append('')
            result_list.append(prom_res)

        # showing the result
        for i in range(6):
            for j in range(6):
                result_str += result_list[key_list[j] - 1][i]
        result.delete(0, tk.END)
        result.insert(0, result_str)


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

        choosing_table_algorithm = Menu(menu, tearoff=0)
        choosing_table_algorithm.add_command(label='Зашифровать', command=lambda: self.update_current_function(4))
        choosing_table_algorithm.add_separator()
        choosing_table_algorithm.add_command(label='Расшифровать', command=lambda: self.update_current_function(5))
        choosing_table_algorithm.add_separator()
        choosing_table_algorithm.add_command(label='Дешифровать', command=lambda: self.update_current_function(6))

        choosing_function.add_separator()
        choosing_function.add_cascade(label='Табличный алгоритм', menu=choosing_table_algorithm)

        # adding tabs to menu
        menu.add_cascade(label='File', menu=file)
        menu.add_cascade(label='Choose function', menu=choosing_function)

        # adding menu to the window
        self.config(menu=menu)

        # running program
        self.mainloop()

    def exit_function(self):
        try:
            os.remove('Keys.txt')  # deleting keys file, 'cause no one should know your keys
        except FileNotFoundError:
            pass
        self.destroy()

    def update_current_function(self, _function_number):  # choosing the right function
        if self.function_number != _function_number:
            self.destroy_everything()  # deleting previous function
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
                self.table_algorithm_show(4, '')  # зашифровать
            elif self.function_number == 5:
                self.table_algorithm_show(5, '')  # расшифровать
            elif self.function_number == 6:
                file_text = choose_directory()
                if file_text == '':
                    self.update_current_function(0)
                    return
                self.table_algorithm_show(6, file_text)  # дешифровать

    def destroy_everything(self):  # deleting previous function -> this is it
        for widget in self.winfo_children():
            if widget.winfo_name() != '!menu':
                widget.destroy()
                # print(widget.winfo_name())

    def home_show(self):  # function to show welcome page
        welcome = tk.Label(
            self,
            text='Hello, world!\n'
                 'Welcome to my application for Cryptography :)\n'
                 'Here you can have some practise in it...',
        )

        welcome.pack()

    def xor_show(self):  # xor show function
        # all widgets
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
            width=80,
        )
        second_arg_label = tk.Label(
            self,
            text="Write down the key",
            pady=10,
        )
        second_arg_entry = tk.Entry(
            self,
            width=80,
        )
        result_entry = tk.Entry(
            self,
            text='',
            width=80,
            bg='#aaf',
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
            command=lambda: xor_function(first_arg_entry, second_arg_entry, result_entry),
        )

        # showing widgets
        header_label.pack()
        first_arg_entry.focus()
        first_arg_label.pack()
        first_arg_entry.pack()
        second_arg_label.pack()
        second_arg_entry.pack()
        separate1.pack()
        function.pack()
        separate2.pack()
        result_entry.pack()

    def replacement_show(self):  # replacement show function
        # all widgets
        header_label = tk.Label(
            self,
            text="Замена",
            pady=10,
        )
        first_arg_label = tk.Label(
            self,
            text="Напишите ваш алфавит, состоящий из уникальных символов",
            pady=10,
        )
        first_arg_entry = tk.Entry(
            self,
            width=80,
        )
        second_arg_label = tk.Label(
            self,
            text="Напишите алфавит, на который будут заменяться буквы первого алфавита,\n"
                 "алфавит также должен состоять из уникальных символов",
            pady=10,
        )
        second_arg_entry = tk.Entry(
            self,
            width=80,
        )
        third_arg_entry = tk.Entry(
            self,
            width=80,
        )
        third_arg_label = tk.Label(
            self,
            text="Напишите сообщение",
            pady=10,
        )
        result_label = tk.Entry(
            self,
            text='',
            width=80,
            bg='#aaf',
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
            command=lambda: replacement_function(first_arg_entry, second_arg_entry, third_arg_entry, result_label),
        )

        # showing widgets
        header_label.pack()
        first_arg_entry.focus()
        first_arg_label.pack()
        first_arg_entry.pack()
        second_arg_label.pack()
        second_arg_entry.pack()
        third_arg_label.pack()
        third_arg_entry.pack()
        separate1.pack()
        function.pack()
        separate2.pack()
        result_label.pack()

    def rsa_show(self):  # rsa show function
        # all widgets
        header_label = tk.Label(
            self,
            text='Rsa encryption',
            pady=10,
        )
        button_generating_keys = tk.Button(self, text='Сгенерировать пару ключей',
                                           command=lambda: self.generating_keys(button_generating_keys))

        # showing widgets
        header_label.pack()
        button_generating_keys.pack()

    def generating_keys(self, button_generating_keys):  # generating keys function
        # disable button, 'cause only one pair can be generated and used
        button_generating_keys['state'] = 'disable'

        self.working_with_keys()

    def working_with_keys(self):  # working with keys function
        # writing keys to the file in the same directory where this program runs
        keys_file = open("Keys.txt", "w+")
        keys_file.write(
            f"Это твой публичный ключ. Поделись им с друзьями :)\n{self.pubkey.save_pkcs1()}\n"
            f"\nЭто твой приватный ключ. Сохрани его в секрете\n{self.privkey.save_pkcs1()}\n")
        keys_file.close()

        # all widgets
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

        result_text = tk.Text(
            self,
            width=40,
            height=7,
        )

        # drop-down menu function
        def callback(*args):
            result_label.configure(text=f'Результутат команды {variable.get()}')
            # print(variable.get())
            if variable.get() == 'Зашифровать':
                self.encryption(message_text.get(1.0, tk.END), result_text)
            elif variable.get() == 'Расшифровать':
                self.decryption(message_text.get(1.0, tk.END), result_text)

        # drop-down menu
        result_label = tk.Label(self, pady=5, text=f'Здесь будет твой ответ')
        variable = tk.StringVar(self)
        variable.set(drop_down_encryption_list[0])  # default value
        variable.trace("w", callback)

        drop_down_encryption_menu = tk.OptionMenu(self, variable, *drop_down_encryption_list)
        result_button = tk.Button(self, text='Поменять',
                                  command=lambda: swap_texts(message_text, result_text))

        # showing widgets
        explanation_label.pack()
        message_label.pack()
        message_text.pack()
        drop_down_encryption_menu.pack()
        result_label.pack()
        result_text.pack()
        result_button.pack()

    def encryption(self, message, result):  # зашифрование rsa
        message = message.encode()
        crypto = rsa.encrypt(message, self.pubkey)
        print(crypto)
        result.delete(1.0, tk.END)
        result.insert(1.0, crypto)

    def decryption(self, crypto, result):  # расшифрование rsa
        # need fix!
        crypto = crypto.encode()
        print(crypto)
        message = rsa.decrypt(crypto, self.privkey)
        message = message.decode()
        result.delete(1.0, tk.END)
        result.insert(1.0, message)

    def table_algorithm_show(self, typo_algorithm, file_text):  # table algorithm show function
        # all widgets
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

        # *preset*
        # if you need preset text
        # main_text_entry.delete(0, tk.END)
        # main_text_entry.insert(0, 'Привет, меня зовут Кот Василий')

        key_label = tk.Label(self, pady=5, text='Ключ')
        key_entry = tk.Entry(self, width=20)

        # replacing symbols by <*> after double left button click
        def filling_squares(event):
            # getting coordinates of double tap
            x = event.x
            y = event.y
            if 250 < x < 430 and 60 < y < 240:  # checking if they are fit the area
                a = (y - 60) // 30
                b = (x - 250) // 30
                # 0 - we should replace <symbol> to <*>
                # 1 - we should replace <*> to <>
                if canvas_fill_squares_list[a][b] == 0:
                    canvas.itemconfigure(canvas_symbols_list[a][b], text='*')
                    canvas_fill_squares_list[a][b] = 1
                elif canvas_fill_squares_list[a][b] == 1:
                    canvas.itemconfigure(canvas_symbols_list[a][b], text='')
                    canvas_fill_squares_list[a][b] = 0

        # checking which algorithm user chooses
        if typo_algorithm == 4:
            main_text_label['text'] = 'Исходный текст'
            header_label['text'] = 'Это табличный алгоритм для зашифрования'
        elif typo_algorithm == 5:
            main_text_label['text'] = 'Шифротекст'
            header_label['text'] = 'Это табличный алгоритм для расшифрования'
        elif typo_algorithm == 6:
            main_text_label['text'] = 'Шифротекст'
            header_label['text'] = 'Это табличный алгоритм для дешифрования'
            self.bind('<Double-Button-1>', filling_squares)  # detecting double left click
            working_with_files(file_text, main_text_entry, key_entry)

        # *preset*
        # key_entry.delete(0, tk.END)
        # key_entry.insert(0, '213456')

        # area where text will be placed and shown
        canvas = tk.Canvas(self)
        canvas.create_rectangle(
            250, 60, 430, 240,
            outline="#aaf", fill="#aaf"
        )
        result_entry = tk.Entry(self, bg='#aaf', width=60)

        # *preset*
        # result_entry.delete(0, tk.END)
        # if typo_algorithm == 4:
        #     result_entry.insert(0, 'р зКсП,  аимооивевтлену итятВй')
        # elif typo_algorithm == 5:
        #     result_entry.insert(0, ',П  а рзКсмиооиеввтлнеу ияттВй')

        result_button = tk.Button(self, text='Получить результат',
                                  command=lambda: working_with_table_algorithm(main_text_entry,
                                                                               key_entry, result_entry,
                                                                               canvas_key_list,
                                                                               canvas_symbols_list,
                                                                               canvas_fill_squares_list,
                                                                               canvas,
                                                                               typo_algorithm))

        # horizontal lines
        canvas.create_line(250, 59, 430, 59)
        canvas.create_line(250, 241, 430, 241)
        canvas.create_line(250, 90, 430, 90)
        canvas.create_line(250, 120, 430, 120)
        canvas.create_line(250, 150, 430, 150)
        canvas.create_line(250, 180, 430, 180)
        canvas.create_line(250, 211, 430, 211)

        # useful lists
        canvas_key_list = [0 for _ in range(6)]  # key numbers
        canvas_symbols_list = [[0 for _ in range(6)] for _ in range(6)]  # main text symbols
        canvas_fill_squares_list = [[0 for _ in range(6)] for _ in range(6)]  # places where <*> is placed

        # default filling canvas
        for i in range(6):
            canvas_key_list[i] = canvas.create_text(265 + i * 30, 50, text=f'{i + 1}')
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

        # show widgets
        header_label.pack()
        main_text_label.pack()
        main_text_entry.pack()
        key_label.pack()
        key_entry.pack()
        canvas.pack(fill=tk.BOTH)
        result_button.pack()
        separate1.pack()
        result_entry.pack()


if __name__ == '__main__':  # run program
    MainWindow()  # call window showing class
