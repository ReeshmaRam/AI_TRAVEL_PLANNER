from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import groq_api_key
llm=ChatGroq(api_key=groq_api_key,model="llama-3.3-70b-versatile",temperature=0.3)
itineary_prompt=ChatPromptTemplate([("system","You are a travel assistant . Create a day itineary for {city} based on user interest: {interests} . Provide a brief , bulleted itineary")
                                    ,("human","create an itineary for my day trip")])

def generate_itineary(city : str,interests : list[str])-> str:
   response=llm.invoke(
      itineary_prompt.format_messages(city=city,interests=",".join(interests))

   )
   return response.content