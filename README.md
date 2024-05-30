clone the repo  
docker-compose up --build -d  

 
 .env file content  
USE_DEMO_DATA=true  # Set to 'true' to use demo data, 'false' to use live SAP B1 connection
SAP_B1_ENDPOINT=http://sapb1server:50000/b1s/v1  
SAP_B1_USERNAME=myusername  
SAP_B1_PASSWORD=mypassword  
SAP_B1_COMPANYDB=mycompanydb  
 


todo:  
implement SAP service layer endpoints  
