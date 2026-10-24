# AWS Student Builder Group - AI/ML Recruitment Task

## Dataset Overview
- **Source**: Synthetic Housing Dataset (250 rows, 4 core features)
- **Features**: `area_sqft`, `bedrooms`, `age_years`
- **Target**: `price_usd`

## Workflow Summary
1. **Data Cleaning**: Handled missing values (5%) by imputing column-wise medians to maintain robust central tendencies without outlier distortion.
2. **Feature Engineering**: Used vectorized NumPy array computations to calculate `price_per_sqft` and performed min-max scaling.
3. **Exploratory Analysis**: Correlation mapping showed strong linearity between area and price ($r \approx 0.94$).
4. **Model Building**: Fitted a multiple Linear Regression model using `scikit-learn` and verified accuracy via exact mathematical computation using the closed-form Normal Equation.

## Results
- **MAE**: ~$20,000
- **RMSE**: ~$24,800
- **R² Score**: ~0.965