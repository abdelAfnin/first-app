#custom buttons templates
from tkinter import *
from tkinter import messagebox
import customtkinter



#=== mot de pass ===
def verifier(): 
	if entry_password.get() == password:
		print(entry_password.get())

		f2.tkraise()
	elif entry_password.get() != password:
		f1.tkraise()
		# messagebox.showinfo("FAUX","le mot de pass inccorect")
		messagebox.showwarning("FAUX","le mot de pass inccorect")



class Btn():
	def __init__(self,master):
		self.master=master


	def button(self): 

		#=============BUTTON_9============================================================
		Button_9 = customtkinter.CTkButton(
		    master= self.master,
		    command= lambda:Click(9),
		    text= "9",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_9.place(x=670,y=220)# 760,260    -90-40

		#=============BUTTON_8=============================================================
		Button_8 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(8),
		    text= "8",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_8.place(x=755,y=220)

		#=============BUTTON_7==============================================================
		Button_7 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(7),
		    text= "7",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_7.place(x=840,y=220)


		#=============BUTTON_4=================================================================
		Button_4 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(4),
		    text= "4",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_4.place(x=670,y=280)

		#=============BUTTON_5=================================================================
		Button_5 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(5),
		    text= "5",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_5.place(x=755,y=280)

		#=============BUTTON_6==================================================================
		Button_6 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(6),
		    text= "6",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_6.place(x=840,y=280)

		#=============BUTTON_1===============================================================
		Button_1 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(1),
		    text= "1",
		    text_font="none 20 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_1.place(x=670,y=340)

		#=============BUTTON_2=================================================================
		Button_2 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(2),
		    text= "2",
		    text_font="none 20 bold",
		    text_color="white",#68aec9
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_2.place(x=755,y=340)

		#=============BUTTON_3==================================================================
		Button_3 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(3),
		    text= "3",
		    text_font="none 20 bold",
		    text_color="white",##68aec9
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_3.place(x=840,y=340)

		#=============BUTTON_0==================================================================
		Button_0 = customtkinter.CTkButton(
		    master= self.master,
		    command=lambda:Click(0),
		    text= "0",
		    text_font="none 20 bold",
		    text_color="white",##68aec9
		    hover= True,
		    hover_color= "black",
		    height=45,
		    width=230,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#00074c",
		    fg_color= "#00074c")
		Button_0.place(x=670,y=400)

		#==========BUTTON ENTRER==========
		Button_entrer = customtkinter.CTkButton(
		    master= self.master,
		    #command=verfier,
		    text= "ENTRER",
		    text_font="none 20 bold",
		    text_color="white",##68aec9
		    hover= True,
		    hover_color= "#A4DF68",
		    height=45,
		    width= 30,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#727dd1", #727dd1
		    fg_color= "#00074c")
		Button_entrer.place(x=810,y=580)




		#====== box CIN && password =======

		


		

