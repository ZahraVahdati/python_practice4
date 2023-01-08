products=[]
def read_file():
    f=open("read.txt","r")
    for line in f:
        result= line.split(",")
        my_dic={"Id":result[0],"Name":result[1],
         "price":result[2],"count":result[3]}
        products.append(my_dic)
        print(products)

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Search")



def add():
    id=input("Id: ")
    name=input("Name: ")
    price=input("Price: ")
    count=input("Count: ")

    new_dic={"Id":id,"Name":name,"Price":price,"Count":count}
    print(products)

def edit():
   print("Which one of information must change : 1-Name  2-Price  3-Count")
   user=int(input("Enter number :"))
   if user==1:
        name=input("Enter correct name: ")
        print("INFORMATION UPDATED")
   elif user==2:
        price=input("Enter correct price: ")
        print("INFORMATION UPDATED")
   elif user==3:
        count=input("Enter correct count: ")
        print("INFORMATION UPDATED")

def search():
    key= input("Enter your key: ")
    for product in products:
        if product["Id"]==key or product["Name"]==key:
            print(product)
            break
    else:
        print("Not found")
