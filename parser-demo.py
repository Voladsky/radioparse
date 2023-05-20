import tkinter as tk
import time


def start_button_click():
    if agreed.get() == 1:

        def parse_click():
            # tyt parsitsya raspisanie
            parse_result_text.set('...')
            root.dooneevent()
            time.sleep(2)
            parse_result_text.set(f"schedule has been parsed\n"
                                  f"для курса {course_input.get()} группы {group_input.get()}")

        manual_root.destroy()

        root = tk.Tk()
        root.bg = 'green'
        root.title('Парсер расписания на python')
        root.geometry('500x360')
        root.resizable(width=False, height=False)

        # всё про курс
        course_input = tk.IntVar(value=1)
        course_label = tk.Label(root, text="Курс:")
        course_entry = tk.Entry(root, textvariable=course_input)

        course_label.grid(row=0, column=0, rowspan=2)
        course_entry.grid(row=0, column=1, rowspan=2)

        # всё про группу
        group_input = tk.IntVar(value=1)
        group_label = tk.Label(root, text="Группа:")
        group_entry = tk.Entry(root, textvariable=group_input)

        group_label.grid(row=0, column=2, rowspan=2)
        group_entry.grid(row=0, column=3, rowspan=2)

        # кнопка парса и поле результата
        parse_button = tk.Button(root, text='Спарсить на изи', bg='lightblue', font=32, command=parse_click)
        parse_result_text = tk.StringVar(value="здесь будет результат парса...")
        parse_result_label = tk.Label(root, textvariable=parse_result_text, font=('Aerial', 17),
                                      anchor="e", justify=tk.CENTER)

        parse_button.grid(row=5, column=2, rowspan=2)
        parse_result_label.place(anchor=tk.CENTER, relx=.5, rely=.3)


    else:
        checkbox = tk.Checkbutton(manual_root, text='Я ознакомился(лась) с инструкцией по использованию программы',
                                  fg='red',
                                  variable=agreed, onvalue=1, offvalue=0, font=('Helvetica', 8, 'bold'),
                                  activeforeground='darkgreen', selectcolor='lightgray')
        checkbox.pack()
        checkbox.place(rely=0.8, relx=0)


manual_root = tk.Tk()
manual_root.title('Инструкция:')
manual_root.wm_attributes('-alpha', 0.9)
manual_root.geometry('400x450')
manual_root.resizable(width=False, height=False)

start_button = tk.Button(manual_root, text='ОК', bg='lightblue', font=100, command=start_button_click)
start_button.pack()
start_button.place(relwidth=0.2, relheight=0.075, relx=0.4, rely=0.9)

i_label = tk.Label(manual_root, font=('Helvetica', 8, 'bold'),
                   text='Перед вами появится окно приложения, которое'
                        '\n позволяет парсить расписание с сайта /URL/.'
                        '\n\n Для этого необходимо ввести курс и группу '
                        '\nзатем нажать на кнопку \"спрарсить расписание\"\n\n')
i_label.pack()

agreed = tk.IntVar()
checkbox = tk.Checkbutton(manual_root, text='Я ознакомился(лась) с инструкцией по использованию программы', fg='blue',
                          variable=agreed, onvalue=1, offvalue=0, font=('Helvetica', 8, 'bold'),
                          activeforeground='darkgreen',
                          selectcolor='lightgray')
checkbox.pack()
checkbox.place(rely=0.8, relx=0)

manual_root.mainloop()
