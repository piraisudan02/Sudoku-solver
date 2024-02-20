![Screenshot (148)](https://github.com/piraisudan02/Sudoku-solver/assets/96645021/4c2882e8-5345-47af-b110-5895c0cd0b5b)
![Screenshot (147)](https://github.com/piraisudan02/Sudoku-solver/assets/96645021/af111c56-0951-4381-8564-293467e2cbc1)
![Screenshot (139)](https://github.com/piraisudan02/Sudoku-solver/assets/96645021/33db351f-0c35-4219-a93c-8f950e2b07b7)
![Screenshot (138)](https://github.com/piraisudan02/Sudoku-solver/assets/96645021/5c98957f-ac48-433d-b978-f79a0720b1bf)
![Screenshot (135)](https://github.com/piraisudan02/Sudoku-solver/assets/96645021/9065c512-5765-4a71-8a23-6db67cff3148)
# Sudoku-solver
User Interface (UI):

The UI consists of a main window created using the Tkinter library.
Within the main window, a frame is created to organize the widgets.
Labels, buttons, and entry fields are used to create the Sudoku grid, display messages, and interact with the user.
Sudoku Solver Logic:

The solver utilizes a backtracking algorithm to solve the Sudoku puzzle.
The solver function implements the backtracking algorithm recursively to find the solution for the Sudoku puzzle.
It checks each empty cell in the Sudoku grid and tries possible values (1 to 9) until a valid solution is found.
Functions:

validcheck: Checks if placing a number in a specific cell of the Sudoku grid is valid according to Sudoku rules (no repetition in row, column, or 3x3 square).
isvalid: Checks if placing a number in a specific cell of the Sudoku grid is valid.
start: Initiates the solving process by calling the solver function.
draw: Draws a 3x3 grid of entry fields representing a 3x3 block in the Sudoku grid.
draw9X9: Draws the entire 9x9 Sudoku grid by calling the draw function for each 3x3 block.
clearValues: Clears all values entered into the Sudoku grid.
getValues: Retrieves the values entered by the user from the Sudoku grid and initiates the solving process.
update: Updates the Sudoku grid with the solved puzzle and displays a message indicating that the Sudoku is solved.
Hover Effect:

The changeOnHover1 function adds a hover effect to the buttons, changing their background color when the mouse cursor enters or leaves the button area.
Execution:

The mainloop function of the frame runs the application, allowing user interaction and handling events such as button clicks.
User Interaction:

Users can fill in the Sudoku grid with numbers from 1 to 9.
Clicking the "Solve" button attempts to solve the Sudoku puzzle.
Clicking the "Clear" button clears all values entered into the Sudoku grid.
Overall, this application provides a simple and interactive way for users to input a Sudoku puzzle and solve it using the implemented solver algorithm.
