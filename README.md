# Chess PGN to Gif

**Purpose**: Convert a chess game given in PGN format to a GIF file using some intermediate
python libraries. This made for a fun afternoon project on which I can keep iterating and
learn new things. It also showcases the power of Python as a *glue* language!

Dedicated to my father a.k.a "baba" from whom I learned the basics of chess :)

# Dependencies 
The scripts have fairly minimal setup requirements. The project was last tested with the
following packages on `Ubuntu 20.04`. **Note:** not tested with other operating systems!

- Python 3.11 
- [python-chess](https://github.com/niklasf/python-chess) 1.9.4
- [imageio](https://imageio.readthedocs.io/en/stable/) 2.26.0

See the `requirements.txt` to test the code out and `environment.yml` for setting up a
dev environment to hack the code.

# Usage

`chess_gif.py` is the main python file to use for creating the gif. Use as:

`$ python chess_gif.py -d DURATION -i INPUT -o OUTPUT`

- `DURATION`: time given to each frame in the output gif.
- `INPUT`: path for `.pgn` file for the chess game.
- `OUTPUT` desired path for output `.gif`.

The board and its moves are represented as an 'ASCII art' image. `text_to_img.py` is an 
intermediate helper script to create image representation of a text file.

# To Do 

No guarantees as to when I'll actually sit down

- [x] Cleanup the repo, update readme, requirements and todo.
- [ ] Make the `images.append()` warning from `imageio` disappear by updating the code
- [ ] Can we avoid writing tmp files and images and instead keep everything in memory?
- [ ] Write code for proper unit tests. For now, `tests/` just contains not so pretty jupyter notebooks left over from >4 years ago! 
- [ ] SVG output files for images. 
- [ ] Custom images for the board pieces instead of letters (i.e more pretty output!)
- [ ] Other output formats: interactive webpage using javascript where one can move forward or backward with the moves.
  - [ ] Custom options for the output like resolution, quality, etc...
- [ ] Host a web frontend where user will upload `.pgn` file and you produce required output with option to save it?
