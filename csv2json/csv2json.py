import argparse
import csv
import json


class MakeJson:

    def __init__(self, input_file, out_file):
        self.input_file = input_file
        self.out_file = out_file

    def open_with_utf8(self, filename):
        is_with_bom = self.is_utf8_file_with_bom(filename)
        encoding = 'utf-8-sig' if is_with_bom else 'utf-8'
        return encoding

    def is_utf8_file_with_bom(self, filename):
        line_first = open(filename, encoding='utf-8').readline()
        return (line_first[0] == '\ufeff')

    def main(self):
        in_file = self.input_file
        out_file = self.out_file
        enc = self.open_with_utf8(in_file)

        with open(in_file, encoding=enc) as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(rows, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("-o", "--out_file", default="sample.json")
    args = parser.parse_args()

    obj = MakeJson(args.input_file, args.out_file)
    obj.main()
