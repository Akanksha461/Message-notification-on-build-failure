import requests
import json

# Check status code for destimoney admin.
response = requests.get("https://api.dealmoney.net/")
print(response.status_code)
if response.status_code ==200:
      print("server is working fine")
  
else:
	response2=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9654770857&message=Their%20is%20some%20server%20issue%20in%20dealmoney%20%20project%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")

	response3=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=8860734935&message=Their%20is%20some%20server%20issue%20in%20dealmoney%20%20project%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")
 	
 
