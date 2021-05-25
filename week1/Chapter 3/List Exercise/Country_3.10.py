#3.10使用各个函数对List进行操作
country = ['China', 'American', 'France', 'Russia', 'Pakistan']
print(country)
print(country[0])
print(country[2])
print(country[3].upper())
print(country[-1].upper())
message = "My favorite country is "+ country[0] +"!"
print(message)
country[1] = 'Canada' #将列表中第二个元素修改为Canada
print(country)
country.append('American')#在列表末尾添加元素
print(country)
country.insert(-1, 'England')#在列表末尾插入元素
print(country)
del country[-1]#删除列表末尾元素
print(country)
popped_country = country.pop()#删除末尾元素并保存到变量popped_country中
print(country)
print(popped_country)
print("The last country I have been to is "+popped_country+".")
first_country = country.pop(0)
print("The first country I have been to is "+first_country+".")

country_del='Canada'
country.remove(country_del)#根据值删除元素
print(country)
print(country_del)

#对列表按照字母顺序进行排序
country.sort()
print(country)
country.sort(reverse=True)#按照字母顺序倒着排序
print(country)

#对列表进行临时排序
country = ['China', 'American', 'France', 'Russia', 'Pakistan']
print(sorted(country))
print(country)

#倒着打印列表
country = ['China', 'American', 'France', 'Russia', 'Pakistan']
country.reverse()
print(country)
print(len(country))#确定列表的长度
# print(country[5])
# country=[]
# print(country[-1])

