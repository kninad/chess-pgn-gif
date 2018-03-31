import os
import shutil
import argparse

import chess
import chess.svg
import chess.pgn
import imageio

#from IPython.display import SVG

from text_to_img import text_image  # custom script


TMP_DIR = './.temp/'

def create_txt_files(pgn_file):
    pgn = open(pgn_file)
    first_game = chess.pgn.read_game(pgn)
    
    # create a temp directory for txt files. Delete it later.
    os.mkdir(TMP_DIR)
    board = first_game.board()
    # starting with 10 to avoid problems with 1 and 10 while sorting file names
    counter = 10    
    
    for move in first_game.main_line():
        fname = TMP_DIR + str(counter) + '_file.txt'    
        with open(fname, 'w') as f:
            print(board, file=f)
        board.push(move)
        counter += 1
    
    # text files written to temp dir


def create_img_files():
    files = os.listdir(TMP_DIR)
    os.mkdir(TMP_DIR + 'imgs/') # temp folder for images
    
    for f in files:
        image = text_image('./.temp/' + f) 
        #image.show()
        imgfile = str(f) + '_img.png'
        image.save('./.temp/imgs/' + imgfile)
    
    # image files written to temp dir


def create_gif(gif_name, gif_durn):
    imgfolder = TMP_DIR + 'imgs/'
    fnames = os.listdir(imgfolder)
    images=[]
    fnames.sort()  # So that images for moves are in order    
    for f in fnames:
        images.append(imageio.imread(imgfolder + f))    
    
    imageio.mimsave(gif_name, images, duration=gif_durn) # Save the list of images as a gif
    shutil.rmtree(TMP_DIR) # Remove the temp txt and png files.
#


if __name__ == '__main__':
    
    ap = argparse.ArgumentParser(description = 'Input arguments')
    
    ap.add_argument("-d", "--duration", required=True,
        help="Time delay between frames of gif")
    ap.add_argument("-i", "--input", required=True,
        help="Input PGN file")
    ap.add_argument("-o", "--output", required=True,
        help="Output GIF file")
    
    args = vars(ap.parse_args())
    
    pgn_file = args["input"]
    gif_name = args["output"]
    durn = args["duration"] # time for each frame in gif

    print("Creating temp text files \n")
    create_txt_files(pgn_file)
    
    print("Creating temp img files \n")
    create_img_files()
    
    print("Creating gif file \n")
    create_gif(gif_name, durn)
    
