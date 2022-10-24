from tkinter import *
import customtkinter
import pygame
import os
import sqlite3
from time import time, sleep
from PIL import ImageTk, Image
import threading
from tkinter import ttk




# def Question():
# 	connection=sqlite3.connect("data.db")
# 	cursor=connection.cursor()
# 	cursor.execute("SELECT image_question,audio_question, * FROM Question limit 40")

# 	variable = cursor.fetchall()
# 	pygame.mixer.init()
# 	for x in variable:
# 		url_image=os.getcwd()+str(x[0])
# 		url_audio=os.getcwd()+str(x[1])

# 		img= ImageTk.PhotoImage(Image.open(url_image))

# 	    lblvideo = Label(self.canvas_video,image=img,width=700,height=500)
# 	    lblvideo.place(x=240, y=10)
# 		print(url+"\n")
# 	    pygame.mixer.music.load(url_audio)
# 	    pygame.mixer.music.play(loops=0)
# 	    time.sleep(10)
# 	connection.commit()
# 	connection.close()

	
	



   # play()
# def call_id(k):
# 	global reponce
# 	reponce = k
# 	return reponce

def stop_and_refresh():
	pygame.mixer.music.stop() 
	label.destroy()           


	# a=Page2(frame_Wait).canvas_video
	# label = Label(a)
	# label.pack()
	


class Page2:
	def __init__(self, master):
		global label
		self.master=master
		self.frame_scroll = Frame(self.master,
					width=200,
					height=710,
					bg='#00074c'
					)
		self.frame_scroll.pack(side=LEFT, fill=BOTH)
		self.canvas_scroll = Canvas(self.frame_scroll,
							width=200,
							height=710,
							bg='#00074c'
							)
		self.canvas_scroll.pack(side=LEFT, fill=BOTH)
		self.Scroll = Scrollbar(self.frame_scroll,
							 orient=VERTICAL,
							 command=self.canvas_scroll.yview
		 					)
		self.Scroll.pack(side=RIGHT, fill=Y)
		self.canvas_scroll.configure(yscrollcommand=self.Scroll.set)
		self.canvas_scroll.bind('<Configure>', lambda e:self.canvas_scroll.config(scrollregion=self.canvas_scroll.bbox("all")))
		self.frm_in =Frame(self.frame_scroll, bg='#00074c')
		self.canvas_scroll.create_window((0,0), window=self.frm_in, anchor="nw")
		#=============================================
		self.Scrollbar_series=self.button_serie() #button_serie.
		#============== Remote answers ===============
		#=============================================
		self.canvas_remote = Canvas(self.master,
								width=200,
								height=450,
								bg='#00074c',
								bd=4,
								relief=RAISED
								)
		self.canvas_remote.place(x=1090, y=130)

		# self.canvas_reponce=Canvas(self.master,width=200,
									 # height=60,
									 # bg='#496997',
									 # bd=0,
									 # relief=SOLID)
		# self.canvas_reponce.place(x=1090, y=40)

		# self.button_remote=Remote(self.canvas_remote)
		# self.buttons_remote=self.button_remote.button_remote()
		


		self.button_remote()

		self.canvas_video = Canvas(self.master,
								width=800,
								height=600,
								bd=4,
								relief=GROOVE
		 						)
		self.canvas_video.place(x=240, y=10)
	

	
	def play(self,k):
		global keyAnswer
		global N
		global answer_txt
		global label


		import sqlite3

		# self.canvas_video = Canvas(self.master,
		# 						width=800,
		# 						height=600,
		# 						bd=4,
		# 						relief=GROOVE
		#  						)
		# self.canvas_video.place(x=240, y=10)
		label = Label(self.canvas_video)
		label.pack()

		self.connection=sqlite3.connect("data.db")
		self.cursor=self.connection.cursor()
		self.cursor.execute('SELECT image_question,audio_question,reponce_txt, * FROM Questions LIMIT 40')

		self.variable = self.cursor.fetchall()
		self.delay = 7

		# label.pack()
		def keyAnswer(k):
			global N
			N = k
			if str(N) == '1':
				Label(self.master,text="1", width=3, height=4,fg='white',font=('Tajawal',18,'bold'),bg='#496997',anchor = 'center').place(x=1090, y=1)
			elif str(N) == '2':
				Label(self.master,text="2", width=3, height=4,fg='white',font=('Tajawal',18,'bold'),bg='#496997',anchor = 'center').place(x=1135, y=1)
			elif str(N) == '3':
				Label(self.master,text="3", width=3, height=4,fg='white',font=('Tajawal',18,'bold'),bg='#496997',anchor = 'center').place(x=1180, y=1)
			elif str(N) == '4':
				Label(self.master,text="4", width=3, height=4,fg='white',font=('Tajawal',18,'bold'),bg='#496997',anchor = 'center').place(x=1225, y=1)
			
			return N

		compteur = 0
		pygame.mixer.init()
		for x in self.variable:
			global answer_txt
			if k == 1:
			
				self.path=os.getcwd()+str(x[0])
				print(self.path)
				
				self.image = Image.open(self.path)
				self.image = self.image.resize((800, 600), Image.LANCZOS)
				self.image_object = ImageTk.PhotoImage(self.image)
				
				label.config(image=self.image_object)
				# label = Label(self.canvas_video)
				
				self.lien = os.getcwd() + str(x[1])
				print(self.lien)

				pygame.mixer.music.load(self.lien)
				pygame.mixer.music.play(loops=0)

				self.lien_txt = os.getcwd() + str(x[2])

				self.var = open(self.lien_txt, "r")

				answer_txt = self.var.readline()[0]
				print(answer_txt)

				if str(N) == answer_txt:

					print(f'le nombre N est :{N}')
					compteur = compteur + 1
				print(f"compteur de reponces est : {compteur}")
				N=0
				'''
				i le id de ligne qui lire
				'''
				self.var.close()
				#===================================================
				
				self.canvas_video.update()
				sleep(self.delay)
			else:
				break
			print(f'la resultat total est:{compteur}/40')

		self.connection.commit()
		self.connection.close()


	# 	#+++++++++++++ canvas video =============
	# 	#"========================================"
	
	def button_remote(self):

		Corriger=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "Corriger",
				    command= lambda:keyAnswer(0),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "red"
 					)
		Corriger.pack(padx=20, pady=10)

		reponce_1=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "الجواب 1",
				    command= lambda:keyAnswer(1),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
 					)
		reponce_1.pack(padx=20, pady=20)


		reponce_2=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "االجواب 2",
				    command= lambda:keyAnswer(2),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", #68aec9
				    bg_color="#00074c",
				    fg_color= "#00074c"
 					)
		reponce_2.pack(padx=20, pady=10)


		reponce_3=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "االجواب 3",
				    command= lambda:keyAnswer(3),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
 					)
		reponce_3.pack(padx=20, pady=10)

		reponce_4=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "الجواب 4",
				    command= lambda:keyAnswer(4),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
 					)
		reponce_4.pack(padx=20, pady=10)

		Validé=customtkinter.CTkButton(
 					master= self.canvas_remote,
				    text= "Validé",
				    command= lambda:id(1),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=40,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "GREY"
 					)
		Validé.pack(padx=20, pady=20)
	def button_serie(self):
		
		btn1=customtkinter.CTkButton(
					master=self.frm_in,
				    text= "السلسلة  1",
				    command=lambda:threading.Thread(target=self.play, args=(1, )).start(),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"

						)
		# btn1.bind("<Button-2>",self.play)
		btn1.grid(row=1,column=1,padx=20, pady=10)

		btn2=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  2",
				    command= lambda:threading.Thread(target=self.play, args=(1, )).start(),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn2.grid(row=2,column=1,padx=20, pady=10)

		btn3=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  3",
				    command= lambda:threading.Thread(target=self.play, args=(1, )).start(),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn3.grid(row=3,column=1,padx=20, pady=10)

		btn4=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  4",
				    command= lambda:call_id(4),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn4.grid(row=4,column=1,padx=20, pady=10)

		btn5=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  5",
				    command= lambda:call_id(5),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn5.grid(row=5,column=1,padx=20, pady=10)

		btn6=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  6",
				    command= lambda:call_id(6),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn6.grid(row=6,column=1,padx=20, pady=10)

		btn7=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  7",
				    command= lambda:call_id(7),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn7.grid(row=7,column=1,padx=20, pady=10)

		btn8=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  8",
				    command= lambda:call_id(8),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn8.grid(row=8,column=1,padx=20, pady=10)

		btn9=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  9",
				    command= lambda:call_id(9),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn9.grid(row=9,column=1,padx=20, pady=10)

		btn10=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  10",
				    command= lambda:call_id(10),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn10.grid(row=10,column=1,padx=20, pady=10)

		btn11=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  11",
				    command= lambda:call_id(11),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
						)
		btn11.grid(row=11,column=1,padx=20, pady=10)

		btn12=customtkinter.CTkButton(
					master= self.frm_in,
				    text= "السلسلة  12",
				    command= lambda:call_id(12),
				    text_font="none 20 bold",
				    text_color="white",
				    hover= True,
				    hover_color= "GREEN",
				    height=45,
				    width= 40,
				    border_width=2,
				    corner_radius=20,
				    border_color= "#68aec9", 
				    bg_color="#00074c",
				    fg_color= "#00074c"
					)
		btn12.grid(row=12,column=1,padx=20, pady=10)
	# def button_remote(self):


	# 	Corriger=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "Corriger",
	# 			    command= lambda:self.call_id(1),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=20,
	# 			    border_color= "#68aec9", 
	# 			    bg_color="#00074c",
	# 			    fg_color= "red"
 # 					)
	# 	Corriger.pack(padx=20, pady=10)

	# 	reponce_1=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "الجواب 1",
	# 			    command= lambda:self.call_id(1),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=20,
	# 			    border_color= "#68aec9", 
	# 			    bg_color="#00074c",
	# 			    fg_color= "#00074c"
 # 					)
	# 	reponce_1.pack(padx=20, pady=20)


	# 	reponce_2=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "االجواب 2",
	# 			    command= lambda:self.call_id(2),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=20,
	# 			    border_color= "#68aec9", #68aec9
	# 			    bg_color="#00074c",
	# 			    fg_color= "#00074c"
 # 					)
	# 	reponce_2.pack(padx=20, pady=10)


	# 	reponce_3=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "االجواب 3",
	# 			    command= lambda:self.call_id(3),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=20,
	# 			    border_color= "#68aec9", 
	# 			    bg_color="#00074c",
	# 			    fg_color= "#00074c"
 # 					)
	# 	reponce_3.pack(padx=20, pady=10)

	# 	reponce_4=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "الجواب 4",
	# 			    command= lambda:self.call_id(4),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=20,
	# 			    border_color= "#68aec9", 
	# 			    bg_color="#00074c",
	# 			    fg_color= "#00074c"
 # 					)
	# 	reponce_4.pack(padx=20, pady=10)

	# 	Validé=customtkinter.CTkButton(
 # 					master= self.canvas_remote,
	# 			    text= "Validé",
	# 			    command= lambda:id(1),
	# 			    text_font="none 20 bold",
	# 			    text_color="white",
	# 			    hover= True,
	# 			    hover_color= "GREEN",
	# 			    height=45,
	# 			    width= 40,
	# 			    border_width=2,
	# 			    corner_radius=40,
	# 			    border_color= "#68aec9", 
	# 			    bg_color="#00074c",
	# 			    fg_color= "GREY"
 # 					)
	# 	Validé.pack(padx=20, pady=20)



	# 	#+++++++++++++ canvas video =============
	# 	#"========================================"
	









