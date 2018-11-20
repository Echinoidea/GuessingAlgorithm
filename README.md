# GuessingAlgorithm
Basic algorithm to solve a number guessing game.

I'm relatively new to Python and algorithms. I figured this would be a good place to start.

1: Create a random number 1 - x, where x is user input, as the correct number that the program is trying to guess.

2: Add each number to an array. E.g. [1, 2, 3, ..., x]

3: Program selects the index that is half of the length of the array.

4: If the selection is too low, every index that comes before the selected index is deleted.

5: If it is too high, it deletes every index that comes after the selected index.

6: Program selects the index that is half of the length of the new array, which is half of what it was.

7: Repeat lines 3 - 6 until either the program selects the correct number by chance, or that the list has been reduced to only the correct answer.

8: End game loop.

9: End program.
