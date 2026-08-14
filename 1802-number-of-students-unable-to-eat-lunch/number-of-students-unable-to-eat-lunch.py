from collections import Counter
from typing import List


class Solution:

  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    counts = Counter(students)

    for sandwich in sandwiches:
      if counts[sandwich] > 0:
        counts[sandwich] -= 1
      else:
       
        break

    return counts[0] + counts[1]