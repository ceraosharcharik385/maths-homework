def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

def main():
    print("Enter the length and width of the rectangle:")
    length = float(input())
    width = float(input())
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")

if __name__ == "__main__":
    main()
