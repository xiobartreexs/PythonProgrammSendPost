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
		self.L1 = tk.Label(text = ":", font = "Arial 25", justify = tk.CENTER)
		
		self.dirs = tk.Entry(width = 25)
		self.url = tk.Entry(width = 25)
		self.data = tk.Entry(width = 12)
		self.data_value = tk.Entry(width = 12)

		self.button_file = tk.Button(root, text = "Click file", command =self.file_dir)
		self.button_data = tk.Button(root, text = "Click add", command =self.data_send)
		self.button_delete = tk.Button(root, text = "Click delete", command =self.data_delete)
		self.button_edit = tk.Button(root, text = "Click edit", command =self.data_edit)
		self.send_file = tk.Button(root, text = "Click send", command =self.send)
		self.button_test = tk.Button(root, text = "Click test", command =self.test)
		
		self.list_box_2 = tk.Listbox()

		self.L0.grid(row = 0, column = 2)
		self.L1.grid(row = 1, column = 2)
		
		self.url.grid(row = 1, column = 1)
		self.data.grid(row = 1, column = 1, columnspan = 2)
		self.data_value.grid(row = 1, column = 2, columnspan = 2)
		self.dirs.grid(row = 1, column = 3)

		self.button_file.grid(row = 2, column = 3)

		self.send_file.grid(row = 2, column = 1)

		self.button_edit.grid(row = 2, column = 1, columnspan = 2)
		self.button_data.grid(row = 2, column = 2, columnspan = 1)
		self.button_delete.grid(row = 2, column = 2, columnspan = 3)
		
		self.button_test.grid(row = 3, column = 3)

		

		self.list_box_2.grid(row = 4 ,column = 2, sticky = tk.W+tk.E)

		self.dirs.insert(0,'Выбериет файл который хотите отправить на сервер')
		self.url.insert(0,'http://httpbin.org/post')
		
		self.list_box_2.bind("<<ListboxSelect>>", self.test)

	def data_edit(self):
		data = self.data.get()
		data_value = self.data_value.get()
		index = self.list_box_2.curselection()

		self.list_box_2.delete(index, index)
		self.list_box_2.insert(0, f'{data} : {data_value}')


	def test(self,get):
		data = self.list_box_2.get(self.list_box_2.curselection())
		
		data_key = data.split(" : ")[0]
		data_value = data.split(" : ")[1]

		self.data.delete(0, tk.END)
		self.data_value.delete(0, tk.END)

		self.data.insert(0, data_key)
		self.data_value.insert(0, data_value)


	def file_dir(self):
		file = filedialog.askopenfilename()
		self.dirs.delete(0, tk.END)
		self.dirs.insert(0, f"{file},")

	def data_send(self):
		
		data = self.data.get()
		data_value = self.data_value.get()
		if data == '':
			pass
		else:
			sel = self.list_box_2.curselection()
			self.list_box_2.insert(0, f'{data} : {data_value}')

	def data_delete(self):

		

		sel = self.list_box_2.curselection()

		if sel == ():
			pass
		else:
			self.list_box_2.delete(sel[0])

	def send(self):
		dirs = self.dirs.get()
		url = self.url.get()
		dir_file = dirs.split(',')
		files = {'file' : dir_file}
		data_box = {}

		for data in self.list_box_2.get(0, tk.END):
			data_key = data.split(" : ")[0]
			data_value = data.split(" : ")[1]
			if data_value == "":
				pass
			else:
				data_box[data_key] = data_value

		s = requests.post(url, data = data_box, files= files if files == "" else None)
		log = s.text
		json_data = json.loads(log)
		list_box = tk.Listbox()
		list_box.grid(row = 2 ,column = 2, sticky = tk.W+tk.E)
		

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