import openai
import os
import streamlit as st

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function to generate text using GPT-3
def generate_text(prompt):
    # Set up the GPT-3 engine and parameters
    engine = "text-davinci-002"
    max_tokens = 100
    temperature = 0.5
    
    # Generate text from the prompt using GPT-3
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    text = response.choices[0].text.strip()
    
    return text

# Define a function to get user input for a destination
def get_destination():
    # Prompt the user for a destination
    st.write("Let's plan your next vacation!")
    destination = st.text_input("Where would you like to go?")
    return destination

# Define a function to generate suggestions for activities and things to do at the destination
def get_activities(destination):
    # Generate suggestions for activities and things to do at the destination
    prompt = f"Here are some activities and things to do in {destination}:\n"
    prompt += generate_text(f"What are some popular tourist attractions in {destination}?")
    prompt += "\n\n"
    prompt += generate_text(f"What are some local events happening in {destination} during your travel dates?")
    prompt += "\n\n"
    prompt += generate_text(f"What are some outdoor activities you can do in {destination}?")
    
    return prompt

# Define a function to generate suggestions for accommodations at the destination
def get_accommodations(destination):
    # Generate suggestions for accommodations at the destination
    prompt = f"Here are some recommended accommodations in {destination}:\n"
    prompt += generate_text(f"What are some highly rated hotels in {destination}?")
    prompt += "\n\n"
    prompt += generate_text(f"What are some unique lodging options in {destination}?")
    
    return prompt

# Define a function to generate a travel itinerary for the destination
def get_itinerary(destination):
    # Generate a travel itinerary for the destination
    prompt = f"Here's a sample travel itinerary for your trip to {destination}:\n"
    prompt += generate_text(f"What are some must-see attractions in {destination}?")
    prompt += "\n\n"
    prompt += generate_text(f"What are some good restaurants to try in {destination}?")
    prompt += "\n\n"
    prompt += generate_text(f"What are some fun activities to do in {destination} at night?")
    
    return prompt

# Create the Streamlit app
st.title("Plan Your Next Vacation!")
destination = get_destination()
if destination:
    activities_prompt = get_activities(destination)
    accommodations_prompt = get_accommodations(destination)
    itinerary_prompt = get_itinerary(destination)

    st.subheader("Activities and Things to Do")
    st.write(activities_prompt)

    st.subheader("Accommodations")
    st.write(accommodations_prompt)

    st.subheader("Travel Itinerary")
    st.write(itinerary_prompt)
