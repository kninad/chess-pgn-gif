import os
import sys
import shutil
import argparse

import chess
import chess.svg
import chess.pgn
import imageio

from text_to_img import text_image

TMP_DIR = './.temp/'

def create_txt_files(pgn_file: str):
    ''' Creates a bunch of text files corresponding to every move in the game
    Input:
        pgn_file: path to the .pgn file for the chess game
    '''
    with open(pgn_file, 'r') as pgn:
        first_game = chess.pgn.read_game(pgn)
    # create a temp directory for txt files. Delete it later.
    os.mkdir(TMP_DIR)
    board = first_game.board()
    # starting with 10 to avoid problems with 1 and 10 while sorting file names
    counter = 10    
    for move in first_game.mainline_moves():
        fname = os.path.join(TMP_DIR, f'{counter}_file.txt') 
        with open(fname, 'w') as f:
            print(board, file=f)
        board.push(move)
        counter += 1


def create_img_files():
    files = os.listdir(TMP_DIR)
    tmp_img_dir = os.path.join(TMP_DIR, 'imgs')
    os.mkdir(tmp_img_dir) # temp folder for images
    for f in files:
        image = text_image(os.path.join(TMP_DIR, f)) 
        imgfile = f'{f}_img.png'
        image.save(os.path.join(tmp_img_dir, imgfile))


def create_gif(gif_name: str, gif_duration: int):
    ''' Reads the temp image files created and glues together a gif file. Also cleans up
    the tmp files.

    Input:
        gif_name: output gif file path
        gif_duration: how many seconds should each frame last?
    '''
    imgfolder = os.path.join(TMP_DIR, 'imgs')
    fnames = os.listdir(imgfolder)
    images=[]
    fnames.sort()  # So that images for moves are in order    
    for f in fnames:
        images.append(imageio.imread(os.path.join(imgfolder, f)))    
    imageio.mimsave(gif_name, images, duration=gif_duration) # Save the list of images as a gif
    shutil.rmtree(TMP_DIR) # Remove the temp txt and png files.

def make_args():
    ap = argparse.ArgumentParser(
        prog = 'chess_gif',
        description = 'Convert a PGN file for a chess game to a gif showing the moves made.',
        epilog='Not at all professional code, use at your own risk!')
    
    ap.add_argument("-d", "--duration", required=True,
        help="Time delay between frames of gif")
    ap.add_argument("-i", "--input", required=True,
        help="Input PGN file")
    ap.add_argument("-o", "--output", required=True,
        help="Output GIF file")
    args = ap.parse_args()
    return args

def main(args):
    pgn_file = args.input
    gif_file = args.output
    frame_duration = args.duration # time for each frame in gif

    if os.path.exists(TMP_DIR):
        print(f"[ERROR] Delete the temp dir ({TMP_DIR}) and retry!")
        sys.exit(0)

    print("Creating temp text files \n")
    create_txt_files(pgn_file)
    
    print("Creating temp img files \n")
    create_img_files()
    
    print("Creating gif file \n")
    create_gif(gif_file, frame_duration)


if __name__ == '__main__':
    args = make_args()
    main(args)
