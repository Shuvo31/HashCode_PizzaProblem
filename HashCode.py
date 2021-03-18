import os
import random
files = os.listdir('input_files/')
l = len(files)

for i in range(l):
    files[i] = files[i][:-3]


def solve(m, p2, p3, p4, ing, shuff):
    i, score = 0, 0

    random.shuffle(shuff)

    pp, ppp, pppp = [], [], []

    while i < m:

        if i + 2 <= m and p2 > 0:
            p2 -= 2
            pp.append([shuff[i], shuff[i + 1]])
            ss = len(set(ing[shuff[i]] + ing[shuff[i + 1]]))
            i += 2

        elif i + 3 <= m and p3 > 0:
            p3 -= 3
            ppp.append([shuff[i], shuff[i + 1], shuff[i + 2]])
            ss = len(set(ing[shuff[i]] + ing[shuff[i + 1]] + ing[shuff[i + 2]]))
            i += 3

        elif i + 4 <= m and p4 > 0:
            p4 -= 4
            pppp.append([shuff[i], shuff[i + 1], shuff[i + 2], shuff[i + 3]])
            ss = len(set(ing[shuff[i]] + ing[shuff[i + 1]] + ing[shuff[i + 2]] + ing[shuff[i + 3]]))
            i += 4


        else:
            break

        score += ss ** 2

    return len(pp), len(ppp), len(pppp), pp, ppp, pppp, score


for i in range(l):

    with open('input_files/' + files[i] + '.in', 'r') as f:

        content = f.readlines()
        ingredients = []
        m, p2, p3, p4 = [int(x) for x in content[0].split()]
        for j in range(1, m + 1):
            ingredient = content[j].split()[1:]
            ingredients.append((ingredient))

    bscore = 0
    btwo, bthree, bfour = [], [], []
    val = list(range(m))

    for _ in range(10000):
        q2, q3, q4, two, three, four, score = solve(m, 2 * p2, 3 * p3, 4 * p4, ingredients, val)

        if score > bscore:
            bscore, btwo, bthree, bfour = score, two, three, four

    with open('output_files/' + files[i] + '.out', 'w') as f:
        f.write(str(q2 + q3 + q4) + '\n')

        for ii in range(q2):
            f.write('2 ')
            for j in range(2):
                f.write(str(btwo[ii][j]) + ' ')
            f.write('\n')
        for ii in range(q3):
            f.write('3 ')
            for j in range(3):
                f.write(str(bthree[ii][j]) + ' ')
            f.write('\n')
        for ii in range(q4):
            f.write('4 ')
            for j in range(4):
                f.write(str(bfour[ii][j]) + ' ')
            f.write('\n')

    print("Done ", files[i], "\nScore :", bscore)

print("Done and Dusted")