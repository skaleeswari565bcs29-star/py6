class Supplier:
    c=0
    def __init__(self,n):
        self.name=n
        Supplier.c+=1
class Product:
    c=0
    class Specifications:
        def __init__(self,cat):
            self.category=cat
    def __init__(self,n,supplier,cat):
        self.name=n
        self.supplier=supplier
        self.specs=Product.Specifications(cat)
        Product.c+=1
    def display(self):
        print("Product Name:",self.name)
        print("Supplier:",self.supplier.name)
        print("Category:",self.specs.category)
n=int(input("Enter no of products:"))
products=[]
for i in range(n):
    print("enter details of product",i+1 )
    pname=input("Enter product name:")
    sname=input("Enter supplier name:")
    category=input("Enter category:")
    s=Supplier(sname)
    P=Product(pname,s,category)
    products.append(P)
print("\n---Product Details---")
for p in products:
    p.display()
print("\nTotal Products:",Product.c)
print("Total Suppliers:",Supplier.c)
