class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size
    
    def hash_function_3(self, key):
        # Using Python's default hash function
        return hash(key) % self.size

    def insert(self, key, word, cmd):
        if cmd is 1:
            index = self.hash_function_1(key)
        if cmd is 2:
            index = self.hash_function_2(key)
        if cmd is 3:
            index = self.hash_function_3(key)  
        self.table[index].insert(0, word)

    def delete(self, word):
        for slot in self.table:
            if word in slot:
                slot.remove(word)
                break

    def print_table(self):
        my_result = []
        for i, slot in enumerate(self.table):
            words = ' '.join(slot)
            # print(f"{i}: {words}")
            my_result.append(f"{i}: {words}")
        return my_result

def process_commands(numbers, command_list, type_command):
    hash_table = HashTable(32)
    commands = []
    for _ in range(numbers):
        commands.append(command_list)

    for command in commands:
        if command.startswith("del "):
            word_to_delete = command[4:]
            hash_table.delete(word_to_delete)
        else:
            key = sum(ord(char) for char in command)
            hash_table.insert(key, command, type_command)
    
    result = hash_table.print_table()
    return result