# Market_Basket_Analaysis
Market basket analysis is a data mining technique that uncovers hidden relationships between items purchased at the same time.
This analysis can be used to inform product marketing, pricing strategies, loyalty program design and inventory planning.
For example, if two items are often purchased together, the business can use this knowledge to promote those items together in order to improve customer satisfaction and drive more sales. 

As far as the implementation of algorithms for the above output, Apriori and FP-Growth are the two main algorithms used for market basket analysis.
Apriori is a simple algorithm that works by finding frequent itemsets in a transaction dataset and deriving association rules from them.
FP-Growth is a more complex algorithm that requires some pre-processing prior to execution and compresses the transaction dataset into a prefix tree structure for faster processing of frequent patterns. 

Additionally, Grid search can be used for automated optimization of the parameters for market basket analysis, such as support, confidence and lift values.
Grid search works by testing different combinations of parameters on a small sample of data to determine the optimal values for each parameter. The results can then be used to refine the code using multiple runs with different min_support values and sorting the results accordingly.

## Prerequisites 

- Python 3
- Numpy 
- Pandas

## Installing

Clone the GitHub repository: 
```
git clone git@github.com:mussiehaile/market-basket-analysis.git
```

Install the required packages: 
```
pip install -r requirements.txt
```
