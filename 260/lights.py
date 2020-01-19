import numpy as np
import pandas as pd
from typing import List


class LightsGrid:
    def __init__(self, grid_size: int, instructions: List[str]):
        self.grid_size = grid_size
        self.grid = pd.DataFrame(np.zeros([grid_size, grid_size], dtype=int))
        self.instructions = instructions

    def process_grid_coordinates(self, s1: str, s2: str):
        """A helper function you might want to create to process
          the top left hand corner coordinates and the bottom 
          right hand coordinates given in the instructions
          
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        Suggested return are 4 integers representing x1, x2, y1, y2 [hint]"""

        x1 = int(s1.split(",")[0])
        y1 = int(s1.split(",")[1])

        # x2 & y2 are + 1 because we are using matrix slices
        #    e.g. x1, x2 = 2, 4 only returns rows 2 up to but
        #         not including row 4 i.e. rows 2 & 3 only
        x2 = int(s2.split(",")[0]) + 1
        y2 = int(s2.split(",")[1]) + 1

        return x1, x2, y1, y2

    def validate_grid(self):
        """A helper function you might want to write to verify that:
          - no lights are brighter than 5
          - no lights are less than 0"""
        # Check for intensity values > 5
        too_bright_mask = self.grid > 5
        self.grid[too_bright_mask] = 5

        # Check for intensity values < 0
        negative_mask = self.grid < 0
        self.grid[negative_mask] = 0

        return self.grid

    def turn_on(self, s1: int, s2: int):
        """The turn_on function takes 2 parameters:
        
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        For each light in the grid slice given:
          - If the light is already on, do nothing
          - If the light is off, turn it on at intensity 1
          
        Note: Bob
        
        To make this a little easier we could leave the comments in place"""

        # Process grid coordinates
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)

        # First extract the slice of the grid into a new dataframe
        grid_slice = self.grid.iloc[x1:x2, y1:y2]

        # Now create a mask of all lights == 0 in the slice
        mask = grid_slice == 0

        # # Now turn on all lights that are off
        grid_slice[mask] = 1

        # Finally overwrite the grid with the new values
        self.grid.iloc[x1:x2, y1:y2] = grid_slice

        return self

    def turn_off(self, s1: int, s2: int):
        """The turn_off function takes 2 parameters:
        
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        Turn on all lights in the grid slice given."""
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2, y1:y2] = 0
        return self

    def turn_up(self, amount: int, s1: str, s2: str):
        """The turn_up function takes 3 parameters:
        
        :param amount: The intensity to turn the lights up by
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        For each light in the grid slice given turn the light up 
          by the given amount. Don't turn a light up past 5"""
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2, y1:y2] += amount
        self.validate_grid()
        return self

    def turn_down(self, amount: int, s1: str, s2: str):
        """The turn down function takes 3 parameters:
        
        :param amount: The intensity to turn the lights down by
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        For each light in the grid slice given turn the light down 
          by the given amount. Don't turn a light down past 0"""
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2, y1:y2] -= amount
        self.validate_grid()
        return self

    def toggle(self, s1: str, s2: str):
        """The toggle function takes 2 parameters:
        
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on
        
        For each light in the grid slice given:
          - If the light is on, turn it off
          - If the light is off, turn it on at intensity 3
          
        Note: Bob
        
        To make this a little easier we could leave the comments in place"""

        # Process grid coordinates
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)

        # First extract the slice of the grid into a new dataframe
        grid_slice = self.grid.iloc[x1:x2, y1:y2]

        # Now create a mask of all lights > 0 in the slice
        mask = grid_slice > 0

        # Now turn off all lights that are on in the slice
        # Set all lights that are off to 3 in the slice
        grid_slice[mask] = 0
        grid_slice[~mask] = 3

        # Finally overwrite the grid with the new values
        self.grid.iloc[x1:x2, y1:y2] = grid_slice

        return self

    def follow_instructions(self):
        """Function to process all instructions.
        
        Each instruction should be processed in sequence,
          excluding the first instruction of course.
        """
        for ins in self.instructions:
            if ins.startswith("toggle"):
                s1, _, s2 = ins[7:].split()
                self.toggle(s1, s2)
            elif ins.startswith("turn on"):
                s1, _, s2 = ins[8:].split()
                self.turn_on(s1, s2)
            elif ins.startswith("turn up"):
                amount, s1, _, s2 = ins[8:].split()
                self.turn_up(int(amount), s1, s2)
            elif ins.startswith("turn down"):
                amount, s1, _, s2 = ins[10:].split()
                self.turn_down(int(amount), s1, s2)
            else:
                s1, _, s2 = ins[9:].split()
                self.turn_off(s1, s2)
        return self

    @property
    # Property to get the total intensity of all lights
    # This can be given
    def lights_intensity(self):
        return self.grid.to_numpy().sum()


# Main function that can be used to test the Class methods
# This can be given to aid
if __name__ == "__main__":
    with open("./instructions.txt", "r") as f:
        instructions_str = f.read()

    # Create a list of all the instructions
    instructions = [line.strip() for line in instructions_str.split("\n") if line != ""]

    # The grid size instruction is first
    # Extract it and convert to int
    grid_size = int(instructions[0].split(" ")[4])

    # Create a LightsGrid Class instance
    lights = LightsGrid(grid_size, instructions[1:])

    # Follow the instructions
    lights.follow_instructions()

    # Print the total intensity of the lights
    # The correct answer is 12317
    print(f"Total intensity of Lights on: {lights.lights_intensity}\n")

