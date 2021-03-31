import pyautogui as keyboard
import time
import os


def main():
    text_file = os.path.join('..', 'file', 'to_type.txt')

    time.sleep(3)

    total = len(open(text_file, 'r').readlines())

    with open(text_file, 'r') as f:
        i = 0
        for line in f.readlines():
            i += 1
            keyboard.write(line, interval=0.04)
            print('Line %s of %s' % (i, total), end='\r')


if __name__ == '__main__':
    main()
