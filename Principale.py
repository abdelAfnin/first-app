from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import customtkinter
import os
import Frm
import pygame
import time
import Frm

#=======Password===========
password = '0000'

#============ functions ==========

#====== create numbers in entry ==========
def Click(k):
	compt =entry_password.get()
	entry_password.delete(0,END)
	entry_password.insert(0, str(compt) + str(k))

#===swap frames ====
def Go_to(frames):
	frames.tkraise()

 #=== create number in entry ======

def go_to_frame_question():
	time.sleep(3)
	frame_Wait.tkraise().destroy()
	frame_question.tkraise()

#============ Password function==========
def verifier(): 
	if entry_password.get() == password:
		print(entry_password.get())
		frame_Wait.tkraise()
		
	elif entry_password.get() != password:
		frame_home.tkraise()
		delete()
		# messagebox.showerror("FAUX","le mot de pass inccorect")
		messagebox.showwarning("ERROR","le mot de pass inccorect")

#========= fun delete ===========
def delete():
	entry_password.delete(0, END)

#======== CLASS ============

#==== class modern buttons ==========

class Btn():
	def __init__(self,master):
		self.master=master
				#------canvas message 'entrer votre mot de pass'------
		self.canvas_message=Canvas(self.master,width=275,height=130,bg="#00074c",bd=5,relief=RAISED)
		self.canvas_message.place(x=645,y=50)
				
		#===========Frames ==========================================
		self.frm_categorie=Frame(self.master,width=500,height=150,bg='#6b75c3')
		self.frm_categorie.place(x=70,y=485)

		#=========== canvas Buttons ================================
		self.canvas_buttons=Canvas(self.master,width=275,height=260,bg="#00074c",bd=5,relief=GROOVE)
		self.canvas_buttons.place(x=645,y=200)
	
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
		    command=verifier,
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
		#========== BUTTON DELETE ======
		Button_delete = customtkinter.CTkButton(
		    master= self.master,
		    command=delete,
		    text= "X",
		    text_font="none 15 bold",
		    text_color="white",##68aec9
		    hover= True,
		    hover_color= "red",
		    height=45,
		    width= 20,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#727dd1", #727dd1
		    fg_color= "#00074c")
		Button_delete.place(x=905,y=495)

#==== class infos condidats==========

class Lbl:
	def __init__(self,master):
		self.master=master
	def labels(self):


		lbl_arb = customtkinter.CTkButton(
		    master= self.master,
		    text= "رقم البطاقة\n الوطنية",
		    text_font="none 12 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width= 120,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_arb.place(x=450,y=488)

		lbl_arb_type = customtkinter.CTkButton(
		    master= self.master,
		    text= "نوع الرخصة",
		    text_font="none 12 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width= 120,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_arb_type.place(x=450,y=540)


		lbl_fr_arb = customtkinter.CTkButton(
		    master= self.master,
		    text= " العربية ",
		    text_font="none 12 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=42,
		    width= 220,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_fr_arb.place(x=220,y=588)
		

		lbl_fr_type = customtkinter.CTkButton(
		    master= self.master,
		    text= "TYPE PERMIS",
		    text_font="none 10 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width= 60,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_fr_type.place(x=75,y=540)

		lbl_cat = customtkinter.CTkButton(
		    master= self.master,
		    text= "CATEGORIE B",
		    text_font="none 10 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width= 220,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_cat.place(x=220,y=540)

		lbl_arab = customtkinter.CTkButton(
		    master= self.master,
		    text= "اللغة",
		    text_font="none 12 bold",
		    text_color="white",##68aec9
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width= 120,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_arab.place(x=450,y=588)

		lbl_fr_cin = customtkinter.CTkButton(
		    master= self.master,
		    text= "NUMERO CIN ",
		    text_font="none 10 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=48,
		    width= 80,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_fr_cin.place(x=75,y=488)# -15px

		lbl_fr_langue = customtkinter.CTkButton(
		    master= self.master,
		    text= "LANGUE",
		    text_font="none 10 bold",
		    text_color="white",
		    hover= True,
		    hover_color= "#00074c",
		    height=45,
		    width=130 ,
		    border_width=2,
		    corner_radius=20,
		    border_color= "#68aec9", 
		    bg_color="#6b75c3",
		    fg_color= "#00074c")
		lbl_fr_langue.place(x=75,y=588)

		#==== Label msg "ENTRER VOTRE MOT DE PASS" =====
		lbl_msg=Label(self.master,text="Entrer votre mot de passe \n\n أدخلوا رقمكم السري",fg='white',font=('Helvetica',16,'bold'),bg='#00074c')
		lbl_msg.place(x=650,y=75)

#========== HOME WINDOW ============
root= Tk()
# root.geometry("1210x710+1+1")
root.state("zoomed")
root.title('AppWork')
# root.iconbitmap('logo1.ico')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
#===========================


#======insertion image au home=========
path_image=os.getcwd()
print("this path only :"+path_image+"\\car.png")
img= ImageTk.PhotoImage(Image.open(path_image+"\\car.png"))
#============================

##=============frame d'application ====================
frame_home = Frame(root,bg='#496997')
frame_Wait= Frame(root,bg='#496997')
frame_question=Frame(root,bg='cyan')

for frames in (frame_home,frame_Wait, frame_question):
	frames.grid(row=0,column=0,sticky='nsew')

# #============ Frame login ============================
frame_login=Frame(frame_home,
				width=1040,
				height=680,
				bg='#727dd1',
				highlightbackground="#7581df",
			 	highlightthickness=20)
frame_login.place(x=150,y=15)
#============== Labels =================================
canvas_car  = Label(frame_login,
					image=img,
					width=500,
					height=450,
					bg='white'
					)
canvas_car.place(x=70,y=25)



#============== call class buttons ====================
botons = Btn(frame_login)
btn=botons.button()

#=========== Entry Password =========

entry_password = Entry(frame_login,
						width=10,
						font=('Tajawal',20,'bold'),
						fg='white',
						bg='#00074c',
						show="*"
						)
entry_password.place(x=725 ,y=500)

#==== Entry N° CIN ====

entry_cin=Entry(frame_login,
				width=16,
				fg='white',
				bg="#00074c",
				font=('Tajawal 18 bold')
				)
entry_cin.place(x=224, y=496)
#============== call class info condidats ========
info=Lbl(frame_login)
infos=info.labels()
#============ class frame Wait ===========

page = Frm.Page2(frame_Wait)

#======= button of exit program ==========

# stopped=Button(frame_Wait, text='STOP', font=('Tajawal', 15, 'bold'),command=Frm.stop_and_refresh)
# stopped.place(x=1135, y=20)
def sortie():
	frame_Wait.quit()

def stoop():
	win.destroy()
	
sortie=customtkinter.CTkButton(
					master=frame_Wait,
				    text= "خروج",
				    command= sortie,
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "red",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#496997",
				    fg_color= "GREEN"
						)
sortie.place(x=1135, y=640)

#=========================================

frame_home.tkraise()

root.protocol("WM_WINDOW_DELETE", stoop)

root.mainloop()