import data
import itertools
from collections import Counter

def parseChallengeString (input) -> dict:
    input_list = input.split(',')

    if not 5 == len(input_list):
        raise ValueError('Input does not have all 5 numbers needed, separated by comma!')

    parsed_input = {
        data.WHITE_SHIP: int(input_list[0]),
        data.RED_SHIP: int(input_list[1]),
        data.ISLAND: int(input_list[2]),
        data.CAVE: int(input_list[3]),
        data.BOAT: int(input_list[4])
    }

    if parsed_input[data.WHITE_SHIP] > data.MAX_WHITE_SHIPS:
        raise ValueError('WHITE_SHIPS count cannot be more than: ' + str(data.MAX_WHITE_SHIPS))

    if parsed_input[data.RED_SHIP] > data.MAX_RED_SHIPS:
        raise ValueError('RED_SHIPS count cannot be more than: ' + str(data.MAX_RED_SHIPS))

    if parsed_input[data.ISLAND] > data.MAX_ISLANDS:
        raise ValueError('ISLANDS count cannot be more than: ' + str(data.MAX_ISLANDS))

    if parsed_input[data.CAVE] > data.MAX_CAVES:
        raise ValueError('CAVES count cannot be more than: ' + str(data.MAX_CAVES))

    if parsed_input[data.BOAT] > data.MAX_BOATS:
        raise ValueError('BOATS count cannot be more than: ' + str(data.MAX_BOATS))

    return parsed_input

def rotateMultiDimensionalList(listToRotate) -> list:
    return [list(r) for r in zip(*listToRotate[::-1])]

def generateMasksVariationsBuckets() -> list:
    mask1_bucket = []
    mask2_bucket = []
    mask3_bucket = []
    mask4_bucket = []

    # Our mask 1 is a special case mask, which only gives 2 unique transpositions
    # We only rotate it once
    mask1_bucket.append(data.MASK1)
    mask1_bucket.append(rotateMultiDimensionalList(mask1_bucket[-1]))

    mask2_bucket.append(data.MASK2)
    for rotation in range(1, 4):
        mask2_bucket.append(rotateMultiDimensionalList(mask2_bucket[-1]))

    mask3_bucket.append(data.MASK3)
    for rotation in range(1, 4):
        mask3_bucket.append(rotateMultiDimensionalList(mask3_bucket[-1]))

    mask4_bucket.append(data.MASK4)
    for rotation in range(1, 4):
        mask4_bucket.append(rotateMultiDimensionalList(mask4_bucket[-1]))
            
    return [mask1_bucket, mask2_bucket, mask3_bucket, mask4_bucket]

def permuteLists(listToPermute) -> list:
    return list(itertools.permutations(listToPermute))

def productOfLists(listsToProduct) -> list:
    return list(itertools.product(*listsToProduct))

def attemptToSolve(challenge, masksCombination) -> bool:
    filtered_data = []

    for dataset_index, dataset in enumerate(data.DATA):
        for data_row_num, data_row in enumerate(dataset):
            for position, value in enumerate(data_row):
                if 0 == masksCombination[dataset_index][data_row_num][position] and not value is None:
                    filtered_data.append(value)
    
    game_elements_count = dict(Counter(filtered_data))
    filtered_challenge = {x:y for x, y in challenge.items() if y != 0}

    return filtered_challenge == game_elements_count

def drawSolution(solution, filled_symbol, empty_symbol) -> None:
    print('Solved by: ' + "\n")
    output = [[],[],[],[],[],[],[]]
    second_row_num_addition = 0

    for card_no, card in enumerate(solution):
        if card_no > 1:
            second_row_num_addition = 4
        for row_no, row in enumerate(card):
            for element in row:
                if 1 == element:
                    output[row_no + second_row_num_addition].append(filled_symbol)
                else:
                    output[row_no + second_row_num_addition].append(empty_symbol)
            if 0 == card_no % 2:
                output[row_no + second_row_num_addition].append('   ')

    for line in output:
        for char in line:
            print(char, end='')
        print()
    print()
