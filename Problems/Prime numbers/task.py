def is_prime_number(number: int):
    if number < 2:
        return False

    divisions = [number % divider != 0 for divider in range(2, number)]
    return all(divisions)


numbers = range(1001)
prime_numbers = [number for number in numbers if is_prime_number(number)]
# prime_numbers = [str(number) for number in prime_numbers]
# print(", ".join(prime_numbers))
