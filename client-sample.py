from zeep import Client

client = Client('http://localhost:8080/Hello/services/Hello?wsdl')
result = client.service.helloName('AOS 621 Project')
print(result)

#assert result == 62.137
