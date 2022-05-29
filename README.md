![image](https://user-images.githubusercontent.com/77823971/170848482-6bc55e70-8c8a-4a0d-9c7d-88c6d0cc54cd.png)
# Face-Recognition-Attendance-Portal 💻
Recognition of people's faces Building an Attendance Portal entails creating an Attendance System that employs facial recognition technology to track attendance. Students/employees can track their attendance by using a camera to recognise their faces. It can be used to track attendance in numerous offices, corporate sectors, schools, and enterprises. The goal of this project is to automate the traditional attendance method, which involves manually marking attendance.
# Description
## Scope of the project
In contemporary society, facial recognition technology is becoming more prevalent. It's useful in a variety of fields, including law enforcement, medicine, and industry. It can recognize a person's face in a crowd, separate the face from the rest of the scene, and compare it to a database of previously saved photos. This software must be able to distinguish between a basic face and the rest of the background in order to function. The capacity to recognize a face and then quantify the numerous aspects of the face is the foundation of facial recognition software.

This project may be the foundation for other projects based on facial recognition. This project also involves Database management and Web Development with a UI.


## How application performs?
There are 2 type of users exist:
1. User (Employee/Student)
2. Admin

### Functionalities performed by Admin:
* Log in themselves on the portal.

![image](https://user-images.githubusercontent.com/77823971/170851418-c52e7869-e905-477b-bbe9-5db26c202d99.png)
![image](https://user-images.githubusercontent.com/77823971/170851679-f04ca1bd-d121-4faf-b2b3-8d26057ce085.png)

* Add new students to the database with their image

![image](https://user-images.githubusercontent.com/77823971/170851597-ddeac928-2e58-46ea-8f72-f1448cd836be.png)


* View the attendance of students

![image](https://user-images.githubusercontent.com/77823971/170851721-ed294bec-c294-478a-b3d2-f9ff782ef50a.png)
![image](https://user-images.githubusercontent.com/77823971/170854044-6faf5b5a-575a-4591-a4b3-b3ea75ed6f9e.png)



### Functionalities performed by User:
* Mark the attendance

![image](https://user-images.githubusercontent.com/77823971/170851896-eab28794-9f47-4f55-bf41-f347b5fd99a8.png)
![image](https://user-images.githubusercontent.com/77823971/170853638-8d242984-4362-4e2f-b5b8-99ee36f7dcba.png)

* View Attendance

![image](https://user-images.githubusercontent.com/77823971/170853758-beb9e59e-11af-45fa-914f-e2a493a0a23e.png)







## Technology and Tools
* Django
* Dlib
* Open CV 
* Open Source Face Recognition Library
* Javascript
* Bootstrap
* SQLite Database

## AGILE Methodology
### What is Agile?
Agile software development refers to software development methodologies centered around the idea of iterative development, where requirements and solutions evolve through collaboration between self-organizing cross-functional teams. 

### How I applied it into my project?
I divided the software development process in 3 phases according to agile methodology. 
* Phase-1 (4 May 2022 - 17 May 2022): (Learning, Planning, Research and Design)                                                                                         
I looked into many Face Recognition Libraries and APIs.
Designed the wireframe, which included all capabilities, as well as the user interface.
Choose the technologies and learn about them via YouTube tutorials and documentation.
* Phase-2 (18 May 2022 - 23 May 2022): (Software Development and Debugging)  
For the first time, I created a web application using Django and the Open CV Face Recognition Library.
I got the bugs, which I fixed with the help of StackOverflow and my mentor.                                                                                           
* Phase-3 (24 May 2022 - 27 May 2022): (Addition of more Features, Debugging & Documentation)  
Added a feature that Admin should be able to register a new student on the site.
Add a functionality that allows users and administrators to view attendance.
I finished the documentation section.




## Features to Implement in future
* Users' attendance should be distributed in such a way that each user can only view his or her own attendance. He or she will be unable to view the attendance of others.
* Show the attendance to user/admin in form of Graphs and Charts, through which they can visualize their reports.
* Add a feature for admins to download attendance reports of every employee/student.

# How to run?
* Fork the repository
* Clone the repository using the command ```git clone https://github.com/shikha2961/Face-Recognition-Attendance-Portal.git```
* Make a separate python virtual environment or use the default one already installed on your machine.
* Download the file requirements.txt
* Run pip install -r requirements.txt inside /Face-Recognition-Attendance-Portal/ directory
* Create the superuser by following command: ```python manage.py createsuperuser```
* Run python manage.py runserver inside /Face-Recognition-Attendance-Portal/ directory to run the project
* yayyy!! Set up 🤝

# Resources Used:
* Open CV Face Recognition Library: https://pypi.org/project/face-recognition/
* Django Documentation: https://docs.djangoproject.com/en/4.0/
* Django tutorial CodeWithHarry: https://www.youtube.com/watch?v=JxzZxdht-XY&t=4698s
* Python tutorial CodeWithHarry: https://www.youtube.com/watch?v=gfDE2a7MKjA

