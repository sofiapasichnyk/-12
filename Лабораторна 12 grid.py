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
root.geometry("350x650")
root['bg'] = 'hotpink'

# Прізвище
Label(root, text="Прізвище:", bg='pink').grid(row=0, column=0, sticky='w', padx=10, pady=5)
entry_surname = Entry(root)
entry_surname.grid(row=0, column=1, padx=10, pady=5)

# Ім'я
Label(root, text="Ім'я:", bg='pink').grid(row=1, column=0, sticky='w', padx=10, pady=5)
entry_name = Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

# По батькові
Label(root, text="По батькові:", bg='pink').grid(row=2, column=0, sticky='w', padx=10, pady=5)
entry_patronymic = Entry(root)
entry_patronymic.grid(row=2, column=1, padx=10, pady=5)

# Стать
Label(root, text="Стать:", bg='pink').grid(row=3, column=0, sticky='w', padx=10, pady=5)
check_var1 = IntVar()
check_var2 = IntVar()
Checkbutton(root, text="ч", variable=check_var1, bg='pink').grid(row=3, column=1, sticky='w', padx=5)
Checkbutton(root, text="ж", variable=check_var2, bg='pink').grid(row=4, column=1, sticky='w', padx=5)

# Курс
Label(root, text="Виберіть курс:", bg='pink').grid(row=5, column=0, sticky='w', padx=10, pady=5)
course_var = IntVar()
course_var.set(1)
for i in range(1, 5):
    Radiobutton(root, text=str(i), variable=course_var, value=i, bg='pink').grid(row=5 + i, column=1, sticky='w', padx=5)

# Спеціальність
Label(root, text="Спеціальність:", bg='pink').grid(row=10, column=0, sticky='w', padx=10, pady=5)
entry_specialty = Entry(root)
entry_specialty.grid(row=10, column=1, padx=10, pady=5)

# Кнопка "Про спеціальність"
Button(root, text="Про спеціальність", command=show_specialty_info).grid(row=11, column=0, columnspan=2, pady=5)

# Фото
photo_button = Button(root, text="Вибрати фото", command=select_photo)
photo_button.grid(row=12, column=0, columnspan=2, pady=5)

# Кнопка відповісти
submit_button = Button(root, text="Відповісти", command=submit)
submit_button.grid(row=14, column=0, columnspan=2, pady=10)

root.mainloop()

