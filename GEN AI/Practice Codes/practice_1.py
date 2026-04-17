from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal,Optional

model = ChatOpenAI(model="gpt-4o")

class review(TypedDict):
    domain:Annotated[str,"Give the topic the whole resume is based on"]
    name:Annotated[str,"Name of the applicant"]
    age: Annotated[Optional[str], "Return the age ONLY if explicitly stated in the resume. Otherwise return null."]
    skills:Annotated[list[str],"The skillset of the applicant"]
    internship:Annotated[list[str],"The onternship the applicant is done"]


new_model = model.with_structured_output(review)

resume= '''
Aarav Mehta, a final-year Bachelor of Technology student in Computer Science from Savitribai Phule Pune University (2022 to 2026, CGPA: 8.7/10), is an aspiring data scientist based in Pune, Maharashtra, India, applying on 18 April 2026 for entry-level data science roles. He possesses a strong foundation in programming languages such as Python, R, and SQL, along with hands-on experience in libraries and tools including NumPy, Pandas, Scikit-learn, TensorFlow, Matplotlib, and Seaborn, complemented by expertise in data visualization using Power BI and Tableau and database management systems like MySQL and MongoDB.

During his academic journey, Aarav has worked on several impactful projects, including a customer churn prediction model achieving 87 percent accuracy using Logistic Regression and Random Forest algorithms, a sentiment analysis system leveraging NLP techniques such as TF-IDF and Naive Bayes to classify social media data, and a sales forecasting model based on ARIMA that improved prediction accuracy by 20%. His practical exposure is further strengthened by his internship as a Data Science Intern at TechNova Solutions Pvt. Ltd., Bangalore (May to July 2025), where he performed data cleaning, analysis, dashboard creation, and contributed to predictive modeling for business optimization.

In addition to technical skills, Aarav has demonstrated excellence through achievements such as being a finalist in a National Data Analytics Hackathon 2025, completing certifications like the Google Data Analytics Professional Certificate, Machine Learning by Andrew Ng, and IBM Data Science with Python, and ranking among the top 5 percent in beginner-level Kaggle competitions. With strong problem-solving abilities, analytical thinking, communication skills, and a collaborative mindset, he is fluent in English and Hindi and aims to contribute effectively to data-driven decision-making in a professional environment.

'''

result = new_model.invoke(resume)

print(result["name"],result["domain"],result["age"],result["skills"],result["internship"])