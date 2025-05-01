# Fundamental-Beta-Estimation
Beta Re-imagined
The standard procedure to estimate betas is to regress stock returns (R j ) against market returns (R m ):
R j = a + b*R m
where b is the slope of the regression, corresponding to beta of the stock and measures the
riskiness of the stock
Beta has two problems: (1) it has high standard error; (2) it reflects the firm’s business mix and financial
leverage (and possibly other relevant risk characteristics) over the (past) period of the regression, not
the present, nor is it predictive of future riskiness.
Solutions to the Regression Beta problem:
- Modify the index used to estimate the beta (What exactly is the problem with using S&P500? What might be better?)
- Use standard deviation of stock prices instead of regression against an index
- Include accounting information of the company to predict the future
- Use accounting earnings or revenues (which are less noisy than stock prices) to estimate beta
- Use accounting measures of risk (liquidity risk ratios, solvency risk ratios, financial leverage ratios, operating leverage estimates, profitability ratios, book-to-market, price/earnings

Objectives
- Obtained 10 years of WRDS data 2000-2010
- Divided into Training sample 2000-2008 &amp; Test sample 2008-2010
- Obtain/compute returns R j for each firm-year and corresponding market returns R m .
- Obtain “Standard” beta b from R j = a + b*R m
- [Try also a year fixed effect in the equation in addition to R m ]
- Use a and b above to estimate returns RS j in the Test sample. RS j is the return for firm j
using a and the standard estimation of beta b.
- Obtain a and slopes b 1 through b 5 from R j = a f + b 1 *Liquidity + b 1 *Solvency + b 3 *(Debt/Equity) + b 4 *Profitability + b 5 *Book-to-Market
- All the accounting ratios above are to be used in their standardized (z-score) forms with respect to the average of that ratio across all firms
- [In the future, also try adding R m to the above independent variables to examine the incremental effect.]
- For now, use a f and b 1 through b 5 from above to estimate RF j in the Test sample. RF j is the return for firm j using a f and b 1 through b 5 , i.e., the estimate of return based on fundamentals.
- Compute (RS j – R j ) and (RF j – R j ), i.e., the differences of the estimated returns (of each model) from the actual (historical) returns.
- Plot differences (RS j – R j ) and (RF j – R j ) on y-axis against
- SIC code groupings on x-axis (i.e., plot the differences by industry groupings).
- [First-digit SIC codes will yield 10 groups ‘0’ through ‘9’. Using two-digit SIC codes – if we can fit them on the x-axis – will provide about 83 groups]

Python Notebook Guide:

autosearch: Intakes DJIA 10Ks and outputs .csv file with complexity word counts for every firm from 2012-2021
funddata: Intakes fundamental accounting variables from CCM and merges with Beta/Price/Return DataFrame (need retprc & sprtrn .csv files for beta calculation), then outputs combined .csv file
finalmerge: Loads the previous .csv files created for further analysis

Data can be found here: https://drive.google.com/drive/folders/1odY6iixbBp0mGhqyNei-n10uW3BxIZkm?usp=drive_link
