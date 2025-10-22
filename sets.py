1)
rainfall_data = {120, 150, 180, 120, 90, 110, 130}
print(len(rainfall_data))
2)
Set are unordered 
There is no index values in set
It is immutable
rainfall_data.remove(120)
rainfall_data.add(200)
3)
if 150 in rainfall_data:
    print("150 is present in the rainfall data")
else:
    print("150 is not present")
4)
rain_list = list(rainfall_data)
print(rain_list)  
5)
for value in rainfall_data:
    print(value) 
6)
rainfall_data.remove(120)
print(rainfall_data)
7)
print("Before adding 110:", rainfall_data)
rainfall_data.add(110)
print("After adding 110:", rainfall_data)
Set only can take unique elements.So there is no effect.

1)
rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
chennai_madurai = rainfall_chennai | rainfall_madurai
print("Unique rainfall:",chennai_madurai)
2)
merged_union = rainfall_chennai | rainfall_madurai | rainfall_coimbatore
merged_update = set(rainfall_chennai) 
merged_update.update(rainfall_madurai, rainfall_coimbatore)
3)
common_all = rainfall_chennai & rainfall_madurai & rainfall_coimbatore
print(common_all)
4)
unique_chennai = rainfall_chennai - rainfall_madurai - rainfall_coimbatore
print(unique_chennai)
5)
chennai_madurai = rainfall_chennai & rainfall_madurai       
chennai_coimbatore = rainfall_chennai & rainfall_coimbatore
madurai_coimbatore = rainfall_madurai & rainfall_coimbatore 
atleast_two = chennai_madurai | chennai_coimbatore | madurai_coimbatore
print(atleast_two)
6)
increased_chennai = {x + 10 for x in rainfall_chennai}
print(increased_chennai)