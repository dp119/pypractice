import calc
import sys
#aus_1_score = 250
aus_1_score = sys.argv[1]
aus_1_score = int(aus_1_score)
#ind_1_score = 220
ind_1_score = sys.argv[2]
ind_1_score = int(ind_1_score)
#aus_2_score  = 150
aus_2_score = sys.argv[3]
aus_2_score = int(aus_2_score)
aus_total = calc.add (aus_1_score, aus_2_score)
ind_need = calc.sub(aus_total, ind_1_score) + 1
print ("ind_need", ind_need)
print("from ESPN", __name__)
