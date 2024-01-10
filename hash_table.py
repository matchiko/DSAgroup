class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return ((1731 * key + 520123) % 524287) % self.size

    def insert(self, key, word):
        index = self.hash_function_2(key)  
        self.table[index].insert(0, word)

    def delete(self, word):
        for slot in self.table:
            if word in slot:
                slot.remove(word)
                break

    def print_table(self):
        for i, slot in enumerate(self.table):
            words = ' '.join(slot)
            print(f"{i}: {words}")

def process_commands(hash_table):
    num_commands = int(input("Enter the number of commands: "))
    
    commands = []
    for _ in range(num_commands):
        command = input("Enter a command: ")
        commands.append(command)

    for command in commands:
        if command.startswith("del "):
            word_to_delete = command[4:]
            hash_table.delete(word_to_delete)
        else:
            key = sum(ord(char) for char in command)
            hash_table.insert(key, command)

if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    process_commands(hash_table)
    hash_table.print_table()