"""
    Authors: Jess Bunnag, Tiffany Lin, Anna Zuo
"""
import cv2
import os
import sys
import random

def main(mood, settings):
    vid_name = mood+'_'+str(settings[0])+'_'+str(settings[1])
    path = os.path.join('videos', mood, vid_name+'.mp4')
    video = cv2.VideoCapture(path)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)
    frames_list = list(range(total_frames))
    frames_list = random.sample(frames_list, round(total_frames/10))

    # creating a folder named data
    dir_path = os.path.join('videos', mood, vid_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # frame
    currentframe = 0
    while(True):
        # reading from frame
        ret,frame = video.read()
    
        if ret:
            if currentframe in frames_list:
                # if video is still left continue creating images
                name = os.path.join('videos', mood, vid_name, vid_name+'_frame'+str(currentframe)+'.jpg')
                print ('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Create a list of file paths in the directory
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    # Write the file paths to a text file
    file_name = vid_name + '.txt'
    with open(file_name, 'w') as f:
        for file_path in file_paths:
            f.write(file_path + '\n')

if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print('Usage: python script_name.py mood settings')
    else:
        mood = sys.argv[1]
        settings = [int(x) for x in sys.argv[2].split(',')]
        main(mood, settings)