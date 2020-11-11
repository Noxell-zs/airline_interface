import tkinter


def main():
    about = tkinter.Tk()
    about.title('О программе')
    about.configure(background='lightcyan')
    about.geometry('600x150')

    tkinter.Label(about,
                  font='Arial 13',
                  background='lightcyan',
                  wraplength=600,
                  justify=tkinter.LEFT,
                  text='Descriptions of the business process of reservation '
                       'seats in the airline with graphical interface'
                  ).pack(expand=1, anchor=tkinter.NW)

    texts = (
        'Version: 0.1',
        'Author: Semen Zamolotskii',
        'Email: semrole@yandex.ru',
        'Website: https://github.com/Noxell-zs/airline_interface')

    for i, t in enumerate(texts):
        tkinter.Label(about,
                      background='lightcyan',
                      justify=tkinter.LEFT,
                      text=t).pack(expand=1, anchor=tkinter.SW)

    about.mainloop()


if __name__ == '__main__':
    main()
