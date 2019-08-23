def minBins(weight, capacity):
  weight.sort(reverse = True)
  if len(weight) == 0:
    return 0
  index = 1
  dict_bins = dict()
  for w in weight:
    flag = 0
    if len(dict_bins) > 0:
      for k, v in dict_bins.items():
        if v >= w:
          dict_bins.update({k:v-w})
          print(dict_bins)
          flag = 1
          break
    if flag == 0:
      dict_bins[index] = capacity - w
      index +=1
      print(dict_bins)
  # print(dict_bins)

  return len(dict_bins)


weight = [4,8,1,4,2,1]
capacity = 10
sol = minBins(weight,capacity)
print(sol)
