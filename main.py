import pandas as pd

df = pd.read_csv("./dataset.csv")

#Dividing data by version

current_df = df[df["version"] == "Current"]
previous_df = df[df["version"] == "Previous"]

#Reviewing market cap

market_cap_previous = previous_df["market_cap"].sum()
market_cap_current = current_df["market_cap"].sum()

print("Current market cap: " + str(market_cap_current))
print("Previous market cap: " + str(market_cap_previous))

gap = market_cap_current - market_cap_previous

if gap > 0:
    print("Market cap has increased by: " + str(gap))
else:
    print("Market cap has decreased by: " + str(gap))

#Reviewing market cap by industry

market_cap_by_industry_previous = previous_df.groupby("industry")["market_cap"].sum()
market_cap_by_industry_current = current_df.groupby("industry")["market_cap"].sum()

print("Current market cap by industry: ")
print(market_cap_by_industry_current)
print("Previous market cap by industry: ")
print(market_cap_by_industry_previous)

gap_by_industry_market_cap = market_cap_by_industry_current - market_cap_by_industry_previous

max_market_cap_industry = gap_by_industry_market_cap.idxmax(), gap_by_industry_market_cap.max()
min_market_cap_industry = gap_by_industry_market_cap.idxmin(), gap_by_industry_market_cap.min()

print("Market cap by industry has increased or decreased by:")
print(gap_by_industry_market_cap)
print("industry with highest market cap gap: " + str(max_market_cap_industry))
print("industry with lowest market cap gap: " + str(min_market_cap_industry))

#Revieweing impact
impact_previous = previous_df["impact"].sum()
impact_current = current_df["impact"].sum()

print("Current Impact: " + str(impact_current))
print("Previous Impact: " + str(impact_previous))

gap = impact_current - impact_previous

if gap > 0:
    print("Impact has increased by: " + str(gap))
else:
    print("Impact has decreased by: " + str(gap))

#Reviewing impact by industry
impact_by_industry_previous = previous_df.groupby("industry")["impact"].sum()
impact_by_industry_current = current_df.groupby("industry")["impact"].sum()

print("Current Impact by industry: ")
print(impact_by_industry_current)
print("Previous Impact by industry: ")
print(impact_by_industry_previous)

gap_by_industry_impact = impact_by_industry_current - impact_by_industry_previous

max_impact_industry = gap_by_industry_impact.idxmax(), gap_by_industry_impact.max()
min_impact_industry = gap_by_industry_impact.idxmin(), gap_by_industry_impact.min()

print("Impact by industry has increased or decreased by:")
print(gap_by_industry_impact)
print("industry with highest impact gap: " + str(max_impact_industry))
print("industry with lowest impact gap: " + str(min_impact_industry))

#Reviewing impact by Goal
impact_by_goal_previous = previous_df.groupby("goal")["impact"].sum()
impact_by_goal_current = current_df.groupby("goal")["impact"].sum()

print("Current Impact by goal: ")
print(impact_by_goal_current)
print("Previous Impact by goal: ")
print(impact_by_goal_previous)

gap_by_goal_impact = impact_by_goal_current - impact_by_goal_previous

max_impact_goal = gap_by_goal_impact.idxmax(), gap_by_goal_impact.max()
min_impact_goal = gap_by_goal_impact.idxmin(), gap_by_goal_impact.min()

print("Impact by goal has increased or decreased by:")
print(gap_by_goal_impact)
print("goal with highest impact gap: " + str(max_impact_goal))
print("goal with lowest impact gap: " + str(min_impact_goal))


#Merging result for summary view
merged_data = pd.merge(current_df, previous_df, on=['company_name', 'goal'], suffixes=('_current', '_previous'))

merged_data['impact_difference'] = merged_data['impact_current'] - merged_data['impact_previous']

top_changes = merged_data[['company_name', 'goal', 'impact_current', 'impact_previous', 'impact_difference']].sort_values(by='impact_difference', ascending=False)

head_top_changes = top_changes.head(10)

print(head_top_changes)


#####Analysis on impact#####

descriptive_current = current_df["impact"].describe()
descriptive_previous = previous_df["impact"].describe()

print("Current version stats:")
print(descriptive_current)
print("Previous version stats:")
print(descriptive_previous)