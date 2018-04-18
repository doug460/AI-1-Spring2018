'''
Created on Apr 7, 2018

@author: DougBrownWin
'''

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import math



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

def getEdu(country, data):
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
        country = 'Burma'
        
    
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None
    
    return data[indx][0,1]

def getEduExpense(country, data):
    # get terrorism indx
    # country, value, date
    if country == 'United States of America':
        country = 'United States'
    elif country == 'Viet Nam':
        country = 'Vietnam'
    elif country == 'DR Congo':
        country = 'Congo, Republic of the'
    elif country == 'U.K.':
        country = 'United Kingdom'
    elif country == 'Myanmar':
        country = 'Burma'
    elif country == 'Nigeria':
        return 14.84
    elif country == 'Egypt':
        return 11
    elif country == 'Iraq':
        return 6.43
    elif country == 'Afghanistan':
        return 12.51
        
        
    
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None
    
    string = data[indx][0,1]
    string = string.replace('%','')
    return float(string)

def getBirth(country, data):
    # get terrorism indx
    # country, value, date
    if country == 'United States of America':
        country = 'United States'
    elif country == 'Viet Nam':
        country = 'Vietnam'
    elif country == 'DR Congo':
        country = 'Congo, Republic of the'
    elif country == 'U.K.':
        country = 'United Kingdom'
    elif country == 'Myanmar':
        country = 'Burma'
        
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None
    
    string = data[indx][0,1].replace(' per 1,000 people','')

    return float(string)

def getPoverty(country, data):
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
        country = 'Burma'
    elif country == 'Italy':
        return 7.51
        
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None
    
    string = data[indx][0,1].replace('%\n per 1 million people','')

    return float(string)

def getArmed(country, data):
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
        country = 'Burma'
    elif country == 'Tanzania':
        return 0.728
    elif country == 'Iraq':
        return 8.71
    elif country == 'Afghanistan':
        return 0.902
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None

    return data[indx][0,1]

def getMilitaryExpense(country, data):
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
        country = 'Burma'
    elif country == 'Egypt':
        return 1.6673
    elif country == 'Iran':
        return 3.0
    elif country == 'South Korea':
        return 2.6
        
    
    # get indx of all of country values
    indx = data[:,0] == country

    # check if country exists
    if sum(indx) == 0:
        return None
    
    stuff = data[indx][0,1].replace('%','')
    stuff = float(stuff)

    return stuff

def normData(data):
    # basically just zero mean unit variance data
    # INPUTS: is array of data set
    # OUTPUTS: simply normalized data
    data -= np.mean(data)
    data = data/np.std(data)
    return data

    

if __name__ == '__main__':
    pass
    # dir to save stuff
    dir = '/home/dabrown/Dropbox/Current/School 2018 Spring/CPA/project/figs_info/'

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
    
    #~~~~~~~~~~~~~~~~~~ years of edu ~~~~~~~~~~~~~~#
    eduBase = pd.read_csv('educationAmount.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ % money on edu ~~~~~~~~~~~~~~#
    eduExp_base = pd.read_csv('educationExpense.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ % birth rate / 1000 ~~~~~~~~~~~~~~#
    birth_base = pd.read_csv('birth.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ % % below poverty line/ 1M peeps ~~~~~~~~~~~~~~#
    poverty_base = pd.read_csv('poverty.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ % armed forces / 1000 ~~~~~~~~~~~~~~#
    armed_base = pd.read_csv('armedForces.csv').as_matrix()
    
    #~~~~~~~~~~~~~~~~~~ % military expense % of GDP ~~~~~~~~~~~~~~#
    miliaryExpense_base = pd.read_csv('militaryExpense.csv').as_matrix()
    
    # combined matrix of all data
    varNum = 10
    data = np.zeros((varNum, dataLeng))
    
    # list of countries :P
    for indx, country in enumerate(countrys):
        # get data
        data[0,indx] = getHomicide_rate(country, homBase)
        data[1,indx] = getDisposable(country, incomeBase)
        data[2,indx] = getInfant_mort(country, infantMort_base)
        data[3,indx] = getTerror(country, terrorIndx_base)
        data[4,indx] = getEdu(country, eduBase)
        data[5,indx] = getEduExpense(country, eduExp_base)
        data[6,indx] = getBirth(country, birth_base)
        data[7,indx] = getPoverty(country, poverty_base)
        data[8,indx] = getArmed(country, armed_base)
        data[9,indx] = getMilitaryExpense(country, miliaryExpense_base)
        
    # check most recent data set
    # if there is missing, throw error
    indx = np.isnan(data[varNum - 1,:])
    if(sum(indx) > 0):
        print('These countries do not exists in recent data set')
        print(countrys[indx])
        raise Exception('country DNE in data')
    
    
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
        plt.savefig(dir + 'cumulitive_sum.png')
        
        
        
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
        plt.savefig(dir + 'countries.png')
    
    
    # output z stuff!!
    out = open(dir + 'info.txt', 'w')
    string = 'PCs (%variance explained) are:\n'
    for indx, array in enumerate(eigVect):
        string += '%2d (%%%5.2f): [' % (indx, varExplained[indx])
        for value in array:
            string += '%7.4f, ' % (value)
        string += ']\n'
    
    print(string)
    out.write(string)
        
    out.close()
        
    
    # show stuff
    #plt.show()
























    
    
    
    
    