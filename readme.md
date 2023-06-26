Tech Stack Used :

1# Django & Sqlite

why: Instead of creating Apis , used django form and returned the response and show to the user.

It can easily be converted into API , as request and response changes , but Logic is used Same

    
Used Sqlite as data points are not that much as if data grow we can use MongoDB.

    http://127.0.0.1:8000/
Input :

    {
    "tier_id": 1 , # 1 , 2 for tier-1 , tier 2 
    "tenure_id": 1 , # 1 , 2 , 3  for 1 year, 2- year , 3 year
    "sum_insured": 300000, # chould have used choices here as well for sum insured
    "adults": [55,34],
    "children": [1,2,3]
    }

Output : 
    
     {
        "total_amount": 10 ,
        result : [{'base_rate': 22107, 'floater_discount': 0, 'discounted_rate': 22107, 'description': 'Adult 1', 'age': 56}, {'base_rate': 8838, 'floater_discount': 50, 'discounted_rate': 4419.0, 'description': 'Adult 2', 'age': 21}]
        }


Installation:

1# install docker
2# docker compose up
3# run docker file for installing python 



extras:

if i wanted to use flask and mongo DB.

for query i would use Sqlalchemy for DB query
and created two apis:

1# Config : (gives all the options) GET
    url : localhost:8000/insurance/config 

    output : 
        {   
        "sum_insured":{
                1:300000,
                2:400000,
                3:500000},
        "city":{
                        1:"tier-1",
                        2:"tier-2"}
                
        "tenure":{
                                1:"1 year",
                                2:"2 year"}
                  
            }

2# Calculate premium :POST

    url : localhost:8000/insurance/calculate-premium

    input :
         {
        "tier_id": 1 , 
        "tenure_id": 1 ,  
        "sum_insured": 300000,  
        "adults": [55,34],
        "children": [1,2,3]
    }

    output : 
       {
            
            result : [{'base_rate': 22107, 'floater_discount': 0, 'discounted_rate': 22107, 'description': 'Adult 1', 'age': 56}, {'base_rate': 8838, 'floater_discount': 50, 'discounted_rate': 4419.0, 'description': 'Adult 2', 'age': 21}]
            }
     


This does not have separate frontend