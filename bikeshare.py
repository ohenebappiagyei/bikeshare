import time
import pandas as pd
import numpy as np

CITY_DATA={'chicago':'chicago.csv',
           'new york city':'new_york_city.csv',
           'washington':'washington.csv'
           }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
    (str)city - name of the city to analyze
    (str)month - name of the month to filter by, or "all" to apply no month filter
    (str)day - name of the day of the week to filter by, or "all" to apply
    """
    print('Hello! Let\'s explore the US bikeshare data!')
    # Get user input for city
    while True:
        # Get user input for city
        city = input('Enter the city (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please enter a valid city name.')

    while True:
    # Ask if the user wants to filter by month, day, not at all or both
        filter_choice = input('\nWould you like to filter the data by month, day, both, not at all? Type "month", "day", "both", or "none": ').lower()
        if filter_choice in ('month', 'day', 'both', 'none'):
            break
        else:
            print('Invalid choice. Please enter a "month", "day", "none" or "both".')
    month = 'all'
    day = 'all'

    if 'month' in filter_choice:
        while True:
            month = input('Which month - January, February, March, April, May, or June? ').title()
            if month in ('January', 'February', 'March', 'April', 'May', 'June'):
                break
            else:
                print('Invalid month. Please enter a valid month.')
    if 'day' in filter_choice:
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
            if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                break
            else:
                print('Invalid day. Please enter a valid day.')

    print('-' * 40)
    return (city, month, day)

def load_data(city, month, day):
    # Load the dataset for the specified city
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of the week
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Apply month filter
    if month.lower() != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        if month.lower() in months:
            month_num = months.index(month) + 1
            df = df[df['Month'] == month_num]
        else:
            print('Invalid month. Data will not be filtered by month.')

        # Apply day filter
    if day != 'All':
        df = df[df['Day of Week'] == day]

    return (df)

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if df.empty:
        print('No data available for the selected filters.')
    else:
        # Most common month
        common_month = df['Month'].mode()[0]
        print(f'The most common month is: {common_month}')
        
        # Most common day of the week
        common_day = df['Day of Week'].mode()[0]
        print(f'The most common day of the week is: {common_day}')

        # Most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        common_hour = df['Hour'].mode()[0]
        print(f'The most common start hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    if df.empty:
        print("No data available for the selected filters.")
    else:
        # Most commonly used start station
        common_start_station = df['Start Station'].mode()[0]
        print(f'The most commonly used start station is: {common_start_station}')

        # Most commonly used end station
        common_end_station = df['End Station'].mode()[0]
        print(f'The most commonly used end station is: {common_end_station}')

        # Most frequent combination of start station and end station trip
        df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
        common_trip = df['Trip'].mode()[0]
        print(f'The most frequent combination of start station and end station trip is: {common_trip}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ')
    print(user_types)

    # Display counts of gender if available
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    else:
        print('\nGender information not available for this city.')

        # Display earliest, most recent, and most common year of birth if available
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        if not df['Birth Year'].empty: #Check if the 'Birth Year' Column is not empty
            common_birth_year = df['Birth Year'].mode()[0]
            print('\nBirth Year Statistics:')
            print(f'Earliest Birth Year: {earliest_birth_year}')
            print(f'Most Recent Birth Year: {most_recent_birth_year}')
            print(f'Most Common Birth Year: {common_birth_year}')
        else:
            print('\nBirth Year information not available for this city.')
    else:
        print('\nBirth Year information not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Mean travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time (in seconds): {total_travel_time}')

    # Total travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time (in seconds): {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    start = 0
    end = 5
    while True:
        raw_data = input('\nWould you like to see 5 rows of the raw data? Enter "yes" or "no".\n')
        if raw_data.lower() == 'yes':
            print(df.iloc[start:end])
            start += 5
            end += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__=="__main__":
    main()
