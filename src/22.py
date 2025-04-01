import math
import sympy as sp

def calculate_area_rectangle(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
    """
    return length * width

def calculate_area_triangle(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.
    
    Parameters:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
        
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height

def main() -> None:
    # Example usage
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area_rectangle = calculate_area_rectangle(length, width)
    area_triangle = calculate_area_triangle(base=length, height=height)
    
    print(f"The area of the rectangle is {area_rectangle:.2f}")
    print(f"The area of the triangle is {area_triangle:.2f}")

if __name__ == "__main__":
    main()
