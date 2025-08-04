
## Convert the time entered in hh, min and sec into seconds.

i_sec = int(input("Enter the sec: "))

hr = i_sec // 3600
r_sec = i_sec - 3600

min = r_sec // 60
sec = r_sec-(min*60)

print(f"{hr} hr, {min} min and {sec} sec are remaining")
