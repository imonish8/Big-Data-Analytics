N = 25
MEAN_pop = 5
MEAN_sample = 5.8
STD_ = 1.2
alpha = 0.05

std_err = STD_ / (N ** 0.5)

print("Researcher is looking for a change not specidef weather he wants to see increase or decrease"
      "\nso researcher is looking at a Two Tailed test which might be either increase or dec.")
print("\nA two tailed test offers to detect in eother direction not restricted to unidirection")

Null_H = "new diet program didnt changed the weight"
Alt_H = "New diet Program has changed the weight (Increase or decrease)"


z_score_two_tail = round((MEAN_sample - MEAN_pop) / std_err,2)
print(f"Z Score is : {z_score_two_tail}")

if(z_score_two_tail > 1.96) :
    print(f"Rejecting Null Hypothesis,'{Null_H}' is being rejected")
else:
    print(f"we may fail to reject, {Null_H}")