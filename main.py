import random

def calculate_probabilities(outcomes, trials):
    # Calculate the expected occurrences for each outcome
    probability = 1 / outcomes  # Each outcome has an equal probability
    expected_results = {f"Outcome {i+1}": trials * probability for i in range(outcomes)}  # Expected occurrences
    actual_results = {f"Outcome {i+1}": 0 for i in range(outcomes)}  # Initialize count for each outcome

    # Simulate trials
    for _ in range(trials):
        result = random.randint(1, outcomes)  # Random outcome from 1 to 'outcomes'
        actual_results[f"Outcome {result}"] += 1  # Increment the count for the outcome

    return expected_results, actual_results

def main():
    print("Probability Calculator")

    try:
        # Ask the user for the number of possible outcomes
        outcomes = int(input("How many possible outcomes are there? (e.g., 6 for a die, 2 for coin toss): "))
        if outcomes <= 0:
            print("Please enter a positive number.")
            return

        # Ask the user for the number of trials
        trials = int(input("How many trials would you like to perform? "))
        if trials <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Calculate and display the results
    expected_results, actual_results = calculate_probabilities(outcomes, trials)
    print("\nResults:")
    print("Expected Values (Probabilities):")
    for outcome, expected_count in expected_results.items():
        print(f"{outcome}: {expected_count:.2f} times")

    print("\nActual Results:")
    for outcome, actual_count in actual_results.items():
        print(f"{outcome}: {actual_count} times")

if __name__ == "__main__":
    main()
