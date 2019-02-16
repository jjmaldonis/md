from path import Path
import re


def log_to_steps(filename):
    filename = Path(filename)
    ext = filename.ext
    output_filename = filename[:-len(ext)] + '.steps'
    print(output_filename)

    with open(filename) as f:
        line = ""
        while not line.startswith("Step"):
            line = f.readline().strip()
        header = line.split()
        regex = r"^( *-*\d+\.*\d* *){NUMBER}\n$"
        regex = regex.replace("NUMBER", str(len(header)))
        regex = re.compile(regex)

        with open(output_filename, 'w') as of:
            of.write(" ".join(header) + "\n")

            for line in f:
                if re.match(regex, line) is not None:
                    of.write(line)


if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    log_to_steps(filename)
