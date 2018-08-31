"""
Relatively Efficient Sort
----------------------------------
A sorting algorithm, of sorts.
----------------------------------
Copyright (c) 2018 Christopher Sacchi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def thesort(x):
    c_x = x
    l_x = len(x)
    odd = (l_x % 2)
    checked = i = amt = tmp = 0
    
    if odd:
        c_x.append(-1020202)
    while checked < 2:
        if i == (l_x - 1):
            if c_x[0] > c_x[i]:
                tmp = c_x[0]
                c_x[0] = c_x[i]
                c_x[i] = tmp
                checked = 0
            elif c_x[0] < c_x[i] and amt == i:
                checked += 1
            i = amt = 0
        else:
            if c_x[i] < c_x[i + 1] or c_x[i] == c_x[i + 1]:
                amt += 1
            else:
                tmp = c_x[i]
                c_x[i] = c_x[i + 1]
                c_x[i + 1] = tmp
                checked = amt = 0
            i += 1
                
    if odd:
        del c_x[c_x.index(-1020202)]
    
    return c_x
