import math
import random
import time

# Display program information
print("DYGS Score Python Program v0.1")

# Main program loop
while True:
    # Display program creator's name
    print("Created By: Did You Get Sniped?")
    print("This DYGS Score calculator for War Brokers is not an official program or calculation and is made only for fun.\n")

    # Get user input for the selected option
    print("Select an option:")
    print("1. Calculate DYGS Score")
    print("2. Explain the Process")

    option = input("Enter the option number (1 or 2): ")

    if option == "1":
        # Display the loading screen before the calculation
        print("Loading Calculator...")

        # Create a loading bar with 50 steps
        for i in range(50):
            time.sleep(0.08)  # Pause for 4 seconds divided into 50 steps
            print("\r[" + "=" * i + " " * (50 - i) + "]", end='', flush=True)

        # Get user input for Level, K/D ratio, and ELO
        level = float(input("\nEnter the player's Level: "))
        kd_ratio = float(input("Enter the player's Kills/Death ratio: "))
        elo = float(input("Enter the player's ELO: "))

        # Generate a random number of seconds to wait between 2 and 10 seconds
        wait_time = round(random.uniform(2, 10))

        # Display the calculated wait time
        print(f"Calculating... Please wait about {wait_time} seconds")

        # Create a progress bar
        for i in range(50):
            time.sleep(wait_time / 50)
            print("\r[" + "=" * i + " " * (50 - i) + "]", end='', flush=True)

        # Calculate the DYGS Score
        dygs_score = (0.45 * level) + (0.35 * kd_ratio) * 100 + (0.20 * elo)

        # Round the DYGS Score to one decimal point
        dygs_score = round(dygs_score, 1)

        # Display the calculated DYGS Score with one decimal point
        print(f"\nThe DYGS Score is: {dygs_score:.1f}")

    elif option == "2":
        # Explain the process of getting the score

        # This section provides a step-by-step breakdown of how the DYGS Score is calculated:
        print("\nExplanation of the DYGS Score Calculation Process:")

        # Step 1: Level Contribution
        print("1. We take the player's level and multiply it by 0.45.")
        print("   This accounts for the player's experience and progression in the game. A higher level means a higher contribution to the DYGS Score, as it reflects more experience and skill.")

        # Step 2: Kills/Death (K/D) Ratio Contribution
        print("2. We take the player's K/D ratio, multiply it by 100, and multiply it by 0.35.")
        print("   The K/D ratio is a crucial indicator of a player's performance. This step rewards players with a high K/D ratio, indicating their proficiency in eliminating opponents while minimizing deaths.")

        # Step 3: ELO Contribution
        print("3. We take the player's ELO and multiply it by 0.20.")
        print("   ELO is a common rating system in competitive games, representing a player's skill level. A higher ELO rating positively impacts the DYGS Score, highlighting the player's competitiveness in ranked matches.")

        # Step 4: Calculate the Final DYGS Score
        print("4. Finally, we add the results of the three steps to get the DYGS Score.")
        print("   The final DYGS Score is a comprehensive assessment of a player's performance, experience, and competitive abilities in War Brokers.")

    else:
        print("Invalid option. Please select either 1 or 2.")

    # Ask the user if they want to exit or restart
    restart_option = input("\nPress 1 to exit or 2 to restart the program: ")

    if restart_option == "1":
        break  # Exit the program
    elif restart_option != "2":
        print("Invalid option. Exiting the program.")
        break  # Exit the program
