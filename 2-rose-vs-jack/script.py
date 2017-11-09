# Passengers that survived vs passengers that passed away
print(train["Survived"].value_counts())

# As proportions
print(train["Survived"].value_counts(normalize = True))

# Males that survived vs males that passed away
print(train["Survived"][train["Sex"] == 'male'].value_counts())

# Females that survived vs Females that passed away
print(train["Survived"][train["Sex"] == 'female'].value_counts())

# Normalized male survival
print(train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True))

# Normalized female survival
print(train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True))

#0    549
#1    342
#Name: Survived, dtype: int64
#0    0.616162
#1    0.383838
#Name: Survived, dtype: float64
#0    468
#1    109
#Name: Survived, dtype: int64
#1    233
#0     81
#Name: Survived, dtype: int64
#0    0.811092
#1    0.188908
#Name: Survived, dtype: float64
#1    0.742038
#0    0.257962
#Name: Survived, dtype: float64