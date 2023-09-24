











name : Metro Project
Packages Required :
	1.tkinter ->For Graphical User Interface
	2.mysqlconnector ->For Connecting MySQL workbench database
	3.twilio ->For OTP service
How to install ?
	1.tkinter -> pip install tk
	2.mysqlconnector -> pip install mysql-connector-python
	3.twilio -> pip install twilio
Sign-Up & Other setup for Twilio :
	1.You have to do sign-up on their website to use their
	API services of SMS sending
	2.copy account_sid,auth_token and phone number which will
	given by them to code in 'signup.py' file's details, right now
	my account details are already in code.
Tables Required in MySQL Workbench :
	1.Install MySQL Workbench 
	2.Username will by default 'root'
	3.set Password as '1516' , You can change it later on.
	4.Execute these below commands One by One to create tables.
	
	create database passenger;

	use passenger;

	create table login(
  	first_name varchar(20),
  	last_name varchar(20),
  	username varchar(30) primary key,
  	password varchar(30),
  	confirm_password varchar(30),
  	age varchar(5),
  	contact varchar(30));

	 create table ticket(
 	 id int primary key,
  	username varchar(30),
 	 pnr int,
 	 source varchar(20),
  	destination varchar(20),
  	rate int,
 	 constraint FK_passengers_username foreign key (username) references login(username)
 	 );

	  create table card(
   	  username varchar(30) primary key,
  	  amount int,
  	  constraint FK_card_username foreign key (username) references login(username));
	
How to Run ?
	1.Load "metroproject.py" file, rest other files are already imported
	  in that file using import modules
	2.Execute that file , snapshots of it is also provided in Folder.
Working of Project :
1.You can sign-up , using email id , phone number and other details, data will
be stored in database and email id/username is primary key , so no duplicate
value is allowed of that field
2.Real time OTP will be sent on User's Phone number ,Only by verifying it, User will
able to create Account.
3.Login window is provided for user , after only Successful Login username and password
it'll redirect User to Dashboard.
4.On dashboard there are 4 diffrent features ,
	1.booking window
	2.Create SmartCard
	3.Recharge SmartCard
	4.View Previous Transaction
5.SmartCard balance is essential for booking Metro Ticket
6.We have consider , 4 Metro Trains running b/w diffrent stations , but 
their ending station is same , so user can travel among all the places.
7.Fare is calculated upon station distances.
8.In booking window , user will get options to select source and destination
stations,then it will show Fare and ask user to give username , which will check
smart card issued or not , if issued already then it has enough balance or not.
9.If it has enough balance it will charge that amount from database and issue 
ticket , which will pop up using small window, & data can be retrived using
'show transaction' option in dashboard.
10.User can also add balance in SmartCard.

Features of project :

1.Log In & Sign-Up window, Password Protected
2.OTP service for Phone number Verification
3.Metro Ticket Booking
4.SmartCard for Balance

Team Details :

19BCE198 - Siddharth Patel
19BCE199 - Tirth Patel
19BCE201 - Viraj Patel

Website of Twilio :

https://www.twilio.com/docs/usage/api





















