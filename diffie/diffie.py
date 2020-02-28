 # publicly known 
 n=22 
 # publicly known
 g=42 

 x=13 # only Alice knows this 
 y=53 # only Bob knows this

 aliceSends = (g**x)%n 
 bobComputes = aliceSends**y 
 bobSends = (g**y)%n
 aliceComputes = bobSends**x


 print("Alice sends    ", aliceSends )
 print("Bob computes   ", bobComputes) 
 print("Bob sends      ", bobSends) 
 print("Alice computes ", aliceComputes)

 print("In theory both should have ", (g**(x*y))%n)