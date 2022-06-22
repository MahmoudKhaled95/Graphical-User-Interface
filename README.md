# Graphical-User-Interface
GUI for medical robot
# Graphical user interface (GUI Tkinter) inside the medical robot
The graphic user interface of the medical robot is characterized by simplicity and is user-friendly. GUI enables the user or patient to deal with our robot easily to achieve the simplicity and no boredom of the patient. The medical robot is specialized in medical diagnosis, and vital measures and makes it easy for the patients to communicate with doctors over long distances with a video call referencing feature. So, the Graphical user interface (GUI Tkinter) includes these features combined with each other so that the user can easily use our services with no effort. In the case of medical diagnosis, the Graphical user interface (GUI Tkinter) includes both the diagnosis of coronavirus and pneumonia through CT scans using machine learning models. The Graphical user interface (GUI Tkinter) also includes the ability to measure vital signs like body temperature, heart rate, and oxygen percentage. The Graphical user interface (GUI Tkinter) also introduces a video call conferencing feature which improves the communication between the patients and doctors over long distances.
The Graphical user interface consists of some major screens like the following:
•	Welcome screen.
•	ID screen.
•	Main menu screen which includes:
  o	Coronavirus test button
  o	Pneumonia test button
  o	Video call conferencing feature button
  o	Vital measurement button which includes:
      	Measuring body temperature screen.
      	Measuring heart rate and oxygen percentage screen.
  o	Logout button
Each of the above screens contains the date and time. Our screens in the GUI are simple to allow the patient to easily interact with its features.

Each of the above screens contains the date and time. Our screens in the GUI are simple to allow the patient to easily interact with its features.
GUI will be displayed on LCD screen; this screen is a touch screen that allow the user (patient) to deal with our GUI easily without any needs for external peripherals like keyboard or mouse. For more information about this touch screen see Appendix Q.
# Welcome screen
The welcome screen is the first screen in the Graphical user interface (GUI Tkinter). It welcomes the user or the patient at the beginning and it includes a button which directs the user to the ID screen.
![image](https://user-images.githubusercontent.com/100867843/175025754-876a6d48-074e-4fe6-8e80-974730e745d7.png)

# ID screen 
The ID screen is the next screen after the welcome screen. It is where the user is assigned a special ID that the user should memorize so that all his medical data will be related to that ID. The ID screen includes a back button if the user wants to return to the welcome page as well as a button top go to the next screen which is the main menu. The ID is specific for each patient, once new patient is interacting with the GUI a new ID is given to him. This allows us to easily store each patient's data so that there is no interference with other patients' data.
![image](https://user-images.githubusercontent.com/100867843/175025819-5fed3d4c-7df7-407b-9f89-804accff4061.png)

# Main menu screen
In the main menu screen, all our services and features are included which are:
•	Coronavirus test.
•	Pneumonia test.
•	Vital signs measurement.
•	Video call conferencing feature.
The main menu includes buttons for all these features as well as a back button to return to the ID screen in case a patient forgets to take his ID number. Each button will take you to the desired measure that you want. Also, the main menu screen includes a logout button to allow the patient to log out in order to give the new patient a new ID to achieve not overwrite the measurement of the new patient on the old patient so a new ID must be given.
 ![image](https://user-images.githubusercontent.com/100867843/175025842-3b236c00-e9a3-49a7-872b-f8fc646b5d1f.png)

# Coronavirus test 
In case the user selects the coronavirus test in the main menu screen through the covid-19 button he will be automatically directed to screen through which he can test for coronavirus and take a CT scan via the camera (see Appendix R for more details about the Logitech camera).The user will need to open the camera from the open camera button on the left so that he can see the image that will be taken. Once the user puts the image in the right place and in the right way, he will press the capture button on the right to finally take the final image. After the image was taken the user will press the covid-19 check button and with the ability of the machine learning model that will analyze the image and knows if the person is infected with the coronavirus or not the result will be displayed to the user.
 ![image](https://user-images.githubusercontent.com/100867843/175025864-dadcc70b-161e-4ef1-b710-e18a36b01f77.png)

# Pneumonia test
In case the user selects the pneumonia test in the main menu screen through the pneumonia button he will be automatically directed to screen through which he can test for pneumonia and take a CT scan via the camera. The user will need to open the camera from the open camera button on the left so that he can see the image that will be taken. Once the user puts the image in the right place and in the right way, he will press the capture button on the right to finally take the final image. After the image was taken the user will press pneumonia check button and with the ability of the machine learning model that will analyze the image and knows if the person is infected with the pneumonia or not the result will be displayed to the user.
 ![image](https://user-images.githubusercontent.com/100867843/175025901-f07962db-73f3-4d1b-a0f4-d685dd2aeed8.png)

# Vital signs measuring 
Vital signs are useful in detecting or monitoring medical problems. Vital signs can be measured in a medical environment, at home, at a medical emergency site, or elsewhere. 
Vital sign measuring includes these following features:
  •	Measuring body temperature
  •	Measuring heart rate and oxygen percentage
=>Measuring body temperature screen
One of the most important vital signs is body temperature, so if vital measures button is selected from the main menu the user will be directed a new screen to measure his temperature first and after measuring it, he will go to another screen so that he can measure his heart rate and oxygen percentage.
In the temperature screen the patient will be asked to put his finger above the temperature sensor and the robot will measure it once the patient click on “Press to see your Temperature” button and display it on the screen.
 ![image](https://user-images.githubusercontent.com/100867843/175025942-59c2af91-3646-4c74-aace-6b931323ba32.png)

=>Measuring heart rate and oxygen percentage screen 
Once the user finishes measuring his body temperature, he will press the heart rate and oxygen percentage button and he will be automatically directed to the screen through which he can measure both heart rate and oxygen percentage.
The user will be instructed so that he will put his finger above the heart rate and oxygen percentage sensor and press on “Measure your Heart rate & Oxygen percentage” button and wait for a given amount of time after that the result will be displayed to the user so that he can check it. after finishing the user can return to the main menu again through the main menu button so that he can run more tests if he wants.
 ![image](https://user-images.githubusercontent.com/100867843/175026131-2c1f20e0-47b9-4cbe-b5f0-c7a89f01c618.png)

# Video call referencing feature 
Our medical robot introduces video conferencing feature so that the patient can effectively communicate with doctors and ask for their opinions and consultation. The patient can use our video conferencing feature from the main menu and once it was selected the patient will be directed to a room where he can communicate with patient. 
While the patient selects the video call video conferencing feature the doctor will be notified by email address that a patient wants to talk with him in a video call, also the doctor can see all the measures that the patient made in order to inspect the patient’s health. The doctor can join the patient through our mobile application and talk with the patient.
![image](https://user-images.githubusercontent.com/100867843/175026224-2ec317eb-544e-47c2-a691-0cb922cfffbf.png) 
In case you want to look at the code of the GUI see Appendix S. The code of the GUI includes the libraries of the sensors used in the robot to access the measured value from the sensor and display it in the GUI (See the Appendix T and U in case you want to look at their codes).
