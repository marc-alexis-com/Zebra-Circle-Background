import os
from PIL import Image, ImageDraw
import math

def get_color_input(prompt):
    """
    Prompt the user to enter a color in hexadecimal or RGB format.
    """
    while True:
        color = input(prompt).strip()
        if color.startswith('#'):
            # Convert hexadecimal to RGB
            hex_color = color.lstrip('#')
            if len(hex_color) == 6:
                try:
                    r = int(hex_color[0:2], 16)
                    g = int(hex_color[2:4], 16)
                    b = int(hex_color[4:6], 16)
                    return (r, g, b)
                except ValueError:
                    pass
        else:
            # Try to parse as RGB
            try:
                parts = color.split(',')
                if len(parts) != 3:
                    raise ValueError
                r, g, b = [int(part.strip()) for part in parts]
                if all(0 <= val <= 255 for val in (r, g, b)):
                    return (r, g, b)
            except ValueError:
                pass
        print("Invalid input. Please enter a color in hexadecimal (e.g., #FF5733) or RGB format (e.g., 255,87,51).")

def create_radial_stripes(size, colors, distance):
    """
    Create an image with radial stripes of specified colors and distance.

    :param size: Tuple (width, height) of the image.
    :param colors: List of colors (R, G, B).
    :param distance: Angle in degrees between stripes.
    :return: Image with radial stripes.
    """
    width, height = size
    center_x = width / 2
    center_y = height / 2

    # Create a new image with transparency
    stripes = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(stripes)

    total_angle = 360
    current_angle = 0
    color_index = 0
    num_colors = len(colors)

    while current_angle < total_angle:
        end_angle = current_angle + distance
        if end_angle > total_angle:
            end_angle = total_angle

        # Draw a pie slice covering the entire image to ensure full coverage
        draw.pieslice(
            [0, 0, width, height],
            start=current_angle,
            end=end_angle,
            fill=colors[color_index % num_colors]
        )

        current_angle += distance
        color_index += 1

    return stripes

def add_radial_stripes_background(input_image_path, output_image_path, colors, distance):
    """
    Add a radial stripes background to a transparent PNG image.

    :param input_image_path: Path to the input image.
    :param output_image_path: Name of the output image.
    :param colors: List of colors (R, G, B).
    :param distance: Angle in degrees between stripes.
    """
    try:
        image = Image.open(input_image_path).convert("RGBA")
    except IOError:
        print(f"Cannot open image {input_image_path}.")
        return

    width, height = image.size

    if width != height:
        print("The image must be square.")
        return

    # Create radial stripes
    stripes = create_radial_stripes((width, height), colors, distance)

    # Combine stripes with the original image
    final_image = Image.alpha_composite(stripes, image)

    # Set output folder to current directory
    output_folder = os.getcwd()

    # Save the final image
    output_path = os.path.join(output_folder, output_image_path)
    final_image.save(output_path, format='PNG')
    print(f"Image saved to {output_path}.")

def main_menu():
    print("=== Radial Stripes Background Generator ===")

    # Input image path
    input_image = input("Enter the path to your square transparent PNG image: ").strip()
    if not os.path.isfile(input_image):
        print("The specified file does not exist.")
        return

    # Output image name
    output_image = input("Enter the name for the output image (e.g., final_image.png): ").strip()
    if not output_image.lower().endswith('.png'):
        output_image += '.png'

    # Choose stripe type
    print("\nChoose the type of stripes:")
    print("1. Multicolor Stripes")
    print("2. Zebra Stripes (2 colors)")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if choice == '1':
        # Multicolor Stripes
        while True:
            try:
                num_colors = int(input("Enter the number of colors (minimum 1): ").strip())
                if num_colors >= 1:
                    break
                else:
                    print("The number of colors must be at least 1.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        colors = []
        for i in range(num_colors):
            color = get_color_input(f"Enter color {i+1} in hexadecimal (e.g., #FF5733) or RGB (e.g., 255,87,51): ")
            colors.append(color)
    else:
        # Zebra Stripes with 2 colors
        print("\n=== Zebra Stripes Configuration ===")
        color1 = get_color_input("Enter the first color in hexadecimal (e.g., #FF5733) or RGB (e.g., 255,87,51): ")
        color2 = get_color_input("Enter the second color in hexadecimal (e.g., #33C1FF) or RGB (e.g., 51,193,255): ")
        colors = [color1, color2]

    # Distance between stripes
    while True:
        try:
            distance = float(input("Enter the distance between stripes in degrees (e.g., 10): ").strip())
            if 0 < distance <= 360:
                break
            else:
                print("Distance must be a number between 0 and 360.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Summary of parameters
    print("\n=== Summary of Parameters ===")
    print(f"Input Image: {input_image}")
    print(f"Output Image: {output_image}")
    print(f"Stripe Type: {'Multicolor Stripes' if choice == '1' else 'Zebra Stripes (2 colors)'}")
    print(f"Colors: {', '.join([f'#{c[0]:02X}{c[1]:02X}{c[2]:02X}' for c in colors])}")
    print(f"Distance between stripes: {distance} degrees")

    confirm = input("Do you want to proceed? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Operation cancelled.")
        return

    # Generate the final image
    add_radial_stripes_background(
        input_image_path=input_image,
        output_image_path=output_image,
        colors=colors,
        distance=distance
    )

if __name__ == "__main__":
    main_menu()