from collections import Counter

def read_input_file(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
        left_list = []
        right_list = []
        for line in lines:
            numbers = line.split()
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))
        return left_list, right_list
    
def calculate_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    return total_distance
        
def similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    similarity = 0
    for number in left_list:
        similarity += number * right_counts[number]
    return similarity

if __name__ == "__main__":
    left_list, right_list = read_input_file("Text Files/Day1.txt")
    distance = calculate_distance(left_list, right_list)
    similarity = similarity_score(left_list, right_list)