N = 60
MEAN_pops = 300
mean_sample = 290
std_ = 15

alpha = 0.05
critical_value = 1.96

null_h = "average = 300"
alt_h = "average is not equal to 300 |  [greater or equal to DO NOT KNOW])"

Std_error = (std_ / N ** 0.5)
z_score = round((mean_sample - MEAN_pops) / Std_error, 2)

if(abs(z_score) > critical_value ):
    print(f"Z SCORE IS : {z_score} > {critical_value} critical "
          f"\nReject Hypothesis, which states that {null_h}")
elif(abs(z_score) < critical_value):
    print(f"Z SCORE IS : {z_score}"
          f"\nFail to reject, which states that {null_h}")