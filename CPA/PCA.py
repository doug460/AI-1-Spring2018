'''
Created on Apr 7, 2018

@author: DougBrownWin
'''

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt



def getHomicide_rate(country, data):
# function get get homicide data
# INPUT:
#    country: string of country name :P
#    data: array of homicide data
# OUTPUT:
#    kills: most recent number of homicides
    
    # make adjustments for specific countries
    if country == 'Russia':
        country = 'Russian Federation'
        
    if country == 'DR Congo':
        country = 'Democratic Republic of the Congo'
    
    if country == 'Iran':
        country = 'Iran (Islamic Republic of)'
    
    if country == 'U.K.':
        country = 'United Kingdom of Great Britain and Northern Ireland'
    
    if country == 'Tanzania':
        country = 'United Republic of Tanzania'
        
    if country == 'South Korea':
        country = 'Republic of Korea'
        
    
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        string = 'country DNE: %s in homicide Data' % (country)
        raise Exception(string)
    
    # get years
    years = data[indx]
    # get most recenter number of homicides
    maxYear_indx = years[:,1].argmax()
    kills = years[maxYear_indx, 2]
    
    return(kills)

def getDisposable(country, data):
    # see get homicide for format
    if country == 'United States of America':
        country = 'United States'
        
    elif country == 'Viet Nam':
        country = 'Vietnam'
    
    elif country == 'DR Congo':
        country = 'Democratic Republic of the Congo'
    elif country == 'U.K.':
        country = 'United Kingdom'
    elif country == 'Myanmar':
        country = 'Burma'
    
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        string = 'country DNE: %s in disposable income Data' % (country)
        raise Exception(string)
    
    # get rid of '$' and ','
    valueString = data[indx][0,1]
    valueString = valueString.replace('$', '')
    valueString = valueString.replace(',','')
    
    return float(valueString)
    
def getInfant_mort(country, data):
    # see get infant mortality reate
    # country, year, variant, value
    # value is / 1000 live births
    
    if country == 'Russia':
        country = 'Russian Federation'
        
    if country == 'DR Congo':
        country = 'Democratic Republic of the Congo'
        
    if country == 'Iran':
        country = 'Iran (Islamic Republic of)'
    
    if country == 'U.K.':
        country = 'United Kingdom'
    
    if country == 'Tanzania':
        country = 'United Republic of Tanzania'
        
    if country == 'South Korea':
        country = 'Republic of Korea'
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        string = 'country DNE: %s in infant mortality Data' % (country)
        raise Exception(string)
    
    return data[indx][0,3]

def getTerror(country, data):
    # get terrorism indx
    # country, value, date
    if country == 'United States of America':
        country = 'United States'
    elif country == 'Viet Nam':
        country = 'Vietnam'
    elif country == 'DR Congo':
        country = 'Democratic Republic of the Congo'
    elif country == 'U.K.':
        country = 'United Kingdom'
    elif country == 'Myanmar':
        return 4.96
        
    
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        string = 'country DNE: %s in terror indx Data' % (country)
        raise Exception(string)
    
    return data[indx][0,1]
    
def normData(data):
    # basically just zero mean unit variance data
    # INPUTS: is array of data set
    # OUTPUTS: simply normalized data
    data -= np.mean(data)
    data = data/np.std(data)
    return data

    

if __name__ == '__main__':
    pass

    # get to data dir
    os.chdir('excel')
    
    # population is the only xlsx file, rest are csv
    popFile = 'population.xlsx'
    popData = pd.read_excel(popFile).as_matrix()
    
    # get list of countries, this will hold all info
    countrys = popData[:,0]
    
    # data length
    dataLeng = countrys.size
    
    
    #~~~~~~~~~~~~~~~~~~ HOMICDIDES ~~~~~~~~~~~~~~#
    # country, year, count, rate
    # homice number/100,000
    homBase = pd.read_csv('homicide.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ disposable income ~~~~~~~~~~~~~~#
    incomeBase = pd.read_csv('disposableIncome.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ infant mortality ~~~~~~~~~~~~~~#
    # per 1000 births
    infantMort_base = pd.read_csv('infantMortality.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ terror indx ~~~~~~~~~~~~~~#
    terrorIndx_base = pd.read_csv('terrorIndx.csv').as_matrix()
    
    
    # combined matrix of all data
    varNum = 4
    data = np.zeros((varNum, dataLeng))
    
    # list of countries :P
    for indx, country in enumerate(countrys):
        # get data
        data[0,indx] = getHomicide_rate(country, homBase)
        data[1,indx] = getDisposable(country, incomeBase)
        data[2,indx] = getInfant_mort(country, infantMort_base)
        data[3,indx] = getTerror(country, terrorIndx_base)
    
    # normalize data
    # zero mean unit variance
    for indx in range(varNum):
        data[indx,:] = normData(data[indx,:])
    
    # get covariance matrix
    # becomes varNum x varNum
    cov = np.cov(data)
    
    # get eignvalues and vectors
    eigVal, eigVect = np.linalg.eig(cov)
    
    # sort eigen vecotrs by eigen values
    eigPairs = [(eigVal[indx], eigVect[:,indx]) for indx in range(varNum)]
    
    # basically sort based off of first element and put in reverse order so decending order
    eigPairs.sort(key=lambda x: x[0], reverse=True)
    for indx in range(len(eigPairs)):
        eigVal[indx] = eigPairs[indx][0]
        eigVect[indx,:] = eigPairs[indx][1]
    
    # look at explaining variance
    total = sum(eigVal)
    varExplained = eigVal * 100 / total
    cumsum = np.cumsum(varExplained)
    
    # plot explained variance
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(6, 4))
    
        plt.bar(range(varNum), varExplained, alpha=0.5, align='center',
                label='individual explained variance')
        plt.step(range(varNum), cumsum, where='mid',
                 label='cumulative explained variance')
        plt.ylabel('Explained variance ratio')
        plt.xlabel('Principal components')
        plt.legend(loc='best')
        plt.title('Explained Variance')
        plt.tight_layout()
        
        
        
    # now going to prject data onto frist two eigen vectors
    project = eigVect[:,0:2]
    data = data.transpose()
    dataProject = np.dot(data, project)
    
    
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(10, 6))
        plt.scatter(dataProject[:,0],dataProject[:,1])
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.legend(loc='lower center')
        plt.title('%d%% of Variance' % (cumsum[1]))
        for indx, country in enumerate(countrys):
            plt.annotate(country, (dataProject[indx,0], dataProject[indx,1]))
        plt.tight_layout()

    
    print('Principal component 1: ', eigVect[:,0])
    print('Principal component 2: ', eigVect[:,1])
    
    
    
    # show stuff
#     plt.show()
    
    
    
    
    