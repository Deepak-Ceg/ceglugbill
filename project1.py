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
			print("enter 1 to list out the products,\n2 to add product or any other key to exit")
			choice = input()
			if int(choice)==2:
				print("enter name of product to add to cart")
				ite = input();	
				dat = self.search(ite)
				if(type(dat)==list):
					print ("the item is not available right now. Sorry for the inconvenience")
				
				else:
					print ("the price of",dat['name'],"is",dat['price'],". How much do you want?")
				q = int(input());
				if q>float(dat['stock']):
					print ("there is less stock (",dat['stock'],"). Sorry for the inconvenience. Please retype the quantity you want.")
					q = int(input());
				total = total + q*float(dat['price']);
				self.update(ite,int(dat['stock']) - q)
			elif int(choice)==1:
				self.display();
			else:
				if total!=0:
					print("The total amount is",total,"Thanks for shopping");
				else:
					print("thank you");
				break;

def owner():
	while(1):
		print(" 1 to add,\n 2 to delete,\n 3 to search,\n 4 to update or any other key to exit")
		choice =input()
		if int(choice)==1:
			p.add()
		elif int(choice)==2:
			print("enter the product to be deleted");
			na = input()
			p.delete(na)

		elif int(choice)==3:
			print(" 1 for category,\n 2 for product?")
			search_choice= int(input())
			if search_choice==2:
				print("enter the product to be searched");
				na = input()
				result=p.search(na)
				if type(result)==list:
					print(" the selected item is not in stock. Do you want to add it?\n Y for yes,N for no")
					user_in= input()
					if(user_in=="Y"):
						self.add(name);
				else:
					for n in FN:
						print(n,end="\t")
					for i in result:
						print (result[i],end="\t")
			else:
				result=p.search()
				print()
				if result==[]:
					print("There is no such category")
				else:
					for n in FN:
						print(n,end="\t")
					print()
					for pro in result:
						for j in FN:
							print(pro[j],end=" ")
						print()	
		elif int(choice)==4:
			print("enter the product name",end=" ")
			na = input()
			p.update(na)
			print();
		else:
			break;
	p.display()
	
p = Product()
switch_=1
while(switch_):
	switch_=0;				
	print("1 to customer\n2 to owner")
	person_choice = input()
	if(int(person_choice) == 1):
		p.billing()
	elif (int(person_choice)==2):
		owner()
	else:
		print("u have entered the wrong value.please enter correct value")
		_switch=1

	
	
	 

	
