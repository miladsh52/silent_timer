import matplotlib.pyplot as plt
import numpy as np

WEEKS_IN_YEAR = 52
WEEKS_IN_MONTH = 4

def get_user_input():
    lifespan_years = int(input("How many years do you think you will live? "))
    age_years = int(input("Enter your age in years: "))
    if age_years > lifespan_years:
        raise ValueError("Your actual age must be less than your anticipated age.")
    age_months = int(input("Enter the months (from 0 to 12): "))
    if not (0 <= age_months <= 12):
        raise ValueError("Please enter a valid number of months (0 to 12).")
    return lifespan_years, age_years, age_months

def calculate_weeks(lifespan_years, age_years, age_months):
    total_weeks = lifespan_years * WEEKS_IN_YEAR
    lived_weeks = age_years * WEEKS_IN_YEAR + age_months * WEEKS_IN_MONTH
    remaining_weeks = total_weeks - lived_weeks
    return total_weeks, lived_weeks, remaining_weeks

def plot_life(total_weeks, remaining_weeks):
    grid_size = int(np.ceil(np.sqrt(total_weeks)))
    grid = np.zeros((grid_size, grid_size))
    grid.flat[:remaining_weeks] = 1
    
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(grid, cmap="gray", extent=[0, grid_size, 0, grid_size], origin='upper')
    
    ax.set_xticks(np.arange(0, grid_size, 1), minor=False)
    ax.set_yticks(np.arange(0, grid_size, 1), minor=False)
    ax.grid(which="major", color="#E0E0E0", linestyle="-", linewidth=0.5)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    ax.set_title(f"Weeks in a {lifespan_years}-Year Life (Gray: Lived, White: Left)", fontsize=14)
    
    plt.show()

if __name__ == "__main__":
    lifespan_years, age_years, age_months = get_user_input()
    total_weeks, lived_weeks, remaining_weeks = calculate_weeks(lifespan_years, age_years, age_months)
    plot_life(total_weeks, remaining_weeks)