import sys

def process_file(filename):
    longest_line = ""
    longest_line_num = 0
    total_length = 0
    num_lines = 0
    lines_dict = {}

    # Read and process the file
    with open(filename, 'r') as file:
        for line in file:
            if '|' in line:
                text, line_num = line.rsplit('|', 1)
                line_num = int(line_num.strip())
                lines_dict[line_num] = text.strip()

                #longest line
                if len(text) >= len(longest_line):
                    longest_line = text
                    longest_line_num = line_num

                #total length and line count for average
                total_length += len(text)
                num_lines += 1

    #average length, sort by line number, prepare output file
    average_length = round(total_length / num_lines)
    sorted_lines = [lines_dict[num] for num in sorted(lines_dict)]
    book_code = filename.split('.')[0]
    output_filename = f"{book_code}_book.txt"

    #output file
    with open(output_filename, 'w') as out_file:
        out_file.write(f"{book_code}\n")
        out_file.write(f"Longest line ({longest_line_num}): {longest_line}\n")
        out_file.write(f"Average length: {average_length}\n")
        for line in sorted_lines:
            out_file.write(f"{line}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python library.py <bookfile>")
        sys.exit(1)

    filename = sys.argv[1]
    process_file(filename)


main()
