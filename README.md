# myprojects

I performed data profiling on the Zomato dataset to understand its structure, completeness, and quality using various Python packages.

1️⃣ Data Profiling
Used ydata-profiling (formerly pandas-profiling) to generate an automated exploratory data analysis (EDA) report, which included:

1. Summary statistics of numerical and categorical columns
2. Missing values and duplicate records
3. Correlation analysis between features

Used sweetviz to create an interactive report for feature distribution, missing values, and relationships.


#ZOMATO Dashboard

The Zomato Dashboard provides a comprehensive view of key metrics and insights derived from the Zomato dataset. The dashboard aims to give users an intuitive understanding of restaurant ratings, price categories, and other critical data points, helping make data-driven decisions.

Key Features & Metrics:
#Restaurant Ratings: The dashboard showcases ratings of restaurants categorized into "High Rated" and "Low Rated" based on the Extracted Rating column. Ratings greater than 3.8 are classified as High Rated, while others are considered Low Rated.

#Price Categories: Restaurants are categorized into "Expensive" or "Cheap" based on their price range. This classification is determined by the Amount column, where any value greater than 500 is labeled as Expensive.

#Visualization: Key metrics are displayed through a series of interactive visuals, such as:

#Bar charts showing the count of restaurants in each rating and price category.
#Pie charts for distribution of high-rated and low-rated restaurants.
Tables with detailed restaurant information.

#Data Transformations and Calculations:

Utilized DAX (Data Analysis Expressions) for creating calculated columns, including:

#Extracted Rating: A custom DAX formula was used to extract numerical ratings from strings like "4.1/5".
#Rating Category: Based on the extracted rating, a DAX expression classifies restaurants as High Rated or Low Rated.
#Price Category: A DAX formula categorizes the restaurants into Expensive or Cheap based on the price value.

#Outcome & Insights:

The Zomato Dashboard enables users to analyze restaurant ratings and pricing in an easy-to-understand, visual format. By utilizing DAX for dynamic calculations, the dashboard helps identify trends and correlations, empowering better decision-making in restaurant selection.
