"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
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
    year_num = len(YEARS)
    one_space = ((width-GRAPH_MARGIN_SIZE*2) / year_num)
    x_coordinate = int(GRAPH_MARGIN_SIZE + year_index * one_space)
    return x_coordinate


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

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + LINE_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE + LINE_WIDTH, text=YEARS[i], anchor=tkinter.NW)


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

    # Write your code below this line
    #################################

    color_round = 0   # the index of Constant COLOR
    for lookup_name in lookup_names:
        if lookup_name in name_data:
            for i in range(len(YEARS)):
                str_year = str(YEARS[i])
                if str_year in name_data[lookup_name]:
                    show_rank = name_data[lookup_name][str_year]
                    int_rank = int(show_rank)
                    uni = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE)/1000
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, GRAPH_MARGIN_SIZE + int_rank * uni, text=(lookup_name, show_rank), anchor=tkinter.SW, fill=COLORS[color_round])
                else:   # there's no data of this year of the name(the rank is out of 1000)
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=(lookup_name + ' *'), anchor=tkinter.SW, fill=COLORS[color_round])
        color_round += 1
        color_round = color_round % len(COLORS)
    x1 = 0  # these four variables are the ends of point A(x1, y1) and point B(x2, y2), to draw the line of name data
    y1 = 0
    x2 = 0
    y2 = 0
    color_round = 0    # the index of Constant COLOR
    for lookup_name in lookup_names:
        if lookup_name in name_data:
            for i in range(len(YEARS)):
                str_year = str(YEARS[i])
                if str_year in name_data[lookup_name]:
                    show_rank = name_data[lookup_name][str_year]
                    int_rank = int(show_rank)
                    uni = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / 1000
                else:   # there's no data of this year of the name(the rank is out of 1000)
                    int_rank = 1000
                    uni = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / 1000
                if x1 == 0 and y1 == 0:    # the first point of the line(the most left one)
                    x1 = get_x_coordinate(CANVAS_WIDTH, i)
                    y1 = GRAPH_MARGIN_SIZE + int_rank * uni
                else:
                    x2 = get_x_coordinate(CANVAS_WIDTH, i)
                    y2 = GRAPH_MARGIN_SIZE + int_rank * uni
                if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_round])
                    x1 = x2    # to link every point of the name data
                    y1 = y2
                    x2 = 0
                    y2 = 0
        x1 = 0     # start to draw the line of another name, clear the data of point
        y1 = 0
        x2 = 0
        y2 = 0
        color_round += 1
        color_round = color_round % len(COLORS)


# main() code is provided, feel free to read through it but DO NOT MODIFY
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
