from itertools import product

def brute_force_attack(target_password, charset, max_length):
    for length in range(1, max_length + 1):
        for combination in product(charset, repeat=length):
            attempt = ''.join(combination)
            if attempt == target_password:
                return attempt

# Example usage:
charset = "abc123"
print(brute_force_attack("a3", charset, 2))

