#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'all']
days = ['monday' , 'tuesday', 'wednesday' , 'thursday', 'friday', 'saturday' , 'sunday', 'all']


# In[3]:


def get_filters(): 
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
      
    while True:
        city=input('\nWhich city data would you like to see? Chicago, New York City or Washington?\n').lower()
        if city not in CITY_DATA:
            print('This is not a valid City. Please try again.')
        else:
            break
       
    while True:
        month=input('\nChoose a month between January and June. Or type "all" to see data for all six months.\n' ).lower()
        if month not in months:
            print('This is not a valid month. Please try again.')
        else:
            break
      
    while True:
        day=input('\nwhich day data would you like to see? You can also type "all" to see all the days of the week.\n' ).lower()
        if day not in days:
            print('This is not a valid day. Please try again.')
        else:
            break

    print('-'*40)   
    return city, month, day


# In[4]:


city, month, day = get_filters()


# In[5]:


city, month, day


# In[6]:


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

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]
    return df


# In[7]:


df = load_data(city, month, day)


# In[ ]:





# In[8]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    df['Start Time'] = pd.to_datetime(df['Start Time'])

    common_month = df['month'].mode()[0]
    print('The most common month is:' , (common_month))

    day = df['day_of_week']
    common_day_of_week= df['day_of_week'].mode()[0]
    print('The most common day of week is' , (common_day_of_week))
 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', (common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


time_stats(df)


# In[10]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is:' , (common_start_station))

    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station is:' , (common_end_station))
 
    frequent_trip_comb = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most frequent combination of Start Station and End Station Trip is:' , (frequent_trip_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)  


# In[11]:


station_stats(df)


# In[12]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:' , (total_travel_time))

    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:' , (mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[13]:


trip_duration_stats(df)


# In[14]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    counts_user_types = df['User Type'].value_counts()
    print('\nThe count of user types is:\n', (counts_user_types))


    if 'Gender' not in df:
        print('\nThere is no Gender data for this city\n')
    else:
        counts_gender = df['Gender'].value_counts()
        print('\nThe count of gender is:', (counts_gender))



    if 'Birth Year' not in df:
        print('There is no Birth Year data for this city. No earliest birth year will be provided.')
    else:        
        earliest_year = df['Birth Year'].min()
        print('\nThe earliest year of birth is:' , (earliest_year)) 


    if 'Birth Year' not in df:
        print('There is no Birth Year data for this city. No recent birth year will be provided.')
    else:
        recent_year = df['Birth Year'].max()
        print('The most recent year of birth is:' , (recent_year)) 




    if 'Birth Year' not in df:
        print('There is no Birth Year data for this city. No common birth year will be provided.\n')
    else:
        common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is:' , (common_year)) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[15]:


user_stats(df)


# In[16]:


def get_raw_data(df):
    """Display 5 lines of raw data upon user's request"""
    pd.set_option('display.max_columns',200)
    i = 0

    while True:
        raw_data = input('\nWould you like to see raw data for the city you selected? Enter yes or no.\n').lower() 
        if raw_data == 'yes':
             print(df.iloc[i:i+5])
   
             i+=5
        if raw_data == 'no':
            break

get_raw_data(df)


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        get_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()            

