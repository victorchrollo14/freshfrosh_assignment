# Solution approach

1. split the string into a list at ','
2. iterate through each item, find the index of seperator which is ':'
3. Items before the seperator are ids and the ones after are keys values.
4. Strip off unnecessary characters from ids and keys.
5. From ids we remove double quotes("), then from state values we remove all characters expect digits.
6. Finally just append them into a list.
