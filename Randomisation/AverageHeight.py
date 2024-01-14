def convert_input_to_integers(input_string):
    """
    Convert a space-separated string of numbers to a list of integers.

    Parameters:
    - input_string (str): A space-separated string of numbers.

    Returns:
    - list of int: A list containing the converted integers.
    """
    return [int(height) for height in input_string.split()]

def calculate_average_height(heights):
    """
    Calculate the average height from a list of heights.

    Parameters:
    - heights (list of int): A list containing student heights.

    Returns:
    - int: The average height.
    """
    total_height = sum(heights)
    number_of_students = len(heights)
    avg_height = round(total_height / number_of_students) if number_of_students > 0 else 0
    return avg_height

def main():
    # Get student heights as input and convert them to integers
    input_heights = input("Enter student heights separated by spaces: ")
    student_heights = convert_input_to_integers(input_heights)

    # Calculate total height, number of students, and average height
    total_height = sum(student_heights)
    number_of_students = len(student_heights)
    avg_height = calculate_average_height(student_heights)

    # Display results
    print(f"Total height: {total_height}")
    print(f"Number of students: {number_of_students}")
    print(f"Average height: {avg_height}")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
