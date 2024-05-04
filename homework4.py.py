immutable_var = (1, 'qweerty', True)
print('immutable_var:',immutable_var)
mutable_list=[1, 'qweerty', True]
mutable_list[0]=2
mutable_list[1]=mutable_list[1][::-1]
mutable_list[2]=False
print('mutable_list:',mutable_list)




