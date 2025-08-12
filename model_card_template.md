# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
MLPClassifier(random_state=1, max_iter=300)
from https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

## Intended Use
Introductory & experimental usage while getting acquainted with python framework fastAPI

## Training Data
census.csv

## Evaluation Data
census.csv

## Metrics
_Please include the metrics used and your model's performance on those metrics._
# %%
Precision: 0.2421 | Recall: 1.0000 | F1: 0.3898

## Ethical Considerations
Although data does not contain information that could be traced back to a person/organization, we should be mindful of the implications of how personal attributes such as sex, race or working class can affect salary.

## Caveats and Recommendations
This is purely intended for training and learning of fastAPI. 
