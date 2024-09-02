import matplotlib.pyplot as plt
import re


str='''
<contour>
        <pt x="29" y="431" on="1"/>
        <pt x="29" y="491" on="1"/>
        <pt x="354" y="491" on="1"/>
        <pt x="354" y="442" on="1"/>
        <pt x="330" y="417" on="0"/>
        <pt x="283" y="349" on="0"/>
        <pt x="235" y="265" on="0"/>
        <pt x="200" y="179" on="0"/>
        <pt x="186" y="134" on="1"/>
        <pt x="169" y="71" on="0"/>
        <pt x="163" y="-4" on="1"/>
        <pt x="99" y="-4" on="1"/>
        <pt x="100" y="25" on="0"/>
        <pt x="112" y="97" on="0"/>
        <pt x="123" y="139" on="1"/>
        <pt x="145" y="223" on="0"/>
        <pt x="186" y="300" on="1"/>
        <pt x="207" y="340" on="0"/>
        <pt x="252" y="405" on="0"/>
        <pt x="275" y="431" on="1"/>
      </contour>
'''


x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str)]
y = [int(i) for i in re.findall(r'y="(.*?)" on=', str)]

print(x)
print(y)


plt.plot(x, y)
plt.show()

# e3d
# uniE3DF 7
# uniE3EC 2
# uniEA60 6
# uniEA6F 0
# uniEB19 9
# uniED30 1
# uniEF28 8
# uniF11C 3
# uniF3E8 5
# uniF7D2 4

