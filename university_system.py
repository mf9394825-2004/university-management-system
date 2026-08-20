from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, messagebox

# ==================== Color Palette (Professional Dark Theme) ====================
COLOR_BG          = "#12141c"   # main background
COLOR_SIDEBAR     = "#181b26"   # sidebar / header background
COLOR_CARD        = "#1e2230"   # cards / panels
COLOR_CARD_HOVER  = "#262b3d"
COLOR_ACCENT      = "#6c5ce7"   # primary accent (purple)
COLOR_ACCENT_DARK = "#5849c2"
COLOR_TEXT        = "#f2f3f7"
COLOR_TEXT_MUTED  = "#9aa0b4"
COLOR_SUCCESS     = "#2ecc71"
COLOR_DANGER      = "#e74c3c"
COLOR_WARNING     = "#f4b942"
COLOR_INFO        = "#3ea6ff"
COLOR_BORDER      = "#2a2f42"

FONT_TITLE   = ("Segoe UI", 24, "bold")
FONT_SUB     = ("Segoe UI", 11)
FONT_HEADING = ("Segoe UI", 16, "bold")
FONT_LABEL   = ("Segoe UI", 10)
FONT_ENTRY   = ("Segoe UI", 11)
FONT_BTN     = ("Segoe UI", 11, "bold")
FONT_CARD    = ("Segoe UI", 12, "bold")
FONT_CARD_SM = ("Segoe UI", 9)

# ---------------- Root ----------------
root = tk.Tk()
root.geometry("1100x750")
root.minsize(950, 650)
root.title("University Management System")
root.config(bg=COLOR_BG)

students_list = []
doctors_list = []
courses_list = []


# ==================== OOP Classes (unchanged logic) ====================
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    def __init__(self, name, id, major):
        super().__init__(name)
        self.id = id
        self.major = major
        self.courses = []

    def add_courses(self, course):
        self.courses.append(course)

    def display_info(self):
        courses_str = ", ".join([f"{c.course_name} ({c.doctor.name})" for c in self.courses])
        return f"{self.name} | {self.id} | {self.major} | Courses: {courses_str}"


class Doctor(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display_info(self):
        return f"{self.name} | {self.department}"


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.doctor = None
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def set_doctor(self, doctor):
        self.doctor = doctor


# ==================== Initial Data ====================
initial_doctors = [
    ("Dr. Ahmed", "CS"),
    ("Dr. Mona", "IS"),
    ("Dr. Omar", "AI"),
    ("Dr. Sara", "SE"),
    ("Dr. Tamer", "Networks")
]

initial_courses = [
    ("Data Structures", "Dr. Ahmed"),
    ("DB Systems", "Dr. Mona"),
    ("Machine Learning", "Dr. Omar"),
    ("Software Eng", "Dr. Sara"),
    ("Networks", "Dr. Tamer")
]

initial_students = [
    ("Ali", "101", "CS", ["Data Structures", "DB Systems"]),
    ("Sara", "102", "IS", ["DB Systems", "Software Eng"]),
    ("Omar", "103", "AI", ["Machine Learning"])
]

for name, dept in initial_doctors:
    doctors_list.append(Doctor(name, dept))

for cname, dname in initial_courses:
    course = Course(cname)
    for d in doctors_list:
        if d.name == dname:
            course.set_doctor(d)
    courses_list.append(course)

for sname, sid, major, c_list in initial_students:
    student = Student(sname, sid, major)
    for c_name in c_list:
        for c in courses_list:
            if c.course_name == c_name:
                student.add_courses(c)
                c.add_student(student)
    students_list.append(student)


# ==================== Reusable UI Helpers ====================
def style_window(win, w, h, title):
    win.title(title)
    win.geometry(f"{w}x{h}")
    win.config(bg=COLOR_BG)
    win.resizable(False, False)
    win.transient(root)
    win.grab_set()


def window_header(win, text, subtitle=None):
    header = tk.Frame(win, bg=COLOR_SIDEBAR)
    header.pack(fill="x")
    tk.Label(header, text=text, font=FONT_HEADING, bg=COLOR_SIDEBAR, fg=COLOR_TEXT).pack(
        anchor="w", padx=25, pady=(18, 2)
    )
    if subtitle:
        tk.Label(header, text=subtitle, font=FONT_LABEL, bg=COLOR_SIDEBAR, fg=COLOR_TEXT_MUTED).pack(
            anchor="w", padx=25, pady=(0, 18)
        )
    else:
        tk.Frame(header, bg=COLOR_SIDEBAR, height=18).pack()
    tk.Frame(win, bg=COLOR_ACCENT, height=2).pack(fill="x")


def styled_entry(parent, label_text):
    tk.Label(parent, text=label_text, font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_TEXT_MUTED).pack(
        anchor="w", padx=30, pady=(14, 4)
    )
    wrap = tk.Frame(parent, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER)
    wrap.pack(fill="x", padx=30)
    entry = tk.Entry(
        wrap, font=FONT_ENTRY, bg=COLOR_CARD, fg=COLOR_TEXT,
        insertbackground=COLOR_TEXT, relief="flat", bd=0
    )
    entry.pack(fill="x", padx=12, pady=10)
    return entry


def styled_dropdown(parent, label_text, options, variable):
    tk.Label(parent, text=label_text, font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_TEXT_MUTED).pack(
        anchor="w", padx=30, pady=(14, 4)
    )
    wrap = tk.Frame(parent, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER)
    wrap.pack(fill="x", padx=30)
    variable.set(options[0])
    dropdown = tk.OptionMenu(wrap, variable, *options)
    dropdown.config(
        font=FONT_ENTRY, bg=COLOR_CARD, fg=COLOR_TEXT, activebackground=COLOR_CARD_HOVER,
        activeforeground=COLOR_TEXT, relief="flat", bd=0, highlightthickness=0, anchor="w"
    )
    dropdown["menu"].config(bg=COLOR_CARD, fg=COLOR_TEXT, font=FONT_ENTRY, activebackground=COLOR_ACCENT)
    dropdown.pack(fill="x", padx=8, pady=6)
    return dropdown


def styled_checklist(parent, label_text, courses):
    tk.Label(parent, text=label_text, font=FONT_LABEL, bg=COLOR_BG, fg=COLOR_TEXT_MUTED).pack(
        anchor="w", padx=30, pady=(16, 6)
    )
    wrap = tk.Frame(parent, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER)
    wrap.pack(fill="x", padx=30)

    courses_var = []
    for course in courses:
        var = tk.IntVar()
        text = course.course_name
        if course.doctor:
            text += f"   ·   {course.doctor.name}"
        chk = tk.Checkbutton(
            wrap, text=text, variable=var,
            bg=COLOR_CARD, fg=COLOR_TEXT, font=FONT_LABEL,
            selectcolor=COLOR_SIDEBAR, activebackground=COLOR_CARD,
            activeforeground=COLOR_TEXT, anchor="w", relief="flat",
            highlightthickness=0, bd=0
        )
        chk.pack(anchor="w", fill="x", padx=12, pady=4)
        courses_var.append((var, course))
    return courses_var


def styled_action_button(parent, text, color, hover_color, command):
    btn = tk.Button(
        parent, text=text, bg=color, fg="white", font=FONT_BTN,
        relief="flat", bd=0, activebackground=hover_color, activeforeground="white",
        cursor="hand2", command=command
    )
    btn.pack(fill="x", padx=30, pady=(26, 20), ipady=10)
    btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    return btn


# ==================== Add Doctor ====================
def open_add_doctor():
    win = tk.Toplevel(root)
    style_window(win, 420, 380, "Add Doctor")
    window_header(win, "Add Doctor 👨‍🏫", "Register a new faculty member")

    name_entry = styled_entry(win, "Doctor Name")
    dept_entry = styled_entry(win, "Department")

    def save():
        name = name_entry.get().strip()
        dept = dept_entry.get().strip()
        if not name or not dept:
            messagebox.showerror("Error", "Fill all fields!")
            return
        doctors_list.append(Doctor(name, dept))
        messagebox.showinfo("Success", "Doctor Added!")
        win.destroy()

    styled_action_button(win, "Save Doctor", COLOR_SUCCESS, "#27ae60", save)


# ==================== Add Course ====================
def open_add_course():
    if not doctors_list:
        messagebox.showerror("Error", "Add Doctor First!")
        return

    win = tk.Toplevel(root)
    style_window(win, 420, 420, "Add Course")
    window_header(win, "Add Course 📚", "Create a course and assign an instructor")

    name_entry = styled_entry(win, "Course Name")

    selected = tk.StringVar()
    doctor_names = [d.name for d in doctors_list]
    styled_dropdown(win, "Assigned Doctor", doctor_names, selected)

    def save():
        name = name_entry.get().strip()
        doctor_name = selected.get()
        if not name or not doctor_name:
            messagebox.showerror("Error", "Fill all fields!")
            return
        course = Course(name)
        for d in doctors_list:
            if d.name == doctor_name:
                course.set_doctor(d)
        courses_list.append(course)
        messagebox.showinfo("Success", "Course Added!")
        win.destroy()

    styled_action_button(win, "Save Course", COLOR_SUCCESS, "#27ae60", save)


# ==================== Add Student ====================
def open_add_student():
    if not courses_list:
        messagebox.showerror("Error", "Add Courses First!")
        return

    win = tk.Toplevel(root)
    style_window(win, 460, 720, "Add Student")
    window_header(win, "Add Student 🎓", "Enroll a new student")

    name_entry = styled_entry(win, "Full Name")
    id_entry = styled_entry(win, "Student ID")
    major_entry = styled_entry(win, "Major")
    courses_var = styled_checklist(win, "Enrolled Courses", courses_list)

    def save():
        name = name_entry.get().strip()
        sid = id_entry.get().strip()
        major = major_entry.get().strip()
        if not name or not sid or not major:
            messagebox.showerror("Error", "Fill all fields!")
            return
        if any(s.id == sid for s in students_list):
            messagebox.showerror("Error", "ID Exists!")
            return
        student = Student(name, sid, major)
        for var, course in courses_var:
            if var.get() == 1:
                student.add_courses(course)
                course.add_student(student)
        students_list.append(student)
        messagebox.showinfo("Success", "Student Added!")
        win.destroy()

    styled_action_button(win, "Save Student", COLOR_SUCCESS, "#27ae60", save)


# ==================== View Students ====================
def view_students():
    win = tk.Toplevel(root)
    style_window(win, 620, 560, "Students List")
    window_header(win, "Students List 📋", f"{len(students_list)} student(s) registered")

    container = tk.Frame(win, bg=COLOR_BG)
    container.pack(fill="both", expand=True, padx=30, pady=20)

    if not students_list:
        tk.Label(container, text="No Students Found", font=FONT_LABEL,
                  bg=COLOR_BG, fg=COLOR_TEXT_MUTED).pack(pady=40)
        return

    canvas = tk.Canvas(container, bg=COLOR_BG, highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_BG)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=560)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for s in students_list:
        card = tk.Frame(scroll_frame, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER)
        card.pack(fill="x", pady=6)
        tk.Label(card, text=f"{s.name}   ·   ID {s.id}", font=FONT_CARD,
                  bg=COLOR_CARD, fg=COLOR_TEXT).pack(anchor="w", padx=16, pady=(12, 2))
        tk.Label(card, text=f"Major: {s.major}", font=FONT_CARD_SM,
                  bg=COLOR_CARD, fg=COLOR_TEXT_MUTED).pack(anchor="w", padx=16)
        courses_str = ", ".join([f"{c.course_name} ({c.doctor.name if c.doctor else '—'})" for c in s.courses]) or "No courses"
        tk.Label(card, text=courses_str, font=FONT_CARD_SM, wraplength=520, justify="left",
                  bg=COLOR_CARD, fg=COLOR_INFO).pack(anchor="w", padx=16, pady=(2, 12))


# ==================== Delete Student ====================
def delete_student():
    if not students_list:
        messagebox.showerror("Error", "No Students!")
        return

    win = tk.Toplevel(root)
    style_window(win, 420, 340, "Delete Student")
    window_header(win, "Delete Student 🗑️", "This action cannot be undone")

    selected = tk.StringVar()
    names = [f"{s.id} - {s.name}" for s in students_list]
    styled_dropdown(win, "Select Student", names, selected)

    def remove():
        sid = selected.get().split(" - ")[0]
        for s in students_list:
            if s.id == sid:
                students_list.remove(s)
                messagebox.showinfo("Deleted", "Student Deleted!")
                win.destroy()
                return

    styled_action_button(win, "Delete Student", COLOR_DANGER, "#c0392b", remove)


# ==================== Update Student ====================
def update_student():
    if not students_list:
        messagebox.showerror("Error", "No Students!")
        return

    win = tk.Toplevel(root)
    style_window(win, 460, 760, "Update Student")
    window_header(win, "Update Student ✏️", "Edit details or course enrollment")

    selected = tk.StringVar()
    names = [f"{s.id} - {s.name}" for s in students_list]
    styled_dropdown(win, "Select Student", names, selected)

    name_entry = styled_entry(win, "New Name")
    major_entry = styled_entry(win, "New Major")
    courses_var = styled_checklist(win, "Update Courses", courses_list)

    def save_update():
        sid = selected.get().split(" - ")[0]
        for student in students_list:
            if student.id == sid:
                new_name = name_entry.get().strip()
                new_major = major_entry.get().strip()
                if new_name:
                    student.name = new_name
                if new_major:
                    student.major = new_major
                for c in student.courses:
                    if student in c.students:
                        c.students.remove(student)
                student.courses = []
                for var, course in courses_var:
                    if var.get() == 1:
                        student.add_courses(course)
                        course.add_student(student)
                messagebox.showinfo("Updated", "Student Updated!")
                win.destroy()
                return

    styled_action_button(win, "Update Student", COLOR_WARNING, "#e0a800", save_update)


# ==================== Logout ====================
def logout():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


# ==================== Main Layout ====================
header = tk.Frame(root, bg=COLOR_SIDEBAR, height=110)
header.pack(fill="x")
header.pack_propagate(False)

title_box = tk.Frame(header, bg=COLOR_SIDEBAR)
title_box.pack(side="left", padx=40, pady=20)
tk.Label(title_box, text="University Management System", font=FONT_TITLE,
          bg=COLOR_SIDEBAR, fg=COLOR_TEXT).pack(anchor="w")
tk.Label(title_box, text="Manage students, doctors and courses in one place",
          font=FONT_SUB, bg=COLOR_SIDEBAR, fg=COLOR_TEXT_MUTED).pack(anchor="w", pady=(4, 0))

tk.Frame(root, bg=COLOR_ACCENT, height=3).pack(fill="x")

# ---- Stats strip ----
stats_frame = tk.Frame(root, bg=COLOR_BG)
stats_frame.pack(fill="x", padx=40, pady=(25, 10))

def stat_card(parent, label, get_value, color):
    card = tk.Frame(parent, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER)
    card.pack(side="left", fill="both", expand=True, padx=8)
    val_lbl = tk.Label(card, text=str(get_value()), font=("Segoe UI", 22, "bold"), bg=COLOR_CARD, fg=color)
    val_lbl.pack(anchor="w", padx=18, pady=(14, 0))
    tk.Label(card, text=label, font=FONT_LABEL, bg=COLOR_CARD, fg=COLOR_TEXT_MUTED).pack(anchor="w", padx=18, pady=(0, 14))
    return val_lbl

students_stat = stat_card(stats_frame, "Students", lambda: len(students_list), COLOR_INFO)
doctors_stat = stat_card(stats_frame, "Doctors", lambda: len(doctors_list), COLOR_ACCENT)
courses_stat = stat_card(stats_frame, "Courses", lambda: len(courses_list), COLOR_SUCCESS)

def refresh_stats():
    students_stat.config(text=str(len(students_list)))
    doctors_stat.config(text=str(len(doctors_list)))
    courses_stat.config(text=str(len(courses_list)))
    root.after(800, refresh_stats)

# ---- Action grid ----
btn_frame = tk.Frame(root, bg=COLOR_BG)
btn_frame.pack(pady=20, padx=40, fill="both", expand=True)
for i in range(3):
    btn_frame.grid_columnconfigure(i, weight=1)

def create_button(parent, icon, text, subtitle, color, hover_color, command, row, col):
    card = tk.Frame(parent, bg=COLOR_CARD, highlightthickness=1, highlightbackground=COLOR_BORDER, cursor="hand2")
    card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    bar = tk.Frame(card, bg=color, height=4)
    bar.pack(fill="x")

    icon_lbl = tk.Label(card, text=icon, font=("Segoe UI", 26), bg=COLOR_CARD, fg=color)
    icon_lbl.pack(anchor="w", padx=18, pady=(16, 4))

    text_lbl = tk.Label(card, text=text, font=FONT_CARD, bg=COLOR_CARD, fg=COLOR_TEXT, anchor="w")
    text_lbl.pack(anchor="w", padx=18)

    sub_lbl = tk.Label(card, text=subtitle, font=FONT_CARD_SM, bg=COLOR_CARD, fg=COLOR_TEXT_MUTED, anchor="w")
    sub_lbl.pack(anchor="w", padx=18, pady=(2, 18))

    widgets = [card, bar, icon_lbl, text_lbl, sub_lbl]

    def on_enter(e):
        card.config(bg=COLOR_CARD_HOVER)
        for w in (icon_lbl, text_lbl, sub_lbl):
            w.config(bg=COLOR_CARD_HOVER)

    def on_leave(e):
        card.config(bg=COLOR_CARD)
        for w in (icon_lbl, text_lbl, sub_lbl):
            w.config(bg=COLOR_CARD)

    for w in widgets:
        w.bind("<Enter>", on_enter)
        w.bind("<Leave>", on_leave)
        w.bind("<Button-1>", lambda e: command())


create_button(btn_frame, "🎓", "Add Student", "Enroll a new student", COLOR_SUCCESS, "#27ae60", open_add_student, 0, 0)
create_button(btn_frame, "👨‍🏫", "Add Doctor", "Register a faculty member", COLOR_ACCENT, COLOR_ACCENT_DARK, open_add_doctor, 0, 1)
create_button(btn_frame, "📚", "Add Course", "Create a new course", "#fd7e14", "#e0690f", open_add_course, 0, 2)
create_button(btn_frame, "📋", "View Students", "Browse all students", COLOR_INFO, "#2f8ed6", view_students, 1, 0)
create_button(btn_frame, "🗑️", "Delete Student", "Remove a student record", COLOR_DANGER, "#c0392b", delete_student, 1, 1)
create_button(btn_frame, "✏️", "Update Student", "Edit student information", COLOR_WARNING, "#e0a800", update_student, 1, 2)

# ---- Footer ----
footer = tk.Frame(root, bg=COLOR_SIDEBAR)
footer.pack(fill="x", side="bottom")
logout_btn = tk.Button(
    footer, text="Logout 🚪", bg=COLOR_SIDEBAR, fg=COLOR_DANGER, font=FONT_BTN,
    relief="flat", bd=0, activebackground=COLOR_SIDEBAR, activeforeground="#ff6b5b",
    cursor="hand2", command=logout
)
logout_btn.pack(pady=16)

refresh_stats()
root.mainloop()
