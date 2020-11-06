from tkinter import Entry ,Tk,Button , Label,messagebox,Radiobutton, IntVar,Frame,Scrollbar,Listbox
import secrets
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import pyperclip

letters_low = ascii_lowercase
letters_up = ascii_uppercase
numbers = digits
punctuations = punctuation 

char_list = [letters_low,letters_up,numbers,punctuations]

class PasswordGen:
	
	def __init__(self,base):

		self.low = IntVar()
		self.upper = IntVar()
		self.digit=IntVar()
		self.punct=IntVar()

		self.base = base
		base.title('Password Generator')
		base.geometry('400x400')

		self.title_lbl = Label(base,text = 'Password Generator')
		self.title_lbl.pack()
		
		self.frame = Frame(base)
		self.frame.pack()

		self.mid_frame = Frame(base)
		self.mid_frame.pack()

		self.lbl_lowercase = Label(self.frame,text = 'Do you want lowercase letters (a-z) ?:')
		self.lbl_lowercase.grid(column = 0,row = 1)

		self.lower_yes = Radiobutton(self.frame,text = 'Yes', variable = self.low, value = 1)
		self.lower_yes.grid(column = 1,row = 1)

		self.lower_no = Radiobutton(self.frame,text = 'No', variable = self.low, value = 0)
		self.lower_no.grid(column = 2,row = 1)

		self.lbl_uppercase = Label(self.frame,text = 'Do you want uppercase letters (A-Z) ?:')
		self.lbl_uppercase.grid(column = 0,row = 2)
		
		self.upper_yes = Radiobutton(self.frame,text = 'Yes', variable = self.upper, value = 1)
		self.upper_yes.grid(column = 1,row = 2)

		self.upper_no = Radiobutton(self.frame,text = 'No', variable = self.upper, value = 0)
		self.upper_no.grid(column = 2,row = 2,sticky = 'e')

		self.lbl_digits = Label(self.frame,text = 'Do you want numbers (0-9) ?:')
		self.lbl_digits.grid(column = 0,row = 3)
		
		self.digits_yes = Radiobutton(self.frame,text = 'Yes', variable = self.digit, value = 1)
		self.digits_yes.grid(column = 1,row = 3)

		self.digits_no = Radiobutton(self.frame,text = 'No', variable = self.digit, value = 0)
		self.digits_no.grid(column = 2,row = 3,sticky = 'e')

		self.lbl_punct = Label(self.frame,text = 'Do you want punctuation marks \n(eg:!\"#$%&\'()*+,-.) ?:')
		self.lbl_punct.grid(column = 0,row = 4)
		
		self.punct_yes = Radiobutton(self.frame,text = 'Yes', variable = self.punct, value = 1)
		self.punct_yes.grid(column = 1,row = 4)

		self.punct_no = Radiobutton(self.frame,text = 'No', variable = self.punct, value = 0)
		self.punct_no.grid(column = 2,row = 4,sticky = 'e')

		self.lbl_length = Label(self.frame,text = 'Password Length')
		self.lbl_length.grid(column = 0,row = 5)

		vcmd = base.register(self.validate)

		self.inputbox_length = Entry(self.frame,width=10,validate="key",validatecommand=(vcmd,'%P'))
		self.inputbox_length.grid(column = 1,row = 5)

		self.password_lbl = Label(self.mid_frame,text = 'Password')
		self.password_lbl.pack()

		self.scroll_bar = Scrollbar(self.mid_frame,orient='''horizontal''')
		self.scroll_bar.pack(side='''bottom''',fill='''x''')

		self.display_password = Listbox(self.mid_frame,height=1,width = 30,xscrollcommand=self.scroll_bar.set)
		self.display_password.pack(side='''left''')
		self.scroll_bar.config(command=self.display_password.xview)

		self.generate_btn = Button(self.mid_frame,text = "Generate",command = self.display)
		self.generate_btn.pack(side='''left''')

		self.bottom_frame = Frame()
		self.bottom_frame.pack()

		self.copy_btn = Button(self.bottom_frame,text = "Copy to Clipboard",command = self.copy)
		self.copy_btn.pack()

		self.exit_btn = Button(self.bottom_frame,text = 'exit',command = base.destroy)
		self.exit_btn.pack()


	def validate(self,text):
		if text == "":
			return True
		elif text.isdigit():
			return True 
		else:
			return False


	def get_choice(self):
		choice_str = ''
		choice_list = [self.low.get(),self.upper.get(),self.digit.get(),self.punct.get()]

		for i in range(len(choice_list)):
			if choice_list[i]:
				choice_str = choice_str + char_list[i]
		return choice_str

	def generate(self):
		password = ''
		choice = self.get_choice()
		length = self.inputbox_length.get()	

		if length == '0':
			messagebox.showinfo("Info","Please Enter Number greater than 0.")
		else:
			try: 
				for i in range(int(length)):
					password = password + secrets.choice(choice)
			except ValueError:
				messagebox.showinfo("Enter Length","Please enter a number in the length field.")
			except IndexError:
				messagebox.showinfo("No option selected","Please select at least one option 'Yes'.")
		return password

	def display(self):
		password = self.generate()
		self.display_password.delete(0,"end")
		self.display_password.insert(0,password)
		


	def copy(self):
		password = self.display_password.get(0)
		if password == '':
			messagebox.showinfo("Password not generated.","Please Generate a password first.")
		else:
			pyperclip.copy(password)
			messagebox.showinfo(title='Info',message='Password has been copied to your Clipboard')


	
root = Tk()
gui = PasswordGen(root)
root.mainloop()
