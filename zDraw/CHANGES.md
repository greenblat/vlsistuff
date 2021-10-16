
8oct2021:
    import cucu.py   : in terminal (now also in .zdrawrc).
      in cucu.py define function "def run(wrds):"   
      from terminal, type :    cucu aaa bb ccc  
      the run() function will be called with wrds = ['aaa','bb','ccc']
      Glbs is slapped onto module cucu ifter importing, to access whole database.

    all placements of instances obey grid.   "grid = 0.5" is the recommended option.


9oct2021:
    drawing grid:    in terminal:   gridDraw = 0 : no grid, gridDraw = 1 : lines grid, gridDraw = 2 : dots grid.

10oct2021:
    new "concat" picture to concat busses into wide bus.
    "add nand"  - will print all available cells starting with nand*
    mousedown prints underneath instance name and associated params.
    grouping:   after "G" press, mousedown will add underneatch instance to bus
    log.flush after each write to logfile

11oct2021:
    - added "import cucu.py" to .zdrawrc
    - made "0" leave empty frame around detail.
14oct2021
    - added wire_direction context to put little circle at the end of a wire.
    - added pickle command
    - added Save command : does save, verilog,print and pickle.

