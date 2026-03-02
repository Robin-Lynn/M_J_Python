def midpoint(p1,p2):
     x1,y1=p1
     x2,y2=p2
     return (x1+x2)/2,(y1+y2)/2

#Get two points from th user
pt1=float(input("Enter the 1st x val:")),\
     float(input("Enter the 1st y val:"))
pt2=float(input("Enter the 2nd x val:")),\
     float(input("Enter the 2nd y val:"))    
mid =midpoint(pt1,pt2)

#Display the result
print( "The midpoint of ",pt1,"and",pt2,"is",mid)
