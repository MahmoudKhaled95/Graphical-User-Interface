'''*****************************************************************************************************************************************************************
* File Name: GUI.py 
*
* Description: GUI for medical robot
*
* Author: Mahmoud Khaled
          Mohamed Adel
          Mohamed Ragab
*
********************************************************************************************************************************************************************'''

from ast import Pass
from distutils.command.bdist_rpm import bdist_rpm
import random
from click import command
import cv2
import imutils
import webbrowser
import numpy as np
import smtplib
from pygame import mixer
from tkinter import *
from PIL import ImageTk,Image
from time import strftime,sleep
import threading
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#sensors imports
import time
import os
#import max30100
#from smbus2 import SMBus
#from mlx90614 import MLX90614


#Vital measures Global
global g_Temperature_Test
g_Temperature_Test = "Not Tested"
global g_HeartRate_Test
g_HeartRate_Test = "Not Tested"
global g_OxygenPrecentage_Test
g_OxygenPrecentage_Test = "Not Tested"
global g_Covid19_Test
g_Covid19_Test = "Not Tested"
global g_Pneumonia_Test
g_Pneumonia_Test = "Not Tested"
bpm = None
spo2 = None
temp = 0
#ID of Patiant
Patient_ID_Num = 10
ID_list = []

def changeIdNumber():
    global g_Temperature_Test
    global g_HeartRate_Test
    global g_OxygenPrecentage_Test
    global g_Covid19_Test
    global g_Pneumonia_Test
    #reset al measures for new Patient with new ID
    g_Temperature_Test = "Not Tested"
    g_HeartRate_Test = "Not Tested"
    g_OxygenPrecentage_Test = "Not Tested"
    g_Covid19_Test = "Not Tested"
    g_Pneumonia_Test = "Not Tested"
    #Patient ID Global variable
    #import random number for patient ID
    g_ID_NUM =random.randint(1,100)
    #print (g_ID_NUM)
    #genrate ID without repetition
    global ID_list 
    while g_ID_NUM in ID_list:
        g_ID_NUM = random.randint(1,100)
    ID_list.append(g_ID_NUM)
    global Patient_ID_Num
    Patient_ID_Num = g_ID_NUM
    #print(Patient_ID_Num)
    #print(ID_list)
    return g_ID_NUM
    

#Initializing mixer
mixer.init()

def play_welcome():
    mixer.music.load("welcome_screen.mp3")
    mixer.music.play()

def play_id():
    mixer.music.load("id_screen.mp3")
    mixer.music.play()

def play_PageTwo():
    mixer.music.load("second_screen.mp3")
    mixer.music.play()

def play_video():
    mixer.music.load("video_call.mp3")
    mixer.music.play()

def play_tempreature():
    mixer.music.load("temp_audio.mp3")
    mixer.music.play()

def play_oximeter():
    mixer.music.load("oximeter_audio.mp3")
    mixer.music.play()

def play_covid():
    mixer.music.load("covid19_audio.mp3")
    mixer.music.play()

def play_pneumonia():
    mixer.music.load("pneumonia_audio.mp3")
    mixer.music.play()

def play_videocall():
    mixer.music.load("video_audio.mp3")
    mixer.music.play()

# Creating th main class for the app
class SentinelApp(Tk):
    def __init__ (self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title("Sentinels Medical User Interface")
        self.geometry("800x480+0+0")                #720 * 300
        #self.attributes('-fullscreen', True)

        # Create a container to control the frames  
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # To switch between frames
        self.frames={}
        for F in (WelcomePage , ID , PageTwo, Pneumonia, Covid_19, VitalMeasures, HeartRate):
            page_name=F.__name__
            frame=F(parent=container , controller=self)   
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(background="#00A7E6")
        self.show_frame("WelcomePage")

    def show_frame(self,page_name):
        frame=self.frames[page_name]
        frame.tkraise()
    


class WelcomePage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        fr1 = Frame(self,width=110,height=480,bg="#148F77")
        fr1.place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77")
        fr2.place(x=690,y=0)
        self.controller = controller
        button1=Button(self,text="Go To The ID Page",command=lambda: [controller.show_frame("ID"), play_id()],font=("Comic Sans",25,"bold"),foreground="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,compound=RIGHT,height=1,width=15)
        button1.place(x=220,y=300)
        label=Label(self,text="Welcome To Sentinels\n  Medical Robot",font=("Comic Sans",30,"bold"),foreground='white',background="#081448")
        label.place(x=165,y=100)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()
        play_welcome()
        
        #Robotic photo design
        global img_robotic
        image_robotic = Image.open("robotic.png")
        resize_image_robotic = image_robotic.resize((100, 130))
        img_robotic = ImageTk.PhotoImage(resize_image_robotic)
        my_label_1=Button(image=img_robotic, relief=SUNKEN, borderwidth=0, highlightthickness=0,bg="#148F77", activebackground="#148F77")
        my_label_1.place(x=698,y=320)


class ID (Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        global Patient_ID_Num  
        fr1 = Frame(self,width=110,height=480,bg="#148F77")
        fr1.place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77")
        fr2.place(x=690,y=0)
        self.controller = controller
        self.random=StringVar()
        def ID_NUM_TIME():
            global Patient_ID_Num
            label_num.config(text = Patient_ID_Num)
            label_num.after(1,ID_NUM_TIME)
        label_ID_num=Label(self,text="Your ID number is :",font=("Comic Sans",32,"bold"),foreground='white',background="#081448")
        label_ID_num.place(x=180,y=100)
        label_num=Label(self,text= changeIdNumber(),font=("Comic Sans",32,"bold"),foreground='white',background="#081448")
        label_num.place(x=385,y=180)
        ID_NUM_TIME()
        button_next=Button(self,text="Next",font=("Comic Sans",26,"bold"),height=1,width=10,command=lambda: [controller.show_frame("PageTwo"),play_PageTwo()],foreground="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,compound=RIGHT)
        button_next.place(x=285 ,y=300)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()
        ##back button
        global img_back_id
        back_img_id=Image.open('back.png')
        resize_back_img_id = back_img_id.resize((40,40))
        img_back_id = ImageTk.PhotoImage(resize_back_img_id)
        back_button_id=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back_id,relief=GROOVE ,state="active", command=lambda: controller.show_frame("WelcomePage"))
        back_button_id.place(x=26,y=210)


class PageTwo (Frame):
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        global g_Temperature_Test
        global g_HeartRate_Test
        global g_OxygenPrecentage_Test
        global g_Covid19_Test
        global g_Pneumonia_Test
        global Patient_ID_Num

        fr1 = Frame(self,width=110,height=480,bg="#148F77")
        fr1.place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77")
        fr2.place(x=690,y=0)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()

        label = Label(self,text="Hello, How can i help you?",font=("Comic Sans",18,"bold"),fg='white',bg="#081448")
        label.place(x=220,y=55)

        def callback():
            gmailUser = '7madanges99@gmail.com'
            gmailPassword = 'ua07ua07'
            recipient = 'talalmahmoud110@gmail.com'

            message = f"""A Patient with ID {Patient_ID_Num} tries to call you. Would you mind entering a video call with him, doctor.\nMeasurements taken by the patient:\n\t=> Temperature: {g_Temperature_Test} C\n\t=> Heart Rate: {g_HeartRate_Test} bpm\n\t=> Precentage of oxygen: {g_OxygenPrecentage_Test} %\n\t=> Covid-19 Test = {g_Covid19_Test}\n\t=> Pneumonia Test = {g_Pneumonia_Test}\n"""

            msg = MIMEMultipart()
            msg['From'] = f'"Sentinel Robot" <{gmailUser}>'
            msg['To'] = recipient
            msg['Subject'] = "Patient wants to make video call with Doctor"
            msg.attach(MIMEText(message))

            try:
                mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(gmailUser, gmailPassword)
                mailServer.sendmail(gmailUser, recipient, msg.as_string())
                mailServer.close()
                print ('Email sent!')
            except:
                print ('Something went wrong...')
            webbrowser.open_new(r"https://chat.1410inc.xyz/?room=room1_tld08fae099")


        #Covid-19
        #Covid-19 image for Covid-19 button
        global img_covid
        covid_img = Image.open("covid19.png")
        resize_covid_img = covid_img.resize((50, 50))
        img_covid = ImageTk.PhotoImage(resize_covid_img)
        #Covid-19 button
        Covid =Button(self,text="Covid-19  ",font=("Comic Sans",20,"bold"),height=65,width=200,fg="black",bg="#FCA725",activebackground="#FCA725",justify=CENTER,relief=GROOVE,image=img_covid,compound=RIGHT, command=lambda: [controller.show_frame("Covid_19"), play_covid()])
        Covid.place(x=158,y=115)
        
        #Vital measures
        #Vital measures image for Vital measures button
        global img_vital
        vital_img = Image.open("vital.png")
        resize_vital_img = vital_img.resize((50, 50))
        img_vital = ImageTk.PhotoImage(resize_vital_img)
        #Vital measures button
        Vital_measures = Button(self,text="Vital Measures ",font=("Comic Sans",13,"bold"),height=65,width=200,fg="black",bg="#FF00A6",activebackground="#FF00A6",justify=CENTER,relief=GROOVE,image=img_vital,compound=RIGHT,command=lambda: [controller.show_frame("VitalMeasures"),play_tempreature()])
        Vital_measures.place(x=410,y=115)

        #Pneumonia
        #pneumonia image for pneumonia button
        global img_pneumonia
        pneumonia_img = Image.open("Pneumonia.png")
        resize_pneumonia_img = pneumonia_img.resize((45, 55))
        img_pneumonia = ImageTk.PhotoImage(resize_pneumonia_img)
        #Pneumonia button
        Pneumonia = Button(self,text="Pneumonia ",font=("Comic Sans",19,"bold"),height=65,width=200,fg="black",bg="#89A725",activebackground="#89A725",justify=CENTER,relief=GROOVE,image=img_pneumonia,compound=RIGHT,command=lambda: [controller.show_frame("Pneumonia"),play_pneumonia()])
        Pneumonia.place(x=158,y=225)

        #Video Call
        #video call image for video call button
        global img_video
        video_img = Image.open("videocall.png")
        resize_video_img = video_img.resize((50, 35))
        img_video = ImageTk.PhotoImage(resize_video_img)
        #video call button
        Video_call = Button(self,text="Video Call ",font=("Comic Sans",20,"bold"),height=65,width=200,fg="black",bg="gray",activebackground="gray",justify=CENTER,relief=GROOVE,image=img_video,compound=RIGHT,command=lambda: [callback(), play_videocall()])
        Video_call.place(x=410,y=225)

        #logout Button
        global img_logout
        logout_img = Image.open("logout.png")
        resize_logout_img = logout_img.resize((60, 60))
        img_logout = ImageTk.PhotoImage(resize_logout_img)

        Log_out_Button = Button(self,text=" LogOut",font=("Comic Sans",18,"bold"),image=img_logout,height=60,width=185,fg="black",bg="#0E816A",activebackground="#0E816A",justify=CENTER,relief=GROOVE,compound=LEFT,command=lambda: [controller.show_frame("WelcomePage"),changeIdNumber()])
        Log_out_Button.place(x=300,y=330)

        ##back button
        global img_back
        back_img=Image.open('back.png')
        resize_back_img = back_img.resize((40,40))
        img_back = ImageTk.PhotoImage(resize_back_img)
        back_button_id=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back,relief=GROOVE ,state="active", command=lambda: controller.show_frame("ID"))
        back_button_id.place(x=26,y=210)

class Pneumonia(Frame):
    global cap
    cap = None
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        #frame of the camera
        label_1 =Label(self,bg="#00A7E6")
        label_1.place(x=245,y=105) #x = 303  #y = 132

        fr1 = Frame(self,width=110,height=480,bg="#148F77")
        fr1.place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77")
        fr2.place(x=690,y=0)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()

        
        #title_covid = Label(self, text='Capture your Ct-scan here', font=("Comic Sans",16,"bold"),fg='white',bg="#081448").place(x=230,y=10)
        
        #Capture image button
        global imo_cam_pneumonia
        photo_pneumonia = Image.open("capture-icon-25.jpg")
        photo_img_pneumonia = photo_pneumonia.resize((50, 45))
        imo_cam_pneumonia = ImageTk.PhotoImage(photo_img_pneumonia)

        title_Pneumonia = Label(self, text='Capture your Ct-scan here\nPneumonia Test', font=("Comic Sans",18,"bold"),fg='white',bg="#081448")
        title_Pneumonia.place(x=250,y=30)  
        
        global openCamera_pneumonia
        open_image_pneumonia=Image.open('open_camera.png')
        open_image_img_3_pneumonia = open_image_pneumonia.resize((40,40))
        openCamera_pneumonia = ImageTk.PhotoImage(open_image_img_3_pneumonia)
        
        #open camera button
        btn_openCamera_pneumonia = Button(self,text="Open Camera",font=("Comic Sans",10,"bold"),height=60,width=90,image=openCamera_pneumonia,command=lambda:threading.Thread(target = start).start(),compound=TOP)
        btn_openCamera_pneumonia.place(x=125,y=185)

        #close camera button
        #btn_CloseCamera = Button(self,text="Close Camera",command=lambda:end()).place(x=300,y=0)
        
        #capture image
        capture_btn_pneumonia = Button(self,text='Capture',font=("Comic Sans",12,"bold"),height=60,width=90,fg="black",bg="#BCBCBC",activebackground="#BCBCBC",image=imo_cam_pneumonia,command=lambda:threading.Thread(target = cam_pneumonia).start(),compound=TOP)
        capture_btn_pneumonia.place(x=560,y=185) #hieght = 60 width  = 90

        #Checking the model
        pneumonia_btn_check = Button(self,text="Pneumonia Check",font=("Comic Sans",18,"bold"),height=1,width=15,fg="black",bg="#934ACF",activebackground="#934ACF",command=lambda: threading.Thread(target = PressPneumoniaCheckButton).start())
        pneumonia_btn_check.place(x=265,y=387)

        ##back button
        global img_back_2
        back_img_2=Image.open('back.png')
        resize_back_img_2 = back_img_2.resize((40,40))
        img_back_2 = ImageTk.PhotoImage(resize_back_img_2)
        back_button_pneumonia=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back_2,relief=GROOVE ,state="active", command=lambda:[controller.show_frame("PageTwo"), play_PageTwo(), cap.release() if(cap != None) else Pass])
        back_button_pneumonia.place(x=26,y=210)
        
        def visualizer():
            global cap
            if cap is not None:
                ret , frame = cap.read()
                if ret == True:
                    frame = imutils.resize(frame,width=310) # width 200
                    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

                    im = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=im)

                    label_1.configure (image=img)
                    label_1.image = img
                    label_1.after(10,visualizer)
                else:
                    label_1.image = ""
                    cap.release()
        def start():
            global cap
            cap = cv2.VideoCapture(0)
            visualizer()
        def cam_pneumonia():
            global cap
            #cap = cv2.VideoCapture(0)
            ret,image = cap.read()
            cv2.imwrite("Pneumonia_image.png",image)
            cap.release()
            cv2.destroyAllWindows()
        def PressPneumoniaCheckButton():
            global g_Pneumonia_Test
            model=load_model('PNEUMONIA_xray.h5')
            img=image.load_img('Pneumonia_image.png',target_size=(224,224))
            x=image.img_to_array(img)
            x=np.expand_dims(x, axis=0)
            img_data=preprocess_input(x)
            classes=model.predict(img_data)
            result=int(classes[0][0])
            if result==0:
                g_Pneumonia_Test = "Person is Affected By PNEUMONIA"
                label_affected_Pneumonia = Label(self,text="Person is Affected By PNEUMONIA",font=("Comic Sans",13,"bold"),bg="#00A7E6")
                label_affected_Pneumonia.place(x=256,y=350)
            else:
                g_Pneumonia_Test = "Result is Normal"
                label_not_affected_Pneumonia = Label(self,text="Result is Normal",font=("Comic Sans",13,"bold"),bg="#00A7E6")
                label_not_affected_Pneumonia.place(x=329,y=350)




class Covid_19(Frame):
    global cap
    cap = None
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        #frame of the camera
        label_1 =Label(self,bg="#00A7E6")
        label_1.place(x=245,y=105) #x = 303  #y = 132

        fr1 = Frame(self,width=110,height=480,bg="#148F77")
        fr1.place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77")
        fr2.place(x=690,y=0)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()


        #title_covid = Label(self, text='Capture your Ct-scan here', font=("Comic Sans",16,"bold"),fg='white',bg="#081448").place(x=230,y=10)
        
        #Capture image button
        global imo_cam_covid
        photo_covid = Image.open("capture-icon-25.jpg")
        photo_img_covid = photo_covid.resize((50, 45))
        imo_cam_covid= ImageTk.PhotoImage(photo_img_covid)

        title_covid = Label(self, text='Capture your Ct-scan here\nCorona Virus Test', font=("Comic Sans",18,"bold"),fg='white',bg="#081448")
        title_covid.place(x=250,y=30)  
        
        global openCamera
        open_image=Image.open('open_camera.png')
        open_image_img_3 = open_image.resize((40,40))
        openCamera = ImageTk.PhotoImage(open_image_img_3)
        
        #open camera button
        btn_openCamera_covid = Button(self,text="Open Camera",font=("Comic Sans",10,"bold"),height=60,width=90,image=openCamera,command=lambda:threading.Thread(target = start).start(),compound=TOP)
        btn_openCamera_covid.place(x=125,y=185)

        #close camera button
        #btn_CloseCamera = Button(self,text="Close Camera",command=lambda:end()).place(x=300,y=0)
        
        #capture button
        capture_btn_covid = Button(self,text='Capture',font=("Comic Sans",12,"bold"),height=60,width=90,fg="black",bg="#BCBCBC",activebackground="#BCBCBC",image=imo_cam_covid,command=lambda:threading.Thread(target = cam_covid19).start(),compound=TOP)
        capture_btn_covid.place(x=560,y=185)

        #Checking the model
        covid_btn_check = Button(self,text="Covid-19 Check",font=("Comic Sans",18,"bold"),height=1,width=15,fg="black",bg="#934ACF",activebackground="#934ACF",command=lambda:threading.Thread(target = PressCovidCheckButton).start())
        covid_btn_check.place(x=265,y=387)

        ##back button
        global img_back_4
        back_img_4=Image.open('back.png')
        resize_back_img_4 = back_img_4.resize((40,40))
        img_back_4 = ImageTk.PhotoImage(resize_back_img_4)
        back_button_covid=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back_4,relief=GROOVE ,state="active", command=lambda: [controller.show_frame("PageTwo"), play_PageTwo(), cap.release() if(cap != None) else Pass])
        back_button_covid.place(x=26,y=210)
        
        def visualizer():
            global cap
            if cap is not None:
                ret , frame = cap.read()
                if ret == True:
                    frame = imutils.resize(frame,width=310)
                    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

                    im = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=im)

                    label_1.configure (image=img)
                    label_1.image = img
                    label_1.after(10,visualizer)
                else:
                    label_1.image = ""
                    cap.release()
        def start():
            global cap
            cap = cv2.VideoCapture(0)
            visualizer()
        def cam_covid19():
            global cap
            #cap = cv2.VideoCapture(0)
            ret,image = cap.read()
            cv2.imwrite("Covid19_image.png",image)
            cap.release()
            cv2.destroyAllWindows()
        def PressCovidCheckButton():
            global g_Covid19_Test
            model=load_model('cnn_model.h5')
            img=image.load_img('Covid19_image.png',target_size=(128,128))
            x=image.img_to_array(img)
            x=np.expand_dims(x, axis=0)
            img_data=preprocess_input(x)
            classes=model.predict(img_data)
            result=int(classes[0][0])
            if result==0:
                g_Covid19_Test = "Person is Affected By Covid 19"
                label_affected_covid = Label(self,text="Person is Affected By Covid 19",font=("Comic Sans",13,"bold"),bg="#00A7E6")
                label_affected_covid.place(x=276,y=350)
            else:
                g_Covid19_Test = "Result is Normal"
                label_not_affected_covid = Label(self,text="Result is Normal",font=("Comic Sans",13,"bold"),bg="#00A7E6")
                label_not_affected_covid.place(x=329,y=350)


        
class VitalMeasures(Frame):
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        global temp
        fr1 = Frame(self,width=110,height=480,bg="#148F77").place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77").place(x=690,y=0)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()

        

        label_temp = Label(self,text="Temperature of the body",font=("Comic Sans",17,"bold"),fg='white',bg="#081448")
        label_temp.place(x=255,y=10)
        
        #label of the tempreture
        Label_Temp = Label(self,text="The Tempreture of your body:",font=("Comic Sans",14,"bold"),bg="#00A7E6")
        Label_Temp.place(x=125,y=70)

        #Button of the temperature
        button_temp = Button(self,text='Press to see your Temperature',font=("Comic Sans",12,"bold"),height=2,width=25,fg="black",bg="#934ACF",activebackground="#934ACF", command=lambda: [threading.Thread(target=Temp_sensor).start()])
        button_temp.place(x=270,y=150)
        def update_temp():
            global temp
            display_temp_label.config(text = f"Temperature = {temp} C")
            display_temp_label.after(30,update_temp)
        display_temp_label = Label(self,text= f"Temperature = {temp} C",font=("Comic Sans",14,"bold"),bg="#00A7E6")
        display_temp_label.place(x= 310, y=250)
        update_temp()
        #Button of the next page (Spo2 and heart rate page)
        button_next = Button(self,text='Press here for Heart rate and\noxygen percentage in blood',font=("Comic Sans",12,"bold"),height=2,width=25,fg="black",bg="#F33421",activebackground="#F33421",command=lambda:[controller.show_frame("HeartRate"),play_oximeter()])
        button_next.place(x=270,y=365)


        ##back button
        global img_back_vitual_page
        back_img_vital=Image.open('back.png')
        resize_back_img_vital = back_img_vital.resize((40,40))
        img_back_vitual_page = ImageTk.PhotoImage(resize_back_img_vital)
        back_button=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back_vitual_page,relief=GROOVE ,state="active", command=lambda: [controller.show_frame("PageTwo"),play_PageTwo()]).place(x=26,y=210)
        def Temp_sensor():
            global temp
            bus = SMBus(1)
            sensor = MLX90614(bus, address=0x5A)
            error = 3.5
            avg = 20
            time.sleep(6)
            while 1:
                l=[]
                for i in range (avg):
                    celcius = sensor.get_object_1();
                    time.sleep(0.01)
                    l.append(celcius)
                temp = (sum(l)/len(l))+error
                print(temp)
                if temp <= 38 and temp >= 36: 
                    print("Body Temperature : ",(round(temp,2)))
                    break

        


class HeartRate(Frame):
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        global bpm
        global spo2
        fr1 = Frame(self,width=110,height=480,bg="#148F77").place(x=0,y=0)
        fr2 = Frame(self,width=110,height=480,bg="#148F77").place(x=690,y=0)
        time_frame = Frame(self, width=800, height=25, bg="#080A1E")
        time_frame.place(x=0,y=455)
        def my_time():
            time_string = strftime("%H:%M:%S %p, %A, %x")
            l1.config(text=time_string)
            l1.after(1000,my_time)

        l1 = Label(time_frame,font=("ds-digital",9,"bold"),fg="white",bg="#080A1E")
        l1.place(x=300,y=1)
        my_time()
        

        label_heart = Label(self,text="Heart rate and Oxygen precentage in blood",font=("Comic Sans",16,"bold"),fg='white',bg="#081448")
        label_heart.place(x=190,y=10)

        #Button of the spo2 and heart rate
        #button_spo2_heart = Button(self,text='Press to see your Heart rate and\nOxygen Precentage in the blood',font=("Comic Sans",12,"bold"),height=2,width=25,fg="black",bg="#934ACF",activebackground="#934ACF").place(x=230,y=70)

        #label of the Heart Rate
        Label_Heart_rate  = Label(self,text="Heart Rate and Oxygen Precentage in your Blood:",font=("Comic Sans",13,"bold"),bg="#00A7E6")
        Label_Heart_rate.place(x=120,y=50)
        #button for measuring heart rate and spo2
        heart_rate_measuring_button = Button(self, text='Measure your Heart rate &\nOxygen perecentage',font=("Comic Sans",14,"bold"),height=2,width=22,fg="black",bg="#F33421",activebackground="#F33421",command=lambda: [threading.Thread(target=oximeter_sensor).start()])
        heart_rate_measuring_button.place(x=255, y=150)
        def update_oximeter():
            global bpm
            PulseLb.config(text = f"Heart Pulse Rate: {bpm} bpm" )
            PulseLb.after(30,update_oximeter)
        def update_spo2():
            global spo2
            SPO2Lb.config(text = f"Oxygen Pracentage in the blood: {spo2} %")
            SPO2Lb.after(30,update_spo2)
        PulseLb = Label(self,text=f"Heart Pulse Rate: {bpm} bpm",font=("Comic Sans",13,"bold"),bg="#00A7E6")
        PulseLb.place(x=210,y=250)
        SPO2Lb = Label(self,text=f"Oxygen Pracentage in the blood: {spo2} %", font=("Comic Sans",13,"bold"),bg="#00A7E6")
        SPO2Lb.place(x=210,y=280)
        update_oximeter()
        update_spo2()
        #main menu buttun
        button_main_menu = Button(self, text='Main Menu',font=("Comic Sans",14,"bold"),height=2,width=15,fg="black",bg="#F33421",activebackground="#F33421",command=lambda: [controller.show_frame("PageTwo"), play_PageTwo()]).place(x=310, y=365)
        
        ##back button
        global img_back_heart_page
        back_img_heart=Image.open('back.png')
        resize_back_img_heart = back_img_heart.resize((40,40))
        img_back_heart_page = ImageTk.PhotoImage(resize_back_img_heart)
        back_button_heart=Button(self,height=40,width=40,bg="white",activebackground="white",image=img_back_heart_page,relief=GROOVE ,state="active", command=lambda: [controller.show_frame("VitalMeasures"),play_tempreature()]).place(x=26,y=210)
        def moving_average(numbers):
            window_size = 4
            i = 0
            # moving_averages = []
            while i < len(numbers) - window_size + 1:
                this_window = numbers[i : i + window_size]
                window_average = sum(this_window) / window_size
                # moving_averages.append(window_average)
                i += 1
            try:
                return int((window_average/100))
            except:
                pass

        # If HeartRate is <10 function assumes Fingure Not present and will not show incorrect data
        # Also If SpO2 readings goes beyond 100. It will be shown as 100.
        def display_filter(moving_average_bpm,moving_average_sp02):
            try:
                if(moving_average_bpm<10):
                    moving_average_bpm ='NA'
                    moving_average_sp02 = 'NA'
                else:
                    if(moving_average_sp02>100):
                        moving_average_sp02 = 100
                return moving_average_bpm, moving_average_sp02
            except:
                return moving_average_bpm, moving_average_sp02
        def oximeter_sensor():
            global bpm
            global spo2
            mx30 = max30100.MAX30100()
            mx30.enable_spo2()
            while 1:
                mx30.read_sensor()
                hb = int(mx30.ir / 100)
                spo2 = int(mx30.red / 100)
                if mx30.ir != mx30.buffer_ir :
                    moving_average_bpm = (moving_average(mx30.buffer_ir))
                    # print(" MAX30.ir " + str(mx30.ir)) 
                    # print(" mx30.buffer_ir " + str(mx30.buffer_ir)) 
                    # print("|||||| Avg Pulse :" + str(moving_average_bpm)) 
                    # print("|||||| Pulse     :" + str(hb));
                if mx30.red != mx30.buffer_red:
                    moving_average_sp02 = (moving_average(mx30.buffer_red))
                    # print(" MAX30.red " + str(mx30.red)) 
                    # print(" mx30.buffer_red " + str(mx30.buffer_red)) 
                    # print("###### Avg SpO2  :" + str(moving_average_sp02)) 
                    # print(" ##### SPO2     :" + str(spo2));
                bpm,spo2 = display_filter(moving_average_bpm,moving_average_sp02)
                #if ( ((bpm >=80) and (bpm <=131)) and ((spo2 >=90) and (spo2<=100)) ):
                    #break
                print(" *******************")
                print(" bpm : "+ str(bpm))
                print(" SpO2: "+ str(spo2))
                print(" -------------------")
                time.sleep(1)        

root=SentinelApp()
root.mainloop()