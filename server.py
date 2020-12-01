# first of all import the socket library 
import socket

arr=0*[0]
def Calk(k):
    s=""
    try:
        s=eval(k);
        arr.append(s);
    except:
        return "wrong query";
    return str(s)

        

# next create a socket object 
s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port) )
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr) 
  
   # send a thank you message to the client.  
   c.send('Thank you for connecting'.encode())


  
   
   while(True):
      s.listen(5)
      k = c.recv(1024).decode()
      if(k=="end"):
          mini=arr[0];
          maxi=arr[0];
          suma=0;
          cnt=len(arr);
          if (cnt==0):
              print("there was no queries");
              break;
          for i in arr:
              suma+=i;
              mini=min(mini,i);
              maxi=max(maxi,i);
          ans="number correct of querys == "+str(cnt)+'\n'+"max result  == "+str(maxi)+'\n'+"min result  == "+str(mini);
          print("number of querys == ",cnt);
          print("max result  == ",maxi);
          print("min result == ",mini);
          c.send(ans.encode())
          break
          
        
      c.send(Calk(k).encode())
      print("query processed for "+k)
   # Close the connection with the client
   c.close()
