
Biology=['Nutrition','Respiration']
Chemistry=['Valencies','Reactions']
History=['Napoleon']

def topic_selector(subject):
    if subject=="History":
        return History
    
    elif subject=="Chemistry":
        return Chemistry
    
    elif subject=="Biology":
        return Biology
    
    else:
        return "No Topic Was Selected"

def concept_selector(subject, index):
    index -= 1
    if subject=="History":
        return History[index]

    elif subject=="Chemistry":
        return Chemistry[index]

    elif subject=="Biology":
        return Biology[index]

    else:
        return "No Topic Was Selected"
    