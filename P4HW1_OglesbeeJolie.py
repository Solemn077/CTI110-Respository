# Pseudocode for Score Analysis Program

# Initialize an empty list to store scores
score_list = []

# Ask the user for the number of scores they want to enter
num_scores = input("Enter the number of scores you'd like to enter: ")

# Convert the input to an integer
num_scores = int(num_scores)

# Loop to collect scores
for i in range(num_scores):
    while True:
        try:
            # Ask the user for a score
            score = float(input(f"Enter score {i + 1}: "))
            
            # Check if the score is valid (between 0 and 100)
            if 0 <= score <= 100:
                # Add the valid score to the list
                score_list.append(score)
                break
            else:
                print("Invalid score. Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculate the lowest score
lowest_score = min(score_list)

# Remove the lowest score from the list
score_list.remove(lowest_score)

# Calculate the average of the modified list
average_score = sum(score_list) / len(score_list)

# Determine the letter grade based on the average
if 90 <= average_score <= 100:
    letter_grade = "A"
elif 80 <= average_score < 90:
    letter_grade = "B"
elif 70 <= average_score < 80:
    letter_grade = "C"
elif 60 <= average_score < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print(f"Lowest score entered: {lowest_score}")
print(f"Score List after dropping lowest score: {score_list}")
print(f"Average score: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")
