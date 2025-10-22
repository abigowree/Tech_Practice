1)
monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
total_rainfall=sum(monthly_rainfall)
print(total_rainfall)
2)
average_rainfall=(total_rainfall/len(monthly_rainfall))
print(average_rainfall)
3)
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
months_120 = [months[i] for i, value in enumerate(monthly_rainfall) if value == 120]
print(months_120)
4)
high=max(monthly_rainfall)
low=min(monthly_rainfall)
print(high)
print(low)