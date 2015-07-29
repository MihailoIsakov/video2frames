#! /usr/bin/env python
__author__ = 'zieghailo'

import cv2


def video2frames(path, skip=1):
    video_object = cv2.VideoCapture(path)

    index = 0
    while True:
        success, frame = video_object.read()
        if success:
            if index % skip == 0:
                cv2.imwrite(path[:-4] + "_" + str(index) + ".jpg", frame)  # assumes that the extension is three letters long
        else:
            break

        index += 1


def main():
    import argparse
    parser = argparse.ArgumentParser("Enter the filename of a video")
    parser.add_argument('filename')
    parser.add_argument('--skip')
    args = parser.parse_args()

    if args.skip is None:
        args.skip = 1
    video2frames(args.filename, int(args.skip))

if __name__ == "__main__":
    main()

