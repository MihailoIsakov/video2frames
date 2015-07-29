#! /usr/bin/env python
__author__ = 'zieghailo'

import cv2


def video2frames(path):
    video_object = cv2.VideoCapture(path)

    index = 1
    while True:
        success,frame = video_object.read()
        if success:
            # assumes that the extension is three letters long
            cv2.imwrite(path[:-4] + "_" + str(index) + ".jpg", frame)
            index += 1
        else:
            break


def main():
    import argparse
    parser = argparse.ArgumentParser("Enter the filename of a video")
    parser.add_argument('filename')
    args = parser.parse_args()

    video2frames(args.filename)

if __name__ == "__main__":
    main()

