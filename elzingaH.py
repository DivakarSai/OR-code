import numpy as np
import random
import sys
import math

def distance(a,b):
     #Euclidean distance between two points a and b
     return math.sqrt((a[0, 0]-b[0, 0])*(a[0, 0]-b[0, 0]) + (a[0, 1]-b[0, 1])*(a[0, 1]-b[0, 1])) 

def lyingIn(points,center,radius):
     n=np.shape(points)[0]
     for i in range(n):
          if(distance(points[i:i+1],center)>radius):
               return i
     return n

def circumcenter(edge1,edge2,edge3):
     a1 = 2*(edge2[0: 0]-edge1[0: 0])
     a2 = 2*(edge3[0: 0]-edge2[0: 0])
     b1 = 2*(edge2[0: 1]-edge1[0: 1])
     b2 = 2*(edge3[0: 1]-edge2[0: 1])
     c1 = edge2[0: 0]*edge2[0: 0] - edge1[0: 0]*edge1[0: 0] + edge2[0: 1]*edge2[0: 1] - edge1[0: 1]*edge1[0: 1]
     c2 = edge3[0: 0]*edge3[0: 0] - edge2[0: 0]*edge2[0: 0] + edge3[0: 1]*edge3[0: 1] - edge2[0: 1]*edge2[0: 1]

     center = np.array(shape =(1,2),dtype=float)
     center[0: 0]= (b2*c1 - b1*c2)/(b2*a1-b1*a2)
     center[0: 1]= (a2*c1 - a1*c2)/(a2*b1-a1*b2)
     return center

def checkType(edge1,edge2,outlier):
     
     dotProduct = (edge1[0:0]-edge2[0:0])*(edge1[0:1]-edge2[0:1]) - (edge2[0:0]-outlier[0:0])*(edge2[0:1]-outlier[0:1])
     if dotProduct<0:
          return 1
     else :
          return 0
     
def step3(points,edge1,edge2,edge3):
     center = circumcenter(edge1,edge2,edge3)
     radius = distance(edge1,center)
     outlier = lyingIn(points,center,radius)
     if outlier< np.shape(points)[0] :
          #step4
          pl = points[outlier:outlier+1]
          d1 = distance(pl,edge1)
          d2 = distance(pl,edge2)
          d3 = distance(pl,edge3)
          
          if d1>d2 and d1>d3 :
               
               if checkType(edge1,edge2,pl):
                    return step3(points,pl,edge1,edge3)
               else:
                    return step3(points,pl,edge1,edge2)
          elif d2>d1 and d2>d3 :
               if checkType(edge2,edge3,pl):
                    return step3(points,pl,edge2,edge1)
               else:
                    return step3(points,pl,edge2,edge3)
          else:
               if checkType(edge3,edge1,pl):
                    return step3(points,pl,edge3,edge2)
               else:
                    return step3(points,pl,edge3,edge1)
     else :
          return center     


def step2(points,edge1,edge2):
     #center = np.array(shape = (1,2),dtype=float)
     center = (edge1+edge2)/2
     radius = distance(edge1,center)
     outlier = lyingIn(points,center,radius)
     if outlier<np.shape(points)[0]:
         #angleType2 = checkType(edges[1:2],edges[0:1],points[outlier:outlier+1]) 
          if checkType(edge1,edge2,points[outlier:outlier+1])  :
               return step2(points,edge1,points[outlier:outlier+1])
          elif checkType(edge2,edge1,points[outlier:outlier+1]) :
               return step2(points,edge2,points[outlier:outlier+1])
          else:
               return step3(points,edge1,edge2,points[outlier:outlier+1])
     else :
          return center

              


def elzingaH (points):
    
    if points.size()==1:
         return points

    center = step2(points,points[0:1],points[1:2])
    return center
