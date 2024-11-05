# Zebra-Circle-Background

A Python script that adds a radial striped background to a transparent PNG image. The script allows you to create either multicolored stripes or zebra stripes with two colors, with a configurable distance between each stripe. It is ideal for customizing your images with dynamic and attractive visual effects.

![showcase](https://github.com/user-attachments/assets/fe1e50f0-843d-4ab1-9625-1eb648a8cf12)


## Features

- **Customizable Radial Stripes**: Choose between multicolored stripes or zebra stripes with two colors.
- **Color Selection**: Enter colors in hexadecimal or RGB format.
- **Configurable Distance**: Define the angle in degrees between each stripe to control the density of the stripes.
- **Compatibility**: Works with square PNG transparent images (width = height).
- **Interactive Interface**: User-friendly command-line interface for easy configuration.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. You can download it [here](https://www.python.org/downloads/).
- **Pillow**: A Python library for image processing.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/marc-alexis-com/Zebra-Circle-Background.git
   cd Zebra-Circle-Background
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install Pillow
   ```

## Usage

1. **Prepare Your Image**

   - Ensure your input image is a transparent PNG and square (width = height).

2. **Run the Script**

   ```bash
   python zebra-circle-background.py
   ```

3. **Follow the On-Screen Instructions**

   - **Input Image Path**: Enter the path to your transparent PNG image.
   - **Output Image Name**: Specify the name for the output file (e.g., `final_image.png`). `.png` will be appended if not provided.
   - **Stripe Type**:
     - `1` for multicolored stripes.
     - `2` for zebra stripes (two colors).
   - **Number of Colors** (if multicolored): Enter the desired number of colors.
   - **Color Selection**: Enter colors in hexadecimal (e.g., `#FF5733`) or RGB (e.g., `255,87,51`) format.
   - **Distance Between Stripes**: Define the angle in degrees between each stripe (e.g., `10`).

4. **Confirm Parameters**

   - Review the summary of your settings and confirm to generate the final image.

5. **Result**

   - The generated image will be saved in the current directory with the specified name.

## Other examples

![examples](https://github.com/user-attachments/assets/71f9bb13-eda9-4c92-bcc5-e9dbc4ad0da2)

## License

This project is licensed under the [MIT License](LICENSE). jk, no license. Enjoy
