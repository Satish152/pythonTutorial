var={1:'testing',2:'automation',3:'API'}
print(var)
print(var.keys())
print(var.get(1))
print(var.get(4,"Not Found")) #if there is no key present in the dictoonary, it will print the given value
print(var.values())

#combining two lists in to dictionary using zip and dict functions
list=['satish','ramesh','testing',4]
list2=['test','dev','uat','23']
output=dict(zip(list,list2))
print(output)

output['cricket']='worldcup'
print(output)