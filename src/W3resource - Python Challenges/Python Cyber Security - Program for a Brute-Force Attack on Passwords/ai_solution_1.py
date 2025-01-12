from itertools import product

def brute_force_attack(target_password, charset, max_length):
    def recursive_attempt(current_password):
        if current_password == target_password:
            return current_password
        for char in charset:
            attempt = current_password + char
            if len(attempt) <= max_length:
                result = recursive_attempt(attempt)
                if result:
                    return result
        return None

    return recursive_attempt("")

# Example usage:
charset = "abc123"
print(brute_force_attack("a3", charset, 2))

