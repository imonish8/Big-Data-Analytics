N = 40
MEAN_sample = 82
MEAN_pops = 85
STD_ = 6
alpha = 0.05


print("Since the we are interested in finding weather or not they are"
      "less than only, we are interested in only less finding out"
      "One tailed Test best fit")

print("NULL H : School sverage test mean is 85 ,mu = 85"
      "Alt H : School average  is less than or equal to 85 , mu < 85")
std_err = STD_ / (N ** 0.5)
print(f"Standard Error is : {std_err}")
z_score_ssample =( MEAN_sample - MEAN_pops) / std_err
print(f"Z score is : {z_score_ssample}")

if(z_score_ssample < -1.645):
      print("Rejecting the Null Hypothesis"
            "\nwhich means the school has less average than claimed 85 significantly")
elif(z_score_ssample > -1.645):
      print("Failed to Reject Null Hypothesis, "
            "\nAverage test score is correct as claimed by school 85. ")
else :
      print("Check code")
