import xml.etree.ElementTree as Et


my_tree = Et.parse('x1.xml')
my_root = my_tree.getroot()
# print(my_root)

# print(my_root.tag)
# print(my_root.attrib)
# print(my_root[0].tag)

# for x in my_root:
#     print(x.tag, x.attrib)

# for x in my_root.findall('food'):
#     item = x.find('item').text
#     price = x.find('price').text
#     print(f"{item}:", price)

for price in my_root.iter('price'):
    old_price = float(price.text.strip('$'))
    price.text = '$' + str(old_price + 1)
    price.set('new_price', 'yes')

Et.SubElement(my_root[0], "tasty")
for temp in my_root.iter('tasty'):
    temp.text = str('Yes')

print(my_root[2][0].attrib.pop('name'))
print(my_root.remove((my_root[2])))
my_tree.write('modified.xml')
