passes = 0
failures = 0
for student in range(10):
    result = int(input("Enter result (1=PASS, 2=FAIL)"))
    if result ==1:
        passes = passes+1
    else:
        failures = failures+1
print(f'Passed:{passes}')
print(f'Failed:{failures}')
if passes> 8:
        print('Bonus to Instructor')