# Coded by Aryan Agrawal of NPS Koramangala
# Please install the tkinter module on your divice using pip install
from tkinter import *
import warnings
import datetime
from datetime import *
import time
# Please install the calander module on your divice using pip install
import calendar
warnings.filterwarnings("ignore")
import wikipedia
from webbrowser import *
import wikipedia 
import bs4
# color chart used - http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png
todo_list = []
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

flag = "Normal" 
class ChatApplication:
    # Basic defining of the Tkinter window. Template by PythonEngineer youtube channel
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    #Making the chatbot run forever in the bachground
    def run(self):
        self.window.mainloop()
    #Basic design of the Window
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=1000, height=550, bg=BG_COLOR)
        
        # head label Says Stay Ahead the name of the app
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Stay Ahead", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider - Used to keep the head label mentioned above
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget - This is where all the text goes
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, "Hi, for getting to know the commands please type -help- and I will be there for you\n\n\n\n_________________________\n")
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
     
    def _on_enter_pressed(self, event):
        global flag
        msg = self.msg_entry.get()
        # When we are providing the element to be added to the todo list
        if(flag=="add"):
            todo_list.append(msg)
            self.msg_entry.delete(0, END)
            msg1 = f"You: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)
            flag = "Normal"
        #identifying when the person is asking to add to the todo list
        elif(msg.find("add")!=-1 and msg.find("todo")!=-1):
            flag = "add"
            self._insert_message(msg, "You")
        else:
            self._insert_message(msg, "You")
    def _insert_message(self, msg, sender):
        global flag
        def get_answer(question):
            global flag
            question = question.lower()
            if(question.find("hi")!=-1):
                return "Hi, for getting to know the commands please type -feautures- and I will be there for you\n\n_________________________________\n"
            elif(question.find("features")!=-1 or question.find("what can you do")!=-1 or question.find("help")!=-1):
                return "This is a student helper\n These are the following ways in which it can help you:\n 1. Inorder to save  a hw in the virtual todo list please type -add todo + task name-\n 2. If you want to check what all is on your todo list, please type mytodo\n 3.If you want me to open a website for you please type -open webpage + name of webpage-\n 4. If you want me to give wikipedia gists please type -research- and the rest steps will come on its own\n 5. If you ever have any problems with any command please type -help-\n I am Always there to help you!\n 6. What is the Day and Date today use command -today-\n 7. To get the calander of the current month please type the command calender\n 8. Set a timer for yourself by giving timer+ time command NOTE: You can set timer in seconds\n 9. Get motivated by the thought of the day by entering -thought-\n 10. Get to know if you have school tomorrow by enterring -working_day-\n\n\n\n_______________________________________________________\n"
            elif(question.find("add")!=-1 and question.find("todo")!=-1):
                return "What do you want me to add to your todo list?\n"
            elif(question.find("list")!=-1 or question.find("show")!=-1):
                answer = ""
                counter = 1
                if(len(todo_list)==0):
                    return "No tasks in the todo list #winning\n\n\n_____________________________\n"
                for item in todo_list:
                    answer+=str(counter)+". "
                    counter+=1
                    answer=answer+item;
                    answer+="\n"
                return answer+"\n\n\n____________________________________\n"
            elif(question.find("open webpage")!=-1):
                mainy_boy = question.replace("opened webpage If it has not opened on your computer please check if you have installed the necessary packages mentioned above and try again\n\n\n\n______________________\n","")
                webbrowser.open(mainy_boy, new=1)
            elif(question.find("research")!=-1):
                mainy_boy = question.replace("research ","")
                try:
                    result = BeautifulSoup(html).find_all('li')
                except wikipedia.exceptions.DisambiguationError:
                    return "The words spelling is either wrong or wikipedia doesn't contain anything about that. There is also a probability of you downloading a corrupted package please reinstall the package\n\n\n\n\n_____________________________________\n"
                return result+"\n\n\n\n________________________________\n"
            elif(question=="added"):
                return "Added successfully"
            elif(question=="today"):
                current_date = date.today()
                return str(current_date.month)+"/"+str(current_date.day)+"/"+str(current_date.year)
            elif(question=="calendar"):
                current_date = date.today()
                return str(calendar.month(current_date.year, current_date.month))
            elif(question.find("timer")!=-1):
                time_for = question.replace("timer","")
                time_final = int(time_for)
                time.sleep(time_final)
                return "Your timer is up"
            elif(question.find("thought")!=-1):
                return "DONT RUN AWAY FROM CHALLENGES\nRUN OVER THEM\n"
            elif(question=="working_day"):
                date_day = datetime.today().weekday()
                if(date_day==4):
                    return "Tomorrow is a holiday!"
                else:
                    return "You have school tomorrow :("
            else:
                return "Sorry I can't help you with that yet, but I am constantly learning!"
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # The bots message is diplayed
        msg2 = get_answer(msg)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
def run_main_app():
    splash_screen.destroy()
    app = ChatApplication()
    app.run()   

splash_screen = Tk()
splash_screen.title("Stay Ahead!")
splash_screen.geometry("450x650")
splash_screen_bg = PhotoImage(file = "SpashBG .png")
background_paceholder = Label(splash_screen,image=splash_screen_bg)
background_paceholder.place(x=0,y=0,relwidth=1,relheight=1)
splash_screen.after(3000,run_main_app)
mainloop()