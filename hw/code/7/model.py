# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:47:36 2015

@author: akond
"""

from random import uniform
import math 

class Model(object):
    def __init__(self):
        self.decisionVec=[0]        
        self.lowerRange=[0]
        self.numOfDec=0
        self.numOfObjs=0        
        self.upperRange=[0]


    def check(self):
        for count in range(0,self.numOfDec):
            if (self.decisionVec[count]<self.lowerRange[count]) or (self.decisionVec[count]>self.upperRange[count]):
              return False
        return True

    def copy(self,other):
        self.decisionVec = [_ for _ in other.decisionVec]
        self.lowerRange = [_ for _ in other.lowerRange]
        self.numOfDec = other.numOfDec
        self.numOfObjs = other.numOfObjs        
        self.upperRange = [_ for _ in other.upperRange]

    def generateInitialVector(self):
        ## we use random.uniform() as it geives floating point values as well 
        while True:
            for cnt in range(0,self.numOfDec):
                self.decisionVec[cnt]=uniform(self.lowerRange[cnt],self.upperRange[cnt])
            if self.check(): break

    def getobj(self):
        return []

    def sumOfObjs(self):
        return sum(self.getobj())

class Golinski(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0,0,0,0,0,0,0]        
        self.lowerRange=[2.6,0.7,17.0,7.3,7.3,2.9,5.0]
        self.numOfDec=7
        self.numOfObjs=10
        self.upperRange=[3.6,0.8,28.0,8.3,8.3,3.9,5.5]
        ## then create the initialization 
        self.generateInitialVector()

    def check(self):
        constCheckerVec    = [0,0,0,0,0,0,0,0,0,0,0]
        constCheckerVec[0] = ((1.0)/(self.decisionVec[0]*math.pow(self.decisionVec[1],2)*self.decisionVec[2])) - (1.0/27.0) 
        constCheckerVec[1] = ((1.0)/(self.decisionVec[0]*math.pow(self.decisionVec[1],2)*self.decisionVec[2])) - (1.0/27.0)  

        constCheckerVec[2] = (math.pow(self.decisionVec[3],3)/(self.decisionVec[1]*math.pow(self.decisionVec[2],2)*math.pow(self.decisionVec[5],4)) - (1.0/1.93) 
        constCheckerVec[3] = (math.pow(self.decisionVec[4],3)/(self.decisionVec[1]*math.pow(self.decisionVec[2],1)*math.pow(self.decisionVec[6],4)) - (1.0/1.93) 

        constCheckerVec[4] = self.decisionVec[1]*self.decisionVec[2] - 40
        constCheckerVec[5] = (self.decisionVec[0]/self.decisionVec[1]) - 12
        constCheckerVec[6] = 5 - (self.decisionVec[0]/self.decisionVec[1]) 
        constCheckerVec[7] = 1.9 - self.decisionVec[3] + 1.5*self.decisionVec[5] 
        constCheckerVec[8] = 1.9 - self.decisionVec[4] + 1.1*self.decisionVec[6] 
        obj_temp           = self.getobj
        constCheckerVec[9] = obj_temp[1] - 1300
        a                  = 745.0*self.decisionVec[4]/(self.decisionVec[1]*self.decisionVec[3])
        b                  = 1.575*math.pow(10,8)
        a_squared          = math.pow(a,2)
        constCheckerVec[10]=(math.sqrt(a_squared+b)/(0.1*math.pow(self.decisionVec[6],3))) - 1100

        for cnt in range(0,self.numOfDec):
            if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]) or (constCheckerVec[cnt] > 0):
              return False
        return True


    def getobj(self):
        
        giveSquaredValue = lambda val : math.pow(val, 2)
        giveCubeValue    = lambda val : math.pow(val, 3)
        giveSeventhPower = lambda val : math.pow(val, 7)

        # Temporary values for f1
        tmp1 = (10*giveSquaredValue(self.decisionVec[2])/3) + 14.933*self.decisionVec[2] - 43.0934
        tmp2 = 1.508*self.decisionVec[0](giveSquaredValue(self.decisionVec[5]) + giveSquaredValue(self.decisionVec[6]))
        tmp3 = 7.477*(giveCubeValue(self.decisionVec[5]) + giveCubeValue(self.decisionVec[6]))
        tmp4 = 0.7854*(self.decisionVec[3]*giveSquaredValue(self.decisionVec[5]) + self.decisionVec[4]*giveSquaredValue(6))

        f1   = 0.7854*self.decisionVec[0]*giveSquaredValue(self.decisionVec[1])(tmp1) - tmp2 + tmp3 + tmp4

        # Temporary values for f2
        x    = 745.0*self.decisionVec[3]/(self.decisionVec[1]*self.decisionVec[2])
        y    = 1.69*giveSeventhPower(10)
        z    = 0.1*giveCubeValue(self.decisionVec[5])

        f2   = math.sqrt(giveSquaredValue(x) + y) / z
        
        return [f1,f2]

class Osyczka2(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0,0,0,0,0,0]        
        self.lowerRange=[0,0,1,0,1,0]
        self.numOfDec=6
        self.numOfObjs=2
        self.upperRange=[10,10,5,6,5,10]
        ## then create the initialization 
        self.generateInitialVector()

    def check(self):
        constCheckerVec = [0,0,0,0,0,0]
        constCheckerVec[0]=     (self.decisionVec[0]) + (self.decisionVec[1]) - 2 
        constCheckerVec[1]= 6 - (self.decisionVec[0]) - (self.decisionVec[1])
        constCheckerVec[2]= 2 - (self.decisionVec[1]) + (self.decisionVec[0])
        constCheckerVec[3]= 2 - (self.decisionVec[0]) + (3*self.decisionVec[1])
        constCheckerVec[4]= 4 - (self.decisionVec[3]) - math.pow(((self.decisionVec[2]) - 3), 2)
        constCheckerVec[5]=     math.pow((self.decisionVec[4]-3), 3) + ((self.decisionVec[5]) - 4) 
        for cnt in range(0,self.numOfDec):
            if (self.decisionVec[cnt] < self.lowerRange[cnt]) or (self.decisionVec[cnt]>self.upperRange[cnt]) or (constCheckerVec[cnt] < 0):
              return False
        return True


    def getobj(self):
        giveSquaredValue = lambda val : math.pow(val, 2)
        f1=-(
             25 * math.pow((self.decisionVec[0]-2), 2)+
             math.pow((self.decisionVec[1]-2), 2)     +
             math.pow((self.decisionVec[2]-1), 2)     * 
             math.pow((self.decisionVec[3]-4), 2)     + 
             math.pow((self.decisionVec[4]-1), 2)
             )
        
        f2=( 
             giveSquaredValue(self.decisionVec[0]) + 
             giveSquaredValue(self.decisionVec[1]) +
             giveSquaredValue(self.decisionVec[2]) +
             giveSquaredValue(self.decisionVec[3]) +
             giveSquaredValue(self.decisionVec[4]) +
             giveSquaredValue(self.decisionVec[5])
           )
        return [f1,f2]



class Schaffer(Model):

    def __init__(self):
        ## first specify the requirements         
        self.decisionVec=[0]
        self.lowerRange=[-100000]
        self.numOfDec=1
        self.numOfObjs=2
        self.upperRange=[100000]
        ## then create the initialization 
        self.generateInitialVector()

    def getobj(self):
        f1=math.pow(self.decisionVec[0], 2)
        f2=math.pow((self.decisionVec[0]-2), 2)
        return [f1,f2] 



class Kursawe(Model):

    def __init__(self):
        ## first specify the requirements 
        self.decisionVec=[0,0,0]        
        self.lowerRange=[-5,-5,-5]
        self.numOfDec=3
        self.numOfObjs=2
        self.upperRange=[5,5,5]
        ## then create the initialization 
        self.generateInitialVector()

    def getobj(self):
        f1=0
        f2=0 
        theA = 0.8
        theB = 1.0
        for cntI in range(0,self.numOfDec):
            if cntI< self.numOfDec-1: 
                f1 = f1 + ( -10*math.exp(-0.2*math.sqrt( math.pow( self.decisionVec[cntI], 2) + math.pow( self.decisionVec[cntI+1], 2))))
                f2 = f2 + ( math.pow( abs(self.decisionVec[cntI]), theA ) + 5 * math.sin( math.pow( self.decisionVec[cntI], theB) ) )
        return [f1,f2]