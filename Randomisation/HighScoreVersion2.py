def convert_input_to_integers(input_string):
    """
    Convert a space-separated string of numbers to a list of integers.

    Parameters:
    - input_string (str): A space-separated string of numbers.

    Returns:
    - list of int: A list containing the converted integers.
    """
    return [int(score) for score in input_string.split()]

def find_highest_score(scores):
    """
    Find the highest score from a list of scores.

    Parameters:
    - scores (list of int): A list containing student scores.

    Returns:
    - int: The highest score.
    """
    highest_score = max(scores) if scores else 0
    return highest_score

def main():
    # Get student scores as input and convert them to integers
    input_scores = input("Enter student scores separated by spaces: ")
    student_scores = convert_input_to_integers(input_scores)

    # Find the highest score
    highest_score = find_highest_score(student_scores)

    # Display the result
    print(f"Highest score is {highest_score}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
