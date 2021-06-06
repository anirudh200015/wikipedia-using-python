import wikipedia
from wikipedia import summary
#query=input("what is it that you are searching: ")
#text=wikipedia.search(query,results=10,suggestion=False)  # suggestion= false will give a list of result 
                                                            # suggestion =true will give a tuple
query=input("which topic summary you want:  ") 
no_of_sentence=input(" No of  sentences required (less than 10) ")
result=wikipedia.summary(query,no_of_sentence)
print("As per wikipedia:- ")                                                       
print(result)