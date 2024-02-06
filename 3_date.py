months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def int_num(a:list[int]) -> int:
    return int("".join(map(str, a)))

def is_leap_year(y:list[int]) -> bool:
    y = int_num(y)
    return y%400==0 or (y%100!=0 and y%4==0)

def get_date(y:list[int], m:list[int], d:list[int]) -> tuple[int, ...]:
    # check year
    if y[0] == 10:
        y = [1] + [0] + y[1:]
        y, m, d = get_date(y, m, d)
    for i in range(1, len(y)):
        if y[i] == 10:
            y[i-1] += 1
            y[i] = 0
            y, m, d = get_date(y, m, d)
        if y[i] in y[:i]:
            y[i] += 1
            y, m, d = get_date(y, [1], [1])
    # check month
    if m == [10]:
        m = [1, 0]
    if int_num(m) >= 10:
        if int_num(m) == 13 or 1 in y:
            y[-1] += 1
            y, m, d = get_date(y, [1], [1])
        if m == [1, 1] or m[1] in y:
            m[1] += 1
            y, m, d = get_date(y, m, [1])
    else:
        if m[0] in y:
            m[0] += 1
            y, m, d = get_date(y, m, [1])
    # check day
    if d == [10]:
        d = [1, 0]
    if len(d) == 1:
        if d[0] in y or d[0] in m:
            d[0] += 1
            y, m, d = get_date(y, m, d)
    else:
        if d[0] in y or d[0] in m or d[1] in y or d[1] in m:
            d[1] += 1
            if d[1] == 10:
                d[0] += 1
                d[1] = 0
            if int_num(m) == 2 and is_leap_year(y) and int_num(d) > 28 or int_num(d) > months[int_num(m)]:
                m[-1] += 1
                d = [1]
            y, m, d = get_date(y, m, d)

    return y, m, d

d_in = input()
m_in = input()
y_in = input()

y_in = [int(x) for x in y_in]
m_in = [int(x) for x in m_in]
d_in = [int(x) for x in d_in]
d_in[-1] += 1

res = get_date(y_in, m_in, d_in)
y_out = "".join(map(str, res[0]))
m_out = "".join(map(str, res[1]))
d_out = "".join(map(str, res[2]))
print(f"{y_out}.{m_out}.{d_out}")

# test1
# input: 10 9 1234
# output: 1235.4.6

# test2
# input: 10 9 987655
# output: 1023456.7.8
