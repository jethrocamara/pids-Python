'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    13 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Express the parameters' case types.

    str(letter)
    int(shift)

    # Create a tuple of uppercase English letters.

    alphabet = tuple(map(chr, range(ord("A"), ord("Z") + 1)))

    # Write the statement specifying the functions for shift_letter.

    if letter == " ":
        return letter
    else:
        return alphabet[(ord(letter) - ord("A") + shift) % len(alphabet)]

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    18 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Express the parameters' case types.

    str(message)
    int(shift)
    
    # Create a tuple of the unicode numbers of the message.
    
    unicode = tuple(map(ord, tuple(message)))
    
    # Map the shifted unicode numbers of the message into their encrypted characters.
    
    encrypt = map(chr, [x + shift for x in unicode])
    
    # Concatenate the elements into a combined string of characters.
    
    c_encrypt = ''.join(encrypt)
    
    # Assign a separator for separating the characters.
    
    separator = chr(ord(" ") + shift)
    
    # Separate the characters per the separator.
    
    c_encrypt_s = c_encrypt.split(separator)
    
    # Write the statement specifying the function for caesar_cipher.
    
    return " ".join(c_encrypt_s) 

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    18 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Express the parameters' case types.
    
    str(letter)
    str(letter_shift)
    
    # Create a tuple of uppercase English letters.

    alphabet = tuple(map(chr, range(ord("A"), ord("Z") + 1)))

    # Write the statement specifying the functions for shift_by_letter.
    # Note: The (ord(letter) + ord(letter_shift) - 2 * ord("A")) % len(alphabet)-th item of alphabet is a simplified expression of (ord(letter) - ord("A") + ord(letter_shift) - ord("A")) % len(alphabet).

    if letter == " ":
        return letter
    else:
        return alphabet[(ord(letter) + ord(letter_shift) - 2 * ord("A")) % len(alphabet)]

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    23 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # Express the parameters' case types.

    str(message)
    str(key)

    # Ignore the spaces in the message parameter.

    message_n = message.split()
    j_message_n = ''.join(message_n)

    # Create tuples of the unicode numbers of the variables message (with spaces ignored) and key.

    message_t = tuple(ord(i) for i in j_message_n)
    key_t = tuple(ord(i) for i in key)

    # Create a tuple of uppercase English letters.

    alphabet = tuple(map(chr, range(ord("A"), ord("Z") + 1)))

    # Add the values of the elements of the inputs' tuples.

    message_key = tuple((sum(i) - 2 * ord("A")) % (len(alphabet)) for i in zip(message_t, key_t * len(message_t[0:len(message_t):len(key_t)])))

    # Map the values of message_key into their respective alphabet values.

    encrypted = list(alphabet[i] for i in message_key)
 
    # Write the statement specifying the function for vigenere_cipher.
   
    return ''.join(encrypted)

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    23 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Express the parameters' case types.

    str(message)
    int(shift)
   
    # Create lists of the characters of the message, as well in cases where additional underscores are needed.

    message_l = list(message)
    message_l_u = list(message) + list("_" for i in range(shift - (len(message) % shift)))
    
    # Create a string of message_l_u list

    ''.join(message_l_u)

    # Create lists of the index positions of the aforementioned lists.

    message_i = list(i for i, x in enumerate(message))
    message_i_u = list(i for i, x in enumerate(message_l_u))

    # Construct the algorithm shifting the messages into their encrypted positions.

    encrypted_i = [(i // shift) + (len(message) // shift) * (i % shift) for i in message_i]
    encrypted_i_u = [(i // shift) + ((len(message) + (shift - (len(message) % shift))) // shift) * (i % shift) for i in message_i_u]
    
    # Create a list of encrypted characters of the message.
    
    encrypted = [message_l[i] for i in encrypted_i]
    encrypted_u = [message_l_u[i] for i in encrypted_i_u]

    # Write the statement specifying the functions for scytale_cipher.

    if len(message) % shift == 0:
        return ''.join(encrypted)
    else:
        return ''.join(encrypted_u)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    25 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Express the parameters' case types.

    str(message)
    int(shift)
   
    # Create lists of the characters of the message.

    message_l = list(message)

    # Create lists of the index positions of the message.

    message_i = list(i for i, x in enumerate(message))

    # Construct the algorithm shifting the messages into their decrypted positions.

    decrypted_i = [((i * shift) % len(message)) + (i // (len(message) // shift)) for i in message_i]
    
    # Create a list of decrypted characters of the message.
    
    decrypted = [message_l[i] for i in decrypted_i]

    # Write the statement specifying the functions for scytale_decipher.

    return ''.join(decrypted)
