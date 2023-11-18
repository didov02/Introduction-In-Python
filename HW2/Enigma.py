def plugboard(plugboard_str, plugboard_list):
    conv = ''
    for symbol in plugboard_str:
        for curr_set in plugboard_list:
            if symbol in curr_set:
                conv += (curr_set - {symbol}).pop()
                break
        else:
            conv += symbol

    return conv


def rotor(rotor_str, rotor_dict):
    conv = ''
    for symbol in rotor_str:
        conv += rotor_dict.get(symbol, symbol)

    return conv


def enigma_encrypt(plugboard_position, rotor_position):

    def encrypt_decorator(encrypt_func):

        def encrypt(encrypt_str):
            new_str = plugboard(encrypt_str, plugboard_position)
            return encrypt_func(rotor(new_str, rotor_position))

        return encrypt
        
    return encrypt_decorator


def enigma_decrypt(plugboard_position, rotor_position):

    def decrypt_decorator(decrypt_func):

        def decrypt(decrypt_str):
            new_dict = {rotor_position[element]: element for element in rotor_position}
            
            new_str = rotor(decrypt_str, new_dict)
            return decrypt_func(plugboard(new_str, plugboard_position))
        
        return decrypt
    
    return decrypt_decorator