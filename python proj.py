# Python Project 2022
# by Siwakorn Sirikanerat (65011542)


from tkinter import *
import time
import random
import os.path
from tkinter.filedialog import *
import tkinter.messagebox

class Reaction:
    def __init__(self):
        #configs
        if os.path.isfile("configs.txt"):
            inconfig = open("configs.txt", "r")
            self.font = inconfig.readline().split(",")
            self.bg_color = inconfig.readline().strip()
            inconfig.close()
        else:
            inconfig = open("configs.txt", "w")
            inconfig.write('Comic Sans MS,10,bold\n')
            inconfig.write("#fff0c7")
            inconfig.close()
            self.bg_color = "#fff0c7"
            self.font = ("Comic Sans MS",10,"bold")
        

        #window
        self.window = Tk()
        self.window.geometry("600x600")
        self.window.title("Reaction Speed Test")

        #top main frame
        self.top_frame = Frame(self.window, bg = self.bg_color)
        self.top_frame.pack(fill = BOTH)
        credit_message = Label(self.top_frame, text = "Made for python project 2022", bg = self.bg_color, font = self.font)
        credit_message.pack(side = "bottom")
        self.exit_button = Button(self.top_frame, text = "Exit", command = exit, font = self.font)
        self.exit_button.pack(side = "left")
        self.option_button = Button(self.top_frame, text = "Options", command = self.options, font = self.font)       
        self.option_button.pack(side = "right")
        self.stats_button = Button(self.top_frame, text = "Statistics", command = self.stats, font = self.font)
        self.stats_button.pack()
        
        #main frame
        self.main_frame = Frame(self.window, bg = self.bg_color)
        self.main_frame.pack(fill = BOTH, side = "top", expand = 1)
        self.title_name = Label(self.main_frame, text = "Reaction Speed test", bg = self.bg_color, font = self.font)
        self.title_name.pack(fill = BOTH, expand = 1)
        self.start_button = Button(self.main_frame, text = "Start", command = self.start, font = self.font)
        self.start_button.pack(side= "bottom", fill = BOTH)
        
        #option frame
        self.option_frame = Frame(self.window, bg = self.bg_color)

        self.return_to_main_button4 = Button(self.option_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button4.pack(side = "bottom", fill = BOTH)
        self.option_bg_color_frame = Frame(self.option_frame, bg = self.bg_color)
        self.option_bg_color_frame.pack(side = "left")
        self.color_variable = StringVar()
        self.option_bg_color_Label = Label(self.option_bg_color_frame, text = "Background Color\n (restart to make changes)\n",bg = self.bg_color, font = self.font)
        self.option_bg_color_Label.pack(padx = 20)
        self.option_bg_color_light_yellow = Radiobutton(self.option_bg_color_frame, text = "Light Yellow", variable = self.color_variable, value = "light_yellow", bg = self.bg_color, command = self.process_color, font = self.font)
        self.option_bg_color_light_yellow.pack(padx = 20)
        self.option_bg_color_light_red = Radiobutton(self.option_bg_color_frame, text = "Light Red", variable = self.color_variable, value = "light_red", bg = self.bg_color, command = self.process_color, font = self.font)
        self.option_bg_color_light_red.pack(side = "bottom")
        self.option_bg_color_light_blue = Radiobutton(self.option_bg_color_frame, text = "Light Blue", variable = self.color_variable, value = "light_blue", bg = self.bg_color, command = self.process_color, font = self.font)
        self.option_bg_color_light_blue.pack(side = "bottom")
        self.option_save_load_frame = Frame(self.option_frame, bg = self.bg_color)
        self.option_save_load_frame.pack(side="right", padx = 20)
        self.option_save_load_label = Label(self.option_save_load_frame, text = "Save files\n", bg = self.bg_color, font = self.font)
        self.option_save_load_label.pack(padx = 20)
        self.option_load_button = Button(self.option_save_load_frame, text = "Load file", command = self.load_save, font = self.font)
        self.option_load_button.pack()
        self.option_create_save_button = Button(self.option_save_load_frame, text = "Create a new save file", command = self.create_save, font = self.font)
        self.option_create_save_button.pack()   
        self.option_load_status = Label(self.option_save_load_frame, text = "", bg = self.bg_color, font = self.font)
        self.option_load_status.pack()

        #stats frame
        self.stats_frame = Frame(self.window, bg = self.bg_color)
        self.stats_label = Label(self.stats_frame, text = "History", bg = self.bg_color, font = self.font)
        self.stats_label.pack(side = "top")
        self.history_list = Text(self.stats_frame, font = self.font)
        self.history_list.pack(pady = 20)
        self.return_to_main_button5 = Button(self.stats_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button5.pack(side = "bottom", fill = BOTH)

        #mode selection frame
        self.mode_select_frame = Frame(self.window, bg = self.bg_color)
        self.select_mode = Label(self.mode_select_frame, text = "Select Mode", bg = self.bg_color, font = self.font)
        self.select_mode.pack()
        self.color_mode_button = Button(self.mode_select_frame, text = "Color", command = self.color_mode, font = self.font)
        self.color_mode_button.pack(pady = 20)
        self.circle_mode_button = Button(self.mode_select_frame, text = "Circle", command = self.circle_mode, font = self.font)
        self.circle_mode_button.pack(pady = 20)
        self.return_to_main_button = Button(self.mode_select_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button.pack(side = "bottom", fill = BOTH)
  

        #top color mode frame 
        self.top_color_mode_frame = Frame(self.window, bg = self.bg_color)
        self.color_instruction = Label(self.top_color_mode_frame, text = "Click the screen when it changes to green", bg = self.bg_color, font = self.font)
        self.color_instruction.pack(fill = BOTH)
        self.start_color_mode_button = Button(self.top_color_mode_frame, text = "Start", command = self.random_time, font = self.font)
        self.start_color_mode_button.pack(side = "bottom")
        
        #main color mode frame
        self.main_color_mode_frame = Frame(self.window, bg = self.bg_color)
        self.main_color_mode_canvas = Canvas(self.main_color_mode_frame, bg = "white")
        self.main_color_mode_canvas.pack(fill = BOTH, expand = 1)
        self.main_color_mode_canvas.bind("<Button-1>", self.process_reaction_time_color)
        

        #bottom color mode frame
        self.bottom_color_mode_frame = Frame(self.window, bg = self.bg_color)
        self.return_to_main_button2 = Button(self.bottom_color_mode_frame, text = "Return to main menu", command = self.return_to_main, bg = self.bg_color, font = self.font)
        self.return_to_main_button2.pack(side = "bottom", fill = BOTH)

        #top circle mode frame
        self.top_circle_mode_frame = Frame(self.window, bg = self.bg_color)
        self.circle_instruction = Label(self.top_circle_mode_frame, text = "Click the circles when it appears", bg = self.bg_color, font = self.font)
        self.circle_instruction.pack(fill = BOTH)
        self.start_circle_mode_button = Button(self.top_circle_mode_frame, text = "Start", command = self.random_circle)
        self.start_circle_mode_button.pack()
        
        #main circle mode frame
        self.main_circle_mode_frame = Frame(self.window, bg = self.bg_color)
        self.main_circle_mode_canvas = Canvas(self.main_circle_mode_frame, bg = "#FFFFFF")
        self.main_circle_mode_canvas.pack(fill = BOTH, expand = 1)
        self.main_circle_mode_canvas.bind("<Button-1>", self.out_of_bound)
        

        #bottom circle mode frame
        self.bottom_circle_mode_frame = Frame(self.window, bg = self.bg_color)
        self.return_to_main_button6 = Button(self.bottom_circle_mode_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button6.pack(side = "bottom", fill = BOTH)

        #color result frame
        self.color_result_frame = Frame(self.window, bg = self.bg_color)
        self.main_color_mode_result = Label(self.color_result_frame, text = "", bg = self.bg_color, font = self.font) #this will be used in process reaction time function
        self.main_color_mode_result.pack(pady = 200)
        self.return_to_main_button3 = Button(self.color_result_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button3.pack(side = "bottom", fill = BOTH)

        #circle result frame
        self.circle_result_frame = Frame(self.window, bg = self.bg_color)
        self.main_circle_mode_result = Label(self.circle_result_frame, text = "", bg = self.bg_color, font = self.font) #this will be used in process reaction time circle function
        self.main_circle_mode_result.pack(pady = 200)
        self.return_to_main_button7 = Button(self.circle_result_frame, text = "Return to main menu", command = self.return_to_main, font = self.font)
        self.return_to_main_button7.pack(side = "bottom", fill = BOTH)

        #handle no save file error at the beginning of program launch
        try:
            if self.loaded_save_file.closed != False:
                pass
        except:
            pass

        self.window.mainloop()


    def start(self):
        self.remove_widgets()
        self.mode_select_frame.pack(fill = BOTH, expand = 1)
        
    def options(self):
        self.remove_widgets()
        self.option_frame.pack(fill = BOTH, expand = 1)
    
    def stats(self):
        self.history_list.delete("1.0", "end")
        try:
            save_file = open(self.load_file_name, "r")
            save_file_list = save_file.readlines()
            for line in save_file_list[1:]:
                self.history_list.insert(END, line)
            self.remove_widgets()
            self.stats_frame.pack(fill = BOTH, expand = 1)
        except:
            tkinter.messagebox.showwarning("No save found", "No save file has been selected")


    def return_to_main(self):
        self.remove_widgets()
        self.top_frame.pack(fill = BOTH)
        self.main_frame.pack(fill = BOTH, side = "top", expand = 1)
    
    def color_mode(self):
        self.remove_widgets()
        self.main_color_mode_canvas.configure(bg = "white")
        self.start_color_mode_button.pack(side = "bottom")
        self.top_color_mode_frame.pack(fill= BOTH)
        self.main_color_mode_frame.pack(fill = BOTH)
        self.bottom_color_mode_frame.pack(fill = BOTH, side = "bottom")
    
    def circle_mode(self):
        self.main_circle_mode_canvas["bg"] = "#FFFFFF"
        self.main_circle_mode_canvas.delete("all")
        self.start_circle_mode_button.pack(side = "bottom")
        self.remove_widgets()
        self.top_circle_mode_frame.pack(fill = BOTH)
        self.main_circle_mode_frame.pack(fill = BOTH)
        self.bottom_color_mode_frame.pack(fill = BOTH, side = "bottom")

    def random_circle(self):
        self.start_circle_mode_button.forget()
        self.main_circle_mode_canvas["bg"] = "#FEFFFF"
        number1 = [x for x in range(1,11)]
        number2 = [(x/100) for x in range(1,11)]

        time.sleep(random.choice(number1) + random.choice(number2))
        
        range_listx = [i for i in range(30,560)]
        range_listy = [i for i in range(30,240)]
        random_center1 = random.choice(range_listx)
        random_center2 = random.choice(range_listy)
        self.x1 = random_center1 - 30
        self.y1 = random_center2 - 30
        self.x2 = random_center1 + 30
        self.y2 = random_center2 + 30
        self.time_start_circle = time.time()
        self.circle = self.main_circle_mode_canvas.create_oval(self.x1,self.y1,self.x2,self.y2, tags = "circle", fill = "green")
        self.main_circle_mode_canvas.tag_bind(self.circle, '<Button-1>', self.process_reaction_time_circle)

    def random_time(self):
        number1 = []
        for x in range(1,11):
            number1.append(x)
        number2 = []
        for x in range(1,11):
            number2.append(x/100)
            
        time.sleep(random.choice(number1) + random.choice(number2))

        self.start_color_mode_button.forget()
        self.time_start = time.time()
        self.main_color_mode_canvas.config(bg = "green")
    
    def process_reaction_time_color(self,event):
        if self.main_color_mode_canvas["bg"] == "white":
            pass
        else:
            self.time_end = time.time()
            self.time_elapsed_in_ms = round((self.time_end - self.time_start)*1000, 3)

            if self.time_elapsed_in_ms < 25:
                self.remove_widgets()
                self.main_color_mode_result.config(text = "You clicked too early!")
                self.color_result_frame.pack(fill = BOTH, expand = 1)
                return

            self.remove_widgets()
            result_time = str(self.time_elapsed_in_ms) + " ms"
            self.main_color_mode_result.config(text = result_time)
            self.color_result_frame.pack(fill = BOTH, expand = 1)
            try:
                self.loaded_save_file = open(self.load_file_name, "a")
                infile_for_counting_lines = open(self.load_file_name, "r")
                number_of_lines = len(infile_for_counting_lines.readlines())
                infile_for_counting_lines.close()
                current_time_in_secs = time.time()
                local_time = time.ctime(current_time_in_secs)
                self.loaded_save_file.write("\n" + str(number_of_lines) + "." + " " + result_time + " Color Mode " + local_time)
                self.loaded_save_file.close()
            except:
                pass

    def process_reaction_time_circle(self,event):
        self.time_end_circle = time.time()
        self.time_elapsed_in_ms_circle = round((self.time_end_circle - self.time_start_circle)*1000, 3)

        self.remove_widgets()
        result_time_circle = str(self.time_elapsed_in_ms_circle) + " ms"
        self.main_circle_mode_result.config(text = result_time_circle)
        self.circle_result_frame.pack(fill = BOTH, expand = 1)
        try:
            self.loaded_save_file = open(self.load_file_name, "a")
            infile_for_counting_lines = open(self.load_file_name, "r")
            number_of_lines = len(infile_for_counting_lines.readlines())
            infile_for_counting_lines.close()
            current_time_in_secs = time.time()
            local_time = time.ctime(current_time_in_secs)
            self.loaded_save_file.write("\n" + str(number_of_lines) + "." + " " + result_time_circle + " Circle Mode " + local_time)
            self.loaded_save_file.close()
        except:
            pass

    def out_of_bound(self,event):
        try:
            if event.x > self.x1 and event.x < self.x2 and event.y > self.y1 and event.y < self.y2 or self.main_circle_mode_canvas["bg"] == "#FFFFFF":
                return
            self.remove_widgets()
            self.main_circle_mode_result.config(text = "You clicked outside of circle!")
            self.circle_result_frame.pack(fill = BOTH, expand = 1)
        except AttributeError:
            pass

    def process_color(self):
        if self.color_variable.get() == "light_yellow":
            inconfig = open("configs.txt", "r")
            configs_list = inconfig.readlines()
            configs_list[1] = "#fff0c7"
            inconfig.close()
            outconfig = open("configs.txt", "w")
            for line in configs_list:
                outconfig.write(line)
                    
        elif self.color_variable.get() == "light_red":
            inconfig = open("configs.txt", "r")
            configs_list = inconfig.readlines()
            configs_list[1] = "#FFC7C7"
            inconfig.close()
            outconfig = open("configs.txt", "w")
            for line in configs_list:
                outconfig.write(line)
        elif self.color_variable.get() == "light_blue":
            inconfig = open("configs.txt", "r")
            configs_list = inconfig.readlines()
            configs_list[1] = "#C7EDFF"
            inconfig.close()
            outconfig = open("configs.txt", "w")
            for line in configs_list:
                outconfig.write(line)

    def load_save(self):
        try:
            self.load_file_name = askopenfilename()
            outfile = open(self.load_file_name, "r")
            if outfile.read(5) != "Saves":
                raise InvalidSaveFile(self.load_file_name)
            else:
                outfile.close()
                save_name = self.load_file_name.split("/")
                self.option_load_status["text"] = save_name[-1] + " is loaded"  

        except InvalidSaveFile as ex:
            tkinter.messagebox.showerror("File Error", (str(ex.filename) + " is not a valid save file."))
        except:
            pass
                
    def create_save(self):
        try:
            self.create_file_name = asksaveasfilename()
            if os.path.isfile(self.create_file_name):
                tkinter.messagebox.askyesno("Overwrite save", "File already exists, do you want to overwrite it?")
            self.created_save_file = open(self.create_file_name, "w")
            self.created_save_file.write("Saves")
            self.created_save_file.close()
        except:
            pass

    def remove_widgets(self):
        for widget in self.window.winfo_children():
            widget.forget()

    def exit():
        exit()
    
class InvalidSaveFile(Exception):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

if __name__ == "__main__":
        reaction = Reaction()
        reaction.title("Reaction Speed Test")
        reaction.mainloop()