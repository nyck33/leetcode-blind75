# -*- coding: utf-8 -*-
#argparse allows the parsing of command line arguments
import argparse
#utility functions for cs 6515 projects
#import GA_ProjectUtils as util

 
"""
Initialize the table to be used to record the best value possible for given 
item idx and weight
NOTE : this table must be 2 dimensional (i.e. T[x][y])
"""
def initTable(numItems, maxWt):
    #Replace the following with your code to initialize the table properly!
    # items are rows and weights are cols
    T = [[x for x in range(maxWt+1)] for y in range(numItems+1)]

    # 0 for first row and column
    for i in range(1):
        for j in range(len(T[0])):
            T[i][j] = 0

    return T

"""
Build item iterator - iterator through all available items
    numItems : number of items
"""
def buildItemIter(numItems):
    #Replace the following with your code to build the item iterator!
    # can do for x in items:
    # 1 idx'ing
    items = range(1, numItems+1)
    return items

"""
Build weight iterator - iterator of all possible integer weight values
    maxWt : maximum weight available
"""
def buildWeightIter(maxWt):
    #Replace the following with your code to build the weight iterator!
    weights = range(0, maxWt+1)
    return weights

"""
Define the subproblem to solve for each table entry - set the value to be maximum for a given
item and weight value
    T : the table being populated
    iterWt : weight from iteration through possible weight values
    itemIDX : the index of the item from the loop iteration
    itemWt : the weight of the item
    itemVal : the value of the item
"""
#todo: table is 0 index, items is 1, weights is 1
def subProblem(T, iterWt, itemIDX, itemWt, itemVal):
    # table, w, itmIdx, itemWt,
    # itemIDX is 1 so no row above it
    prev_wt = iterWt - itemWt

    if itemIDX == 1:
        if prev_wt >= 0:
            T[itemIDX][iterWt] = max(0, T[itemIDX-1][prev_wt] + itemVal)
        else:
            T[itemIDX][iterWt] = 0
    else:
        #Replace the following with your code to solve the subproblem appropriately!
        #todo: do iterWt - itemWt on its own to stay in bounds of array < 0
        if prev_wt >=0:
            T[itemIDX][iterWt] = max(T[itemIDX-1][iterWt], T[itemIDX-1][prev_wt] + itemVal)
        else:
            T[itemIDX][iterWt] = T[itemIDX-1][iterWt]

    return T[itemIDX][iterWt]

"""
Construct list of tuples of items that should be chosen.  

    T : the populated table of item values, indexed by item idx and weight
    items : list of items
    maxWt : maximum weight allowed
"""
def buildResultList(T, items, maxWt):
    """"""
    # check T
    #for m in range(len(T)):
     #   print(T[m])

    result = []
    numItems = len(items)

    """
    start at bottom right T(n,W), if T(i,w) come from row above don't include
    row item, go to T(i-1, w)
    Else include item, go to T(i-1, w - w_i) and repeat
    """
    i = numItems
    w = maxWt

    while i > 0 and w > 0:
        # did not come from prev. row so include row item
        curr = T[i][w]
        prev = T[i-1][w]
        if curr != prev:
            row_item, itemWt, itemVal = items[i]
            result.append(items[i])
            i -= 1
            w -= itemWt
        else:
            i -= 1



    #Your code goes here to build the list of chosen items!
    return result

"""
Solve the knapsack problem for the passed list of items and max allowable weight
DO NOT MODIFY THE FOLLOWING FUNCTION
NOTE : There are many ways to solve this problem.  You are to solve it
        using a 2D table, by filling in the function templates above.  
        If not directed, do not modify the given code template.
""" 
def knapsack(items, maxWt):
    numItems = len(items)
    #initialize table properly
    table = initTable(numItems, maxWt)
    #build iterables
    #item iterator
    itemIter = buildItemIter(numItems)
    #weight iterator
    weightIter = buildWeightIter(maxWt)
    
    for itmIdx in itemIter:
        #query item values from list
        item, itemWt, itemVal = items[itmIdx]
        for w in weightIter:
            #expand table values by solving subproblem
            table[itmIdx][w] = subProblem(table, w, itmIdx, itemWt, itemVal)
            
    #build list of results - chosen items to maximize value for a given weight
    return buildResultList(table, items, maxWt)

"""
main
"""
def main():	
    #DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    #You may change default values, but any values you set will be overridden when autograded
    parser = argparse.ArgumentParser(description='Knapsack Coding Quiz')
    parser.add_argument('-i', '--items',  help='File holding list of possible Items (name, wt, value)', default='defaultItems.txt', dest='itemsListFileName')
    parser.add_argument('-w', '--weight',  help='Maximum (integer) weight of items allowed', type=int, default=400, dest='maxWeight')
   
    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-n', '--sName',  help='Student name, used for autograder', default='GT', dest='studentName')
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')
    args = parser.parse_args()
    
    #DO NOT MODIFY ANY OF THE FOLLOWING CODE
    #configData is a dictionary that holds relevant info for the problem
    itemsList = util.buildKnapsackItemsDict(args) 
    #calculate optimal knapsack loadout
    itemsChosen = knapsack(itemsList, args.maxWeight)
    #display results
    util.displayKnapSack(args, itemsChosen)

if __name__ == '__main__':
    main()