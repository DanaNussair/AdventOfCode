from functools import reduce

arr = [1941,1887,1851,1874,1612,1960,1971,1983,1406,1966,1554,1892,1898,1926,1081,1992,1073,1603,177,1747,1063,1969,1659,1303,1759,1853,1107,1818,1672,1352,2002,1838,1985,1860,1141,1903,1334,1489,1178,1823,1499,1951,1225,1503,1417,1724,1165,1339,1816,1504,1588,1997,1946,1324,1771,1982,1272,1367,1439,1252,1902,1940,1333,1750,1512,1538,1168,2001,1797,1233,972,1306,1835,1825,1822,1880,1732,1785,1727,1275,1355,1793,1485,1297,1932,1519,1587,1382,1914,1745,1087,1996,1746,1962,1573,2008,1868,1278,1386,1238,1242,1170,1476,1161,1754,1807,1514,1189,1916,1884,1535,1217,1911,1861,1493,1409,1783,1222,1955,1673,1502,607,2010,1846,1819,1500,1799,1475,1146,1608,1806,1660,1618,1904,978,1762,1925,1185,1154,1239,1843,1986,533,1509,1913,287,1707,1115,1699,1859,1077,1915,1412,1360,1646,1973,1627,1755,1748,1769,1886,1422,1686,950,100,1372,1068,1370,1428,1870,1108,190,1891,1794,1228,1128,1365,1740,1888,1460,1758,1906,1917,1989,1251,1866,1560,1921,1777,1102,1850,1498,683,1840,1800,1112,1908,1442,1082,1071]
obj = {n: i for (i, n) in enumerate(arr)}

# Part #1
print("Part 1:")
def two_num_sum(requested_sum):
    for index, num in enumerate(arr):
        if requested_sum - num in obj and index != obj.get(requested_sum - num):
            return [num, requested_sum - num]
    return False

two_numbers = two_num_sum(2020)
multiplied = reduce(lambda a, b: a * b, two_numbers)
print("Two Numbers: ", two_numbers)
print("Multiplied: ", multiplied)


#############################
# Part #2
print("Part 2")
def three_num_sum(requested_sum):
    for number in arr:
        two_numbers = two_num_sum(requested_sum - number)
        if two_numbers:    
            return [number] + two_numbers

three_numbers = three_num_sum(2020)
multiplied = reduce(lambda a, b: a * b, three_numbers)
print("Three Numbers", three_numbers)
print("Multiplied: ", multiplied)
