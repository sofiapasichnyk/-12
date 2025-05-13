from tkinter import *
from tkinter import filedialog, messagebox

def select_photo():
    filename = filedialog.askopenfilename(title="Виберіть фото", filetypes=[("Image files", "*.jpg *.png *.gif")])
    if filename:
        photo_label.config(text=filename)

def submit():
    print("Анкету надіслано!")

def show_specialty_info():
    messagebox.showinfo("Інформація про спеціальність", "Це коротка інформація про обрану спеціальність.")

# Створення головного вікна
root = Tk()
root.title("Анкета")
root.geometry("300x550")
root['bg'] = 'hotpink'

# Прізвище
Label(root, text="Прізвище:", bg='pink').pack()
entry_surname = Entry(root)
entry_surname.pack()

# Ім'я
Label(root, text="Ім'я:", bg='pink').pack()
entry_name = Entry(root)
entry_name.pack()

# По батькові
Label(root, text="По батькові:", bg='pink').pack()
entry_patronymic = Entry(root)
entry_patronymic.pack()

# Прапорці
Label(root, text="Стать:", bg='pink').pack()
check_var1 = IntVar()
check_var2 = IntVar()
Checkbutton(root, text="ч", variable=check_var1, bg='pink').pack()
Checkbutton(root, text="ж", variable=check_var2, bg='pink').pack()

# Вибір курсу
Label(root, text="Виберіть курс:", bg='pink').pack()
course_var = IntVar()
course_var.set(1)
for i in range(1, 5):
    Radiobutton(root, text=str(i), variable=course_var, value=i, bg='pink').pack()

# Спеціальність
Label(root, text="Спеціальність:", bg='pink').pack()
entry_specialty = Entry(root)
entry_specialty.pack()

# Кнопка "Про спеціальність"
Button(root, text="Про спеціальність", command=show_specialty_info).pack(pady=5)

# Фото
photo_button = Button(root, text="Вибрати фото", command=select_photo)
photo_button.pack()

# Кнопка відповісти
submit_button = Button(root, text="Відповісти", command=submit)
submit_button.pack()

# Запуск вікна
root.mainloop()

