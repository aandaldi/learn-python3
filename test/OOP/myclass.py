class MyRouter(object) :                                                #objects is actually an istance of the class
    "This is a class that describes the characteristic of a router."    #You can create many class using this method
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_roter(self,manuf_date):                                  #this is function, you can call using objectname.functionname (eg. MyRouter.printrouter)
        print("The router name is : ", self.routername)
        print("The router model is: ",self.model)
        print("The serial number is: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ",self.model+manuf_date)

#eg for objec from MyRouter class

# router1 = MyRouter("R1","2600", "12345", 12.4)
#router1.model                                      #to see model of router1
# getattr(router1, "routername")                      #to get value from object.routername
# getattr(router1, "routername", "R2")                #to set value of object.routername
# hasattr(router1, "routername")                      #to check if attribute is exist
# delattr(router1,  "routername")                     #to delete atribut from object
# isinstance(router1,MyRouter)                        #to check is object are instance of class
