def calculate_circle_properties(radius):
    # Calculate diameter
    diameter = 2 * radius

    # Calculate circumference (C = 2πr)
    circumference = 2 * 3.14159 * radius

    # Calculate area (A = πr^2)
    area = 3.14159 * radius ** 2

    # Format the results
    formatted_diameter = format(diameter, ".1f")
    formatted_circumference = format(circumference, ".2f")
    formatted_area = format(area, ".3f")

    # Display the results
    print(f"Radius: {radius}")
    print(f"Diameter: {formatted_diameter}")
    print(f"Circumference: {formatted_circumference}")
    print(f"Area: {formatted_area}")

# Example usage
user_radius = float(input("Enter the radius: "))
calculate_circle_properties(user_radius)

