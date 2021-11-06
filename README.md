# Booking

## Adviser- Booking system prepared using Django REST-API.

The project structure looks like this-

A) Admin
1. API: Add an advisor
a) Method:
  i) POST
b) Authentication
   i) Not needed for this assignment
c) Endpoint: 
   i) /admin/advisor/
d) Request:
   i) Advisor name
   ii) Advisor Photo URL
e) Response:
   i) No Response
   ii) Just return 200_OK if the request is successful
   iii) Return 400_BAD_REQUEST if any of the above fields are missing
   
B) User
1. API: Can register as a user
a) Method:
   i) POST
b) Endpoint: 
   i) /user/register/
c) Request:
   i) Name
   ii) Email
   iii) Password
d) Response:
   i) Body:
      1) JWT Authentication Token
      2) User id
   ii) Status
     1) 200_OK if the request is successful
     2) 400_BAD_REQUEST if any of the above fields are missing
2. API: Can log in as a user
  a) Method:
     i) POST
  b) Endpoint: 
     i) /user/login/
  c) Request:
     i) Email
     ii) Password
     iii) Response:
  d) Body:
     i) JWT Authentication Token
     ii) User id
  e) Status
    i) 200_OK if the request is successful
    ii) 400_BAD_REQUEST if any of the above fields are missing
    iii) Return 401_AUTHENTICATION_ERROR if the email/password combination was wrong

  


