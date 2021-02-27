from tkinter import *
from tkinter import ttk
from read_scholarships import get_scholarships, scholarship_names, eligibility, awards, deadline_dates, links
import webbrowser
import textwrap


root = Tk()
root.title("Scholarly")
tableframe = Frame(root)
tableframe.pack(side=BOTTOM)

# initializing variable
filter_var = StringVar(root)
treeview = None

# default font
DEFAULT_FONT = ('Helvetica', 10)
HEADING_FONT = ('Helvetica', 11)
lab = ttk.Label(root, text="Scholarly", font=HEADING_FONT)
lab.pack()

s = ttk.Style()


def fixed_map(option):
    """
        Fix for the tag related background
    """
    global s
    # Returns the style map for 'option' with any styles starting with
    # ("!disabled", "!selected", ...) filtered out

    # style.map() returns an empty list for missing options, so this should
    # be future-safe
    return [elm for elm in s.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]


s.theme_use()
s.map("Treeview",
      foreground=fixed_map("foreground"),
      background=fixed_map("background"))
s.configure('Treeview', rowheight=30, borderwidth=1, relief='flat')
s.configure('Treeview.Heading', font=HEADING_FONT)
s.configure('Treeview.Column', font=DEFAULT_FONT, padding=15)
s.configure('Button', padding=6, font=DEFAULT_FONT)


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


def wrap(string, lenght=60):
    """
        Function to wrap text according to the length
    """
    return "" if string is None else '\n'.join(textwrap.wrap(string, lenght))


def init_table():
    """
        Initialize scholarships table
    """
    global treeview
    col = ("Scholarship Name", "Eligibility", "Award", "Deadline", "Link")
    treeview = ttk.Treeview(tableframe, height=10,
                            show="headings", columns=col)
    treeview.tag_configure('odd', background='#ededed')
    treeview.tag_configure('even', background='#b5b5b5')

    # treeview column config
    treeview.column("Scholarship Name", width=400)
    treeview.column("Award", width=200)
    treeview.column("Eligibility", width=200)
    treeview.column("Deadline", width=100)
    treeview.column("Link", width=400)

    # treeview headings
    treeview.heading("Scholarship Name", text="Scholarship Name")
    treeview.heading("Award", text="Awards Provided")
    treeview.heading("Eligibility", text="Eligibility")
    treeview.heading("Deadline", text="Deadline Date")
    treeview.heading("Link", text="Link")

    treeview.pack(side=BOTTOM)


def insert_data():
    """
        Insert data into table
    """
    global treeview

    # get all the scholarship data
    get_scholarships()

    # tries to delete already inserted data
    try:
        treeview.delete(*treeview.get_children())
    except:
        pass

    # inserting data into scholarship table
    n = len(scholarship_names)
    for i in range(n):
        if i % 2 == 0:
            treeview.insert(
                '',
                i,
                values=(wrap(scholarship_names[i]),
                        wrap(eligibility[i]), wrap(awards[i]), wrap(deadline_dates[i]), wrap(links[i])),
                tag='even'
            )
        else:
            treeview.insert(
                '',
                i,
                values=(wrap(scholarship_names[i]),
                        wrap(eligibility[i]), wrap(awards[i]), wrap(deadline_dates[i]), wrap(links[i])),
                tag='odd'
            )


def handle_click():
    """
        Handles the filter button click
    """
    insert_data()


# initializing the scholarship data
init_table()

options = ['Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Graduation', 'Post Graduation', 'Phd', 'ITI',
           'Polytechnique/Diploma', 'Post Doctoral', 'Vocational Courses', 'Coaching Classes']

filter_var.set("Choose Class")

class_filter = ttk.OptionMenu(root, filter_var, *options)
class_filter.pack(side=LEFT)


filter_submit = ttk.Button(root, text="Filter Results", command=handle_click)
filter_submit.pack(side=LEFT)


root.mainloop()
