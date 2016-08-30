let me know when you can see this screen
Hello! 

/users
    {
        id: 1234,
        name: "John Smith",
        company: "Entic"
    
    },
    {
        id: 1235,
        name: "John Smith Jr.",
        company: "Entic"
    
    }
    ...
    
  10,000 
  
  
  # time_stamp -> 
  # who's logged in? 
  
  Tables -> 
  
  Users
      -id (foreign Key in Login)
      -name 
      -company 
 
  Login
     - login_id -> combine (id, time)
     - time - time_stamp 
     - 
    
  Login
      - user_id
      - login_time
      - logout_out (NULL)
      
      where logout_time is null
  
  
  login & Users -> WHERE time = now() 
          login_id.id == users.id 
  
  
# all the groups associated 

/users/1234/group

    {
     id:1234
     name:"John Doe"
     groups:["Product", "Sales"]  
        
    }
    
     
    1. How would you send the request to the API to create a user?
        
    2. if successful, how you deal with showing the newly added user on the table?