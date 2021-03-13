# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:35:29 2021

@author: j.wadhwani
"""

def gender_to_numeric(x):
    if x=='Female': return 2
    if x=='Male':   return 1
    if x=='Other':   return 0
    
def rel_experience(x):
    if x=='Has relevent experience': return 1
    if x=='No relevent experience':   return 0
    
def enrollment(x):
    if x=='no_enrollment'   : return 0
    if x=='Full time course':   return 1 
    if x=='Part time course':   return 2 
    
def edu_level(x):
    if x=='Graduate'       :   return 0
    if x=='Masters'        :   return 1 
    if x=='High School'    :   return 2 
    if x=='Phd'            :   return 3 
    if x=='Primary School' :   return 4 
    
def major(x):
    if x=='STEM'                   :   return 0
    if x=='Business Degree'        :   return 1 
    if x=='Arts'                   :   return 2 
    if x=='Humanities'             :   return 3 
    if x=='No Major'               :   return 4 
    if x=='Other'                  :   return 5 
    
def experience(x):  
    if x>20     :   return 21
    else : return x
    
def company_t(x):
    if x=='Pvt Ltd'               :   return 0
    if x=='Funded Startup'        :   return 1 
    if x=='Early Stage Startup'   :   return 2 
    if x=='Other'                 :   return 3 
    if x=='Public Sector'         :   return 4 
    if x=='NGO'                   :   return 5 
    

def company_s(x):
    if x<10          :   return 0
    if x>=10 and x<=49        :   return 1 
    if x>=50 and x<=99         :   return 2 
    if x>=100 and x<=499       :   return 3
    if x>=500 and x<=999       :   return 4 
    if x>=1000 and x<=4999     :   return 5 
    if x>=5000 and x<=9999     :   return 6
    if x>=10000       :   return 7 
    
def last_job(x): 
    if x>4           :   return 5
    else : return x
    
