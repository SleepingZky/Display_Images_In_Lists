import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_lists','-i',help='the file lists need to be converted')

    args = parser.parse_args()

    file_path = args.input_lists

    if os.path.exists(file_path):
        img_list = [i.rstrip() for i in open(file_path).readlines()]

        file_name = 'img_path.xml'

        target_file = open(file_name,'w')

        head = '<?xml version="1.0" encoding="UTF-8" ?>'
        target_file.write(head+'\n')
        target_file.write('<image>\n')

        for i in img_list:
            content = '<photo> '
            content += i
            content += ' </photo>\n'

            target_file.write(content)
        target_file.write('</image>')

        target_file.close()
    


