val = input()

if len(val) == 1:
    val = "0" + val[0]


temp = val
count = 0

while True:
    if (count > 0) and (val == temp):
        print(count)
        break
    else:
        if count != 0:
            if len(val) == 1:

                val = "0" + val[0]
                sum = int(val[0]) + int(val[1])
                sum = str(sum)
                val = val[-1] + sum[-1]

                count += 1

        sum = int(val[0]) + int(val[1])
        sum = str(sum)
        val = val[-1] + sum[-1]
        count += 1
