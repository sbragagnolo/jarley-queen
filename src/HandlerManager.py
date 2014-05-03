import xmpp



class HandlerManager():
    handler = None
    
    handlersDeMensajes = []
    handlersDeEstado = []
    
    @classmethod 
    def registrarCliente (self,cliente):
        cliente.RegisterHandler("message", handlerDeMensajeNuevo)
        cliente.RegisterHandler("presence", handlerDeEstado)
        return HandlerManager.handlerInstance()
    
    @classmethod
    def handlerInstance(self):
        if (HandlerManager.handler == None):
            HandlerManager.handler = HandlerManager()
        return HandlerManager.handler
    
    def registrarHandler(self, handler):
        self.registrarHandlerDeEstado(handler)
        self.registrarHandlerDeMensajes(handler)
        
    def registrarHandlerDeMensajes(self, handler):
        self.handlersDeMensajes.append(handler)
    
    def registrarHandlerDeEstado(self, handler):
        self.handlersDeEstado.append(handler)

    
    def mensajeNuevo(self, cliente, mensaje):
        for handler in self.handlersDeMensajes:
            handler.manejarMensaje(cliente, mensaje)
            
    
    def cambioDeEstado(self, cliente, estado):
        for handler in self.handlersDeEstado:
            handler.manejarEstado(cliente, estado)

    

"""
################################################################################################################
    Estas dos funciones cumplen con lo que requiere XMPP-PY para manejar cada evento. 
    Delegan la responsabilidad en el manager
################################################################################################################
"""


def handlerDeMensajeNuevo (cliente, mensaje):
    handler = HandlerManager.handlerInstance()
    return handler.mensajeNuevo(cliente, mensaje)
    
def handlerDeEstado (cliente, estado):
    handler = HandlerManager.handlerInstance()
    return handler.cambioDeEstado(cliente, estado)


"""
################################################################################################################
    Baterias Incluidas
    Handler: Clase vacia, muestra los metodos que hay que implementar para que ande la cosa. 
    HandlerDeEstado: Clase que maneja estados de clientes, respeta el protocolo y mantiene un diccionario con el 
    estado
    HandlerDeMensajes: Clase que maneja mensajes mostrandolos por pantalla como usuario dice: <lo que diga>
    HandlerBasico: Clase que hereda de las otras dos, armando un handler que muestra por pantalla 
    y registra el estado
################################################################################################################
"""

class Handler():
    pass
    # def manejarMensaje(self,cliente, mensaje):
    # def manejarEstado(self,cliente, estado):
      


class HandlerDeEstado(Handler):
    estados = {}
    
    def estadoDe(self,mail):
        return self.estados[mail]
    
    def manejarEstado(self,cliente, estado):
        tipo = estado.getType()
        usuario = estado.getFrom()
        self.estados[str(usuario)] = tipo
        print " Usuario:" + str(usuario) + " Estado:" + str(tipo)
        
        if(tipo == "subscribe"):
            cliente.send(xmpp.Presence(to=usuario, typ="suscribed"))
            cliente.send(xmpp.Presence(to=usuario, typ="suscribe"))
        return True

class HandlerDeMensajes(Handler):    
    def manejarMensaje(self,cliente, mensaje):
        print str(mensaje.getFrom()) + " dice:" + str(mensaje.getBody())
        return True

    
class HandlerBasico(HandlerDeEstado,HandlerDeMensajes):
    pass
    