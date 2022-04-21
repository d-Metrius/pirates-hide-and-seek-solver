import logic

FILLED_MASK_SYMBOL = '▒'
EMPTY_MASK_SYMBOL = ' '

print("\n" + 'SmartGames "Pirates: Hide and Seek" game solver by Dmitry Baranov')
print('made as an entry "Hello, World!" application in Python')
print('===')
print('Format of the input: WHITE_SHIPS,RED_SHIPS,ISLANDS,CAVES,BOATS integer numbers')
print('For example: 2,1,2,0,0' + "\n")

try:
    challenge_string = input('Please enter a challenge: ')
    challenge = logic.parseChallengeString(challenge_string)
    print("\n" + 'Challenge: ' + str(challenge) + "\n")
    
    masks_variations_buckets = logic.generateMasksVariationsBuckets()
    buckets_permutations = logic.permuteLists(masks_variations_buckets)
    solved = False

    for permutation in buckets_permutations:
        for product in logic.productOfLists(permutation):
            if logic.attemptToSolve(challenge, product):
                if True == solved:
                    print('Also ', end='')
                logic.drawSolution(product, FILLED_MASK_SYMBOL, EMPTY_MASK_SYMBOL)
                solved = True

    if False == solved:
        print('Challenge not solvable...' + "\n")
except Exception as e:
    print(str(e) + "\n")
