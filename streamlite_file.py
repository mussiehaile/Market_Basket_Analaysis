import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from csv import reader
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
st.write("""
# Market Basket Analysis for small grocery data
""")
st.sidebar.header('User input parameters')



min_support= st.sidebar.slider('support',0.0,1.0,0.02,step=0.01)
min_length= st.sidebar.slider('lenght',1,5,2,step=1)
lift= st.sidebar.slider('lift',1.0,4.0, 1.0,step=0.1)  
confidence =st.sidebar.slider('confidence',0.2, 1.0, 0.5,step=0.1) 



#min_threshold= st.sidebar.slider('min_threshold',0.01,1.0,0.5,step=0.01)

st.subheader('User input parameters')
st.write(min_support,min_length)

groceries = []
with open(r'C:\\Users\Nardos\Downloads\archive/groceries.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        groceries.append(row)


# fitting the list and converting the transactions to true and false
encoder = TransactionEncoder()
transactions = encoder.fit(groceries).transform(groceries)
# converting the true and false to 1 and 0
transactions = transactions.astype('int')
# converting the transactions array to a datafrmae
df1 = pd.DataFrame(transactions, columns=encoder.columns_)
#displaying the one hot encoded data
st.subheader('One hot encoded data')
st.write(df1)

# applying the apriori algorithm
frequent_itemsets = apriori(df1.astype('bool'), min_support=0.05, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
# displaying frequent_items
st.subheader('frequent items genrated by apriori')
st.write(frequent_itemsets)

# sorting the dataframe
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
st.write(len(frequent_itemsets))
# getting support and length from the user
st.write(f"frequent_itemsets with **min_support** of {min_support} and  **length** of {min_length}")

def frequency(support,length):

  k=frequent_itemsets[ (frequent_itemsets['length'] == length) &(frequent_itemsets['support'] >= support) ][0:5]
  return k

st.write(frequency(min_support,min_length))

# finding top 10 association rules with minimum support of 2%
rules = association_rules(frequent_itemsets, metric='support', min_threshold=0.05,support_only=True)
rules
st.write(rules)
st.write('finding association for a given value of min support ')

#def Filter_rule(support,lift,confidence):
  #filtered=rules[
  #    (rules['support'] >= support) & (rules['lift'] > lift ) & (rules['confidence'] > confidence)]
 # return filtered


#st.write(f"frequent_itemsets with **min_support** of {min_support} and  **lift** of {lift} and **confidence** of {confidence}")
#st.write(Filter_rule(min_support,lift,confidence))