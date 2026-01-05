server_1 = "172.10.33.25"
server_2 = "172.10.33.26"

servers = ["172.10.33.25", "172.10.33.26", True, 123, 123.45]
print(type(servers), servers, server_1, server_2)

#python is zero indexed  programming language
server_1 = servers[0]
print("server 1 ip address :", server_1)

#Slicing (start_index:end_index + 1:step_size), end_index in python is not inclusive
simple_slice = servers[1:5:2]
print(simple_slice)



