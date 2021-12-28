import xmlrpc.client


proxy = xmlrpc.client.ServerProxy('http://localhost:8000')
try:
    #azul -> 0000FF
    print(proxy.valor("hgfhf", "rgb"))
    
    #426F42 -> verde oceano
    print(proxy.valor("426F42", "cor"))
    
    #magente -> FF00FF
    print(proxy.valor("verde", "rgb"))
    
    #ADEAEA -> turquesa
    print(proxy.valor("ADEAEA", "cor"))
    
except xmlrpc.client.Fault as err:
    print("Ocorreu uma falha")