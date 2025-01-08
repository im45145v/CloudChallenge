## Architecture
                        ┌───────────────────────────────────┐                                     
                        │                                   │                                     
                        │ SportsData.io backend server      │                                     
                        │                                   │                                     
                        └───────┬─────────────────▲─────────┘                                     
                                │                 │                                               
                                │                 │                                               
                                └───►─────────┼───┘                                               
                                    │         │                                                   
                                    │ NBA API │                                                   
                                    └┬─────▲──┘                                                   
                                     │     │                                                      
                                     │     │                                                      
                            API      │     │                                                      
                            Response │     │   API Request                                        
                                     │     │                                           ┌──────┐   
                                     │     │                                   ┌──────►│      │   
                                     │     │                                   │       └──────┘   
                                     │     │                                   │                  
┌────────────────────┐      ┌────────▼─────┴─────┐    ┌───────────────────┐    │                  
│                    │      │                    │    │                   │    │                  
│ Amazon Event Bridge│      │ AWS lambda function│    │  Amazon SNS Topic ┼────┤                  
│ Schedule Rule      │      │                    │    │                   │    │                  
│                    │      │                    │    │                   │    │                  
└────────┬───────────┘      └────▲───────────┬───┘    └──────────▲────────┘    │                  
         │                       │           │                   │             │        ┌────────┐
         └───────────────────────┘           └───────────────────┘             └───────►│        │
                                                                                        └────────┘

## Goal
Use Amazon SNS, AWS Lambda and Python, Amazon EvenBridge and NBA APIs to updates via emails and SMS to subscribers.

## Workings
- Live data using external API
- Sends sms/email to people
- Amazon EventBridge for corn jobs

