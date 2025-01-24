def calculate_probabilities(outcomes, trials):
    """
    Calculate the expected occurrences for each possible outcome.
    
    Args:
        outcomes (int): The number of possible outcomes (e.g., 6 for a die).
        trials (int): The number of trials to simulate.

    Returns:
        dict: A dictionary mapping each outcome to its expected occurrence.
    """
    # Each outcome has an equal probability
    probability = 1 / outcomes
    results = {f"Outcome {i+1}": trials * probability for i in range(outcomes)}
    return results

def main():
    print("Probability Calculator")

    try:
        # Ask the user for the number of possible outcomes
        outcomes = int(input("How many possible outcomes are there? (e.g., 6 for a die, 2 for coin toss): "))
        if outcomes <= 0:
            print("Please enter a positive number.")
            return

        # Ask the user for the number of trials
        trials = int(input("How many trials would you like to conduct? "))
        if trials <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Calculate and display the results
    results = calculate_probabilities(outcomes, trials)
    print("\nResults (Expected Values):")
    for outcome, count in results.items():
        print(f"{outcome}: {count:.2f} occurrences")

if __name__ == "__main__":
    main()
