"""Calculate the largest prime factor of a given integer.
   
Parameters:
    number (int): The integer for which to find the largest prime factor. 

Returns:
    int: The largest prime factor of the given integer number.

Raises:
    ValueError: If number is less than or equal to 1.

Example:
    >>> largest_prime_factor(13195)
    29
"""

number = int(input("Enter the number: "))
INDEX = 1
if number <0:
    raise ValueError("Number must be positive.")
while INDEX <= number:
    if number%INDEX == 0:
        IS_PRIME = True
        VALUE = 2
        while VALUE < INDEX:
            if INDEX%VALUE == 0:
                IS_PRIME = False
                break
            VALUE += 1
        if IS_PRIME and INDEX > 1:
            print(INDEX)
            GREAT_PRIME_FACTOR = INDEX
    INDEX += 1

if GREAT_PRIME_FACTOR is not None:
    print(f"Greatest prime factor of {number} is {GREAT_PRIME_FACTOR}")
else:
    print("No prime factor is found")
