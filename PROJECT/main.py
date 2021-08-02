import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
import tkinter.filedialog as fd
import rsa
import os

# global variables
sum_tips_filled = [0 for _ in range(6)]
sum_tips_key = [0 for _ in range(6)]
symbols_to_show = [0 for _ in range(2)]
key_answer_list = []  # true key
filled_answer_list = []  # all filled squares
red_squares_list = []  # red filled squares list
show_filled_list = []  # filled positions which should be shown
show_key_list = []  # key positions which should be shown
current_file_open = ''
tasks_answer_list = ['Привет, меня зовут Кот Василий', 'А это лучший криптоалгоритм', 'Который я когда-либо намурлыкал',
                     'Ты, друг мой, избран не случайно', 'Только ты можешь дешифровать это',
                     'И отыскать секретное послание!', 'Now you are the king of cryptography']
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


def choose_directory():  # uploading file
    global current_file_open

    filetypes = (("Текстовый файл", "*.txt"), ("Любой", "*.txt"))
    my_file = fd.askopenfile(title="Открыть файл", initialdir="", filetypes=filetypes)
    # here you can type path to your directory

    if my_file:  # if file is open
        # working with file
        # print(*my_file.readlines())
        current_file_open = os.path.basename(my_file.name)[:-4]
        # print(current_file_open)
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
    first_arg_list = first_arg.encode('cp1251')
    second_arg_list = second_arg.encode('cp1251')
    for i in range(len(first_arg_list)):
        xored_arg = first_arg_list[i % len(first_arg_list)] ^ second_arg_list[i % len(second_arg_list)]
        # additional check ^ second_arg[i % len(second_arg)].encode('cp1251')
        append_object = len(str(hex(xored_arg))[2:]) % 2 * '0' + str(hex(xored_arg))[2:]
        result_list.append(f'0x{append_object} ')  # result in hex format for unicode, not ascii!
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
    global xor_text, key_answer_list, filled_answer_list
    key_answer_list = []
    filled_answer_list = []

    trash_text = file_text.split('/')

    # working with trash text
    result_list = []
    for i in range(len(trash_text)):
        xored_arg = ord(chr(int(trash_text[i % len(trash_text)], 16))) ^ ord(xor_text[i % len(xor_text)]) \
            # ^ ord(xor_text[i % len(xor_text)]) - for check
        result_list.append(f'{chr(int(hex(xored_arg), 16))}')  # (f'{chr(int(hex(xored_arg), 16))}') - for check
    result_output = ''.join(result_list)

    # finding main text and key text
    main_text = ''
    key_text = ''
    for i in range(6):
        s1 = result_output.find(f'${i + 1}')
        s2 = result_output.find(f'{i + 1}$')
        if s1 == -1:
            return -1
        text = result_output[s1 + 2: s2 + 1]
        # print(text)
        key_text += text[-1]
        main_text += text[:-1]

    # finding answer key
    s1 = result_output.find(f'%')
    while not result_output[s1 + 1].isdigit():
        s1 = result_output.find(f'%')
    if s1 == -1:
        return -1
    key_answer = result_output[s1 + 1: s1 + 7]
    # print(key_answer)
    for i in range(6):
        key_answer_list.append(int(key_answer[i]))

    # finding filled squares
    while True:
        s1 = result_output.find(f'&')
        if s1 != -1:
            if result_output[s1 + 1].isdigit() and result_output[s1 + 2].isdigit():
                pair_of_coordinates = result_output[s1 + 1: s1 + 3]
                filled_answer_list.append([int(pair_of_coordinates[0]), int(pair_of_coordinates[1])])
            before_keyword, keyword, after_keyword = result_output.partition('&')
            result_output = after_keyword
        elif s1 == -1:
            break
    # print(filled_answer_list)
    # print(result_output)
    # print(main_text)
    # print(key_text)

    main_text_entry.insert(0, main_text)
    main_text_entry['state'] = 'disable'
    key_entry.insert(0, key_text)

    return 1


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
    if len(main_text) > 36:
        messagebox.showwarning('Warning!', 'Please, enter valid text')
        main_text_entry.delete(0, tk.END)
        main_text_entry.focus()
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
        check_fill = 0
        for i in range(6):
            canvas.itemconfigure(canvas_key_list[i], text=key_list[i])
            for j in range(6):
                if len(main_text) > i * 6 + j - check_fill:
                    if canvas_fill_squares_list[i][j] == 1:
                        check_fill += 1
                    elif canvas_fill_squares_list[i][j] == 0:
                        canvas.itemconfigure(canvas_symbols_list[i][j], text=main_text[i * 6 + j - check_fill])
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
        check_fill = 0
        for i in range(6):
            prom_res = []
            canvas.itemconfigure(canvas_key_list[i], text=key_list[i])
            t = 0
            for j in range(6):
                if key_list[j] - 1 == i:
                    t = j
            for j in range(6):
                if len(main_text) > i * 6 + j - check_fill:
                    if canvas_fill_squares_list[j][t] == 1:
                        check_fill += 1
                        prom_res.append('')
                    elif canvas_fill_squares_list[j][t] == 0:
                        canvas.itemconfigure(canvas_symbols_list[j][t], text=main_text[i * 6 + j - check_fill])
                        prom_res.append(main_text[i * 6 + j - check_fill])
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
        global show_key_list
        filling_squares_with_tips(canvas, canvas_fill_squares_list, canvas_symbols_list)

        check_fill = 0
        result_str = ''
        result_list = []
        for i in range(len(show_key_list)):
            key_list[show_key_list[i][0]] = show_key_list[i][1]
            canvas.itemconfigure(canvas_key_list[show_key_list[i][0]], text=key_list[show_key_list[i][0]])
        for i in range(6):
            for j in range(i + 1, 6):
                if key_list[i] == key_list[j]:
                    messagebox.showwarning('Warning!', 'Please, enter valid key')
                    key_entry.delete(0, tk.END)
                    key_entry.focus()
                    return
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


def filling_squares_with_tips(canvas, canvas_fill_squares_list, canvas_symbols_list):
    global show_filled_list, red_squares_list
    for i in range(len(show_filled_list)):
        for j in range(len(show_filled_list[i])):
            a = show_filled_list[i][j][0]
            b = show_filled_list[i][j][1]
            y = 250 + 30 * b
            x = 60 + 30 * a
            if canvas_fill_squares_list[a][b] == 0:
                red_squares_list.append([canvas.create_rectangle(y, x, y + 30, x + 30, fill='#f00'), y, x])
                canvas.itemconfigure(canvas_symbols_list[a][b], text='*')
                canvas_fill_squares_list[a][b] = 1


def clear_global_variables():
    global sum_tips_filled, sum_tips_key, symbols_to_show, key_answer_list, \
        filled_answer_list, show_filled_list, show_key_list, red_squares_list
    sum_tips_filled = [0 for _ in range(6)]
    sum_tips_key = [0 for _ in range(6)]
    symbols_to_show = [0 for _ in range(2)]
    key_answer_list = []  # true key
    filled_answer_list = []  # all filled squares
    show_filled_list = []  # filled positions which should be shown
    show_key_list = []  # key positions which should be shown
    red_squares_list = []


class Tips(tk.Tk):
    def __init__(self):
        super().__init__()

        # settings for the window
        self.title('Tips')
        self.geometry('300x440+100+100')
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

        self.symbol_first_var = tk.IntVar()
        self.symbol_last_var = tk.IntVar()
        self.symbol_first_show = tk.Checkbutton(self, text='Показать первые 4 символа', variable=self.symbol_first_var,
                                                onvalue=1, offvalue=0, command=lambda: self.symbol_show(0))
        self.symbol_last_show = tk.Checkbutton(self, text='Показать последние 4 символа', variable=self.symbol_last_var,
                                               onvalue=1, offvalue=0, command=lambda: self.symbol_show(1))
        self.symbol_first_show_entry = tk.Entry(self, width=40)
        self.symbol_last_show_entry = tk.Entry(self, width=40)

        # filled answer
        self.filled_tip_label = tk.Label(self, text='Показать запрещенные ячейки в:')

        # all variables for filled squares
        self.tips_var_filled_list = [tk.IntVar() for _ in range(6)]
        self.tips_filled_list = []

        # toggle_click_tip(which_list, which_place)
        # which_list == 0  ->  self.tips_filled_list, which_list == 1  ->  self.tips_key_list
        self.tips_filled_list.append(tk.Checkbutton(self, text='первом столбце', variable=self.tips_var_filled_list[0],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 0)))
        self.tips_filled_list.append(tk.Checkbutton(self, text='втором столбце', variable=self.tips_var_filled_list[1],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 1)))
        self.tips_filled_list.append(tk.Checkbutton(self, text='третьем столбце', variable=self.tips_var_filled_list[2],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 2)))
        self.tips_filled_list.append(tk.Checkbutton(self, text='четвертом столбце',
                                                    variable=self.tips_var_filled_list[3],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 3)))
        self.tips_filled_list.append(tk.Checkbutton(self, text='пятом столбце', variable=self.tips_var_filled_list[4],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 4)))
        self.tips_filled_list.append(tk.Checkbutton(self, text='шестом столбце', variable=self.tips_var_filled_list[5],
                                                    onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(0, 5)))

        # key answer
        self.key_tip_label = tk.Label(self, text='Показать правильное расположение столбцов:')

        # all variables for key answer
        self.tips_var_key_list = [tk.IntVar() for _ in range(6)]
        self.tips_key_list = []

        self.tips_key_list.append(tk.Checkbutton(self, text='первый столбец', variable=self.tips_var_key_list[0],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 0)))
        self.tips_key_list.append(tk.Checkbutton(self, text='второй столбец', variable=self.tips_var_key_list[1],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 1)))
        self.tips_key_list.append(tk.Checkbutton(self, text='третий столбец', variable=self.tips_var_key_list[2],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 2)))
        self.tips_key_list.append(tk.Checkbutton(self, text='четвертый столбец', variable=self.tips_var_key_list[3],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 3)))
        self.tips_key_list.append(tk.Checkbutton(self, text='пятый столбец', variable=self.tips_var_key_list[4],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 4)))
        self.tips_key_list.append(tk.Checkbutton(self, text='шестой столбец', variable=self.tips_var_key_list[5],
                                                 onvalue=1, offvalue=0, command=lambda: self.toggle_click_tip(1, 5)))

        global sum_tips_key, sum_tips_filled, symbols_to_show
        if sum(sum_tips_filled) < 3:
            for i in range(len(sum_tips_filled)):
                if sum_tips_filled[i] == 1:
                    self.tips_filled_list[i].config(state=tk.DISABLED)
                    self.tips_filled_list[i].select()
                elif sum_tips_filled[i] == 0:
                    self.tips_filled_list[i].config(state=tk.NORMAL)
        elif sum(sum_tips_filled) == 3:
            for i in range(len(sum_tips_filled)):
                self.tips_filled_list[i].config(state=tk.DISABLED)
                if sum_tips_filled[i] == 1:
                    self.tips_filled_list[i].select()

        if sum(sum_tips_key) < 3:
            for i in range(len(sum_tips_key)):
                if sum_tips_key[i] == 1:
                    self.tips_key_list[i].config(state=tk.DISABLED)
                    self.tips_key_list[i].select()
                elif sum_tips_key[i] == 0:
                    self.tips_key_list[i].config(state=tk.NORMAL)
        elif sum(sum_tips_key) == 3:
            for i in range(len(sum_tips_key)):
                self.tips_key_list[i].config(state=tk.DISABLED)
                if sum_tips_key[i] == 1:
                    self.tips_key_list[i].select()

        if symbols_to_show[0] == 1:
            self.symbol_first_show.config(state=tk.DISABLED)
            self.symbol_first_show.select()
            self.symbol_first_show_entry.delete(0, tk.END)
            self.symbol_first_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][:4])
        if symbols_to_show[1] == 1:
            self.symbol_last_show.config(state=tk.DISABLED)
            self.symbol_last_show.select()
            self.symbol_last_show_entry.delete(0, tk.END)
            self.symbol_last_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][-4:])

        self.symbol_first_show.pack()
        self.symbol_first_show_entry.pack()
        self.symbol_last_show.pack()
        self.symbol_last_show_entry.pack()
        self.filled_tip_label.pack()
        for i in self.tips_filled_list:
            i.pack()
        self.key_tip_label.pack()
        for i in self.tips_key_list:
            i.pack()

    def symbol_show(self, which_symbol):
        global tasks_answer_list, current_file_open, symbols_to_show
        if which_symbol == 0:
            self.symbol_first_show_entry.delete(0, tk.END)
            self.symbol_first_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][:4])
            symbols_to_show[0] = 1
        elif which_symbol == 1:
            self.symbol_last_show_entry.delete(0, tk.END)
            self.symbol_last_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][-4:])
            symbols_to_show[1] = 1

        if symbols_to_show[0] == 1:
            self.symbol_first_show.config(state=tk.DISABLED)
            self.symbol_first_show.select()
            self.symbol_first_show_entry.delete(0, tk.END)
            self.symbol_first_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][:4])
        if symbols_to_show[1] == 1:
            self.symbol_last_show.config(state=tk.DISABLED)
            self.symbol_last_show.select()
            self.symbol_last_show_entry.delete(0, tk.END)
            self.symbol_last_show_entry.insert(0, tasks_answer_list[int(current_file_open[-1]) - 1][-4:])

    def toggle_click_tip(self, which_list, place):
        global sum_tips_key, sum_tips_filled

        if which_list == 0:
            self.tips_var_filled_list[place].set(not self.tips_var_filled_list[place].get())
            if self.tips_var_filled_list[place].get() == 1:
                sum_tips_filled[place] = 1
            elif self.tips_var_filled_list[place].get() == 0:
                sum_tips_filled[place] = 0
        elif which_list == 1:
            self.tips_var_key_list[place].set(not self.tips_var_key_list[place].get())
            if self.tips_var_key_list[place].get() == 1:
                sum_tips_key[place] = 1
            elif self.tips_var_key_list[place].get() == 0:
                sum_tips_key[place] = 0
        self.check_click_tip()

        if sum(sum_tips_filled) < 3:
            for i in range(len(sum_tips_filled)):
                if sum_tips_filled[i] == 1:
                    self.tips_filled_list[i].config(state=tk.DISABLED)
                    self.tips_filled_list[i].select()
                elif sum_tips_filled[i] == 0:
                    self.tips_filled_list[i].config(state=tk.NORMAL)
        elif sum(sum_tips_filled) == 3:
            for i in range(len(sum_tips_filled)):
                self.tips_filled_list[i].config(state=tk.DISABLED)
                if sum_tips_filled[i] == 1:
                    self.tips_filled_list[i].select()

        if sum(sum_tips_key) < 3:
            for i in range(len(sum_tips_key)):
                if sum_tips_key[i] == 1:
                    self.tips_key_list[i].config(state=tk.DISABLED)
                    self.tips_key_list[i].select()
                elif sum_tips_key[i] == 0:
                    self.tips_key_list[i].config(state=tk.NORMAL)
        elif sum(sum_tips_key) == 3:
            for i in range(len(sum_tips_key)):
                self.tips_key_list[i].config(state=tk.DISABLED)
                if sum_tips_key[i] == 1:
                    self.tips_key_list[i].select()

    def check_click_tip(self):
        global show_filled_list, show_key_list, sum_tips_key, sum_tips_filled, red_squares_list

        show_filled_list = []
        red_squares_list = []

        for i in range(6):
            if sum_tips_key[i] == 1:
                show_key_list.append([i, key_answer_list[i]])

        for i in range(6):
            arr = []
            for j in range(len(filled_answer_list)):
                if filled_answer_list[j][1] == i and sum_tips_filled[i] == 1:
                    arr.append(filled_answer_list[j])
            show_filled_list.append(arr)
        # print(show_filled_list)


class Answer(tk.Tk):
    def __init__(self):
        super().__init__()

        # settings for the window
        self.title('Answer')
        self.geometry('300x440+100+100')
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy())

        self.header = tk.Label(self, text='Проверь свой ответ!', pady=5)
        self.answer_label = tk.Label(self, text='Введи свой ответ', pady=5)
        self.answer_entry = tk.Entry(self, width=40, bg='#aaf')
        self.separate1 = tk.Label(self, text='')
        self.answer_button = tk.Button(self, text='Проверить ответ', command=lambda: self.check_answer())

        # show widgets
        self.header.pack()
        self.answer_label.pack()
        self.answer_entry.pack()
        self.separate1.pack()
        self.answer_button.pack()

    def check_answer(self):
        global tasks_answer_list, current_file_open, sum_tips_key, sum_tips_filled, symbols_to_show
        # print(current_file_open)
        # print(tasks_answer_list[int(current_file_open[-1])])
        if self.answer_entry.get() == tasks_answer_list[int(current_file_open[-1]) - 1]:
            messagebox.showinfo('Ураа', f'Поздравляю, твой ответ верный\n'
                                        f'Твоя оценка:'
                                        f'{5 - (sum(sum_tips_key) + sum(sum_tips_filled) + sum(symbols_to_show)) // 2}')
        else:
            messagebox.showinfo('Упс', 'Попробуй еще раз, твой ответ неверный')


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # settings for the window
        self.title('Cryptography')
        self.geometry('700x570+10+10')
        self.protocol("WM_DELETE_WINDOW", lambda: self.exit_function())

        # some variables
        self.function_number = -1

        # generating keys
        (pubkey, privkey) = rsa.newkeys(512)
        self.pubkey = pubkey
        self.privkey = privkey

        # creating menu
        self.menu = tk.Menu(self)

        # different tabs
        # file tab
        self.file = Menu(self.menu, tearoff=0)
        self.file.add_command(label='Uploading file', command=lambda: choose_directory())
        self.file.add_separator()
        self.file.add_command(label='Exit', command=lambda: self.exit_and_change_all_files())

        # choose function tab
        self.choosing_function = Menu(self.menu, tearoff=0)
        self.choosing_function.add_command(label='Home', command=lambda: self.update_current_function(0))
        self.choosing_function.add_separator()
        self.choosing_function.add_command(label='XOR', command=lambda: self.update_current_function(1))
        self.choosing_function.add_separator()
        self.choosing_function.add_command(label='Replacement', command=lambda: self.update_current_function(2))
        self.choosing_function.add_separator()
        self.choosing_function.add_command(label='RSA', command=lambda: self.update_current_function(3))

        self.choosing_table_algorithm = Menu(self.menu, tearoff=0)
        self.choosing_table_algorithm.add_command(label='Зашифровать', command=lambda: self.update_current_function(4))
        self.choosing_table_algorithm.add_separator()
        self.choosing_table_algorithm.add_command(label='Расшифровать', command=lambda: self.update_current_function(5))
        self.choosing_table_algorithm.add_separator()
        self.choosing_table_algorithm.add_command(label='Дешифровать', command=lambda: self.update_current_function(6))
        self.choosing_table_algorithm.add_separator()
        self.choosing_table_algorithm.add_command(label='Режим демонстрации',
                                                  command=lambda: self.update_current_function(7))

        self.choosing_function.add_separator()
        self.choosing_function.add_cascade(label='Табличный алгоритм', menu=self.choosing_table_algorithm)

        # adding tabs to menu
        self.menu.add_cascade(label='File', menu=self.file)
        self.menu.add_cascade(label='Выберете функцию', menu=self.choosing_function)
        self.menu.add_command(label='Подсказки', state='disabled', command=Tips)

        # adding menu to the window
        self.config(menu=self.menu)

        # running program
        self.mainloop()

    def exit_and_change_all_files(self):
        self.change_task_file('task1')
        self.change_task_file('task2')
        self.change_task_file('task3')
        self.change_task_file('task4')
        self.change_task_file('task5')
        self.change_task_file('task6')
        self.change_task_file('task7')
        self.destroy()

    def exit_function(self):
        global current_file_open
        try:
            os.remove('Keys.txt')  # deleting keys file, 'cause no one should know your keys
        except FileNotFoundError:
            pass
        if current_file_open != '':
            self.change_task_file(current_file_open)
        self.destroy()

    def update_current_function(self, _function_number):  # choosing the right function
        if self.function_number != _function_number:
            self.destroy_everything()  # deleting previous function
            self.function_number = _function_number
            self.menu.entryconfig('Подсказки', state='disabled')
            if self.function_number == 6:
                self.menu.entryconfig('Подсказки', state='normal')

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
            # elif self.function_number == 7:
                # self.table_algorithm_show(7, '')

    def destroy_everything(self):  # deleting previous function -> this is it
        for widget in self.winfo_children():
            if widget.winfo_name() != '!menu':
                widget.destroy()
                # print(widget.winfo_name())

    def home_show(self):  # function to show welcome page
        welcome = tk.Label(self, text='Hello, world!\nWelcome to my application for Cryptography :)\n'
                                      'Here you can have some practise ...')

        welcome.pack()

    def xor_show(self):  # xor show function
        # all widgets
        header_label = tk.Label(self, text="XOR между 2 строками", pady=5)
        first_arg_label = tk.Label(self, text="Введите текст", pady=5)
        first_arg_entry = tk.Entry(self, width=80)
        second_arg_label = tk.Label(self, text="Введите ключ", pady=5)
        second_arg_entry = tk.Entry(self, width=80)
        result_entry = tk.Entry(self, text='', width=80, bg='#aaf')
        separate1 = tk.Label(self, pady=5, text='')
        separate2 = tk.Label(self, pady=5, text='')
        function = tk.Button(self, text="Получить результат",
                             command=lambda: xor_function(first_arg_entry, second_arg_entry, result_entry))

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
        header_label = tk.Label(self, text="Замена", pady=5)
        first_arg_label = tk.Label(self, text="Напишите ваш алфавит, состоящий из уникальных символов", pady=5)
        first_arg_entry = tk.Entry(self, width=80)
        second_arg_label = tk.Label(self, text="Напишите алфавит, на который будут заменяться буквы первого алфавита,\n"
                                               "алфавит также должен состоять из уникальных символов", pady=5)
        second_arg_entry = tk.Entry(self, width=80)
        third_arg_entry = tk.Entry(self, width=80)
        third_arg_label = tk.Label(self, text="Напишите сообщение", pady=5)
        result_label = tk.Entry(self, text='', width=80, bg='#aaf')
        separate1 = tk.Label(self, pady=5, text='')
        separate2 = tk.Label(self, pady=5, text='')
        function = tk.Button(self, text="Получить результат",
                             command=lambda: replacement_function(first_arg_entry, second_arg_entry, third_arg_entry,
                                                                  result_label))

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
        header_label = tk.Label(self, text='Rsa', pady=5)
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
        explanation_label = tk.Label(self, text='Теперь у тебя есть открытый и закртый ключи.\n'
                                                'Они сохранились в папку, из которой была запущена эта программа.\n'
                                                'Найди и открой этот файл, он тебе понадобится.', pady=5)
        message_label = tk.Label(self, text='Введите сообщение которое хотите зашифровать / расшифровать', pady=5)
        message_text = tk.Text(self, width=40, height=7)
        drop_down_encryption_list = [
            "Зашифровать",
            "Расшифровать",
        ]

        result_text = tk.Text(self, width=40, height=7)

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
        result_button = tk.Button(self, text='Поменять', command=lambda: swap_texts(message_text, result_text))

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
        # print(crypto)
        result.delete(1.0, tk.END)
        result.insert(1.0, crypto)

    def decryption(self, crypto, result):  # расшифрование rsa
        # need fix!
        crypto = crypto.encode()
        # print(crypto)
        message = rsa.decrypt(crypto, self.privkey)
        message = message.decode()
        result.delete(1.0, tk.END)
        result.insert(1.0, message)

    def table_algorithm_show(self, typo_algorithm, file_text):  # table algorithm show function
        # all widgets
        header_label = tk.Label(self, pady=5, text='Это табличный алгоритм')
        main_text_label = tk.Label(self, pady=5, text='Исходный текст')
        separate1 = tk.Label(self, text='')
        main_text_entry = tk.Entry(self, width=60)

        key_label = tk.Label(self, pady=5, text='Ключ')
        key_entry = tk.Entry(self, width=20)

        # replacing symbols by <*> after double left button click
        def filling_squares(event):
            # getting coordinates of double tap
            global red_squares_list
            x = event.x
            y = event.y
            if 250 < x < 430 and 60 < y < 240:  # checking if they are fit the area
                a = (y - 60) // 30
                b = (x - 250) // 30
                y = 250 + 30 * b
                x = 60 + 30 * a
                # 0 - we should replace <symbol> to <*>
                # 1 - we should replace <*> to <>
                if canvas_fill_squares_list[a][b] == 0:
                    red_squares_list.append([canvas.create_rectangle(y, x, y + 30, x + 30, fill='#f00'), y, x])
                    canvas_fill_squares_list[a][b] = 1
                elif canvas_fill_squares_list[a][b] == 1:
                    id_of_square = 0
                    for k in range(len(red_squares_list)):
                        if red_squares_list[k][1] == y and red_squares_list[k][2] == x:
                            id_of_square = k
                            break
                    canvas.delete(red_squares_list[id_of_square][0])
                    del red_squares_list[id_of_square]
                    canvas.itemconfigure(canvas_symbols_list[a][b], text='')
                    canvas_fill_squares_list[a][b] = 0

        # checking which algorithm user chooses
        if typo_algorithm == 4:
            main_text_label['text'] = 'Исходный текст'
            header_label['text'] = 'Это табличный алгоритм для зашифрования'
            self.bind('<Double-Button-1>', filling_squares)  # detecting double left click
        elif typo_algorithm == 5:
            main_text_label['text'] = 'Шифротекст'
            header_label['text'] = 'Это табличный алгоритм для расшифрования'
            self.bind('<Double-Button-1>', filling_squares)  # detecting double left click
        elif typo_algorithm == 6:
            main_text_label['text'] = 'Шифротекст'
            header_label['text'] = 'Это табличный алгоритм для дешифрования'
            self.bind('<Double-Button-1>', filling_squares)  # detecting double left click
            check = working_with_files(file_text, main_text_entry, key_entry)
            if check == -1:
                self.update_current_function(0)
                return
            self.menu.entryconfig('Выберете функцию', state='disabled')

        # area where text will be placed and shown
        canvas = tk.Canvas(self)
        canvas.create_rectangle(250, 60, 430, 240, outline="#aaf", fill="#aaf")
        result_entry = tk.Entry(self, bg='#aaf', width=60)

        result_button = tk.Button(self, text='Получить результат',
                                  command=lambda: working_with_table_algorithm(main_text_entry,
                                                                               key_entry, result_entry,
                                                                               canvas_key_list,
                                                                               canvas_symbols_list,
                                                                               canvas_fill_squares_list,
                                                                               canvas,
                                                                               typo_algorithm))

        # horizontal lines
        for i in range(5):
            canvas.create_line(250, 90 + i * 30, 430, 90 + i * 30)
        canvas.create_line(250, 59, 430, 59)
        canvas.create_line(250, 241, 430, 241)

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
        for i in range(5):
            canvas.create_line(280 + i * 30, 50, 280 + i * 30, 240)
        canvas.create_line(249, 50, 249, 240)
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

        if typo_algorithm == 6:
            global current_file_open

            answer_button = tk.Button(self, text='Проверьте ответ', command=Answer)
            exit_button = tk.Button(self, text='Завершить дешифрование',
                                    command=lambda: self.change_task_file(current_file_open))
            separate2 = tk.Label(self)
            separate3 = tk.Label(self)

            separate2.pack()
            answer_button.pack()
            separate3.pack()
            exit_button.pack()

    def change_task_file(self, task_number):
        import random

        # setting variables
        global xor_text

        # $ - peaces of main text
        # % - right key
        # & - filled squares
        # linker--key_text--main_text--key_text--linker
        # different variations of message that should be decoded
        all_main_key_text = {
            'task1': [
                [  # 0
                    f'${1}Птеооа{1}$',
                    f'${2}нвтс{2}$',
                    f'${3}р,яуи{3}$',
                    f'${4}и т л{4}$',
                    f'${5}вм  Ви{5}$',
                    f'${6}езКй{6}$',
                    f'%123456%',
                    f'&01&',
                    f'&11&',
                    f'&15&',
                    f'&23&',
                    f'&42&',
                    f'&45&',
                ],
                [  # 1
                    f'${5}ПвеоК{5}$',
                    f'${2}ренвос{2}$',
                    f'${3}тяути{3}$',
                    f'${6}, т л{6}$',
                    f'${1}и зВи{1}$',
                    f'${4}м ай{4}$',
                    f'%523614%',
                    f'&02&',
                    f'&03&',
                    f'&05&',
                    f'&25&',
                    f'&34&',
                    f'&50&',
                ],
                [  # 2
                    f'${3}П,явоа{3}$',
                    f'${5}р ус{5}$',
                    f'${2}и тти{2}$',
                    f'${4}вмз л{4}$',
                    f'${1}еео и{1}$',
                    f'${6}тнКВй{6}$',
                    f'%352416%',
                    f'&11&',
                    f'&22&',
                    f'&25&',
                    f'&33&',
                    f'&41&',
                    f'&44&',
                ],
                [  # 3
                    f'${5}Птнвс{5}$',
                    f'${4}р,уои{4}$',
                    f'${1} яттл{1}$',
                    f'${3}и   и{3}$',
                    f'${6}вмзВй{6}$',
                    f'${2}ееоКа{2}$',
                    f'%541362%',
                    f'&02&',
                    f'&13&',
                    f'&21&',
                    f'&34&',
                    f'&40&',
                    f'&55&',
                ],
                [  # 4
                    f'${6}Птнос{6}$',
                    f'${5}рявти{5}$',
                    f'${4}и, ул{4}$',
                    f'${3}в т и{3}$',
                    f'${2}мз Вй{2}$',
                    f'${1}ееоКа{1}$',
                    f'%654321%',
                    f'&04&',
                    f'&11&',
                    f'&23&',
                    f'&30&',
                    f'&42&',
                    f'&55&',
                ],
                [  # 5
                    f'${3}П,явКа{3}$',
                    f'${6}р ос{6}$',
                    f'${5}и ути{5}$',
                    f'${1}вмзт л{1}$',
                    f'${4}ееоВи{4}$',
                    f'${2}тн й{2}$',
                    f'%365142%',
                    f'&11&',
                    f'&22&',
                    f'&25&',
                    f'&31&',
                    f'&34&',
                    f'&45&',
                ],
                [  # 6
                    f'${2}П,яуос{2}$',
                    f'${6}р ти{6}$',
                    f'${5}и тл{5}$',
                    f'${1}вмз {1}$',
                    f'${4}еео Ви{4}$',
                    f'${3}тнвКай{3}$',
                    f'%265143%',
                    f'&11&',
                    f'&22&',
                    f'&31&',
                    f'&33&',
                    f'&42&',
                    f'&53&',
                ],
                [  # 7
                    f'${4}П,яуос{4}$',
                    f'${1}р ти{1}$',
                    f'${2}и зт л{2}$',
                    f'${6}вм и{6}$',
                    f'${3}ееоКВй{3}$',
                    f'${5}тнва{5}$',
                    f'%412635%',
                    f'&11&',
                    f'&23&',
                    f'&31&',
                    f'&35&',
                    f'&43&',
                    f'&55&',
                ],
                [  # 8
                    f'${5}ПтнКа{5}$',
                    f'${4}ряоос{4}$',
                    f'${2}и, ви{2}$',
                    f'${1}в утл{1}$',
                    f'${3}емзт и{3}$',
                    f'${6}е Вй{6}$',
                    f'%542136%',
                    f'&05&',
                    f'&11&',
                    f'&23&',
                    f'&25&',
                    f'&30&',
                    f'&42&',
                ],
            ],
            'task2': [
                [  # 0
                    f'${2}тшкар{2}$',
                    f'${4}оирли{4}$',
                    f'${6}А и{6}$',
                    f'${3} лпгт{3}$',
                    f'${1}уйтом{1}$',
                    f'${5}эч о{5}$',
                    f'%246315%',
                    f'&00&',
                    f'&01&',
                    f'&04&',
                    f'&22&',
                    f'&23&',
                    f'&42&',
                    f'&44&',
                    f'&52&',
                    f'&55&',
                ],
                [  # 1
                    f'${1} ирар{1}$',
                    f'${6}Айии{6}$',
                    f'${2} лплт{2}$',
                    f'${5}эу гм{5}$',
                    f'${3}тчт{3}$',
                    f'${4}ошкоо{4}$',
                    f'%162534%',
                    f'&00&',
                    f'&11&',
                    f'&22&',
                    f'&24&',
                    f'&33&',
                    f'&41&',
                    f'&44&',
                    f'&54&',
                    f'&55&',
                ],
                [  # 2
                    f'${6}Ашроо{6}$',
                    f'${1} оир{1}$',
                    f'${5} ий{5}$',
                    f'${4}элйпли{4}$',
                    f'${2}у гт{2}$',
                    f'${3}тиктм{3}$',
                    f'%615423%',
                    f'&02&',
                    f'&04&',
                    f'&10&',
                    f'&22&',
                    f'&31&',
                    f'&34&',
                    f'&41&',
                    f'&45&',
                    f'&52&',
                ],
                [  # 3
                    f'${3}Алироо{3}$',
                    f'${2} йар{2}$',
                    f'${4}эуии{4}$',
                    f'${5}т л{5}$',
                    f'${6}очпт{6}$',
                    f'${1} шктгм{1}$',
                    f'%324561%',
                    f'&11&',
                    f'&13&',
                    f'&22&',
                    f'&24&',
                    f'&31&',
                    f'&33&',
                    f'&42&',
                    f'&44&',
                    f'&53&',
                ],
                [  # 4
                    f'${5}Аткоо{5}$',
                    f'${3}ошрр{3}$',
                    f'${2}  иа{2}$',
                    f'${1}лйили{1}$',
                    f'${4}эупт{4}$',
                    f'${6}ч тгм{6}$',
                    f'%532146%',
                    f'&01&',
                    f'&03&',
                    f'&05&',
                    f'&20&',
                    f'&24&',
                    f'&32&',
                    f'&41&',
                    f'&44&',
                    f'&52&',
                ],
                [  # 5
                    f'${2}ч по{2}$',
                    f'${1}Аошктр{1}$',
                    f'${3}  ои{3}$',
                    f'${4}эла{4}$',
                    f'${5}туирлт{5}$',
                    f'${6}йигм{6}$',
                    f'%213456%',
                    f'&00&',
                    f'&05&',
                    f'&10&',
                    f'&15&',
                    f'&22&',
                    f'&23&',
                    f'&32&',
                    f'&33&',
                    f'&53&',
                ],
                [  # 6
                    f'${4}Аошро{4}$',
                    f'${3}иио{3}$',
                    f'${5}  йар{5}$',
                    f'${6}элпли{6}$',
                    f'${2}у тт{2}$',
                    f'${1}тчкгм{1}$',
                    f'%435621%',
                    f'&01&',
                    f'&04&',
                    f'&11&',
                    f'&23&',
                    f'&32&',
                    f'&35&',
                    f'&41&',
                    f'&44&',
                    f'&50&',
                ],
                [  # 7
                    f'${3} шоо{3}$',
                    f'${1}Аирр{1}$',
                    f'${5} лйиаи{5}$',
                    f'${4}эупл{4}$',
                    f'${2}т гт{2}$',
                    f'${6}очктм{6}$',
                    f'%315426%',
                    f'&00&',
                    f'&11&',
                    f'&14&',
                    f'&23&',
                    f'&30&',
                    f'&34&',
                    f'&41&',
                    f'&45&',
                    f'&53&',
                ],
                [  # 8
                    f'${6}Алроо{6}$',
                    f'${3} иар{3}$',
                    f'${2}эуйии{2}$',
                    f'${4}тч пл{4}$',
                    f'${1}оштт{1}$',
                    f'${5} кгм{5}$',
                    f'%632415%',
                    f'&11&',
                    f'&15&',
                    f'&20&',
                    f'&24&',
                    f'&31&',
                    f'&35&',
                    f'&42&',
                    f'&44&',
                    f'&53&',
                ],
            ],
            'task3': [
                [  # 0
                    f'${2}Кйолнл{2}$',
                    f'${6}огиа{6}$',
                    f'${1}т дмы{1}$',
                    f'${5}ояабук{5}$',
                    f'${4}р ора{4}$',
                    f'${3}ык- л{3}$',
                    f'%261543%',
                    f'&11&',
                    f'&24&',
                    f'&32&',
                    f'&45&',
                    f'&51&',
                ],
                [  # 1
                    f'${1}Кка р{1}$',
                    f'${3}ыо-нл{3}$',
                    f'${4}ойглы{4}$',
                    f'${2}т диак{2}$',
                    f'${6}оябма{6}$',
                    f'${5}р оул{5}$',
                    f'%134265%',
                    f'&01&',
                    f'&10&',
                    f'&24&',
                    f'&25&',
                    f'&42&',
                ],
                [  # 2
                    f'${5}ыолны{5}$',
                    f'${1}Кйиа{1}$',
                    f'${6}о гбмк{6}$',
                    f'${3}тядуа{3}$',
                    f'${4}о аор{4}$',
                    f'${2}рк- лл{2}$',
                    f'%516342%',
                    f'&00&',
                    f'&21&',
                    f'&33&',
                    f'&51&',
                    f'&54&',
                ],
                [  # 3
                    f'${2}Кыкл л{2}$',
                    f'${5}йоины{5}$',
                    f'${1}о гак{1}$',
                    f'${6}тдбма{6}$',
                    f'${3}ояаоу{3}$',
                    f'${4}р -рл{4}$',
                    f'%251634%',
                    f'&01&',
                    f'&13&',
                    f'&32&',
                    f'&45&',
                    f'&54&',
                ],
                [  # 4
                    f'${3}Кк- л{3}$',
                    f'${5}ойоны{5}$',
                    f'${2}т гла{2}$',
                    f'${1}оядимк{1}$',
                    f'${6}р абуа{6}$',
                    f'${4}ыорл{4}$',
                    f'%352164%',
                    f'&10&',
                    f'&15&',
                    f'&25&',
                    f'&31&',
                    f'&52&',
                ],
                [  # 5
                    f'${5}Кыдор{5}$',
                    f'${6}о а л{6}$',
                    f'${4}йк-ны{4}$',
                    f'${3}толак{3}$',
                    f'${1}о има{1}$',
                    f'${2}рягбул{2}$',
                    f'%564312%',
                    f'&02&',
                    f'&11&',
                    f'&13&',
                    f'&20&',
                    f'&24&',
                ],
                [  # 6
                    f'${3}Кйгил{3}$',
                    f'${1}о дба{1}$',
                    f'${2}тяамы{2}$',
                    f'${5}о -оук{5}$',
                    f'${4}ркл а{4}$',
                    f'${6}ыонрл{6}$',
                    f'%312546%',
                    f'&25&',
                    f'&32&',
                    f'&40&',
                    f'&44&',
                    f'&51&',
                ],
                [  # 7
                    f'${6}Коны{6}$',
                    f'${2}ойгла{2}$',
                    f'${5}т димк{5}$',
                    f'${1}ояабуа{1}$',
                    f'${4}р -ор{4}$',
                    f'${3}ык лл{3}$',
                    f'%625143%',
                    f'&10&',
                    f'&25&',
                    f'&30&',
                    f'&51&',
                    f'&54&',
                ],
                [  # 8
                    f'${3}Кйол р{3}$',
                    f'${2}о гнл{2}$',
                    f'${4}тдаы{4}$',
                    f'${1}ояимк{1}$',
                    f'${5}р аба{5}$',
                    f'${6}ык-оул{6}$',
                    f'%324156%',
                    f'&12&',
                    f'&23&',
                    f'&31&',
                    f'&32&',
                    f'&44&',
                ],
            ],
            'task4': [
                [  # 0
                    f'${2}Туйбну{2}$',
                    f'${1}ы,еч{1}$',
                    f'${4},г р а{4}$',
                    f'${3}  ай{3}$',
                    f'${6}дминсн{6}$',
                    f'${5}роз ло{5}$',
                    f'%214365%',
                    f'&11&',
                    f'&23&',
                    f'&31&',
                    f'&43&',
                ],
                [  # 1
                    f'${6}Туйну{6}$',
                    f'${3}ыг,реч{3}$',
                    f'${4}, а а{4}$',
                    f'${2}  инй{2}$',
                    f'${5}дмз сн{5}$',
                    f'${1}робло{1}$',
                    f'%634251%',
                    f'&12&',
                    f'&30&',
                    f'&35&',
                    f'&43&',
                ],
                [  # 2
                    f'${3}розну{3}$',
                    f'${2}Тубеч{2}$',
                    f'${1}ыгйр а{1}$',
                    f'${4}, ,ай{4}$',
                    f'${5}  нсн{5}$',
                    f'${6}дми ло{6}$',
                    f'%321456%',
                    f'&00&',
                    f'&14&',
                    f'&21&',
                    f'&43&',
                ],
                [  # 3
                    f'${5}Трйреч{5}$',
                    f'${2}у, а{2}$',
                    f'${6}ыг асй{6}$',
                    f'${3}, инл{3}$',
                    f'${1} мз ун{1}$',
                    f'${4}добно{4}$',
                    f'%526314%',
                    f'&01&',
                    f'&31&',
                    f'&45&',
                    f'&53&',
                ],
                [  # 4
                    f'${3}Трбу{3}$',
                    f'${4}ыуйрнч{4}$',
                    f'${1},г,аеа{1}$',
                    f'${6}    й{6}$',
                    f'${5}дминсн{5}$',
                    f'${2}оз ло{2}$',
                    f'%341652%',
                    f'&05&',
                    f'&20&',
                    f'&33&',
                    f'&40&',
                ],
                [  # 5
                    f'${1}рйбнч{1}$',
                    f'${2}Ту,реа{2}$',
                    f'${6}ыг  й{6}$',
                    f'${5}, асн{5}$',
                    f'${3} минло{3}$',
                    f'${4}доз у{4}$',
                    f'%126534%',
                    f'&00&',
                    f'&23&',
                    f'&32&',
                    f'&55&',
                ],
                [  # 6
                    f'${6} и у{6}$',
                    f'${2}мзнч{2}$',
                    f'${1}Тдобеа{1}$',
                    f'${5}ырйр й{5}$',
                    f'${4},у,асн{4}$',
                    f'${3} г нло{3}$',
                    f'%621543%',
                    f'&00&',
                    f'&01&',
                    f'&10&',
                    f'&11&',
                ],
                [  # 7
                    f'${4}Туои у{4}$',
                    f'${5}ыйзнч{5}$',
                    f'${2},беа{2}$',
                    f'${3} гр й{3}$',
                    f'${1}д ,асн{1}$',
                    f'${6}рм нло{6}$',
                    f'%452316%',
                    f'&11&',
                    f'&12&',
                    f'&22&',
                    f'&23&',
                ],
                [  # 8
                    f'${6}Туйну{6}$',
                    f'${3}ыг,реч{3}$',
                    f'${5},  а а{5}$',
                    f'${4} исй{4}$',
                    f'${2}дмзнлн{2}$',
                    f'${1}роб о{1}$',
                    f'%635421%',
                    f'&13&',
                    f'&30&',
                    f'&33&',
                    f'&45&',
                ],
            ],
            'task5': [
                [  # 0
                    f'${2}оо фт{2}$',
                    f'${4}Т ждрь{4}$',
                    f'${1}отео {1}$',
                    f'${5}лышевэ{5}$',
                    f'${3}ь шат{3}$',
                    f'${6}кмьио{6}$',
                    f'%241536%',
                    f'&00&',
                    f'&24&',
                    f'&32&',
                    f'&45&',
                ],
                [  # 1
                    f'${6}Т офт{6}$',
                    f'${1}отж рь{1}$',
                    f'${5}лыед {5}$',
                    f'${2}ь еоэ{2}$',
                    f'${3}кшшвт{3}$',
                    f'${4}омьиао{4}$',
                    f'%615234%',
                    f'&14&',
                    f'&23&',
                    f'&30&',
                    f'&42&',
                ],
                [  # 2
                    f'${2}Т о фт{2}$',
                    f'${3}отжрь{3}$',
                    f'${5}лыедо {5}$',
                    f'${4}ь шеэ{4}$',
                    f'${1}кмьшвт{1}$',
                    f'${6}оиао{6}$',
                    f'%235416%',
                    f'&15&',
                    f'&25&',
                    f'&31&',
                    f'&43&',
                ],
                [  # 3
                    f'${5}Т одфт{5}$',
                    f'${6}отжрь{6}$',
                    f'${1}леео {1}$',
                    f'${4}ьышвэ{4}$',
                    f'${3}к ьшт{3}$',
                    f'${2}ом иао{2}$',
                    f'%561432%',
                    f'&12&',
                    f'&31&',
                    f'&33&',
                    f'&44&',
                ],
                [  # 4
                    f'${4}Том рь{4}$',
                    f'${1}о од {1}$',
                    f'${3}лтжеоэ{3}$',
                    f'${6}ыешвт{6}$',
                    f'${5}ь шиа{5}$',
                    f'${2}кьфто{2}$',
                    f'%413652%',
                    f'&03&',
                    f'&15&',
                    f'&41&',
                    f'&54&',
                ],
                [  # 5
                    f'${3}Тм фт{3}$',
                    f'${6}ооорь{6}$',
                    f'${2}л ждо {2}$',
                    f'${5}теевэ{5}$',
                    f'${1}ьышшт{1}$',
                    f'${4}к ьиао{4}$',
                    f'%362514%',
                    f'&03&',
                    f'&10&',
                    f'&21&',
                    f'&44&',
                ],
                [  # 6
                    f'${4}Т ждрь{4}$',
                    f'${6}отее {6}$',
                    f'${5}лышоэ{5}$',
                    f'${2}ь шивт{2}$',
                    f'${3}кмьа{3}$',
                    f'${1}оо фто{1}$',
                    f'%465231%',
                    f'&22&',
                    f'&34&',
                    f'&41&',
                    f'&54&',
                ],
                [  # 7
                    f'${2}То фт{2}$',
                    f'${5}о дрь{5}$',
                    f'${4}лтжео {4}$',
                    f'${3}ьыевэ{3}$',
                    f'${6}к шшт{6}$',
                    f'${1}омьиао{1}$',
                    f'%254316%',
                    f'&10&',
                    f'&21&',
                    f'&33&',
                    f'&44&',
                ],
                [  # 8
                    f'${6}Т жфт{6}$',
                    f'${4}отдрь{4}$',
                    f'${1}лыее {1}$',
                    f'${5}ь шоэ{5}$',
                    f'${2}кмьшвт{2}$',
                    f'${3}оо иао{3}$',
                    f'%641523%',
                    f'&21&',
                    f'&30&',
                    f'&33&',
                    f'&42&',
                ],
            ],
            'task6': [
                [  # 0
                    f'${5}И е л{5}$',
                    f'${1} сспа{1}$',
                    f'${4}октн{4}$',
                    f'${6}таенои{6}$',
                    f'${3}ткое{3}$',
                    f'${2}ыьрес!{2}$',
                    f'%514632%',
                    f'&04&',
                    f'&10&',
                    f'&22&',
                    f'&31&',
                    f'&42&',
                    f'&44&',
                ],
                [  # 1
                    f'${4}сср л{4}$',
                    f'${1}Икепа{1}$',
                    f'${2} атн{2}$',
                    f'${3}отенои{3}$',
                    f'${6}тьосе{6}$',
                    f'${5}ы ке!{5}$',
                    f'%412365%',
                    f'&00&',
                    f'&21&',
                    f'&22&',
                    f'&24&',
                    f'&42&',
                    f'&45&',
                ],
                [  # 2
                    f'${3}Исстпн{3}$',
                    f'${6} кеои{6}$',
                    f'${1}оакнс{1}$',
                    f'${2}ттрое{2}$',
                    f'${4}ьел{4}$',
                    f'${5}ы е а!{5}$',
                    f'%361245%',
                    f'&04&',
                    f'&24&',
                    f'&31&',
                    f'&43&',
                    f'&52&',
                    f'&54&',
                ],
                [  # 3
                    f'${2}Ис е л{2}$',
                    f'${6} кспа{6}$',
                    f'${5}оетн{5}$',
                    f'${3}такни{3}$',
                    f'${1}ытоое{1}$',
                    f'${4}ьрес!{4}$',
                    f'%265314%',
                    f'&05&',
                    f'&12&',
                    f'&24&',
                    f'&31&',
                    f'&42&',
                    f'&43&',
                ],
                [  # 4
                    f'${4}с е а{4}$',
                    f'${1}Икспн{1}$',
                    f'${5} аетол{5}$',
                    f'${3}отне{3}$',
                    f'${6}ткос!{6}$',
                    f'${2}ыьрел{2}$',
                    f'%415362%',
                    f'&00&',
                    f'&14&',
                    f'&23&',
                    f'&31&',
                    f'&43&',
                    f'&55&',
                ],
                [  # 5
                    f'${3}Ис е л{3}$',
                    f'${1}кспа{1}$',
                    f'${6} аетон{6}$',
                    f'${2}отни{2}$',
                    f'${4}ткосе{4}$',
                    f'${5}ыьре!{5}$',
                    f'%316245%',
                    f'&01&',
                    f'&14&',
                    f'&23&',
                    f'&31&',
                    f'&43&',
                    f'&45&',
                ],
                [  # 6
                    f'${5}Ис л{5}$',
                    f'${4} ке а{4}$',
                    f'${6}астпн{6}$',
                    f'${2}отенои{2}$',
                    f'${3}тькое{3}$',
                    f'${1}ырес!{1}$',
                    f'%546231%',
                    f'&02&',
                    f'&15&',
                    f'&21&',
                    f'&30&',
                    f'&40&',
                    f'&44&',
                ],
                [  # 7
                    f'${4}Ик т л{4}$',
                    f'${3} сна{3}$',
                    f'${5}оаепн{5}$',
                    f'${6}ткоои{6}$',
                    f'${1}ытрсе{1}$',
                    f'${2}сьее!{2}$',
                    f'%435612%',
                    f'&11&',
                    f'&13&',
                    f'&32&',
                    f'&34&',
                    f'&41&',
                    f'&45&',
                ],
                [  # 8
                    f'${3}Ис е {3}$',
                    f'${1} кста{1}$',
                    f'${4}аенпн{4}$',
                    f'${6}отоои{6}$',
                    f'${5}ткесе{5}$',
                    f'${2}ыьрл!{2}$',
                    f'%314652%',
                    f'&02&',
                    f'&14&',
                    f'&23&',
                    f'&35&',
                    f'&41&',
                    f'&50&',
                ],
            ],
            'task7': [
                [  # 0
                    f'${2}Nutncg{2}$',
                    f'${1}o hgrr{1}$',
                    f'${5}wae ya{5}$',
                    f'${4} r opp{4}$',
                    f'${3}yekfth{3}$',
                    f'${6}o i oy{6}$',
                    f'%215436%',
                ],
                [  # 1
                    f'${6}Nutncg{6}$',
                    f'${4}o hgrr{4}$',
                    f'${5}wae ya{5}$',
                    f'${2} r opp{2}$',
                    f'${3}yekfth{3}$',
                    f'${1}o i oy{1}$',
                    f'%645231%',
                ],
                [  # 2
                    f'${6}Nutncg{6}$',
                    f'${2}o hgrr{2}$',
                    f'${5}wae ya{5}$',
                    f'${3} r opp{3}$',
                    f'${1}yekfth{1}$',
                    f'${4}o i oy{4}$',
                    f'%625314%',
                ],
                [  # 3
                    f'${4}Nutncg{4}$',
                    f'${1}o hgrr{1}$',
                    f'${3}wae ya{3}$',
                    f'${6} r opp{6}$',
                    f'${2}yekfth{2}$',
                    f'${5}o i oy{5}$',
                    f'%413625%',
                ],
                [  # 4
                    f'${2}Nutncg{2}$',
                    f'${6}o hgrr{6}$',
                    f'${5}wae ya{5}$',
                    f'${1} r opp{1}$',
                    f'${3}yekfth{3}$',
                    f'${4}o i oy{4}$',
                    f'%265134%',
                ],
                [  # 5
                    f'${3}Nutncg{3}$',
                    f'${5}o hgrr{5}$',
                    f'${2}wae ya{2}$',
                    f'${1} r opp{1}$',
                    f'${4}yekfth{4}$',
                    f'${6}o i oy{6}$',
                    f'%352146%',
                ],
                [  # 6
                    f'${6}Nutncg{6}$',
                    f'${5}o hgrr{5}$',
                    f'${4}wae ya{4}$',
                    f'${2} r opp{2}$',
                    f'${1}yekfth{1}$',
                    f'${3}o i oy{3}$',
                    f'%654213%',
                ],
                [  # 7
                    f'${4}Nutncg{4}$',
                    f'${3}o hgrr{3}$',
                    f'${5}wae ya{5}$',
                    f'${2} r opp{2}$',
                    f'${6}yekfth{6}$',
                    f'${1}o i oy{1}$',
                    f'%435261%',
                ],
                [  # 8
                    f'${5}Nutncg{5}$',
                    f'${2}o hgrr{2}$',
                    f'${1}wae ya{1}$',
                    f'${4} r opp{4}$',
                    f'${6}yekfth{6}$',
                    f'${3}o i oy{3}$',
                    f'%521463%',
                ],
            ],
        }
        main_key_text = all_main_key_text[task_number]

        random_main_text_list = [chr(int(hex(random.randint(97, 122)), 16)) for _ in range(571)]
        random_key_text_list = [chr(int(hex(random.randint(97, 122)), 16)) for _ in range(435)]
        random_place = []
        random_text = []
        random_choice = 0
        num_of_tasks = len(main_key_text)
        num_of_strings = len(main_key_text[0])

        while True:
            a = random.randint(0, 570)
            t = 0
            for j in range(len(random_place)):
                if random_place[j] == a:
                    t = 1
                    break
            if t == 0:
                random_place.append(a)

            a = random.randint(0, num_of_strings - 1)
            t = 0
            for j in range(len(random_text)):
                if random_text[j] == a:
                    t = 1
                    break
            if t == 0:
                random_text.append(a)

            if len(random_text) >= num_of_strings and len(random_place) >= num_of_strings:
                random_choice = random.randint(0, 1000000) % num_of_tasks
                try:
                    file1 = open(f'{task_number}_settings.txt', 'r')
                except FileNotFoundError:
                    file1 = open(f'{task_number}_settings.txt', 'w+')
                    file1.write(str(99))
                    file1.close()
                    file1 = open(f'{task_number}_settings.txt', 'r')
                s = file1.read()
                file1.close()
                while random_choice == int(s[0]) or random_choice == int(s[1]):
                    random_choice = random.randint(0, 1000000) % num_of_tasks

                file1 = open(f'{task_number}_settings.txt', 'w+')
                s_new = ''
                s_new += s[1]
                s_new += str(random_choice)
                file1.write(str(s_new))
                file1.close()
                break

        # print(task_number)
        # print(random_choice)
        # print(main_key_text[random_choice])
        # print()

        for i in range(num_of_strings):
            random_main_text_list[random_place[i]] = main_key_text[random_choice][random_text[i]]
        trash_text = f"В{random_main_text_list[0]} этом г{random_key_text_list[0]}од{random_main_text_list[1]}у Republic o{random_main_text_list[2]}f Gamer{random_key_text_list[1]}s исполняется 1{random_main_text_list[3]}5 лет. Мы погово{random_key_text_list[2]}рили с предс{random_main_text_list[4]}тавителем бренда" \
                     f" и выя{random_main_text_list[5]}снили,{random_key_text_list[3]} как всё{random_main_text_list[6]} начиналось{random_main_text_list[7]}, какие продук{random_key_text_list[4]}ты выстреливал{random_main_text_list[8]}и ярче в{random_key_text_list[5]}сего и что отличает геймеров" \
                     f" от дру{random_main_text_list[9]}гих по{random_key_text_list[6]}купателей ПК. Привет{random_main_text_list[10]}! Наверное, нача{random_key_text_list[7]}ть стоит с истоков. Ка{random_main_text_list[11]}к возни{random_key_text_list[8]}к бренд ROG?" \
                     f" Мног{random_main_text_list[12]}ие знаю{random_key_text_list[9]}т, что в A{random_main_text_list[13]}SUS инженеры {random_key_text_list[10]}занимают важное {random_main_text_list[14]}место. Это неспроста{random_key_text_list[11]}, ведь инжене{random_main_text_list[15]}ры компании" \
                     f" с перво{random_main_text_list[16]}го дня{random_key_text_list[12]} старались делать максималь{random_main_text_list[17]}но надёжны{random_key_text_list[13]}й и производител{random_key_text_list[14]}ьный продукт. В{random_main_text_list[18]} процессе" \
                     f" разработ{random_main_text_list[19]}ки и у{random_key_text_list[15]}совершенство{random_main_text_list[20]}вания серийных проду{random_key_text_list[16]}ктов было созда{random_main_text_list[21]}но множество {random_key_text_list[17]}новых технологий" \
                     f" и фишек, {random_main_text_list[22]}устраня{random_key_text_list[18]}ющих узкие места в производительнос{random_main_text_list[23]}ти и пов{random_key_text_list[19]}ышающих удобство наладк{random_key_text_list[20]}и и тонкой" \
                     f" настройки сис{random_main_text_list[24]}темы. {random_key_text_list[21]}А кто-то понял две{random_main_text_list[25]} простых штуки{random_key_text_list[22]}. Первая: компьютер{random_main_text_list[26]}ным энтузиа{random_key_text_list[23]}стам тоже" \
                     f" нравится выж{random_main_text_list[27]}имать вс{random_key_text_list[24]}е соки из железа.{random_main_text_list[28]} Вторая: ПК-{random_key_text_list[25]}энтузиасты и геймеры {random_main_text_list[29]}— это прак{random_key_text_list[26]}тически е{random_main_text_list[30]}диная" \
                     f" аудит{random_main_text_list[31]}ория. Затем{random_key_text_list[27]} внут{random_main_text_list[32]}ренние наработки поп{random_key_text_list[28]}али на рынок{random_main_text_list[33]}? Да, вы уга{random_key_text_list[29]}дали. У нас ро{random_main_text_list[34]}дилась идея:" \
                     f" выдел{random_main_text_list[35]}ить наиболе{random_key_text_list[30]}е инновационные и те{random_main_text_list[36]}хнически {random_key_text_list[31]}заряженные устройс{random_main_text_list[37]}тва в отдел{random_key_text_list[32]}ьный бренд" \
                     f" Republi{random_main_text_list[38]}c of Gam{random_key_text_list[33]}ers. Так в 20{random_main_text_list[39]}06 году появил{random_key_text_list[34]}ась матери{random_main_text_list[40]}нская плата {random_key_text_list[35]}ROG Cross{random_main_text_list[41]}hair Extreme" \
                     f" для про{random_main_text_list[42]}цессоров {random_key_text_list[36]}AMD, а следом з{random_main_text_list[43]}а ней {random_key_text_list[37]}— ROG Command{random_main_text_list[44]}o на попул{random_key_text_list[38]}ярном чипсете Int{random_main_text_list[45]}el P965." \
                     f" Обе пла{random_main_text_list[46]}ты позвол{random_key_text_list[39]}яли оверклок{random_main_text_list[47]}ерам выжим{random_key_text_list[40]}ать из систем{random_main_text_list[48]}ы максимум б{random_key_text_list[41]}ыстродействия,{random_main_text_list[49]} они были горячо" \
                     f" восп{random_main_text_list[50]}риняты энту{random_key_text_list[42]}зиастами и жу{random_main_text_list[51]}рналистами.{random_key_text_list[43]} В итоге получи{random_main_text_list[52]}лось даже луч{random_key_text_list[44]}ше, чем з{random_main_text_list[53]}агадывали:" \
                     f" бре{random_main_text_list[54]}нд, который {random_key_text_list[45]}дол{random_main_text_list[55]}жен был предл{random_key_text_list[46]}агать крут{random_main_text_list[56]}ые продукты{random_key_text_list[47]}, стал во мно{random_main_text_list[57]}гом формировать спрос" \
                     f" на ко{random_main_text_list[58]}мпьютерный{random_key_text_list[48]} гейминг. Получа{random_main_text_list[59]}ется, изна{random_key_text_list[49]}чально вы целились в лю{random_main_text_list[60]}бителе{random_key_text_list[50]}й мощных десктопов," \
                     f" а игр{random_main_text_list[61]}овая аудит{random_key_text_list[51]}ори{random_main_text_list[62]}я с ними {random_key_text_list[52]}просто пер{random_main_text_list[63]}есекалась? {random_key_text_list[53]}Не совсем. 1{random_main_text_list[64]}5 лет назад продукты ROG" \
                     f" разраб{random_main_text_list[65]}атывали{random_key_text_list[54]}сь в перву{random_main_text_list[66]}ю очер{random_key_text_list[55]}едь для ПК-э{random_main_text_list[67]}нтузиасто{random_key_text_list[56]}в и любителей, кото{random_main_text_list[68]}рые хотели получить" \
                     f" о{random_main_text_list[69]}т компьютер{random_key_text_list[57]}а или {random_main_text_list[70]}ноутбука {random_key_text_list[58]}макс{random_main_text_list[71]}имум производ{random_key_text_list[59]}ительности. И т{random_main_text_list[72]}ак уж вышло, что те же самые" \
                     f" люд{random_main_text_list[73]}и двигал{random_key_text_list[60]}и гейми{random_main_text_list[74]}нг вперёд.{random_key_text_list[61]} Это он{random_main_text_list[75]}и собирали ко{random_key_text_list[62]}мпьютеры по{random_main_text_list[76]}д условный «Крайзис». То есть" \
                     f" равн{random_main_text_list[77]}ялись м{random_key_text_list[63]}ы на тех, кто б{random_main_text_list[78]}рал {random_key_text_list[64]}топовое железо и {random_main_text_list[79]}запуск{random_key_text_list[65]}ал на нём АА{random_main_text_list[80]}А-хиты. После успеха" \
                     f" пе{random_main_text_list[81]}рвых прод{random_key_text_list[66]}уктов к{random_main_text_list[82]}омпания привл{random_key_text_list[67]}екла лучших оверк{random_main_text_list[83]}локеров к {random_key_text_list[68]}созданию материн{random_main_text_list[84]}ских плат" \
                     f" и вид{random_main_text_list[85]}еокар{random_key_text_list[69]}т ROG. Так{random_main_text_list[86]} удалось зак{random_key_text_list[70]}репить лиде{random_main_text_list[87]}рство на рынк{random_key_text_list[71]}е по ко{random_main_text_list[88]}личеству рекордов, установленных" \
                     f" с испол{random_main_text_list[89]}ьзова{random_key_text_list[72]}нием наших продукт{random_main_text_list[90]}ов, {random_key_text_list[73]}которое сохраняе{random_main_text_list[91]}тся и {random_key_text_list[74]}сегодня. Многие{random_main_text_list[92]} новые технологии," \
                     f" раз{random_main_text_list[93]}работанные{random_key_text_list[75]} для ROG, пр{random_main_text_list[94]}оходили об{random_key_text_list[76]}катку у ма{random_main_text_list[95]}ксимально т{random_key_text_list[77]}ребовательной ау{random_main_text_list[96]}дитории, а затем" \
                     f" появлял{random_main_text_list[97]}ись в {random_key_text_list[78]}более массовых линей{random_main_text_list[98]}ках.{random_key_text_list[79]} ROG в Р{random_main_text_list[99]}оссии присутс{random_key_text_list[80]}твует уже 15 л{random_main_text_list[100]}ет, за это время явно" \
                     f" нако{random_main_text_list[101]}пились я{random_key_text_list[81]}ркие воспоми{random_main_text_list[102]}нания. Что {random_key_text_list[82]}самое интересн{random_main_text_list[103]}ое прои{random_key_text_list[83]}зошло за эти годы? Был {random_main_text_list[104]}у нас один…" \
                     f" курье{random_main_text_list[105]}зный сл{random_key_text_list[84]}учай на заре с{random_main_text_list[106]}тановлени{random_key_text_list[85]}я бренда в{random_main_text_list[107]} РФ. Олды {random_key_text_list[86]}помнят, что раньше {random_main_text_list[108]}в комплекте со всеми" \
                     f" видео{random_main_text_list[109]}картами{random_key_text_list[87]} шёл CD с дра{random_main_text_list[110]}йверами. {random_key_text_list[88]}Как-то ра{random_main_text_list[111]}з в представ{random_key_text_list[89]}ительство AS{random_main_text_list[112]}US обратилась женщина" \
                     f" с необ{random_main_text_list[113]}ычной {random_key_text_list[90]}проблемой. Он{random_main_text_list[114]}а спросил{random_key_text_list[91]}а, почему{random_main_text_list[115]} на диске дл{random_key_text_list[92]}я видеокарты з{random_main_text_list[116]}аписан фильм для взрослых." \
                     f" Как {random_main_text_list[117]}вы пон{random_key_text_list[93]}имаете, CD произ{random_main_text_list[118]}водят не{random_key_text_list[94]} на том ж{random_main_text_list[119]}е заводе, что {random_key_text_list[95]}и видеокарты, {random_main_text_list[120]}а создают мастер-образ" \
                     f" и п{random_main_text_list[121]}еред{random_key_text_list[96]}ают {random_main_text_list[122]}его подрядчику. Как{random_key_text_list[97]} оказ{random_main_text_list[123]}алось, инженер, ответст{random_key_text_list[98]}венный за {random_main_text_list[124]}подготовку мастер-копии," \
                     f" то л{random_main_text_list[125]}и запис{random_key_text_list[99]}ал не тот файл, то{random_main_text_list[126]} ли о{random_key_text_list[100]}тправил не тот об{random_main_text_list[127]}раз… Ну и п{random_key_text_list[101]}о миру разо{random_main_text_list[128]}шлась партия видеокарт" \
                     f" с сю{random_main_text_list[129]}рпризом{random_key_text_list[102]}. А уже потом ма{random_main_text_list[130]}ма за{random_key_text_list[103]}стала своего сына в та{random_main_text_list[131]}кой пика{random_key_text_list[104]}нтной ситуации. В{random_main_text_list[132]}прочем, я уверен," \
                     f" чт{random_main_text_list[133]}о видеока{random_key_text_list[105]}рты RO{random_main_text_list[134]}G покупали не р{random_key_text_list[106]}ади возможно{random_main_text_list[135]}го «бонуса». В т{random_key_text_list[107]}е времена Twi{random_main_text_list[136]}tter не был особенно" \
                     f" поп{random_main_text_list[137]}улярен,{random_key_text_list[108]} поэтому опи{random_main_text_list[138]}санный слу{random_key_text_list[109]}чай не стал ви{random_main_text_list[139]}русным. Ну а {random_key_text_list[110]}с инженером, са{random_main_text_list[140]}мо собой, контракт" \
                     f" рас{random_main_text_list[141]}торгли.{random_key_text_list[111]} Раз уж вы {random_main_text_list[142]}заговорили {random_key_text_list[112]}про хороший с{random_main_text_list[143]}прос, какие пр{random_key_text_list[113]}одукты выстрелив{random_main_text_list[144]}али лучше всего?" \
                     f" Мож{random_main_text_list[145]}ет, слу{random_key_text_list[114]}чались неож{random_main_text_list[146]}иданные отк{random_key_text_list[115]}рытия? Скажем, {random_main_text_list[147]}привезли как{random_key_text_list[116]}ую-то штуку {random_main_text_list[148]}нишевую в качестве" \
                     f" эксп{random_main_text_list[149]}еримент{random_key_text_list[117]}а, а потом от {random_main_text_list[150]}заказов {random_key_text_list[118]}было неку{random_main_text_list[151]}да деваться. Если{random_key_text_list[119]} говорить п{random_main_text_list[152]}ро сумасшедший спрос," \
                     f" то {random_main_text_list[153]}вспомнил{random_key_text_list[120]}ась такая {random_main_text_list[154]}история. При{random_key_text_list[121]}мерно {random_main_text_list[155]}к 2014 году в портфе{random_key_text_list[122]}ле ROG сфо{random_main_text_list[156]}рмировалась экосистема" \
                     f" прод{random_main_text_list[157]}уктов д{random_key_text_list[123]}ля самой тре{random_main_text_list[158]}бовательно{random_key_text_list[124]}й ауди{random_main_text_list[159]}тории. Помимо оверкл{random_key_text_list[125]}окерской {random_main_text_list[160]}линейки материнских плат" \
                     f" и G{random_main_text_list[161]}PU с мощ{random_key_text_list[126]}ной системо{random_main_text_list[162]}й охлаждени{random_key_text_list[127]}я появил{random_main_text_list[163]}ись игровые ноутбук{random_key_text_list[128]}и, геймер{random_main_text_list[164]}ская периферия, мониторы" \
                     f" и пр{random_main_text_list[165]}оизводи{random_key_text_list[129]}тельные дескт{random_main_text_list[166]}опы. Мони{random_key_text_list[130]}торы сер{random_main_text_list[167]}ии ROG Swift стали {random_key_text_list[131]}первыми {random_main_text_list[168]}решениями на рынке," \
                     f" подд{random_main_text_list[169]}ерживаю{random_key_text_list[132]}щими частоту об{random_main_text_list[170]}новлен{random_key_text_list[133]}ия экрана 16{random_main_text_list[171]}5 Гц и те{random_key_text_list[134]}хнологию NVID{random_key_text_list[135]}IA G-{random_main_text_list[172]}Syn{random_key_text_list[136]}c." \
                     f" Пон{random_main_text_list[173]}ачалу {random_key_text_list[137]}не все" \
                     f" пони{random_main_text_list[174]}мали, ч{random_key_text_list[138]}то даё{random_main_text_list[175]}т новая техно{random_key_text_list[139]}логия, но пото{random_main_text_list[176]}м народ рас{random_key_text_list[140]}пробовал гейми{random_main_text_list[177]}нг с низкой задержкой" \
                     f" выво{random_main_text_list[178]}да карт{random_key_text_list[141]}инки. {random_main_text_list[179]}Спрос появил{random_key_text_list[142]}ся не только у {random_main_text_list[180]}профессиона{random_key_text_list[143]}льных киберспор{random_main_text_list[181]}тсменов и энтузиастов," \
                     f" но {random_main_text_list[182]}и обычны{random_key_text_list[144]}х игрок{random_main_text_list[183]}ов. Производ{random_key_text_list[145]}ство натуральн{random_main_text_list[184]}о не поспев{random_key_text_list[146]}ало за продажами. {random_main_text_list[185]}История с ажиотажным" \
                     f" спро{random_main_text_list[186]}сом на {random_key_text_list[147]}G-Sync з{random_main_text_list[187]}апомнилась {random_key_text_list[148]}многим в то вре{random_main_text_list[188]}мя. А что-н{random_key_text_list[149]}ибудь ещё непредска{random_main_text_list[189]}зуемое было? Из" \
                     f" недав{random_main_text_list[190]}него м{random_key_text_list[150]}ожно вспо{random_main_text_list[191]}мнить запу{random_key_text_list[151]}ск ROG Phone. На{random_main_text_list[192]}чнём с тог{random_key_text_list[152]}о, что запуск новой с{random_main_text_list[193]}ерии — это всегда" \
                     f" вызо{random_main_text_list[194]}в для к{random_key_text_list[153]}омпании п{random_main_text_list[195]}о множеств{random_key_text_list[154]}у причин. Надо пре{random_main_text_list[196]}дугадать{random_key_text_list[155]}, что хочет аудитория{random_main_text_list[197]}. Нужно донести до" \
                     f" потре{random_main_text_list[198]}бителе{random_key_text_list[156]}й, что у т{random_main_text_list[199]}ебя есть р{random_key_text_list[157]}ешение их проблемы.{random_main_text_list[200]} Надо {random_key_text_list[158]}не облажаться с продукт{random_main_text_list[201]}ом… И так далее." \
                     f" Если {random_main_text_list[202]}вспомн{random_key_text_list[159]}ить запуск {random_main_text_list[203]}смартфона{random_key_text_list[160]} ROG Phone, это была{random_main_text_list[204]} чист{random_key_text_list[161]}ой воды авантюра, но в{random_main_text_list[205]}едь выстрелило!" \
                     f" Да, м{random_main_text_list[206]}ы столк{random_key_text_list[162]}нулись с не{random_main_text_list[207]}которой {random_key_text_list[163]}критикой. Нас п{random_main_text_list[208]}ытались уб{random_key_text_list[164]}едить, что нет понят{random_main_text_list[209]}ия «игровой телефон»" \
                     f" и не{random_main_text_list[210]}т таких {random_key_text_list[165]}игр, ради {random_main_text_list[211]}которых л{random_key_text_list[166]}юди захотят с{random_main_text_list[212]}менить гадже{random_key_text_list[167]}т. Но спрос на наш{random_main_text_list[213]}и геймерские смартфоны" \
                     f" еже{random_main_text_list[214]}годно рас{random_key_text_list[168]}тёт уже 4 п{random_main_text_list[215]}околения{random_key_text_list[169]} подряд, у ап{random_main_text_list[216]}парата появил{random_key_text_list[170]}ись конкуренты, {random_main_text_list[217]}да и на мобильном рынке" \
                     f" разв{random_main_text_list[218]}ернулась{random_key_text_list[171]} настоящая в{random_main_text_list[219]}ойна за {random_key_text_list[172]}аудиторию. К {random_main_text_list[220]}слову, о кон{random_key_text_list[173]}курентах. Случ{random_main_text_list[221]}ались ли проблемы" \
                     f" с пов{random_main_text_list[222]}едением{random_key_text_list[174]} конкурентов н{random_main_text_list[223]}а рынке?{random_key_text_list[175]} Знаете, тут{random_main_text_list[224]} вы в точку{random_key_text_list[176]}. Самая большая{random_main_text_list[225]} проблема начинается," \
                     f" когд{random_main_text_list[226]}а с тобо{random_key_text_list[177]}й конкурируют н{random_main_text_list[227]}е в план{random_key_text_list[178]}е качества {random_main_text_list[228]}и инноваций{random_key_text_list[179]}, а занимаются ка{random_main_text_list[229]}рго-культом." \
                     f" Раз{random_main_text_list[230]}мывают ау{random_key_text_list[180]}диторию товарам{random_main_text_list[231]}и, котор{random_key_text_list[181]}ые только вне{random_main_text_list[232]}шне соотв{random_key_text_list[182]}етствуют атриб{random_main_text_list[233]}утам той или иной" \
                     f" ниши {random_main_text_list[234]}рынка. {random_key_text_list[183]}В момент взрыв{random_main_text_list[235]}ного рост{random_key_text_list[184]}а популярности {random_main_text_list[236]}ПК-гейм{random_key_text_list[185]}инга многие венд{random_main_text_list[237]}оры добавляли слово" \
                     f" «игро{random_main_text_list[238]}вой» к {random_key_text_list[186]}названию станда{random_main_text_list[239]}ртных пр{random_key_text_list[187]}одуктов, перекра{random_main_text_list[240]}шивали и{random_key_text_list[188]}х в модные цвета{random_main_text_list[241]}, и всё. А потом" \
                     f" люди{random_main_text_list[242]}, купивш{random_key_text_list[189]}ие ширпотреб по {random_main_text_list[243]}цене пр{random_key_text_list[190]}иличного железа, {random_main_text_list[244]}испытыв{random_key_text_list[191]}ают фрустрацию и н{random_main_text_list[245]}егативно относятся" \
                     f" ко в{random_main_text_list[246]}сему сегме{random_key_text_list[192]}нту рынка. В те{random_main_text_list[247]} дни A{random_key_text_list[193]}SUS не поступилась{random_main_text_list[248]} принц{random_key_text_list[194]}ипами, продолжив вып{random_main_text_list[249]}ускать топовые" \
                     f" продук{random_main_text_list[250]}ты под {random_key_text_list[195]}брендом ROG. А д{random_main_text_list[251]}ля кон{random_key_text_list[196]}куренции в более до{random_main_text_list[252]}ступн{random_key_text_list[197]}ом ценовом клас{random_main_text_list[253]}се создали линейку" \
                     f" TUF Ga{random_main_text_list[254]}ming. Он{random_key_text_list[198]}а закрывает по{random_main_text_list[255]}требнос{random_key_text_list[199]}ти более широкого к{random_main_text_list[256]}руга и{random_key_text_list[200]}гроков, при э{random_main_text_list[257]}том сохраняя" \
                     f" надёжн{random_main_text_list[258]}ость и {random_key_text_list[201]}фирменные техно{random_main_text_list[259]}логии A{random_key_text_list[202]}SUS. Как изменилас{random_main_text_list[260]}ь ваша{random_key_text_list[203]} аудитория с г{random_main_text_list[261]}одами? Что сейчас" \
                     f" выпус{random_main_text_list[262]}кает ROG{random_key_text_list[204]} и для кого? Как{random_main_text_list[263]} я уже{random_key_text_list[205]} говорил, на заре {random_main_text_list[264]}создан{random_key_text_list[206]}ия бренда ROG {random_main_text_list[265]}типичный геймер" \
                     f" зачас{random_main_text_list[266]}тую был {random_key_text_list[207]}одновременно и {random_main_text_list[267]}энтузиа{random_key_text_list[208]}стом, выбирающим с{random_main_text_list[268]}амое м{random_key_text_list[209]}ощное железо и {random_main_text_list[269]}разгоняющим его" \
                     f" для л{random_main_text_list[270]}учшей пр{random_key_text_list[210]}оизводительност{random_main_text_list[271]}и. За п{random_key_text_list[211]}оследнее десятилет{random_main_text_list[272]}ие ком{random_key_text_list[212]}пьютерный гейми{random_main_text_list[273]}нг стал гораздо" \
                     f" попул{random_main_text_list[274]}ярнее и {random_key_text_list[213]}разнообразнее. {random_main_text_list[275]}С одной{random_key_text_list[214]} стороны, многие {random_main_text_list[276]}владель{random_key_text_list[215]}цы консолей нач{random_main_text_list[277]}али играть на ПК," \
                     f" чтобы {random_main_text_list[278]}получит{random_key_text_list[216]}ь максимум от и{random_main_text_list[279]}гры в п{random_key_text_list[217]}лане графики и н{random_main_text_list[280]}е только{random_key_text_list[218]}. С другой — ак{random_main_text_list[281]}тивно выросла армия" \
                     f" любите{random_main_text_list[282]}лей онл{random_key_text_list[219]}айн-баталий. А {random_main_text_list[283]}сам кибе{random_key_text_list[220]}рспорт диверсифи{random_main_text_list[284]}цировал{random_key_text_list[221]}ся: появились н{random_main_text_list[285]}е только любители" \
                     f" казуал{random_main_text_list[286]}ьных хи{random_key_text_list[222]}тов вроде Fortn{random_main_text_list[287]}ite, но {random_key_text_list[223]}и профессиональн{random_main_text_list[288]}ые атле{random_key_text_list[224]}ты в любой игре{random_main_text_list[289]}. Вообще любой." \
                     f" Соотве{random_main_text_list[290]}тственн{random_key_text_list[225]}о, для каждой и{random_main_text_list[291]}з этих м{random_key_text_list[226]}аленьких и перес{random_main_text_list[292]}екающих{random_key_text_list[227]}ся групп нужно {random_main_text_list[293]}что-то своё. Но" \
                     f" самое {random_main_text_list[294]}интерес{random_key_text_list[228]}ное, что в больш{random_main_text_list[295]}инстве {random_key_text_list[229]}случаев разные по{random_main_text_list[296]}требно{random_key_text_list[230]}сти работают на {random_main_text_list[297]}одинаковых" \
                     f" технол{random_main_text_list[298]}огиях. {random_key_text_list[231]}Просто смещается{random_main_text_list[299]} акцент{random_key_text_list[232]}. Ну и ещё стала {random_main_text_list[300]}важна {random_key_text_list[233]}вертикальная инт{random_main_text_list[301]}еграция. Вам уже" \
                     f" недост{random_main_text_list[302]}аточно {random_key_text_list[234]}просто флагманск{random_main_text_list[303]}ой мышк{random_key_text_list[235]}и или монитора дл{random_main_text_list[304]}я побе{random_key_text_list[236]}д. Чем глубже вы{random_main_text_list[305]} погружаетесь" \
                     f" в кибе{random_main_text_list[306]}рспорт,{random_key_text_list[237]} тем быстрее пони{random_main_text_list[307]}маете,{random_key_text_list[238]} что неважных эле{random_main_text_list[308]}ментов{random_key_text_list[239]} нет. Ну да, поб{random_main_text_list[309]}еда складывается" \
                     f" из мал{random_main_text_list[310]}еньких {random_key_text_list[240]}деталей. Как гово{random_main_text_list[311]}рится,{random_key_text_list[241]} «Не было гвоздя {random_main_text_list[312]}— подко{random_key_text_list[242]}ва пропала, не {random_main_text_list[313]}было подковы" \
                     f" — лоша{random_main_text_list[314]}дь захр{random_key_text_list[243]}омала»… Именно! Д{random_main_text_list[315]}ля сет{random_key_text_list[244]}евых шутеров и «к{random_main_text_list[316]}оролевс{random_key_text_list[245]}ких битв» важна{random_main_text_list[317]} производительность" \
                     f" систем{random_main_text_list[318]}ы в цел{random_key_text_list[246]}ом, позволяющая {random_main_text_list[319]}выжать {random_key_text_list[247]}максимальный фрей{random_main_text_list[320]}мрейт, {random_key_text_list[248]}а также возможн{random_main_text_list[321]}ость минимизировать" \
                     f" input {random_main_text_list[322]}lag. И т{random_key_text_list[249]}ут идеальный вы{random_main_text_list[323]}бор — г{random_key_text_list[250]}рафические адаптер{random_main_text_list[324]}ы ново{random_key_text_list[251]}го поколения, и{random_main_text_list[325]}гровая периферия ROG" \
                     f" с надё{random_main_text_list[326]}жными пе{random_key_text_list[252]}реключателями и{random_main_text_list[327]} быстры{random_key_text_list[253]}м оптическим сенсо{random_main_text_list[328]}ром, м{random_key_text_list[254]}ониторы ROG с ч{random_main_text_list[329]}астотой обновления" \
                     f" 360 Гц{random_main_text_list[330]}. Чтобы {random_key_text_list[255]}гарантировать с{random_main_text_list[331]}корость {random_key_text_list[256]}соединения с игро{random_main_text_list[332]}выми с{random_key_text_list[257]}ерверами, Repub{random_main_text_list[333]}lic of Gamers" \
                     f" предлаг{random_main_text_list[334]}ает сер{random_key_text_list[258]}ию беспроводных{random_main_text_list[335]} роутеро{random_key_text_list[259]}в, поддерживающих{random_main_text_list[336]} серви{random_key_text_list[260]}с WTFast. Након{random_main_text_list[337]}ец, мобильный" \
                     f" гейминг{random_main_text_list[338]} ежегод{random_key_text_list[261]}но растёт. Тем,{random_main_text_list[339]} кто хоч{random_key_text_list[262]}ет запускать люби{random_main_text_list[340]}мые рел{random_key_text_list[263]}изы на смартфо{random_main_text_list[341]}не с максимальным" \
                     f" комфорт{random_main_text_list[342]}ом, ком{random_key_text_list[264]}пания предлагае{random_main_text_list[343]}т ROG Pho{random_key_text_list[265]}ne 5. В прошлом {random_main_text_list[344]}году ли{random_key_text_list[266]}нейку мобильны{random_main_text_list[345]}х продуктов" \
                     f" пополни{random_main_text_list[346]}ли мони{random_key_text_list[267]}торы USB-C с час{random_main_text_list[347]}тотой об{random_key_text_list[268]}новления 240 Гц, {random_main_text_list[348]}позвол{random_key_text_list[269]}яющие зарубит{random_main_text_list[349]}ься на телефоне" \
                     f" или но{random_main_text_list[350]}утбуке в {random_key_text_list[270]}популярные хиты{random_main_text_list[351]} с высок{random_key_text_list[271]}им fps. Геймеры п{random_main_text_list[352]}ользую{random_key_text_list[272]}тся разными ус{random_main_text_list[353]}тройствами." \
                     f" Как вы{random_main_text_list[354]} думаете,{random_key_text_list[273]} что отличает эт{random_main_text_list[355]}у аудит{random_key_text_list[274]}орию от других пол{random_main_text_list[356]}ьзова{random_key_text_list[275]}телей? Что она{random_main_text_list[357]} больше всего ценит?" \
                     f" Конеч{random_main_text_list[358]}но же, для{random_key_text_list[276]} геймера главно{random_main_text_list[359]}е — игра,{random_key_text_list[277]} а если ещё точне{random_main_text_list[360]}е: по{random_key_text_list[278]}лучение удовол{random_main_text_list[361]}ьствия от процесса," \
                     f" и удов{random_main_text_list[362]}ольствие {random_key_text_list[279]}это для каждого {random_main_text_list[363]}своё. Кт{random_key_text_list[280]}о-то хочет погруз{random_main_text_list[364]}иться{random_key_text_list[281]} с головой в д{random_main_text_list[365]}ругой мир," \
                     f" которы{random_main_text_list[366]}й сложно {random_key_text_list[282]}отличить от реаль{random_main_text_list[367]}ного. Н{random_key_text_list[283]}апример, попасть {random_main_text_list[368]}на Ди{random_key_text_list[284]}кий Запад в RDR{random_main_text_list[369]}2 или на улицы" \
                     f" неоно{random_main_text_list[370]}вого мегап{random_key_text_list[285]}олиса в Cyberpunk{random_main_text_list[371]} 2077. {random_key_text_list[286]}Кто-то кайфует от{random_main_text_list[372]} онла{random_key_text_list[287]}йн-побед в Warz{random_main_text_list[373]}one, Dota2" \
                     f" или п{random_main_text_list[374]}отому, что{random_key_text_list[288]} первым добегает {random_main_text_list[375]}до фини{random_key_text_list[289]}ша в Fall Guys. Мн{random_main_text_list[376]}огим{random_key_text_list[290]} необходимо общ{random_main_text_list[377]}ение, но абсолютно" \
                     f" каждо{random_main_text_list[378]}му важно, {random_key_text_list[291]}чтобы всё работал{random_main_text_list[379]}о без п{random_key_text_list[292]}роблем. Безусловн{random_main_text_list[380]}о, мы{random_key_text_list[293]} стараемся сдел{random_main_text_list[381]}ать продукты ROG" \
                     f" не тол{random_main_text_list[382]}ько самым{random_key_text_list[294]}и производительны{random_main_text_list[383]}ми, но {random_key_text_list[295]}и надёжными. Испол{random_main_text_list[384]}ьзуе{random_key_text_list[296]}м многоступенча{random_main_text_list[385]}тое тестирование," \
                     f" приме{random_main_text_list[386]}няем лучшу{random_key_text_list[297]}ю элементную базу.{random_main_text_list[387]} Это п{random_key_text_list[298]}озволяет предостав{random_main_text_list[388]}лять {random_key_text_list[299]}расширенную га{random_main_text_list[389]}рантийную политику:" \
                     f" дават{random_main_text_list[390]}ь больше з{random_key_text_list[300]}а те же деньги. Та{random_main_text_list[391]}к, нап{random_key_text_list[301]}ример, для пользова{random_main_text_list[392]}теле{random_key_text_list[302]}й ноутбуков RO{random_main_text_list[393]}G доступно" \
                     f" преми{random_main_text_list[394]}альное обс{random_key_text_list[303]}луживание по прин{random_main_text_list[395]}ципу pi{random_key_text_list[304]}ck up and return: {random_main_text_list[396]}при н{random_key_text_list[305]}аступлении гар{random_main_text_list[397]}антийного случая" \
                     f" курьер{random_main_text_list[398]} заберёт {random_key_text_list[306]}лэптоп в сервис и{random_main_text_list[399]} достав{random_key_text_list[307]}ит его обратно посл{random_main_text_list[400]}е ре{random_key_text_list[308]}монта. Геймера{random_main_text_list[401]}м важно," \
                     f" как вы{random_main_text_list[402]}глядит и {random_key_text_list[309]}ощущается продукт{random_main_text_list[403]}. Поско{random_key_text_list[310]}льку во время панд{random_main_text_list[404]}емии {random_key_text_list[311]}сложно посеща{random_main_text_list[405]}ть магазины, мы" \
                     f" начали{random_main_text_list[406]} снимать {random_key_text_list[312]}ролики с анбоксин{random_main_text_list[407]}гом нов{random_key_text_list[313]}инок, которые дост{random_main_text_list[408]}упны {random_key_text_list[314]}на YouTube-ка{random_main_text_list[409]}нале ROG" \
                     f" Russ{random_main_text_list[410]}ia." \
                     f" А ка{random_main_text_list[411]}к вы относи{random_key_text_list[315]}тесь к RGB-подсве{random_main_text_list[412]}тке в иг{random_key_text_list[316]}ровых устройствах{random_main_text_list[413]}, на {random_key_text_list[317]}тему которой {random_main_text_list[414]}так любят шутить" \
                     f" в ин{random_main_text_list[415]}тернете? RG{random_key_text_list[318]}B-подсветка стала{random_main_text_list[416]} мемом и{random_key_text_list[319]} зачастую восприн{random_main_text_list[417]}имает{random_key_text_list[320]}ся как призна{random_main_text_list[418]}к дурного тона." \
                     f" Она {random_main_text_list[419]}не всегда п{random_key_text_list[321]}рименяется с умом{random_main_text_list[420]} как изг{random_key_text_list[322]}отовителями железа{random_main_text_list[421]}, та{random_key_text_list[323]}к и пользоват{random_main_text_list[422]}елями. Последние" \
                     f" часто{random_main_text_list[423]} даже не в{random_key_text_list[324]}ключают синхрониз{random_main_text_list[424]}ацию под{random_key_text_list[325]}светки, а ведь ASU{random_main_text_list[425]}S Au{random_key_text_list[326]}ra Sync реаль{random_main_text_list[426]}но позволяет делать" \
                     f" очень{random_main_text_list[427]} крутые эф{random_key_text_list[327]}фекты, соединяя п{random_main_text_list[428]}одсветку{random_key_text_list[328]} всех устройств. Д{random_main_text_list[429]}изай{random_key_text_list[329]}неры ROG обла{random_main_text_list[430]}дают чувством" \
                     f" вкуса {random_main_text_list[431]}и умеренн{random_key_text_list[330]}ости. Даже если, {random_main_text_list[432]}допустим{random_key_text_list[331]}, будет выпущен па{random_main_text_list[433]}уэрб{random_key_text_list[332]}анк ROG с RGB{random_main_text_list[434]}-подсветкой, он" \
                     f" будет {random_main_text_list[435]}настолько {random_key_text_list[333]}элегантным и при{random_main_text_list[436]}влекател{random_key_text_list[334]}ьным аксессуаром, ч{random_main_text_list[437]}то {random_key_text_list[335]}в целях безоп{random_main_text_list[438]}асности нам придётся" \
                     f" рекоме{random_main_text_list[439]}ндовать не{random_key_text_list[336]} класть его в нар{random_main_text_list[440]}ужный к{random_key_text_list[337]}арман рюкзака во вр{random_main_text_list[441]}емя{random_key_text_list[338]} уличных прогу{random_main_text_list[442]}лок в тёмное время" \
                     f" суток. {random_main_text_list[443]}Ладно, те{random_key_text_list[339]}перь перейдём к сл{random_main_text_list[444]}ожным {random_key_text_list[340]}вопросам. Как думае{random_main_text_list[445]}те,{random_key_text_list[341]} когда закончи{random_main_text_list[446]}тся дефицит" \
                     f" игровог{random_main_text_list[447]}о железа?{random_key_text_list[342]} Ох, ну и вопросы {random_main_text_list[448]}у вас…{random_key_text_list[343]} Так, давайте попро{random_main_text_list[449]}буе{random_key_text_list[344]}м разложить пр{random_main_text_list[450]}облему на" \
                     f" составл{random_main_text_list[451]}яющие. Для{random_key_text_list[345]} определения сего{random_main_text_list[452]}дняшне{random_key_text_list[346]}й ситуации больше п{random_main_text_list[453]}одхо{random_key_text_list[347]}дит термин «с{random_main_text_list[454]}прос, значительно" \
                     f" превышаю{random_main_text_list[455]}щий предл{random_key_text_list[348]}ожение». Товаров{random_main_text_list[456]} на рын{random_key_text_list[349]}ке не хватает не по{random_main_text_list[457]}тому{random_key_text_list[350]}, что их мень{random_main_text_list[458]}ше производят." \
                     f" Просто с{random_main_text_list[459]}прос наст{random_key_text_list[351]}олько вырос, что{random_main_text_list[460]} не уда{random_key_text_list[352]}ётся удовлетворить {random_main_text_list[461]}все {random_key_text_list[353]}заказы, — при{random_main_text_list[462]}чём даже производя" \
                     f" больш{random_main_text_list[463]}е продукции, {random_key_text_list[354]}чем годом ранее{random_main_text_list[464]}. Здесь{random_key_text_list[355]} виноваты не злые в{random_main_text_list[465]}ендо{random_key_text_list[356]}ры, которые х{random_main_text_list[466]}отят отгружать" \
                     f" комп{random_main_text_list[467]}лектующие втр{random_key_text_list[357]}идорога. Мы бы с{random_main_text_list[468]} радост{random_key_text_list[358]}ью продали втрое бо{random_main_text_list[469]}льше{random_key_text_list[359]}, но в соврем{random_main_text_list[470]}енной экономике всё" \
                     f" вза{random_main_text_list[471]}имосвязано. Вы{random_key_text_list[360]} не можете прост{random_main_text_list[472]}о взять{random_key_text_list[361]} в три раза больше л{random_main_text_list[473]}юде{random_key_text_list[362]}й и оборудова{random_main_text_list[474]}ния, чтобы увеличить" \
                     f" прои{random_main_text_list[475]}зводительност{random_key_text_list[363]}ь на 200%. Есть {random_main_text_list[476]}цепочки {random_key_text_list[364]}поставок, и они час{random_main_text_list[477]}то {random_key_text_list[365]}ограничивают {random_main_text_list[478]}возможности компаний" \
                     f" в та{random_main_text_list[479]}ких непростых{random_key_text_list[366]} ситуациях. Рост{random_main_text_list[480]} произво{random_key_text_list[367]}дства ограничен нех{random_main_text_list[481]}ват{random_key_text_list[368]}кой полупрово{random_main_text_list[482]}дников, вызванной" \
                     f" боль{random_main_text_list[483]}шим лагом в п{random_key_text_list[369]}ланировании чипм{random_main_text_list[484]}ейкерами{random_key_text_list[370]} и прошлогодним лок{random_main_text_list[485]}даун{random_key_text_list[371]}ом из-за COV{random_main_text_list[486]}ID-19. С другой" \
                     f" стор{random_main_text_list[487]}оны, криптова{random_key_text_list[372]}лютный бум привё{random_main_text_list[488]}л к взры{random_key_text_list[373]}вному увеличению сп{random_main_text_list[489]}роса{random_key_text_list[374]} на графическ{random_main_text_list[490]}ие адаптеры." \
                     f" Майн{random_main_text_list[491]}еры готовы по{random_key_text_list[375]}купать видеокарт{random_main_text_list[492]}ы по выс{random_key_text_list[376]}оким ценам. И что т{random_main_text_list[493]}еперь{random_key_text_list[377]} делать гейм{random_main_text_list[494]}ерам? Цены на GPU" \
                     f" дост{random_main_text_list[495]}игли уровня, {random_key_text_list[378]}когда геймерам в{random_main_text_list[496]}ыгоднее{random_key_text_list[379]} приобрести готовый {random_main_text_list[497]}дескт{random_key_text_list[380]}оп или ноутб{random_main_text_list[498]}ук, где зачастую" \
                     f" стои{random_main_text_list[499]}мость системы{random_key_text_list[381]} ниже цены самог{random_main_text_list[500]}о видео{random_key_text_list[382]}адаптера. То, что люд{random_main_text_list[501]}и б{random_key_text_list[383]}ыли вынуждены{random_main_text_list[502]} находиться дома" \
                     f" из-з{random_main_text_list[503]}а коронавирус{random_key_text_list[384]}ных ограничений, {random_main_text_list[504]}привел{random_key_text_list[385]}о к росту спроса на э{random_main_text_list[505]}лек{random_key_text_list[386]}тронику в цел{random_main_text_list[506]}ом и на игровые" \
                     f" устр{random_main_text_list[507]}ойства особен{random_key_text_list[387]}но. NVIDIA, начин{random_main_text_list[508]}ая с м{random_key_text_list[388]}оделей RTX 3070 Ti и {random_main_text_list[509]}RTX{random_key_text_list[389]} 3080 Ti, про{random_main_text_list[510]}изводит версии" \
                     f" с ог{random_main_text_list[511]}раниченной пр{random_key_text_list[390]}оизводительностью{random_main_text_list[512]} в май{random_key_text_list[391]}нинге, что может обес{random_main_text_list[513]}печи{random_key_text_list[392]}ть геймерам {random_main_text_list[514]}лучшую доступность" \
                     f" этих{random_main_text_list[515]} компонентов.{random_key_text_list[393]} Если же эта иниц{random_main_text_list[516]}иатива{random_key_text_list[394]} не поможет, то спрос{random_main_text_list[517]} и п{random_key_text_list[395]}редложение {random_main_text_list[518]}ещё долго могут не" \
                     f" прий{random_main_text_list[519]}ти в равновес{random_key_text_list[396]}ие. По крайней ме{random_main_text_list[520]}ре, в о{random_key_text_list[397]}бозримой перспективе{random_main_text_list[521]} буд{random_key_text_list[398]}ет трудно с{random_main_text_list[522]}ущественно увеличить" \
                     f" произ{random_main_text_list[523]}водство чипо{random_key_text_list[399]}в. А низкая доход{random_main_text_list[524]}ность т{random_key_text_list[400]}радиционных финансовы{random_main_text_list[525]}х и{random_key_text_list[401]}нструментов{random_main_text_list[526]} толкает инвесторов" \
                     f" к вло{random_main_text_list[527]}жениям в кри{random_key_text_list[402]}птовалюты, что ув{random_main_text_list[528]}еличива{random_key_text_list[403]}ет доходность от майн{random_main_text_list[529]}инг{random_key_text_list[404]}а и спрос на{random_main_text_list[530]} видеокарты." \
                     f" Нескол{random_main_text_list[531]}ько лет наз{random_key_text_list[405]}ад запустили прог{random_main_text_list[532]}рамму P{random_key_text_list[406]}owered By ASUS для па{random_main_text_list[533]}ртн{random_key_text_list[407]}ёров, которы{random_main_text_list[534]}е производят мощные" \
                     f" игровы{random_main_text_list[535]}е ПК. Мы от{random_key_text_list[408]}даём приоритет та{random_main_text_list[536]}ким ком{random_key_text_list[409]}паниям при распределе{random_main_text_list[537]}нии{random_key_text_list[410]} горячих тов{random_main_text_list[538]}аров, чтобы" \
                     f" подде{random_main_text_list[539]}ржать геймер{random_key_text_list[411]}ов. Для ASUS игро{random_main_text_list[540]}ки стал{random_key_text_list[412]}и важной аудиторией {random_main_text_list[541]}15 ле{random_key_text_list[413]}т назад, ког{random_main_text_list[542]}да компьютерный" \
                     f" гейм{random_main_text_list[543]}инг не был ма{random_key_text_list[414]}ссовым. Я уверен,{random_main_text_list[544]} что ге{random_key_text_list[415]}ймеры останутся само{random_main_text_list[545]}й важ{random_key_text_list[416]}ной аудитор{random_main_text_list[546]}ией для компании" \
                     f" и за{random_main_text_list[547]}втра. Раз уж м{random_key_text_list[417]}ы заговорили про{random_main_text_list[548]} перспе{random_key_text_list[418]}ктивы, как планирует{random_main_text_list[549]}е раз{random_key_text_list[419]}вивать брен{random_main_text_list[550]}д ROG? Что нас" \
                     f" ждёт{random_main_text_list[551]}? Нейроинтерфе{random_key_text_list[420]}йсы, наноботы и {random_main_text_list[552]}кибероп{random_key_text_list[421]}тика — может быть, и{random_main_text_list[553]} этим{random_key_text_list[422]} займёмся. {random_main_text_list[554]}Кто знает?" \
                     f" Сего{random_main_text_list[555]}дня можно сказ{random_key_text_list[423]}ать одно: ROG — {random_main_text_list[556]}экосисте{random_key_text_list[424]}ма продуктов для ге{random_main_text_list[557]}ймера{random_key_text_list[425]}, отвечающа{random_main_text_list[558]}я самым высоким" \
                     f" запр{random_main_text_list[559]}осам. Мы продо{random_key_text_list[426]}лжим работать на{random_main_text_list[560]}д тем, ч{random_key_text_list[427]}тобы удержать эту {random_main_text_list[561]}планку{random_key_text_list[428]} и поднять {random_main_text_list[562]}её на новый" \
                     f" урове{random_main_text_list[563]}нь. И если иг{random_key_text_list[429]}ры эволюционируют{random_main_text_list[564]} до пря{random_key_text_list[430]}мого подключения в{random_main_text_list[565]} мозг,{random_key_text_list[431]} то будьте {random_main_text_list[566]}уверены: у ROG" \
                     f" будет{random_main_text_list[567]} самый быстры{random_key_text_list[432]}й и производител{random_main_text_list[568]}ьный инт{random_key_text_list[433]}ерфейс. Мы уж пост{random_main_text_list[569]}ара{random_key_text_list[434]}емс{random_main_text_list[570]}я."

        # working with trash text
        result_list = []
        for i in range(len(trash_text)):
            xored_arg = ord(trash_text[i % len(trash_text)]) ^ ord(xor_text[i % len(xor_text)]) \
                # ^ ord(xor_text[i % len(xor_text)]) - for check
            result_list.append(f'{hex(xored_arg)}')  # (f'{chr(int(hex(xored_arg), 16))}') - for check
        result_output = '/'.join(result_list)
        # print(result_output)
        # print(trash_text)

        # working with output file
        file1 = open(f'{task_number}.txt', 'w+')
        file1.write(result_output)

        file1.close()

        self.menu.entryconfig('Выберете функцию', state='normal')
        clear_global_variables()
        self.update_current_function(0)


if __name__ == '__main__':  # run program
    MainWindow()  # call window showing class
