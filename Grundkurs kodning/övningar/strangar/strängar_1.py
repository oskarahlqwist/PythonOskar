tabbar = 0
mellanslag = 0
andra = 0

s = "doo     bee doo    be doo?"

mellanslag = s.count(" ")
tabbar = s.count("\t")
andra = len(s)-(mellanslag+tabbar)

print (mellanslag, tabbar, andra)

