server_1 = "172.10.33.25"
server_2 = "172.10.33.26"

servers = ["172.10.33.25", "172.10.33.26", True, 123, 123.45,1234.56]
print(type(servers), servers, server_1, server_2)

#python is zero indexed  programming language
server_1 = servers[0]
print("server 1 ip address :", server_1)

#Slicing (start_index:end_index + 1:step_size), end_index in python is not inclusive
#step size: 1 (default)
simple_slice = servers[1:6:2] # [1, 1+2, 3+2, 5+2]
print(simple_slice)


#Negative_indexing
simple_slice = servers[-1:-4:-1]
print(simple_slice)

print("Length of list:", len(simple_slice))

#List is a mutable data type
#Mutable : once define can chnage at any time
#Immutable : Once define can't be changed