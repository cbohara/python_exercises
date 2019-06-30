import sys
import csv


def main(args):
	with open('data/original.csv', newline='') as csv_in:
		reader = csv.reader(csv_in, delimiter='|')
		with open('data/fixed.csv', 'w', newline='') as csv_out:
			writer = csv.writer(csv_out, delimiter=',')
			for row in reader:
				writer.writerow(row)


if __name__ == "__main__":
	main(sys.argv)
