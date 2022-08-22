# ICU SURVIVAL PREDICTION
![dashboard](assets/sc.png)
## Table of Contents

  - [Business problem](#business-problem)
  - [Quick glance at the results](#quick-glance-at-the-results)
  - [Limitation and what can be improved](#limitation-and-what-can-be-improved)
  - [Run Locally](#run-locally)
  - [Repository structure](#repository-structure)

## 1. Business problem
<a name = "intro"></a>
The challenge is to create a model that uses data from the early hours of intensive care unit admission to predict patient survival. In clinical practice, estimates of mortality risk can be useful in triage and resource allocation, to determine appropriate levels of care, to prepare discussions with patients and their families around expected outcomes and help policymakers identify and make better health policies.

### 1.1 Objective
Objective of this project is to create a model predict patient survival with better prediction probability than the current apache, model that uses minimize apache features, transparent i.e easy to explain, and generalizability with Less complexity. As current systems often lack generalizability beyond the patients on whom the models were developed, and The models are often proprietary, costly to use (APACHE scoring system...), and suffer from opaque algorithms.

### 1.2 Data Source
MIT's GOSSIS community initiative, with privacy certification from the Harvard Privacy Lab, has provided a dataset of more than  90000 hospital Intensive Care Unit (ICU) visits from patients, spanning a one-year time frame. This data is part of a growing global effort and consortium spanning Argentina, Australia, New Zealand, Sri Lanka, Brazil, and more than 200 hospitals in the United States.

![data](assets/data.png)


## 2. Quick glance at the results
### Exploratory analysis
**1. Percentage Representation of hospital_death**
![Bmi](assets/eda_ps.png)
- The target feature (hospital_death) is highly imbalance with with a ```91%``` survival rate and ```9%``` non survival
- 
**2. Body mass index category**
|||
|-------------------	    |------------------	|
|![Bmi](assets/bmi.jpg)|![Bmi](assets/eda_bmi.png)|
- From the  dataset most of the patient are overweight and above

- ```27%``` of the the patient in the observation has a normal BMI while ```4%``` are underweight

**3. Distribution of Height, weight, BMI and Age**
![dist](assets/eda_ds.png)
- From the above box plot Age seems to a little left skewed with few outliers.
- BMI (body max index) and weight  are right skewed with alot of outliers
- Height has normally distribution. 
- The mean ```age```, ```bmi```, ```height``` and ```weight```  are ```62.48```, ```29.15```, ```169.66cm``` and ```83.98kg``` respectively.
**4. Age group**
|||
|-------------------	    |------------------	|
|![Bmi](assets/age.png)|![Bmi](assets/eda_age.png)|
- ```63%``` patient from the observation are aged above 60 years old adults
### Model performance
**1. ROC_AUC Metrics**
![Bmi](assets/pf.png)

**2. Best 3 models**
The Top 3 with the best performance are

| Model     	            | ROC_AUC score 	    | Recall score|
|-------------------	    |------------------	|-----|
| Logistic Regression   	| 0.706            |65%|
| Gradient boosting    	  | 0.778	            |78%|
| Light Gradient boosting       | 0.778       |78%|


**3. Confusion matrix and ROC_AUC of LightGB classifier**

![Confusion matrix](assets/cs_auc.png)

- Faster traning time.
- Lower memory usage.
- Support parrallisation on distributed systems.
- Better prediction probability.

### 2.1 Metrics Used: Recall and ROC_AUC
Why choose Recall and ROC_AUC as metrics:
  - Since the objective of this problem is to  predict patient survival in the early hour of icu admision, Recall will be a better metric as inaccurate prediction of low survival (false negative) will have dire consequences.
  - ROC_AUC so we can be able to set the best threashold to capture low survival(True positives).
  - Imbalance between dataset.
### 2.2 Limitations And What Can Be Improved
- Minimum domain knowledge.
- Highly imbalanced dataset.
- Plenty of missing variables.
- Hyperparameter tuning: I used RandomSearchCV to save time but could be improved by couple of % with GridSearchCV.
- More data: Alot of factor contrribute to a patient survival in the ICU. Factor such, Qaulity of hospital, experience of doctor etc are not captured in the dataset. 

## 3. Run Locally
```bash
# clone the project.
git clone https://github.com/Sachimugu/ICU-survival.git
```
```bash
# Create a conda virtual environment called icuprediction and install all the packages.
conda create --name icuprediction pandas sklearn Django lightgbm
```
```bash
# Activate the conda environment.
conda activate icuprediction
```
```bash
# enter the Script  directory.
cd ./site/django-web-app
```
```bash
# run server.
python manage.py runserver
```
Go to http://127.0.0.1:8000/ on web-brower
## Repository structure
```
├── assets
│   ├── age.png
│   ├── bmi.jpg
│   ├── Bmi.png
│   ├── cm.png
│   ├── data.png
│   ├── gcs.jpg
│   ├── gcs.png
│   ├── GCS_Subscales.png
│   ├── roc.png
│   └── sc.png
├── Datasets
│   ├── clean_dataset
│   ├── clean_dataset.csv
│   ├── Data Dictionary.csv
│   ├── dataset.csv
│   └── model_metrics.csv
├── Model
│   └── pickel_lgb_model.pkl
├── Notebook
│   ├── 1_Data_Wranglin_and_Analysis.ipynb
│   ├── 2_Preprocessing_and_ML_Model.ipynb
│   └── US_States_ID.json
├── Presentation
│   ├── report.pdf
│   └── reportp.pptx
└── README.md
```
#### Contribution
Pull requests are welcome! For major changes.

### Contact
<a href="mailto:sachimugu@gmail.com"> ![](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white) </a>
<a href="https://www.linkedin.com/in/achimugu-a-79aa8a18a/"> ![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) </a>
<a href="https://twitter.com/achimugu_a"> ![](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white) </a>
<a href="https://medium.com/@sachimugu"> ![](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white) </a>

