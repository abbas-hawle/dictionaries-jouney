def merge_dictionaries(dict1, dict2):
    """Combines dictionaries. If duplicate keys, dict2 wins."""
    merged_dict = dict1 # Forgot to copy, might modify original!
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "d": 4}
print(merge_dictionaries(dict1, dict2))

def count_word_frequency(sentence):
    """Counts how many times words appear."""
    words = sentence.lower().split()
    counts = {}
    for word in words:
        counts[word] += 1 # Initialize before incrementing! Will cause error on first encounter
    return counts

sentence = "apple orange banana apple orange apple"
#print(count_word_frequency(sentence)) # Will cause an error

company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    }
}

print(company_employees)
company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}
print(company_employees)

def count_total_employees(company_dict):
    """Counts all employees."""
    total = 0
    for dept in company_dict.values():
        total += len(dept)
    return total

print(f"Total employees: {count_total_employees(company_employees)}")

def invert_dictionary(input_dict):
    """Swaps keys and values."""
    inverted = {}
    for k, v in input_dict.items():
        if v in inverted:
          inverted[v].append(k)
        else :
          inverted[v] = [k]
    return inverted

example = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
print(invert_dictionary(example))