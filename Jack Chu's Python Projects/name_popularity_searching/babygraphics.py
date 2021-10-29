"""
Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

Name: Jack Chu

DESCRIPTION:
To draw the baby name template, if we key in the name, the template will show the curve of the changing
trend of the name in each decade since 1900 to 2010
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # first get the space length we want for the separation between each straight line
    space = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + space * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # to separate the canvas with straight lines, each line has same space between each other
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, GRAPH_MARGIN_SIZE + CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    
    # to get the space unit we want
    space = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2) / 1000
    # to get each name which be input
    for i in range(len(lookup_names)):
        # prepare to draw the lines between each straight year lines
        for j in range(len(YEARS)-1):
            # to decide if name's dict has the info of that year
            if str(YEARS[j]) in name_data[lookup_names[i]]:
                rank = int(name_data[lookup_names[i]][str(YEARS[j])])
                text1 = lookup_names[i]+' '+str(rank)
            else:
                rank = 1000
                text1 = lookup_names[i]+' '+'*'
            if str(YEARS[j+1]) in name_data[lookup_names[i]]:
                rank2 = int(name_data[lookup_names[i]][str(YEARS[j+1])])
                text2 = lookup_names[i]+' '+str(rank2)
            else:
                rank2 = 1000
                text2 = lookup_names[i]+' '+'*'
            if i < 4:
                color = COLORS[i]
            else:
                p = i % 4
                color = COLORS[p]
            x = get_x_coordinate(CANVAS_WIDTH, j)
            x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
            canvas.create_line(x, GRAPH_MARGIN_SIZE+rank*space, x2, GRAPH_MARGIN_SIZE+rank2*space, width=LINE_WIDTH,
                               fill=color)
            canvas.create_text(x+TEXT_DX, GRAPH_MARGIN_SIZE+rank*space, text=text1, anchor=tkinter.SW)
            canvas.create_text(x2 + TEXT_DX, GRAPH_MARGIN_SIZE + rank2 * space, text=text2, anchor=tkinter.SW)

def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
