## Architecture
```
                         ┌──────────────────────────────┐                                     
                         │ SportsData.io backend server │                                     
                         └──────┬─────────────────▲─────┘                                     
                                │                 │                                               
                                │                 │                                               
                                │   ┌─────────┐   │                                           
                                └──►│ NBA API │───┘                                                   
                                    └┬─────▲──┘                                                   
                                     │     │                                                      
                                     │     │                                                      
                                 API │     │ API                                                      
                            Response │     │ Request                                        
                                     │     │                                            ┌──────┐   
                                     │     │                                    ┌──────►│ SMS  │   
                                     │     │                                    │       └──────┘   
                                     │     │                                    │                  
┌─────────────────────┐      ┌────────▼─────┴─────┐    ┌───────────────────┐    │                  
│ Amazon Event Bridge │      │ AWS lambda function│    │ Amazon SNS Topic  ┼────┤                  
│ Schedule Rule       │      │                    │    │                   │    │                  
└────────┬────────────┘      └────▲───────────┬───┘    └──────────▲────────┘    │                  
         │                        │           │                   │             │       ┌────────┐
         └────────────────────────┘           └───────────────────┘             └──────►│ E-mail │
                                                                                        └────────┘
```
## Goal
Use Amazon SNS, AWS Lambda and Python, Amazon EvenBridge and NBA APIs to updates via emails and SMS to subscribers.

## Workings
- Live data using external API
- Sends sms/email to people
- Amazon EventBridge for corn jobs

## Approach
1. Created SNS topic
2. Created a basic Role to access SNS topic
3. Create, Test and deploy lambda function from [code](src/main.py)
4. Used Event bridge for corn job
