import google.generativeai as genai


def send_query(query):
    genai.configure(api_key="YouNeedToFillThis")
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction='''Convert query to SQL. User wants to search candidates in the ATS/CRM and the table is tblcandidate. 
        The columns are : firstname, lastname, emailid, contactnumber, locality, city, state, country, relevantexperience, position, languageskills, skill. 
        The column names are self explnatory, but just in case, relevantexperience is a number field to denote years of experience, your goal is to make sure the english query is translated to the most efficient sql query. 
        Also help the recruiter by filling in the fields as you deem fit that would perfect results like filling the skills with the role oriented attributes or inclusion of synonyms to broaden the search. 
        Also limit the results to 30 and return the firstname, lastname, email, phone, skills, current position only. ONLY RETURN THE SQL
        There is also the candidate_work_experience_t table which holds the particular candidate's work experience, it has the columns, candidate_id, title, work_company_name, work_location. The candidate_id refers to id in tblcandidate.
        There is also the candidate_education_t table which holds the particular candidate's education history, it has the columns candidate_id, institute_name, educational_qualification, educational_specialization,education_location,education_description. Here the candidate_id refers to id in tblcandidate
        Use work and education as per the user's needs
        Also don't return candidates with no values in first name, last name as the DB can have incomplete data. We will ignore this
        You are not supposed to generate any INSERT, UPDATE, DELETE queries''',
    )
    response = model.generate_content(query).text
    return response
