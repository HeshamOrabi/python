    # web services (xml) (json)

    # xml

import xml.etree.ElementTree as ET
    
data = '''
<person>
    <name>Hesham</name>
    <phone type="intl">+20111111111</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)

print('\nName:', tree.find('name').text) # get back the text within name tag
print('Attr:', tree.find('email').get('hide')) # get back the Attr with in email tag

print('\n------------------------------\n')

    # list of data

inputStr = '''
<live>
    <people>
        <person x="2">
            <name>Hesham</name>
            <phone type="intl">+20111111111</phone>
            <id>01</id>
        </person>
        <person x="4">
            <name>Ali</name>
            <phone type="intl">+20222222222</phone>
            <id>02</id>
        </person>
    </people>
</live>'''

live = ET.fromstring(inputStr)
lst = live.findall('people/person')
print('User count:', len(lst))

for thing in lst:
    print('Name:', thing.find('name').text)
    print('Id:', thing.find('id').text)  
    print('Attr: ', thing.get('x'))

print('\n------------------------------\n')
