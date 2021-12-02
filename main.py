# Model design
from os import cpu_count
import agentpy as ap
from random import randint
import json

from agentpy.agent import Agent

posiciones = []
timer = 240

mainSpawn =  [[100,54.75],
              [100,52.25],
              [100,49.75], 
              [100,47.25]]

mainStop = [[58.55,54.11],
            [58.55, 51.32],
            [58.55,48.77], 
            [58.55,46.49]] 

mainDespawn = [[2.5,54.75],
               [2.5,52.25],
               [2.5, 49.7],
              [2.5, 47.25]]


upperSpawn = [[62.8,3.8],
              [59.4,3.8]]
              #up = [0][1] = 3.8 

upperStop = [[52.24, 43.05],
             [55.36,43.05]]
upperDespawn = [[0,0]]

lowerSpawn = [[77.5, 97.4],
              [74.6, 99.3]]

lowerStop = [[56.4,60.8],
             [53.8,63.1]]

lowerDespawn = [[22,1.6],
                [17.8,2]]

#definir los waypoints que tendremos i guess
class rutas:

  def __init__(self, num):

    if(num == 0):
      self.spawnPoint = mainSpawn[0]
      self.nextPoint = mainStop[0]
      self.endPoint = mainDespawn[0]

    if(num == 1):
      self.spawnPoint = mainSpawn[1]
      self.nextPoint = mainStop[1]
      self.endPoint = mainDespawn[1]

    elif(num == 2):
      self.spawnPoint = mainSpawn[2]
      self.nextPoint = mainStop[2]
      self.endPoint = mainDespawn[2]
    
    elif(num == 3):
      self.spawnPoint = mainSpawn[3]
      self.nextPoint = mainStop[3]
      self.endPoint = mainDespawn[3]
    
    elif(num == 4):
      self.spawnPoint = lowerSpawn[0]
      self.nextPoint = lowerStop[0]
      self.endPoint = lowerDespawn[0]

    elif(num == 5):
      self.spawnPoint = lowerSpawn[1]
      self.nextPoint = lowerStop[1]
      self.endPoint = lowerDespawn[1]


class Vehicle(ap.Agent):

  def setup(self):  
    self.id = self.id - 1             
    self.route = rutas(self.id)
    self.coordX = self.route.spawnPoint[0] 
    self.coordZ = self.route.spawnPoint[1] 
    self.nextPX = self.route.nextPoint[0]
    self.nextPZ = self.route.nextPoint[1]
    self.endPX = self.route.endPoint[0]
    self.endPZ = self.route.endPoint[1]
    posiciones.append([self.id,self.coordX, self.coordZ, self.nextPX, self.nextPZ, self.endPX, self.endPZ])

class Model(ap.Model):
  
  def setup(self):
    self.vehiculos = ap.AgentList(self, 6, Vehicle)



parameters= {
  'steps': 14400
}

def positionsToJSON(ps):
    data = {}
    #data.append("{"Vehicle": [")
    data['Vehicle'] = []
    for p in ps:
      data['Vehicle'].append({
          "id": p[0],
          "coordX" : p[1],
          "coordZ" : p[2],
          "nextPX" : p[3],
          "nextPZ" : p[4],
          "endPX" : p[5],
          "endPZ" : p[6]
    })
      
    return json.dumps(data)

def main():
    model = Model(parameters)
    resultsVehiculo = model.run()
    resultsVehiculo.save()
    resultsVehiculo = ap.DataDict.load('Model')
    jsonData = positionsToJSON(posiciones)
    #open text file

    #cambia depende del local
    path = "C:\\Users\\santi\\OneDrive\\Desktop\\UnityReposSSD\\Proyecto-Unity-Gp7\\RETOGpo7RON\\Assets\\Resources\\results.json"
    text_file = open(path, "w")

    #write string to file
    text_file.write(jsonData)

    #close file
    text_file.close()


main() #si imprimimos el main aparecerá el .json
'''
modelVehiculo = VehicleModel(parametersVehiculo)
resultsVehiculo = modelVehiculo.run()
resultsVehiculo.save()
resultsVehiculo = ap.DataDict.load('VehicleModel')'''
'''resultsSemaforo.save()
modelSemaforo = SemaforoModel(parametersSemaforo)
resultsSemaforo = modelSemaforo.run()
resultsSemaforo = ap.DataDict.load('SemaforoModel')'''