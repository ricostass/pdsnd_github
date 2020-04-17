import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Would you like to see the data for: Chicago, New York City, Washington?\n>").lower()
        if city in cities:
            break

 # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Would you like to see the data for: all, January, February, March, April, May, June\n>").lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Would you like to see the data for: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n>").lower()
        if day in days:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode().values[0]
    print('Most Popular Start Month:', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode().values[0]
    print('Most Popular Start Day:', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode().values[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode().values[0]
    print('Most Popular Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode().values[0]
    print('Most Popular End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + df['End Station']).mode().values[0]
    print('Most Popular Start to End Station Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time in seconds:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time in seconds:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_count = df['User Type'].value_counts()
    print('Count of user types:', user_count)

    # TO DO: Display counts of gender
    check1 = "Gender" in df
    if check1 == True:
        gender_count = df['Gender'].value_counts()
        print('Count of gender:', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    check2 = "Birth Year" in df
    if check2 == True:
        earliest_yob = df['Birth Year'].min()
        print('Earliest year of birth:', earliest_yob)
        most_recent_yob = df['Birth Year'].max()
        print('Most recent year of birth:', most_recent_yob)
        most_common_yob = df['Birth Year'].mode()
        print('Most common year of birth:', most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    data = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

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


if __name__ == "__main__":
	main()
