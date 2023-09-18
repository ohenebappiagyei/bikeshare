import pandas as pd
import matplotlib.pyplot as plt

# Define the city data filename
CITY_DATA = {
        'chicago':'chicago.csv',
        'new york city':'new_york_city.csv',
        'washington':'washington.csv'}

# Function to load data for a specific city
def load_data(city):
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    return df

#Function to create a bar plot of user types
def plot_user_types(df):
    user_type_counts = df['User Type'].value_counts()
    plt.bar(user_type_counts.index, user_type_counts.values)
    plt.xlabel('User Type')
    plt.ylabel('Count')
    plt.title('User Type Distribution')
    plt.show()

# Main function
def main():
    # Get user input for the city
    city = input('Enter the city (Chicago, New York City, Washington): ').lower()

    # Load data for the specified city
    df = load_data(city)

    # Create a bar plot of user types
    plot_user_types(df)

if __name__ == "__main__":
    main ()
