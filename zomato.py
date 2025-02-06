# -*- coding: utf-8 -*-
"""Zomato.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17G70Zrf8pn2LE-OxyQn3wQbAjoRB1n-S
"""

import os
os.chdir('/content/sample_data')
os.getcwd()

!pip install sweetviz

import pandas as pd
df = pd.read_csv("Zomato-data-.csv")
df.head()

import sweetviz as sv

# Generate report
report = sv.analyze(df)

# Show report
report.show_html("sweetviz_report.html")

pip install ydata-profiling

from ydata_profiling import ProfileReport

# Generate profile report
profile = ProfileReport(df, explorative=True)

# Save report to HTML
profile.to_file("data_profiling_report.html")

pip install feature-engine

from feature_engine.selection import DropCorrelatedFeatures

# Drop highly correlated features (threshold = 0.85)
selector = DropCorrelatedFeatures(threshold=0.85)
df_selected = selector.fit_transform(df)

print(df_selected.head())

