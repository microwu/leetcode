# 9 keyboard
def nine_keyboard(string):
    solution = []
    pre = '#'
    offset = 0
    keyboard = [[' '],[',','.','!'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    for index,char in enumerate(string):
        if char == '0':
            if pre != '#':
                solution.append(keyboard[int(pre)][offset])
            solution.append('_')
            pre = '#'
            offset = 0
            continue
        # print("char:%c pre:%c offset:%d"%(char,pre,offset))
        if index == len(string)-1:
            if index == 1:
                solution.append(keyboard[int(char)][0])
            elif char == pre:
                offset+=1
                if pre in ['1','2','3','4','5','6','8']:
                    offset = offset%3
                else:
                    offset = offset%4
                solution.append(keyboard[int(pre)][offset])
            else:
                solution.append(keyboard[int(char)][0])
        if char != '#':
            if pre == '#':
                pre = char
                offset = 0
            elif char != pre:
                solution.append(keyboard[int(pre)][offset])
                pre = char
                offset = 0
            else:
                offset+=1
            if pre in ['1','2','3','4','5','6','8']:
                offset = offset%3
            else:
                offset = offset%4
        else:
            if pre != '#':
                solution.append(keyboard[int(pre)][offset])
            offset = 0
            pre = '#'
    solutionString = ''
    for char in solution:
        solutionString+=char
    return solutionString


def main():
    # for index in range(0,100):
        # myinput = input()
        # myinput = 1
        # print(myinput)
    print(nine_keyboard('99999011020'))

if __name__ == "__main__":
    main()
