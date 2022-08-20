#FIND UR HOSPITAL
import webbrowser

chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

from openpyxl import load_workbook

workbook = load_workbook(filename='newhospitallist.xlsx')
sheet = workbook.active

from tkinter import *

root = Tk()
root.title('Hospital Finder')
root.geometry('1920x1080')

# Back ground

filename = PhotoImage(file="FINAL.frny (1).png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0)


def about():
    root.destroy()
    main_window2 = Tk()
    main_window2.geometry('1920x1080')

    # Background
    a = PhotoImage(file="about (1).png")
    a_label = Label(main_window2, image=a)
    a_label.place(x=0, y=0)

    def con_sig():
        f1 = Frame()
        f1.config(bg='medium blue')
        f1.place(relx=0.25, rely=0.13, width=620, height=530)

        # Lable
        qq = Label(f1, text="User ID:", font=('league spartan', 16), bg='medium blue', fg='white')
        ww = Label(f1, text="Password:", font=('league spartan', 16), bg='medium blue', fg='white')
        rr = Label(f1, text="Name:", font=('league spartan', 16), bg='medium blue', fg='white')
        ee = Label(f1, text="Sign Up", font=('league spartan', 46), bg='medium blue', fg='white')
        xx = Label(f1, text="Phone no:", font=('league spartan', 16), bg='medium blue', fg='white')

        qq.place(relx=0.14, rely=0.41, anchor=CENTER)
        ww.place(relx=0.14, rely=0.54, anchor=CENTER)
        ee.place(relx=0.52, rely=0.1, anchor=CENTER)
        rr.place(relx=0.14, rely=0.28, anchor=CENTER)
        xx.place(relx=0.14, rely=0.67, anchor=CENTER)

        # Entry
        qq_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black')
        ww_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black',show = '*')
        rr_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black')
        xx_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black')

        qq_entry.place(relx=0.61, rely=0.41, anchor=CENTER)
        ww_entry.place(relx=0.61, rely=0.54, anchor=CENTER)
        rr_entry.place(relx=0.61, rely=0.28, anchor=CENTER)
        xx_entry.place(relx=0.61, rely=0.67, anchor=CENTER)

        def sign_entry():
            qq_get = qq_entry.get()
            ww_get = ww_entry.get()
            rr_get = rr_entry.get()
            xx_get = xx_entry.get()

            if qq_get == '' or ww_get == '' or rr_get == '' or xx_get == '':
                retry = Label(f1, text="Invalid User ID or Password", font=('league spartan', 15), bg='medium blue',
                              fg='grey')
                retry.place(relx=0.5, rely=0.75, anchor=CENTER)
            else:
                print(qq_get, ww_get, rr_get, xx_get)

        # Button
        xq = Button(f1, text="Login", font=('league spartan', 18), bg='grey', fg='black', command=login_new)
        xq.place(relx=0.68, rely=0.85, anchor=CENTER)
        tt = Button(f1, text="Confirm", font=('league spartan', 17), bg='grey', fg='black', command=sign_entry)
        tt.place(relx=0.3, rely=0.85, anchor=CENTER)

    def login_new():
        f1 = Frame()
        f1.config(bg='medium blue')
        f1.place(relx=0.25, rely=0.13, width=620, height=530)

        # Lable
        user = Label(f1, text="User Id:", font=('league spartan', 30), bg='medium blue', fg='white')
        pwd = Label(f1, text="password:", font=('league spartan', 30), bg='medium blue', fg='white')
        login = Label(f1, text="Login", font=('league spartan', 46), bg='medium blue', fg='white')

        user.place(relx=0.52, rely=0.28, anchor=CENTER)
        pwd.place(relx=0.53, rely=0.54, anchor=CENTER)
        login.place(relx=0.52, rely=0.1, anchor=CENTER)

        # Entry
        user_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black')
        pwd_entry = Entry(f1, width=20, font=('league spartan', 16), bg='white', fg='black',show = '*')

        user_entry.place(relx=0.53, rely=0.41, anchor=CENTER)
        pwd_entry.place(relx=0.53, rely=0.67, anchor=CENTER)

        def login_entry():
            user_get = user_entry.get()
            pwd_get = pwd_entry.get()

            if user_get == '' or pwd_get == '':
                retry = Label(f1, text="Invalid User ID or Password", font=('league spartan', 15), bg='medium blue',
                              fg='grey')
                retry.place(relx=0.5, rely=0.75, anchor=CENTER)
            else:
                print(user_get, pwd_get)

        # Button
        su = Button(f1, text="Sign up", font=('league spartan', 18), bg='grey', fg='black', command=con_sig)
        su.place(relx=0.68, rely=0.85, anchor=CENTER)
        tt = Button(f1, text="Confirm", font=('league spartan', 18), bg='grey', fg='black', command=login_entry)
        tt.place(relx=0.3, rely=0.85, anchor=CENTER)

    def choice_new():
        main_window2.destroy()
        choice = Tk()
        choice.geometry('1920x1080')

        # Back ground

        e = PhotoImage(file="page1 (1).png")
        e_label = Label(choice, image=e)
        e_label.place(x=0, y=0)

        v = IntVar()
        Radiobutton(choice, variable=v, value=1).place(relx=0.27, rely=0.22, anchor=CENTER)
        Radiobutton(choice, variable=v, value=2).place(relx=0.27, rely=0.27, anchor=CENTER)

        def entry1():

            ee_1 = entry_1.get()

            ch = v.get()
            if ch == 1:
                def entry11():

                    special_index = entry_5.get()

                    choice1.destroy()
                    choice11 = Tk()
                    choice11.geometry('1920x1080')

                    # Back ground

                    efg = PhotoImage(file="22222222222 (1).png")
                    efg_label = Label(choice11, image=efg)
                    efg_label.place(x=0, y=0)

                    special = ['EYE', 'NEURO', 'KIDNEY', 'CARDIAC', 'ORTHO', 'SUPER SPECIALITY', 'GENERAL']
                    # for i in range(len(special)):
                    # print(f"{i + 1}: {special[i]}")
                    # speciality = special[int(input("Enter serial number of the service required: ")) - 1]

                    speciality = special[int(special_index) - 1]

                    if speciality == 'GENERAL':
                        index = 1
                        Lb1 = Listbox(choice11, width=40, height=15, font=('league spartan', 12),bg = 'turquoise',selectbackground = 'light green')
                        Lb1.place(relx=0.65, rely=0.38, anchor=CENTER)
                        scrollbar = Scrollbar(choice11)
                        scrollbar.pack(side=RIGHT, fill=BOTH)

                        for i in hospitals:
                            Lb1.insert(END, f"S. No. {index}")
                            Lb1.insert(END, f"State: {i[1]}")
                            Lb1.insert(END, f"City: {i[2]}")
                            Lb1.insert(END, f"Hospital: {i[3]}")
                            Lb1.insert(END, f"Address: {i[5]}")
                            Lb1.insert(END, f"Pincode: {i[6]}")
                            Lb1.insert(END, f"Phone Number: {i[7]} {i[8]}")
                            Lb1.insert(END, "****")

                            i.append(index)
                            index += 1

                        if index == 1:
                            webbrowser.open(f'https://www.google.com/maps/search/?api=1&query=hospitals + {city}')
                            print("No hospitals found!")
                            exit()

                        Lb1.config(yscrollcommand=scrollbar.set, )
                        scrollbar.config(command=Lb1.yview)

                    else:
                        index = 1
                        Lb1 = Listbox(choice11, width=40, height=15, font=('league spartan', 12),bg = 'turquoise',selectbackground = 'light green')
                        Lb1.place(relx=0.65, rely=0.38, anchor=CENTER)
                        scrollbar = Scrollbar(choice11)
                        scrollbar.pack(side=RIGHT, fill=BOTH)

                        for i in hospitals:
                            if speciality in i[3]:
                                Lb1.insert(END, f"S. No. {index}")
                                Lb1.insert(END, f"State: {i[1]}")
                                Lb1.insert(END, f"City: {i[2]}")
                                Lb1.insert(END, f"Hospital: {i[3]}")
                                Lb1.insert(END, f"Address: {i[5]}")
                                Lb1.insert(END, f"Pincode: {i[6]}")
                                Lb1.insert(END, f"Phone Number: {i[7]} {i[8]}")
                                Lb1.insert(END, "****")

                                i.append(index)
                                index += 1

                        if index == 1:
                            webbrowser.open(
                                f'https://www.google.com/maps/search/?api=1&query= {speciality} hospitals + {city}')
                            print("No hospitals found894!")
                            exit()

                    def final():
                        des = ''
                        desti = int(entry_6.get())
                        for i in hospitals:
                            if i[-1] == desti:
                                des = i[3]
                                break

                        webbrowser.open(
                            f'https://www.google.com/maps/dir/?api=1&origin={ee_1}&destination={des}&travelmode=car')

                    entry_6 = Entry(choice11, width=28, font=('league spartan', 16), bg='turquoise', fg='white')
                    entry_6.place(relx=0.68, rely=0.83, anchor=CENTER)

                    index_chosen = Button(choice11, text="Next", font=('league spartan', 18), bg='turquoise',
                                          fg='white', command=final)
                    index_chosen.place(relx=0.9, rely=0.055, anchor=CENTER)

                    choice11.mainloop()

                city = ee_1
                choice.destroy()
                choice1 = Tk()
                choice1.geometry('1920x1080')

                # Back ground


                ef = PhotoImage(file="cold, smooth & tasty.555555 (1).png")
                ef_label = Label(choice1, image=ef)
                ef_label.place(x=0, y=0)
                # entry
                entry_5 = Entry(choice1, width=28, font=('league spartan', 16), bg='turquoise', fg='white')
                entry_5.place(relx=0.63, rely=0.76, anchor=CENTER)

                hospitals = []
                for i in sheet["C"]:
                    if i.value.lower() == city.lower():
                        c = i.row
                        # print(c)
                        x = []
                        for i in sheet[c]:
                            x.append(i.value)
                        hospitals.append(x)

                # button

                xww = Button(choice1, text="Next", font=('league spartan', 18), bg='turquoise', fg='white',
                             command=entry11)
                xww.place(relx=0.9, rely=0.8, anchor=CENTER)

                choice1.mainloop()


            elif ch == 2:

                choice.destroy()
                choice111 = Tk()
                choice111.geometry('1920x1080')

                # Back ground


                efgh = PhotoImage(file="cold, smooth & tasty. (3).png")
                efgh_label = Label(choice111, image=efgh)
                efgh_label.place(x=0, y=0)

                def hospital_names():
                    hos = entry_7.get()

                    choice111.destroy()
                    choice1111 = Tk()
                    choice1111.geometry('1920x1080')

                    efghi = PhotoImage(file="22222222222 (1).png")
                    efghi_label = Label(choice1111, image=efghi)
                    efghi_label.place(x=0, y=0)

                    address = []
                    for i in sheet["D"]:
                        if hos.lower() in i.value.lower():
                            c = i.row
                            x = []
                            for i in sheet[c]:
                                x.append(i.value)
                            address.append(x)

                    Lb1 = Listbox(choice1111, width=40, height=15, font=('league spartan', 12),bg = 'turquoise',selectbackground = 'light green')
                    Lb1.place(relx=0.65, rely=0.38, anchor=CENTER)
                    scrollbar = Scrollbar(choice1111)
                    scrollbar.pack(side=RIGHT, fill=BOTH)

                    index = 1
                    for i in address:
                        Lb1.insert(END, f"S. No. {index}")
                        Lb1.insert(END, f"State: {i[1]}")
                        Lb1.insert(END, f"City: {i[2]}")
                        Lb1.insert(END, f"Hospital: {i[3]}")
                        Lb1.insert(END, f"Address: {i[5]}")
                        Lb1.insert(END, f"Pincode: {i[6]}")
                        Lb1.insert(END, f"Phone Number: {i[7]} {i[8]}")
                        Lb1.insert(END, "****")

                        i.append(index)
                        index += 1

                    if index == 1:
                        hos = hos + " hospital"
                        webbrowser.open(f'https://www.google.com/maps/search/?api=1&query=  {ee_1} {hos}')
                        print("No hospitals found!")
                        exit()

                    def final2():
                        des = ''
                        desti = int(entry_8.get())
                        for i in address:
                            if i[-1] == desti:
                                des = i[3]
                                break

                        webbrowser.open(
                            f'https://www.google.com/maps/dir/?api=1&origin={ee_1}&destination={des}&travelmode=car')

                    entry_8 = Entry(choice1111, width=28, font=('league spartan', 16), bg='turquoise', fg='white')
                    entry_8.place(relx=0.7, rely=0.85, anchor=CENTER)

                    index_chosen2 = Button(choice1111, text="Next", font=('league spartan', 18), bg='turquoise',
                                           fg='white', command=final2)
                    index_chosen2.place(relx=0.9, rely=0.055, anchor=CENTER)

                    choice1111.mainloop()

                entry_7 = Entry(choice111, width=28, font=('league spartan', 16), bg='turquoise', fg='white')
                entry_7.place(relx=0.63, rely=0.58, anchor=CENTER)

                index_chosen1 = Button(choice111, text="Next", font=('league spartan', 18), bg='turquoise', fg='white',
                                       command=hospital_names)
                index_chosen1.place(relx=0.9, rely=0.055, anchor=CENTER)

                choice111.mainloop()

            else:
                print("Invalid selection")

        xw = Button(choice, text="Next", font=('league spartan', 18), bg='turquoise', fg='white', command=entry1)
        xw.place(relx=0.9, rely=0.055, anchor=CENTER)

        # Entry
        entry_1 = Entry(choice, width=28, font=('league spartan', 16), bg='turquoise', fg='white')
        entry_1.place(relx=0.53, rely=0.58, anchor=CENTER)

        choice.mainloop()

    # Button

    xq = Button(main_window2, text="Sign up", font=('Merlin', 14), bg='white', fg='blue', command=con_sig)
    xq.place(relx=0.7, rely=0.055, anchor=CENTER)

    xx = Button(main_window2, text="Login", font=('Merlin', 14), bg='white', fg='blue', command=login_new)
    xx.place(relx=0.8, rely=0.055, anchor=CENTER)

    xa = Button(main_window2, text="Next->", font=('Merlin', 14), bg='white', fg='blue', command=choice_new)
    xa.place(relx=0.9, rely=0.055, anchor=CENTER)

    main_window2.mainloop()


# main buttons
dd = Button(root, text="Find My Hospital", font=('Berlin Sans FB', 20), bg='blue', fg='white', command=about)
dd.place(relx=0.2, rely=0.8, anchor=CENTER)

root.mainloop()
