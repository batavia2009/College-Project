# ==============================================================================
# PROJECT TITLE: Subscription "Leak" Detector & Optimizer
# DESCRIPTION: A Python application using standard data structures 
#              and math logic to track subscriptions, identify money leaks, and 
#              rank active subscriptions by cancellation priority.
# ==============================================================================

# Global List Storage for User's Active Subscriptions
user_subscriptions = []


# ------------------------------------------------------------------------------

def get_user_input(prompt_text):
    res = input(prompt_text)
    if res is None:
        return ""
    return res.strip()

# ------------------------------------------------------------------------------
# STEP 1: CORE FUNCTIONS
# ------------------------------------------------------------------------------

def add_subscription():
    """Option 1: Collects subscription data safely from user input."""
    print("\n--- 1) Enter New Subscription ---")
    name = get_user_input("Enter subscription name (e.g., Netflix, Gym): ")
    if not name:
        print("Name cannot be empty.")
        return

    try:
        cost = float(get_user_input("Enter monthly cost ($): "))
        usage = int(get_user_input("How many times do you use it per month? "))
        
        if cost < 0 or usage < 0:
            print("Cost and usage must be non-negative values.")
            return

        user_subscriptions.append({
            "name": name,
            "cost": cost,
            "usage": usage
        })
        print(f"Successfully added '{name}'!")
        
    except ValueError:
        print("Invalid input! Please enter numeric values for cost and usage.")


def view_subscriptions_and_ranking():
    """Option 2: Calculates cost per use, sorts by waste priority, and displays."""
    print("\n--- 2) Active Subscriptions & Priority Ranking ---")
    if not user_subscriptions:
        print("No active subscriptions found. Add some first!")
        return

    # Calculate Cost Per Use for all entries
    for sub in user_subscriptions:
        if sub["usage"] > 0:
            sub["cost_per_use"] = sub["cost"] / sub["usage"]
        else:
            sub["cost_per_use"] = sub["cost"]  # Handles zero error if any

    # Sort in descending order (highest cost per use = highest waste rank)
    ranked_list = sorted(user_subscriptions, key=lambda x: x["cost_per_use"], reverse=True)

    print("\n CANCELLATION PRIORITY RANKING (Highest Waste First) ")
    print("=" * 60)
    
    for rank, sub in enumerate(ranked_list, 1):
        yearly_cost = sub["cost"] * 12
        cpu = sub["cost_per_use"]
        
        if cpu > 15.0 or sub["usage"] == 0:
            status = "HIGH PRIORITY LEAK (Consider Canceling)"
        elif cpu > 5.0:
            status = "MODERATE LEAK (Review Value)"
        else:
            status = "GOOD VALUE"

        print(f"Rank #{rank}: {sub['name']}")
        print(f"  ├─ Spend: ${sub['cost']:.2f}/mo  |  ${yearly_cost:.2f}/yr")
        print(f"  ├─ Monthly Usage: {sub['usage']}x")
        print(f"  ├─ Cost Per Session: ${cpu:.2f}")
        print(f"  └─ Status: {status}")
        print("-" * 60)


# ------------------------------------------------------------------------------
# STEP 2: MAIN MENU LOOP INTERFACE
# ------------------------------------------------------------------------------

def main():
    while True:
        print("\n" + "=" * 45)
        print("   SUBSCRIPTION LEAK DETECTOR & OPTIMIZER   ")
        print("=" * 45)
        print("1) Enter New Subscription")
        print("2) View Active Subscriptions & Priority Ranking")
        print("3) Exit")
        
        choice = get_user_input("\nSelect an option (1-3): ")
        
        if choice == "1":
            add_subscription()
        elif choice == "2":
            view_subscriptions_and_ranking()
        elif choice == "3":
            print("\nThank you for using Subscription Leak Detector! Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 3.")

# Run the program
if __name__ == "__main__":
    main()
