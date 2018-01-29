import requests
import json

# Check status code for website.
response = requests.get("url of the website")
print(response.status_code)
if response.status_code ==200:
      print("server is working fine")
  
else:
	response2=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=id&password=password&sender=senderid&to=mobileno&message=Their%20is%20some%20technical%20issue%20in%20lottery%20admin%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")
 
# Check status code for another website".	
response3 = requests.get("url of second wesite")
print(response3.status_code)
if response3.status_code ==200:
      print("server is working fine")

else:
	response2=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=id&password=password&sender=senderid&to=mobileno&message=Their%20is%20some%20technical%20issue%20in%20lottery%20admin%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")
 
