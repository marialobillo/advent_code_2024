def historian_hysteria(list1, list2):
  sorted_list1 = sorted(list1)
  sorted_list2 = sorted(list2)

  total_diff_sum = 0
  for first, second in zip(sorted_list1, sorted_list2):
    total_diff_sum += abs(first - second)
  return total_diff_sum


def main():
  list1 = []
  list2 = []

  with open('data.txt', 'r') as file:
    for line in file:
      col1, col2 = map(int, line.split())
      list1.append(col1)
      list2.append(col2)

  result = historian_hysteria(list1, list2)
  print(result)

if __name__ == "__main__":
  main()