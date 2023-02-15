def backpack(filename):

    with open(filename, "r") as list:
        input = list.read()
        array = input.splitlines()
    trios = [array[i:i+3] for i in range(0, len(array), 3)]
    
    total_score = 0
    
    for trio in trios:
        print(trio)
        common_letter = None
        
        for letter in trio[0]:
            found = True
            
            for item in trio[1:]:
                if letter not in item:
                    found = False
                    break
            
            if found:
                common_letter = letter
                print(letter)
                break
        
        if common_letter:
            if 'a' <= common_letter <= 'z':
                total_score += ord(common_letter) - ord('a') + 1
            elif 'A' <= common_letter <= 'Z':
                total_score += ord(common_letter) - ord('A') + 27
    
    return total_score

filename = "01-advent-of-code-challenge/03/sample.in"
print(backpack(filename))