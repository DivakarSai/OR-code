import math

def distance(a,b):
     #Euclidean distance between two points a and b
     return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])) 

def lyingIn(points,center,radius):
     n=len(points)
     for i in range(n):
          if(distance(points[i],center)>radius):
               return i
     return n

def circumcenter(edge1,edge2,edge3):
     a1 = 2*(edge2[0]-edge1[0])
     a2 = 2*(edge3[0]-edge2[0])
     b1 = 2*(edge2[1]-edge1[1])
     b2 = 2*(edge3[1]-edge2[1])
     c1 = edge2[0]*edge2[0] - edge1[0]*edge1[0] + edge2[1]*edge2[1] - edge1[1]*edge1[1]
     c2 = edge3[0]*edge3[0] - edge2[0]*edge2[0] + edge3[1]*edge3[1] - edge2[1]*edge2[1]

     center = [(b2*c1 - b1*c2)/(b2*a1-b1*a2), (a2*c1 - a1*c2)/(a2*b1-a1*b2)]
     return center

def checkType(edge1,edge2,outlierPoint):
     
     dotProduct = (edge1[0]-edge2[0])*(outlierPoint[0]-edge2[0]) + (edge1[1]-edge2[1])*(outlierPoint[1]-edge2[1])
     #print(edge1)
     #print(edge2)
    # print(outlierPoint)
     #print("end")
     if dotProduct<=0:
          return 1
     else :
          return 0
     
def step3(points,edge1,edge2,edge3):
     center = circumcenter(edge1,edge2,edge3)
     radius = distance(edge1,center)
     outlier = lyingIn(points,center,radius)
     if outlier< len(points) :
          #step4
          pl = points[outlier]
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
          print("The radius of the circle is : "+ str(radius))
          return center     


def step2(points,edge1,edge2):
     center = [(edge1[0]+edge2[0])/2,(edge1[1]+edge2[1])/2]
     radius = distance(edge1,center)
     outlier = lyingIn(points,center,radius)
     if outlier<len(points):
          if checkType(edge1,edge2,points[outlier])  :
               return step2(points,edge1,points[outlier])
          elif checkType(edge2,edge1,points[outlier]) :
               return step2(points,edge2,points[outlier])
          else:
               return step3(points,edge1,edge2,points[outlier])
     else :
          print("The radius of the circle is : "+ str(radius))
          return center

              


def elzingaH (points):
    
    if len(points)==1:
         return points

    center = step2(points,points[0],points[1])
    return center


n = int(input("enter the number of existing facilities : "))
#print("Input the locations of the "+ i+ "th existi")
points = list(list())
for i in range(n):
     a = float(input("Enter the X-cordinate of "+ str(i) +"th facility : "))
     b = float(input("Enter the Y-cordinate of "+ str(i) +"th facility : "))
     points.append([a,b])
print("center of the circle is : "+ str(elzingaH(points)))

