# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Laura Astola, laura.astola@accenture.com
Date: 14.8.2025
Version: 0.1
Type: MLPClassifier(random_state=1, max_iter=300)
Citation details: https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

The model and encoder can be found in the model folder.

## Intended Use
The model should be able to predict whether the salary is below or above a threshold, based on several
personal attributes, such as age, education, workclass, sex etc.

## Training Data
70% of the data in census.csv, which can be found in the data folder. This data contains 14 predictive columns and 'salary' as the target column.
One-hot labels were used for categorical columns.
Train-test splitting was done in ratio of 70/30.

## Evaluation Data
30% of the data in census.csv

## Metrics
_Please include the metrics used and your model's performance on those metrics._
We used the following metrics to measure performance.
Precision: 0.2421 | Recall: 1.0000 | F1: 0.3898

## Ethical Considerations
Although data does not contain information that could be traced back to a person/organization, we should be mindful of the implications of how personal attributes such as sex, race or working class can affect the salary of a person.

## Caveats and Recommendations
For model selection, also cross validation could be used, which may improve the results further.
Also experimenting with several other classifiers can increase the F1 score. That recall was very high and precision low, may indicate that the data was simply unbalanced and the generaization is low. 
