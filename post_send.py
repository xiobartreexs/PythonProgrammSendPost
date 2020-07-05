import requests
from tkinter import filedialog
import tkinter as tk
from tkinter import Menu
import json
 
root = tk.Tk()
root.title("MyFirstProgramm")
menu = Menu(root)
menu.add_command(label='File')
root.config(menu=menu)
new_item = Menu(menu)
new_item.add_command(label='Новое')
menu.add_cascade(label='Файл', menu=new_item)
new_item.add_separator()
new_item.add_command(label='Редактирование')




#file = filedialog.askopenfilename()
#print(file)

#print("--------------------------------------------------")

#files = filedialog.askopenfilenames()
#print(files)

#print("--------------------------------------------------")

#files_txt = filedialog.askopenfilename(filetypes = (('Только текстовые файлы','*.txt'),('Все файлы','*.*')))
#print(files_txt)

#print("--------------------------------------------------")

#dirs = filedialog.askdirectory()
#print(dirs)


class Programm():
	def __init__(self,root):

		self.L0 = tk.Label(text = "Выберите файл который хотите отправить на серврер", font = "Arial 10", justify = tk.CENTER)
		self.dirs = tk.Entry(width = 25)
		self.url = tk.Entry(width = 25)
		self.button_file = tk.Button(root, text = "Click file", command =self.file_dir)
		self.send_file = tk.Button(root, text = "Click send", command =self.send)
		
		self.L0.grid(row = 0, column = 2)
		self.dirs.grid(row = 1, column = 3)
		self.url.grid(row = 1, column = 1)
		self.button_file.grid(row = 2, column = 3)
		self.send_file.grid(row = 2, column = 1)
		
		self.dirs.insert(0,'Выбериет файл который хотите отправить на сервер')
		self.url.insert(0,'http://httpbin.org/post')

	def file_dir(self):
		file = filedialog.askopenfilename()
		self.dirs.delete(0, tk.END)
		self.dirs.insert(0, f"{file},")

	def send(self):
		dirs = self.dirs.get()
		url = self.url.get()
		dir_file = dirs.split(',')
		files = {'file' : dir_file}

		s = requests.post(url, files=files)
		log = s.text
		json_data = json.loads(log)
		list_box = tk.Listbox(width = 100)
		list_box.grid(row = 2 ,column = 2)
		for name in json_data:
			if name == "headers":
				for name_head in json_data['headers']:
					list_box.insert(0, f"{name_head} : {json_data['headers'][name_head]}")
			else:
				if json_data[name] == None or json_data[name] == {} or json_data[name] == " ":
					pass
				else:
					list_box.insert(0, f"{name} : {json_data[name]}")
s = Programm(root)

root.mainloop()
