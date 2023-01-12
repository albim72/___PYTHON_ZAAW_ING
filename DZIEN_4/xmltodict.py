import xmltodict

xml_data = """
<student>
    <id>F34354</id>
    <name>
        <firstname>Olga</firstname>
        <lastname>Knap</lastname>
    </name>
    <email>knap@uczelnia.pl</email>
    <class>inforamtyka</class>
    <subjects>
        <sub1>Sieci neuronowe</sub1>
        <sub2>Programowanie obiektowe</sub2>
    </subjects>
</student>
"""

my_dict = xmltodict.parse(xml_data)
print(my_dict)

print(my_dict['student']['id'])
print(my_dict['student']['name']['firstname'])
print(my_dict['student']['subjects']['sub1'])
