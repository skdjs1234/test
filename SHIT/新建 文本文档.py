def analyze(date):
    # 1. Net Change
    net_change = date[-1] - date[0]
    
    # 2. Yearly Average
    if len(date) <= 1:
        yearly_avg = 0.0
    else:
        yearly_avg = (date[0] - date[-1]) / (len(date) - 1)
    
    # 3. Trend
    trend = "declining"
    if len(date) >= 3:
        first_3 = sum(date[:3])
        last_3 = sum(date[-3:])
        if last_3 > first_3:
            trend = "improving"
        elif last_3 == first_3:
            trend = "stagnating"
    
    # 4. Dips
    dips = 0
    for i in range(1, len(date)):
        if date[i] < date[i-1]:
            dips += 1
    
    # 返回三个数值
    return (net_change, yearly_avg, trend, dips)

# 输入处理
try:
    input_data = input().strip()
    date = []
    if input_data:
        for num in input_data.replace(',', ' ').split():
            date.append(float(num))
except EOFError:
    date = [0.0]

# 调用并输出
result = analyze(date)
print(f"Net Change: {result[0]}")
print(f"Yearly Average: {result[1]}")
print(f"Trend: {result[2]}")
print(f"Dips: {result[3]}")





def analyze(date):
  # Write code below 💖
  
  output= (int(date[0])-int(date[-1])) / (len(date)-1)
  print(output)
  if sum(map(int,date[-3:])) > sum(map(int,date[:3])) :
    print("improving")
  elif sum(map(int,date[-3:])) ==sum(map(int,date[0:3])) :
    print("stagnating")
  else:
    print("declining")
  def compare():
    for i in range(len(date)):
      a=0
      if date[i] > date[i-1] :
        a+=1
    print(a)
  compare()
try:
    # 读取输入并转换为数字列表（支持逗号/空格分隔）
    input_data = input().strip()
    # 处理空输入
    if not input_data:
        percentages = [0.0]
    else:
        # 兼容逗号/空格分隔的输入格式
        percentages = []
        for num_str in input_data.replace(',', ' ').split():
            percentages.append(float(num_str))
except EOFError:
    # 无输入时的默认值，避免程序崩溃
    percentages = [0.0]
except ValueError:
    # 输入非数字时的容错
    percentages = [0.0]

# 调用分析函数
analyze(percentages)