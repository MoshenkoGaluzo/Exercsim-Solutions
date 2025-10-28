flip_dict = {"{":"}", 
             "(":")", 
             "[":"]"}

def is_paired(input_string):
    index = 0

    if input_string == "":
        return True
    
    input_string = "".join([char for char in input_string if char in "([{}])"])

    while len(input_string) != 0:

        if not input_string[index] in flip_dict:
            return False
        
        if len(input_string) <= index + 1:
            return False
        
        if input_string[index + 1] == flip_dict[input_string[index]]:
            input_string = input_string[:index] + input_string[index+2:]
            if index > 0:
                index -= 1
        
        elif input_string[index + 1] in flip_dict:
            index += 1
        else:
            return False
        pass
    return True