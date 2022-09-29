#entregar escrito em inglês um numero de 0 a 100

num1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

num2=['20-twenty', '30-thirty', '40-forty', '50-fifty', '60-sixty', '70-seventy', '80-eighty', '90-ninety']

y = input('digite um  numero: ')
def name_that_number(y):
    if int(y)<=19:
        print(num1[int(y)])
    else:
        x=0
        while x<9: 
            for i in num2[x]:
                if y[0]==i:
                    one = num2[x]
                    two = one[3:8]
                    tree = num1[int(y[1])]
                    print(f'{two} {tree}')
                    x=9
            x+=1
name_that_number(y)
   
