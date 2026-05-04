# uni-bazar-smart-marketplace
Uni Bazar — Smart Campus Marketplace
Project Overview
Uni Bazar is a full-stack smart campus marketplace web application developed for students to buy, sell, and communicate within their campus community. The platform is specially designed for hostelers and day scholars to exchange second-hand campus items efficiently through a secure and user-friendly system.
The application allows users to create accounts, manage personal profiles, upload product listings, save wishlist items, and interact with buyers or sellers using a real-time messaging system powered by Django Channels and WebSocket technology. The project focuses on providing a responsive, interactive, and modern marketplace experience while implementing advanced full-stack development concepts.

Key Features
User Authentication System
The platform includes a secure authentication system that allows users to register, log in, and manage sessions securely. User profile management features were also implemented for maintaining personalized user information.
Features Included


User Signup


User Login & Logout


Secure Session Management


User Profile System



Marketplace System
The marketplace module allows students to upload and manage products for buying and selling purposes. Users can add product images, descriptions, and prices while managing listings through CRUD operations.
Features Included


Product Listing Creation


Product Image Upload


Edit and Delete Listings


Product Detail Page


Wishlist System


Responsive Marketplace Interface



Real-Time Chat System
One of the major features of Uni Bazar is the real-time communication system implemented using Django Channels and WebSockets. This system enables instant messaging between buyers and sellers without refreshing the page.
Features Included


Buyer and Seller Conversations


Real-Time Messaging


Seller Inbox System


Persistent Message Storage


WhatsApp-style Chat Interface


Multiple Chat Rooms



Community & Support Features
The platform also includes community-oriented functionalities for collecting user feedback and improving communication within the application.
Features Included


Public Feedback System


Suggestions and Improvement Wall


Footer Support Section


Social Media Integration



UI/UX Enhancements
Modern user interface and responsive design techniques were implemented to improve usability and user experience across devices.
Features Included


Responsive Design


Hover Animations


Modern Card Layouts


Dark Footer Interface


Smooth User Interactions



Technologies Used
TechnologyPurposePythonBackend ProgrammingDjangoWeb FrameworkDjango ChannelsReal-Time CommunicationWebSocketInstant MessagingDaphneASGI ServerSQLiteDatabase ManagementHTMLWebpage StructureCSSStylingBootstrapResponsive User InterfaceJavaScriptFrontend Interactivity

Real-Time Chat Architecture
The real-time communication system in Uni Bazar was developed using Django Channels and WebSocket technology. This architecture allows instant message delivery between buyers and sellers without requiring page refreshes.
Communication Workflow


Buyer sends a message.


WebSocket connection is established.


ChatConsumer receives the message request.


Message is stored in SQLite database.


Message is broadcasted to the chat room.


Seller receives the message instantly.


This architecture helped in understanding asynchronous communication and real-time application development.

Database Models
The project uses multiple database models for managing application functionalities efficiently.
Main Models Used


User


Profile


Item


Wishlist


ChatRoom


Message


Feedback


These models help maintain structured data management and relationship handling throughout the application.

Project Structure
The project follows a modular Django application structure for maintainability and scalability.
uni_bazar_structure/
├── apps/
├── accounts/   
├── listings/  
├── chat/  
└── core/
├── static/
├── templates/
├── media/
├── manage.py
└── requirements.txt
The structure separates functionalities into reusable applications for better project organization.

Installation Guide
Clone Repository

git clone https://github.com/Sudip-kr/uni-bazar-smart-marketplace.git

Open Project Directory
cd uni-bazar-smart-marketplace
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows

venv\\Scripts\\activate

Install Required Dependencies
pip install -r requirements.txt
Apply Database Migrations
python manage.py makemigrationspython manage.py migrate
Start Development Server
daphne uni_bazar.asgi:application

Future Improvements
Several additional features can be implemented in future versions of the project for improving functionality and user experience.
Planned Features


AI Recommendation System


Product Search and Filters


Sold Product Badge


Seller Dashboard


Recently Viewed Products


Dark Mode Interface



Learning Outcomes
This project provided valuable practical experience in full-stack web development and real-time communication systems.
Skills Learned


Full Stack Web Development


Django Framework


WebSocket Architecture


Real-Time Communication


Database Management


Authentication Systems


Responsive UI Design


Frontend and Backend Integration


The project significantly improved problem-solving, debugging, and scalable application development skills.

Project Status
Functionally Complete
The Uni Bazar project successfully demonstrates a modern smart campus marketplace platform with secure authentication, responsive UI, real-time communication, and scalable backend architecture.

Author
Developed with dedication by:

Sudipta Kumar Bag

Diploma CSE Student at LPU
Python Full Stack Development Enthusiast

License
This project was developed for educational, learning, and internship demonstration purposes.
