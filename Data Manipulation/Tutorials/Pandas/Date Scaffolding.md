# Advanced Pandas: Date Scaffolding
## Introduction
#### When you're working with dates, there may come a time when some dates may be missing or you would like to change the level of detail from months to days. To help with these issues, there is an advanced data manipulation techniques known as _Date Scaffolding_. Although Pandas doesn't have a specified function to help with this process, it still provides us with the tools necessary to fill in the missing data.
## Files Used in This Tutorial
#### To help keep the examples in this tutorial consistent, please click the link below to download the input file used in this tutorial:
- [Input File 1](Files/Player-Training.zip)
- [Input File 2](Files/Amortization-Schedule.zip)
## Date Scaffolding Techniques
### Filling in Missing Dates
#### - As mentioned above, sometimes dates will be missing in your dataset. There are various ways to go about solving this problem so we'll start with the most simple method:
##### 1. Setup your Project:
        import pandas as pd
        players = pd.read_csv('[file path]')
        players.head()
![This is an img](Pictures/players_prev.png)
##### 2. Organize DataFrame to Identify Missing Dates:
        players = players.sort_values(by=['Date', 'Player'])
        players = players[players['Player'] == 'Player 1'].head(25)
        players.head(10)
![This is an img](Pictures/players_prev2.png)
##### 3. Convert Date Convert "Date" Column to Date Data Type and Set as Index:
        players['Date'] = pd.to_datetime(players['Date'])
        players = players.set_index('Date')
        players.head(10)
![This is an img](Pictures/players_idx.png)
##### 4. Group by Player and Resample the Date Index and Convert to Discrete Measure:
        players = players.groupby('Player').resanple('1D').mean()
        players = players.reset_index()
        players.head(10)
![This is an img](Pictures/players_resample.png)

#### **Although it may be difficult to tell, the NaN values in the 4th step indicate values that were added after the resample.**

### Changing the Level of Detail in a DataFrame
#### - When you are working with any time-series datasets, it can be difficult to understand the level of detail needed for your analysis. The first step in this process is to understand the problem you're trying to solve and the questions being asked by stakeholders. In the example below, we will be changing the level of detail for a mortgage payment schedule, better known as an "Amortization Schedule":
##### 1. Setup your project:
        import pandas as pd
        import numpy as np
        from datetime import date
        import tqdm
        from dateutil.relativedelta import relativedelta
        import warnings
        warnings.filterwarnings('ignore')
        schedule = pd.read_csv('[file path]')
        schedule.head()
##### 2. Set Value for the Start Date:
        schedule['Today'] = '07/11/2022'
        schedule.head()
##### 3. Create a Date Field to Show Repayment Amount:
        schedule[' Monthly Repayment Amount'] = schedule['Monthly Payment'] * (schedule['% of Monthly Repayment going to Capital'] /100)
        schedule.head()
##### 4. Create a Field to Show # of Months Remaining on Mortgage:
        schedule['# of Months Remaining'] = round(schedule['Capital Repayment Remaining'] / schedule['Monthly Repayment Amount'], 0)
        schedule['# of Months Remaining'] = schedule['# of Months Remaining'].astype(int)
        schedule.head()
##### 5. Create a Field to Show When the Mortgage Will Be Paid Off:
        def add_months(start_date, delta_period):
                end_date = start_date + relativedelta(months=delta_period)
                return end_date
        tqdm.pandas()
        schedule['Today'] = pd.to_datetime(schedule['Today'])
        schedule['Capital Repayment Date'] = schedule.progress_apply(lambda row: add_months(row['Today'], row['# of Months Remaining'], axis = 1)
        schedule['Capital Repayment Date'] = schedule['Capital Repayment Date'].df.strftime('%m/%d/%Y')
        schedule.head()
##### 5. 
