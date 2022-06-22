delivery_rank = ["canada","china","philippines","singapore","uae"]
social_rank = ["china","philippines","canada","uae","singapore"]

country = input()
print("country:",)
if (delivery_rank.index(country)==0):
    del_prob = 0.35
elif (delivery_rank.index(country)==1):
    del_prob = 0.3
elif (delivery_rank.index(country)==2):
    del_prob = 0.2
elif (delivery_rank.index(country)==3):
    del_prob = 0.1
else:
    del_prob = 0.05

if (social_rank.index(country)==0):
    soc_prob = 0.35
elif (social_rank.index(country)==1):
    soc_prob = 0.3
elif (social_rank.index(country)==2):
    soc_prob = 0.2
elif (social_rank.index(country)==3):
    soc_prob = 0.1
else:
    soc_prob = 0.05

total = soc_prob * del_prob
print("total %.4f" % (total))