score = float(input("enter your base score: "))
score += 5
score -= 10
score = max(0, min(score, 100))
if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
elif score >= 60:
  grade = "D"
else:
  grade = "F"
print("final_sore:", score)
print("grade:", grade)