#Validation of big and small data in transport sector using traffic flow data in London



## 1 Aim and Objective ##

![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/aim.png)

![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/obj.png)

## 2 Data Source ##

### 2.1 Small Data: Automatic Traffic Counter (ATCs) data from TfL

#### Visualization of counter in the London road network

![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/QGIS.png)
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/QGIS2.png)

#### Distribution of counter data volume in different boroughs
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Counts%20of%20counters%20by%20Borough.png)

#### Distribution of counter data volume on different road classes
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Counts%20of%20counters%20by%20road_class.png)
#### Example from smalldata
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Example%20from%20smalldata.png)

#### Histogram of counter data volume:not normally distributed
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Histogram%20of%20counter.png)

#### Box plot of counter data volume categrized in boroughs
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/box_s.png)

### 2.2 Big Data: Estimated from GPS data from mobile phone

#### Example from bigdata
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Example%20from%20bigdata.png)

#### Histogram of big data volume: skewed distribution
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Histogram%20of%20big.png)

#### Box plot of big data volume categrized in boroughs
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/box_b.png)

### 2.3 Summary of final data
#### Descriptive statistics for all data
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/descri.png)


#### Correlation matrix
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/correlation.png)

## 3 Regression Results: Mixed Cross-section ## 

### 3.1 Summary of conclusions
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/summ.png)


### 3.2 OLS regressions results 

#### OLS regression based on aggregate data
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/1.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Regression%20of%20small_data%20on%20big_data.png" alt="Image 2" width="50%">
</div>

#### OLS regression Residuals vs Fitted Values
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/resi.png)

#### OLS regression based on aggregate data reverted the logarithm transformation
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/2.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/Regression%20of%20log_smalldata%20on%20log_bigdata.png" alt="Image 2" width="50%">
</div>


#### OLS regression categorized by borough
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/hamA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/hamB.png" alt="Image 2" width="50%">
</div>

<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/lamA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/lamB.png" alt="Image 2" width="50%">
</div>

<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/wesA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/wesB.png" alt="Image 2" width="50%">
</div>

#### OLS regression categorized by raod classes
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/straA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/straB.png" alt="Image 2" width="50%">
</div>
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/locA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/locB.png" alt="Image 2" width="50%">
</div>

#### OLS regression cross-categorized by road classes and borough

![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/categorized_by_RoadClass_and_Borough.png)

#### OLS regression consider weekend, road classes and borough as variables
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/varA.png)
### 3.3 Other regressions results 
Borough 0:Lambeth 1: TowerHamlets 2:Wesminster 

roadclasses 0:LocalRoad 1:StrategyRoad

#### Generalized Linear Models (GLM) based on aggregate data
<div style="display: flex; justify-content: space-between;">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/GLMA.png" alt="Image 1" width="50%">
  <img src="https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/GLM results.png" alt="Image 2" width="50%">
</div>

#### Quantile Regression consider weekend, raod classes and borough as variables
![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/quanA.png)


## 4 Improvment ##

![Aaron Swartz](https://raw.githubusercontent.com/wwCARww/DissertationProject/main/images/impro.png)


