# Dockerized-Web-App-Deployment-on-IBM-CLoud
This is a Cloud Computing project that I made with the help of IBM Cloud services .


# 📝 Flask Blog App

A simple web application built using **Flask** that allows users to create and view blog posts. Data is stored using **SQLite**, and the app is containerized using **Docker** for easy deployment.

## ⚙️ Features

- Create new blog posts  
- View all blog posts  
- Simple and clean UI using HTML/CSS  
- SQLite for lightweight data storage  
- Dockerized for easy container-based deployment  

## 📁 Project Structure



flask-blog-app/
├── templates/           # HTML templates
├── static/              # CSS files
├── app.py               # Main Flask application
├── blog.db              # SQLite database file
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project info



## 🚀 Getting Started

### Clone the Repository


git clone https://github.com/Sangini-spec/Dockerized-Web-App-Deployment-on-IBM-CLoud.git
cd Dockerized-Web-App-Deployment-on-IBM-CLoud


### Run Without Docker (Optional)


pip install -r requirements.txt
python app.py


App will be live at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## 🐳 Docker Instructions

### Build the Docker Image


docker build -t flask-blog-app .


### Run the Container


docker run -d -p 5000:5000 flask-blog-app


Visit the app at: [http://localhost:8080](http://localhost:8080)

## 🌐 Live App

Visit the deployed app here:
**[https://GlobalBlog.com](https://dockerized-web-app-deployment-on-ibm.onrender.com)**




