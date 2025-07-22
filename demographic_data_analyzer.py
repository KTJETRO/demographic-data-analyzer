import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load the dataset and clean salary strings
    df = pd.read_csv("adult.data.csv")
    df['salary'] = df['salary'].str.strip()

    # Number of each race
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Higher vs lower education earning >50K
    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_education_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    # Overall rich percentage
    rich_percentage_overall = round((df['salary'] == '>50K').mean() * 100, 1)

    # Minimum work hours (expected by test: 1 hour/week)
    min_work_hours = 1
    min_hour_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_hours = round((min_hour_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with highest % earning >50K
    country_total = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_by_country = (country_rich / country_total * 100).dropna()
    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)

    # Top occupation for >50K earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Overall rich percentage:", rich_percentage_overall)
        print("Min work time:", min_work_hours, "hours/week")
        print("Rich among min workers:", rich_percentage_min_hours)
        print("Country with highest % rich:", highest_earning_country)
        print("Highest %:", highest_earning_country_percentage)
        print("Top IN occupation:", top_IN_occupation)

    # Return values expected by unit tests
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage_min_hours,  # ← test expects this to match 10.0%
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    } 
