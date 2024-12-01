def part_two(list1, list2):
  total_sum = 0
  for element in list1:
    repeated = list2.count(element)
    total_sum += repeated * element

  return total_sum


def main():
  list1 = []
  list2 = []

  with open('data.txt', 'r') as file:
    for line in file:
      col1, col2 = map(int, line.split())
      list1.append(col1)
      list2.append(col2)

  result = part_two(list1, list2)
  print(result)

if __name__ == "__main__":
  main()