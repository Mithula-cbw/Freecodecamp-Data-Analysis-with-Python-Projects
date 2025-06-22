import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    def percentage(df: pd.DataFrame, column: str, value: str) -> float:
        return round((df[df[column] == value].shape[0] / df.shape[0]) * 100, 1)

    # Race count
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == "Male"]['age'].mean(), 1)

    # % with Bachelor's degree
    percentage_bachelors = percentage(df, 'education', 'Bachelors')

    # Higher and lower education
    edu_high = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(edu_high)]
    lower_education = df[~df['education'].isin(edu_high)]

    # % earning >50K
    higher_education_rich = percentage(higher_education, 'salary', '>50K')
    lower_education_rich = percentage(lower_education, 'salary', '>50K')

    # Min hours per week
    min_work_hours = df['hours-per-week'].min()

    # % of rich among min-hour workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = percentage(num_min_workers, 'salary', '>50K')

    # Country with highest % of rich
    country_total = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich / country_total) * 100

    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # Top occupation in India for >50K
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
