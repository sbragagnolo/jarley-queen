import xmpp 
from HandlerManager import HandlerManager, HandlerBasico, Handler
import time

 
login = '' #@gmail.com
mail = ''
pwd   = ''
gtalk = ('talk.google.com',5223)


class HandlerRta(Handler):
    def manejarMensaje(self,cliente, mensaje):
        cliente.send(xmpp.Message( mensaje.getFrom() ," Test "))
        
def goOn(jarley):
    while jarley.stepOn():
        time.sleep(2)



class JarleyQueen ():
    client = None 
    jid = None
    
    def __init__(self):
        
        jid = xmpp.protocol.JID(mail)
        self.client = xmpp.Client(jid.getDomain(), debug=[])
         
        if self.client.connect(server=gtalk) == "":
            print "No se pudo conectar"
            
        logStat = self.client.auth(login, pwd) 
        if  logStat == None:
            print "No se pudo autenticar"
        
        handler = HandlerManager.registrarCliente(self.client)
        handler.registrarHandler(HandlerBasico())
        handler.registrarHandlerDeMensajes(HandlerRta())
        
        self.client.sendInitPresence()
        print "echo"
        
    def process(self):
        self.client.Process(10)
    
        
    def send(self, receptor, message):
        stat = self.client.send(xmpp.Message( receptor ,message ))
        print "STAT: " + str(stat)

    def stepOn (self):
        try:
            self.process()
        except KeyboardInterrupt:
            return 0
        return 1
    


if __name__ == "__main__":
    j = JarleyQueen()
    j.send("andrezrv@gmail.com", "maricon")
    goOn(j)


