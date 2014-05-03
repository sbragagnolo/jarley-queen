'''
Created on 16/09/2010

@author: Santiago
'''



    
class MaquinaDeEstados():
    estados = []
    
class Estado():
    palabrasClave = {}
    delimitador = " "
    descripcion = " Estado de maquina de estados "
    
    
    def registrarSalto(self, palabraClave, estado):
        self.palabrasClave[palabraClave] = estado
        return self
    
    def aplicarA(self, consulta, pedazos):
        indicesQueAplican = []
        index = 0
        for token in pedazos:
            proximo = self.palabrasClave[token]
            if (proximo != None):
                indicesQueAplican.append(index)
            index = index + 1
        
        
        for index in xrange(len(indicesQueAplican)):
            proximo = self.palabrasClave[pedazos[indicesQueAplican[index]]]
            pedazosQueAplican = []
            for subindex in xrange(indicesQueAplican[index], indicesQueAplican[index+1] - 1):
                pedazosQueAplican.append(pedazos[subindex])
                
            proximo.aplicarA(consulta,pedazosQueAplican)
    
    
    
    