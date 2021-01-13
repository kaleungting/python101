my_list = [1,2,3]
your_list = [10,20,30]

print(list(zip(my_list, your_list)))


#good for using it to combining key,values together 
names = ["Ken", "Sam", "Angel"]
phone_numbers = [7187082047,7187082037,7187082049]
email_address = ["klt@gmail.com", "nlt@gmail.com", "hmt@gmail.com"]
print(list(zip(names,phone_numbers,email_address)))