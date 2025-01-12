def brute_force_attack(target_password, charset, max_length):
    def generate_combinations():
        combinations = [""]
        for _ in range(max_length):
            new_combinations = []
            for comb in combinations:
                for char in charset:
                    new_combinations.append(comb + char)
                    yield comb + char
            combinations = new_combinations

    for attempt in generate_combinations():
        if attempt == target_password:
            return attempt

# Example usage:
charset = "abc123"
print(brute_force_attack("b2", charset, 2))

