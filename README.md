# chess-pgn-gif

**Purpose**: Convert a chess game given in PGN format to a GIF file using some python libraries. This made for a fun 3 hour project!

For now the board and its moves are represented as an 'ASCII art' image.


## Dependencies 

- Tested on Python 3.6
- Libraries: python-chess, imageio, PIL/pillow


## Usage

`$ python chess_gif.py -d DURATION -i INPUT -o OUTPUT`

- DURATION is the time given to each frame in the output gif.
- INPUT is the pgn file of the chess game.
- OUTPUT is the name of the output gif file.


## Future work 

- SVG output files for images. 
- Serve it as a web service?? (ask sreeni)









