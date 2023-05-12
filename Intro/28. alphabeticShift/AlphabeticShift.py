def solution(inputString):
    dict1 = {'a':'b',
           'b':'c',
           'c':'d',
           'd':'e',
           'e':'f',
           'f':'g',
           'g':'h',
           'h':'i',
           'i':'j',
           'j':'k',
           'k':'l',
           'l':'m',
           'm':'n',
           'n':'o',
           'o' :'p',
           'p':'q',
           'q':'r',
           'r':'s',
           's':'t',
           't':'u',
           'u':'v',
           'v':'w',
           'w':'x',
           'x':'y',
           'y':'z',
           'z':'a'}
    str1 = ""
    for i in range(len(inputString)):
        str1 = str1 + dict1.get(inputString[i])
    return str1
solution("abcd")    
