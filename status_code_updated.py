import requests
import json
response = requests.get("https://admin.jeruk-emas.org/login")

 # Check status code for lottery admin.
print(response.status_code)
if response.status_code ==200:
      print("server is working fine")
  
else:
	response2=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20admin%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")
 
 	
 # Check status code for lottery "cmd36.com".	
response3 = requests.get("https://cmd36.com/")
print(response3.status_code)
if response3.status_code ==200:
      print("server is working fine")

else:
 	response3=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20cmd36.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")

 # Check status code for lottery "csovegas.com/".	
response4 = requests.get("https://csovegas.com/")
print(response4.status_code)

if response4.status_code ==200:
      print("server is working fine")
else:
 	response4=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20csovegas.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")	
 	
 	
 # Check status code for lottery "ibet36.net/".	
response5 = requests.get("https://ibet36.net/")
  
print(response5.status_code)
  
if response5.status_code ==200:
      print("server is working fine")
else:
 	response5=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20ibet36.net%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")	
 
 # Check status code for lottery "ibet36.com/".	
response6 = requests.get("https://ibet36.com")
print(response6.status_code)

if response6.status_code ==200:
      print("server is working fine")
else:
 	response6=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20ibet36.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")




