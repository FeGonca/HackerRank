# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict

n = int(input())
ordered_dictionary = OrderedDict()

for i in range(n):
    item_name, net_price = map(str, input().rsplit(' ',1))
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + int(net_price)

a = '-'
print(a * 20)
for item_name, net_price in ordered_dictionary.items():
    print(item_name, net_price)
