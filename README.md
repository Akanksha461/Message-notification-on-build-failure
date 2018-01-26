# Message notification on serevr issue

 Here i have written python script using request library we are able to know the status of api . The main perspective of this script is that incase  of any technical issue or server related issue developers should be informed immediately via Email and text message. Here is the [link](https://github.com/Akanksha461/Totojitu/blob/master/status_code.py) of whole code. For continuous integration i have used jenkins so that our script run after each time spam.Below is the step wise process for the same.

 ## Api status code
   For the server related issue we can also check the status of api. While using python we can use request library to check the status of an api.Requests will allow us to send HTTP/HTTPS requests using Python. With it, we can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way.
   
   ### Installation of Request
   I have used pip to install request using
    ```
    pip install requests 
    ```
  Import Requset using
    ```
    import requests 
    ```
    
  Below is the sample of my code to make requset api request
  
   ```
   driver.get("http://lotteryadmin.sia.co.in/#/login")
r = requests.get("http://lotteryadmin.sia.co.in/#/login")
print (r.status_code)
   ```
   
 ## Text SMS
  For text SMS i have used one third party which compose SMS and send to a particular person .Below is the code for the same.
   ```
   ```
   
  
