import pandas as pd
import re


df = pd.read_csv(r"\\tsfsspcweb\SPC_Web\SPC_Dashboards\Critical Charts\backup_of_daily_SPACE_search\06_10_24\F10N_SPC_SearchByFolder_Non_Prod.csv", encoding='ISO-8859-1', keep_default_na=False)
df = df[["Ch Id", "Valuations & Events", "Valuation Parameter"]]
df = df[df["Valuations & Events"].str.contains(r'^0E|\d{2}$|\d{2}[A-Z]$')]


#df_CA_missing.to_csv(r"\\tsfsspcweb\SPC_Web\SPC_Dashboards\SPACE_CF_Cleanup\CAG_dev\Output\F10N_test.csv")

# Sample data
data = {'Valuation Parameter': ['3,4,45,46();60(3;2;3, 4;no);61(3;2;5, 17;no)'],
        'Valuations & Events': ['3,4,60,61\
                    (ETAAlarm_ET State Change_MF_EXC_STG,QualFailure_Non-VCDM Qual,eCAP:F10N_DF_Observation_Q:MRG);\
                45,46,53,54\
                    (ETAAlarm_ET State Change_MF_EXC_STG,LotHold,QualFailure_Non-VCDM Qual,eCAP:F10N_DF_Observation_Q:MRG);\
                5,17']}
 
# Split each cell by ');\'
df['Valuation Parameter'] = df['Valuation Parameter'].str.split('\);')


def extractRepeatedValuations(parameterPartition: str): #for each partition
    SPC_REPEATED_VIOLATIONS = ['60', '61', '62', '63']

    if parameterPartition.endswith("(X") or parameterPartition.endswith("(") or \
        parameterPartition.endswith("()") or parameterPartition.endswith("(X)"):
        return ['']
        #return [item.replace('(','') if '(' else item in item for item in parameterPartition]

    if all(not valuation==parameterPartition.split('(')[0] for valuation in SPC_REPEATED_VIOLATIONS):
        return ['']
    parameterPartition = parameterPartition.split(';')

    parameterPartition[0] = parameterPartition[0][0:2]
    parameterPartition.remove(parameterPartition[1])
    parameterPartition = parameterPartition[0:2]

    #split by comma, then remove whitespaces if there are any
    parameterPartition[1] = [x.strip() for x in parameterPartition[1].split(",")]

    return parameterPartition


def summariseRepeatedValuations(row): #for each row (each row contains multiple partitions)
    if len(row)==1:
        return ['']
    row = row[1:]
    row = list(map(extractRepeatedValuations, row))

    return row


#returns a list of 2 items
# 1st item is a list containing all valuations with assigned CAs
# 2nd item is a list of valuations with NO assigned CAs
def assignedEvents(row: str):
    row = row.split(';')

    #for each partition, split by '(' and take the first item
    #basically extract the numbers and remove the chunks inside the parentheses
    #eg 3,4,5(abcd) becomes 3,4,5
    #leaves out the last partition
    #as it's assumed that the last partition contains just numeric characters with no parentheses behind
    row[:-1] = list(map(lambda x: x.split('(')[0], row[:-1]))
    row[:-1] = list(map(lambda x: x.split(','), row[:-1]))
    
    #----------------------------------------------------------------------
    #combine all valuations with assigned CAs into a list
    for item in row[1:-1]:
        row[0].extend(item)
        row.remove(item)    
    
    row[-1] = row[-1].split(',')
    return row


def checkCA(row):
    try:
        if len(row['Valuations & Events']) == 1:
            return row['Valuations & Events'][0]
        
        to_be_disabled = row['Valuations & Events'][1]
        
        if len(row['Valuation Parameter'])==1 and row['Valuation Parameter'][0]=='':
            return to_be_disabled
       
        for repeated_valuation in row['Valuation Parameter']:
            if repeated_valuation[0] in row['Valuations & Events'][0] or repeated_valuation==''\
                or len(repeated_valuation)<2:
                pass
            
            else:
                for valuation in repeated_valuation[1]:
                    if valuation not in row['Valuations & Events'][0]:
                        to_be_disabled.append(valuation)
    except:
        print(f"{row.name}: {row}")
    
    return to_be_disabled


df['Valuation Parameter'] = df['Valuation Parameter'].apply(summariseRepeatedValuations)
df['Valuations & Events'] = df['Valuations & Events'].apply(assignedEvents)
df['testlength']=df.apply(checkCA, axis=1)
df.to_csv(r"\\tsfsspcweb\SPC_Web\SPC_Dashboards\SPACE_CF_Cleanup\CAG_dev\Output\F10N_test.csv")


