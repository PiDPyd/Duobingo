chem_questions = {
    "Valencies":{
        "Mcq": {1: ["Question: What is valency of Hydroxide ion","a)1","b)-1","c)2","d)-2","2"],
                2: ["Question: What is the Valency of Phosphate ion","a)-2","b)-1","c)-3","d)none","3"]}
    },
    "Reactions": {
        "Mcq": {1: ["Question: Are combustion reactions combination reactions?", "1) Yes", "2) No", "3) Both", "4) None","1"],
                2: ["Question: What is the reaction of thermite welding?", "1) Fe2O3+2Al -> Al2O3+2Fe", "2) Al2O3+2Fe -> Fe2O3+2Al", "3) Fe3O4+2Cu -> CuO+2Fe", "4) None","Answer: Fe2O3+2Al -> Al2O3+2Fe"]
                },
        "Flashcards": {1: ["Identifty the Brown Fumes in Lead Salt Heating Reaction","NO2"],
                       2: ["What is used in black and white photography","AgBr"]
                      },

        "Fill_in_blank": {1: ["Balance this Chemical Reaction H2 + O2 = _H2O","2H2O"],
                          2: ["This type of reaction ____ reacts with sunlight","Photolytic"]
                         }
    }}

def question_answer(subject,topic,ptype,question_number):
    if subject == "Chemistry":
        chem_topic = chem_questions[str(topic)]
        question_type = chem_topic[str(ptype)]
        length=len(question_type)
        question_answer = question_type[question_number]
        return question_answer
    
def question_len(subject,topic,ptype):
    if subject == "Chemistry":
        chem_topic = chem_questions[str(topic)]
        question_type = chem_topic[str(ptype)]
        length=len(question_type)
        return length
    
