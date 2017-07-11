import csv
FN=['name','price','category','stock']
class Product:
	__iname=""
	__price=0
	__stock=0.0
	__cat=""
	def add(self,name=None):
		if(name):
			self.__iname=name;
		else:
			print("enter item name",end=" ")
			self.__iname=input()
		print("enter item category",end=" ")
		self.__cat=input();
		print("enter item price",end=" ")
		self.__price=input()
		print("enter item stock quantity in numbers",end=" ")
		self.__stock=input()
		with open("products.csv",'a') as csvf:
			wr=csv.DictWriter(csvf,fieldnames=FN)
			#wr.writeheader()
			wr.writerow({FN[0]:self.__iname,FN[1]:self.__price,FN[2]:self.__cat,FN[3]:self.__stock});
	def delete(self,name=None):
		item=[];
		flag=0
		with open("products.csv",'r') as csvf:
			read=csv.DictReader(csvf)
			for row in read:
				if(name and row['name']!=name):
					item.append(row);
				if(row['name']==name):
					flag=1;
		if flag==0:
			print("the item is not in stock. Maybe it's already deleted")
		else:
			with open("products.csv",'w') as csvf:
				wr=csv.DictWriter(csvf,fieldnames=FN)
				wr.writeheader();
				for row in item:
					wr.writerow(row)
			print("item successfully deleted")
	def search(self,name=None):
		category=""
		item=[]
		if not name:
			print("enter category",end=" ")
			category = input()
		with open("products.csv",'r') as csvf:
			read=csv.DictReader(csvf)
			for row in read:
				if(name and row['name']==name):
					return row
				elif(row['category']==category):
					item.append(row)
		return item	
	def update(self,name,stock=None):
		item=[];
		flag=0
		with open("products.csv",'r') as csvf:
			read=csv.DictReader(csvf)
			i=0;
			for row in read:
				if(row['name']==name):
					l = i;
					flag=1
				item.append(row)
				i=i+1;
		if flag==0:
			print("the selected item is not in stock. Do you want to add it?")
			st = input()
			if(st=="yes"):
				self.add(name);
			return
		if(stock):
			item[l]['stock']=str(stock)
		else:
			print("the modifiable features are price and stock. Type the feature to be modified")
			k=input()
			print("enter the new value",end=" ")
			newval=input()
			item[l][k]=newval
		with open("products.csv",'w') as csvf:
			wr=csv.DictWriter(csvf,fieldnames=FN)
			wr.writeheader();
			for row in item:
				wr.writerow(row)
	def display(self):
		with open("products.csv",'r') as csvf:
			read=csv.DictReader(csvf)
			for n in FN:
				print(n,end="\t")
			print();
			for row in read:
				for n in FN:
					print(row[n],end="\t")
				print();	
	
	def billing(self):
		total = 0
		while 1:
			print("enter name of product to add to cart or type exit")
			ini = input();	
			if ini=="exit":
				break;
			dat = self.search(ini)
			if(type(dat)==list):
				print ("the item is not available right now. Sorry for the inconvenience")
			else:
				print ("the price of",dat['name'],"is",dat['price'],". How much do you want?")
			q = int(input());
			if q>float(dat['stock']):
				print ("there is less stock (",dat['stock'],"). Sorry for the inconvenience. Please retype the quantity you want.")
				q = int(input());
			total = total + q*float(dat['price']);
			self.update(ini,int(dat['stock']) - q)
		print("The total amount is",total,"Thanks for shopping");

p = Product()				
print("Are you a customer or owner?")
person = input()
if(person == "customer"):
	p.billing()
else:
	print("Do you want to add, delete, search or update?")
	choice = input()
	if choice=="add":
		p.add()
	if choice=="delete":
		print("enter the product to be deleted");
		na = input()
		p.delete(na)

	if choice=="search":
		print("Do you want to search the category or product?")
		na = input()
		if na=="product":
			print("enter the product to be searched");
			na = input()
			k=p.search(na)
			if type(k)==list:
				print("the selected item is not in stock. Do you want to add it?")
				st = input()
				if(st=="yes"):
					self.add(name);
				else:
					for n in FN:
						print(n,end="\t")
					for i in k:
						print (k[i],end="\t")
		else:
			k=p.search()
			if k==[]:
				print("There is no such category")
			else:
				for n in FN:
					print(n,end="\t")
				for i in k:
					for j in i:
						print(i[j],end=" ")
					print()	
	if choice=="update":
		print("enter the product name",end=" ")
		na = input()
		p.update(na)
	print();
	p.display();
	 

	
