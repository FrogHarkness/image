# invert_pdf.py
import sys
from invert import invert_color

def main():
    if len(sys.argv) != 2:
        print("Usage: python invert_pdf.py <input_pdf_path>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    invert_color(input_pdf)
    print("Inverted PDF saved as output.pdf")

if __name__ == "__main__":
    main()