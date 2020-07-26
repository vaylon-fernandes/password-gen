from tkinter import Entry ,Tk,Button , Label,messagebox,Radiobutton, IntVar
import secrets
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
import pyperclip

letters_low = ascii_lowercase
letters_up = ascii_uppercase
numbers = digits
punctuations = punctuation 

char_list = [letters_low,letters_up,numbers,punctuations]

class PasswordGen:

	def __init__(self,base,low,upper,digit,punct):
		self.low = low
		self.upper = upper
		self.digit = digit
		self.punct = punct

		self.base = base
		base.title('Password Generator')
		base.geometry('400x400')

		self.title_lbl = Label(base,text = 'Password Generator')
		self.title_lbl.grid(column =0,row=1)
		
		self.lbl_lowercase = Label(base,text = 'Do you want lowercase letters?:')
		self.lbl_lowercase.grid(column = 0,row = 2)

		self.lower_yes = Radiobutton(base,text = 'Yes', variable = self.low, value = 1)
		self.lower_yes.grid(column = 1,row = 2)

		self.lower_no = Radiobutton(base,text = 'No', variable = self.low, value = 0)
		self.lower_no.grid(column = 2,row = 2)

		self.lbl_uppercase = Label(base,text = 'Do you want uppercase letters?:')
		self.lbl_uppercase.grid(column = 0,row = 3)
		
		self.upper_yes = Radiobutton(base,text = 'Yes', variable = self.upper, value = 1)
		self.upper_yes.grid(column = 1,row = 3)

		self.upper_no = Radiobutton(base,text = 'No', variable = self.upper, value = 0)
		self.upper_no.grid(column = 2,row = 3,sticky = 'e')

		self.lbl_digits = Label(base,text = 'Do you want numbers?:')
		self.lbl_digits.grid(column = 0,row = 4)
		
		self.digits_yes = Radiobutton(base,text = 'Yes', variable = self.digit, value = 1)
		self.digits_yes.grid(column = 1,row = 4)

		self.digits_no = Radiobutton(base,text = 'No', variable = self.digit, value = 0)
		self.digits_no.grid(column = 2,row = 4,sticky = 'e')

		self.lbl_punct = Label(base,text = 'Do you want punctuation marks?:')
		self.lbl_punct.grid(column = 0,row = 5)
		
		self.punct_yes = Radiobutton(base,text = 'Yes', variable = self.punct, value = 1)
		self.punct_yes.grid(column = 1,row = 5)

		self.punct_no = Radiobutton(base,text = 'No', variable = self.punct, value = 0)
		self.punct_no.grid(column = 2,row = 5,sticky = 'e')

		self.lbl_length = Label(base,text = 'Password Length')
		self.lbl_length.grid(column = 0,row = 6)

		self.inputbox_length = Entry(base,width=10)
		self.inputbox_length.grid(column = 1,row = 6)

		self.password_lbl = Label(base,text = 'Password')
		self.password_lbl.grid(column = 0,row = 7 )

		self.display_password = Entry(base,width = 30)
		self.display_password.grid(column = 0, row = 8)
		
		self.generate_btn = Button(base,text = "Generate",command = self.generate)
		self.generate_btn.grid(column = 0,row = 9,)

		self.copy_btn = Button(base,text = "Copy to Clipboard",command = self.copy)
		self.copy_btn.grid(column = 1,row = 9,sticky = 'w')

		self.exit_btn = Button(base,text = 'exit',command = base.destroy)
		self.exit_btn.grid(column =0, row = 10)



	def get_choice(self):
		password_str = ''
		choice_list = [self.low.get(),self.upper.get(),self.digit.get(),self.punct.get()]

		for i in range(len(choice_list)):
			if choice_list[i]:
				password_str = password_str + char_list[i]
		return password_str

	def generate(self):
		password_str = ''
		choice = PasswordGen.get_choice(self)
		length = self.inputbox_length.get()

		if length != '':
			try:
				for i in range(int(length)):
					password_str = password_str + secrets.choice(choice)
				self.display_password.delete(0,'end')
				self.display_password.insert(0,password_str)

			except IndexError:
				messagebox.showinfo('Select option','Please select at least on option as "Yes" ')
		else:
			messagebox.showinfo('Enter Length','Please Enter the Length')

	def copy(self):
		pyperclip.copy(self.display_password.get())
		messagebox.showinfo(title='Info',message='Password has been copied to your Clipboard')


	
root = Tk()
gui = PasswordGen(root,low = IntVar(),upper = IntVar(),digit=IntVar(),punct=IntVar())
root.mainloop()

