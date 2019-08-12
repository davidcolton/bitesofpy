WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
   """Create a chessboard with of the size passed in.
   Don't return anything, print the output to stdout"""

   def _create_even_line(size):
      return ''.join([WHITE if i % 2 else BLACK for i in range(size)])
   
   even_line = _create_even_line(size)
   odd_line = even_line[::-1]
   
   print('\n'.join(even_line if line % 2 else odd_line for line in range(size)))

create_chessboard(4)