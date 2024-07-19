def wave(people):
    result = []
    
    for i in range(len(people)):
        if people[i].isalpha() == True:
            upper_case = people[i].upper()
            new_wave = people[:i] + upper_case + people[i+1:]
            result.append(new_wave)
    return result

print(wave(""))