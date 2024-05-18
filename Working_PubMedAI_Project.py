import streamlit as st
import os 
from dotenv import load_dotenv
from openai import OpenAI
from metapub import PubMedFetcher

load_dotenv()

NCBI_API_KEY = os.getenv("NCBI_API_KEY")
OPEN_AI_API_KEY = os.getenv("OPEN_AI_KEY")

if NCBI_API_KEY is None or OPEN_AI_API_KEY is None:
    raise ValueError("API keys not set. Please check your environment.")

client = OpenAI(api_key=OPEN_AI_API_KEY)

keyword = st.text_input("Enter the search for PubMed AI:")
num_of_articles = st.number_input("How many articles would you like to read?", min_value=1, step=1)
summary_focus = st.selectbox("Choose the focus for the summary:", ["Conclusion", "Methodology", "Results", "General"])

if st.button('Fetch and Summarize'):
    fetch = PubMedFetcher()
    pmids = fetch.pmids_for_query(keyword, retmax=num_of_articles)
    st.write(f"PubMed IDs for articles related to '{keyword}':")
    for pmid in pmids:
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        st.markdown(f"[PMID {pmid}]({link})", unsafe_allow_html=True)

    articles = {}
    summaries = {}

    for pmid in pmids:
        article = fetch.article_by_pmid(pmid)
        articles[pmid] = {
            'title': article.title,
            'abstract': article.abstract
        }

        abstract = articles[pmid]['abstract']
        if abstract:
            prompt_text = f"Please summarize the {summary_focus.lower()} of this paper based on the abstract: {abstract}"
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt_text}],
                    max_tokens=150
                )
                summary = response.choices[0].message.content.strip()
                summaries[pmid] = summary
            except Exception as e:
                st.write(f"Failed to generate summary for PMID {pmid}: {str(e)}")
        else:
            summaries[pmid] = "No abstract available."

    st.write("\nGenerated summaries:")
    for pmid, summary in summaries.items():
        st.write(f"Title: {articles[pmid]['title']}")
        st.write(f"PMID {pmid}: {summary}\n")

<<<<<<< HEAD
#   streamlit run "PubMed_AI/In Progress/Working_PubMedAI_Project.py"
=======

#Functionality Changes: 

#Need to reformat streamlit app for headings
#Need to add more options for the summary focus
#Need to add a function to save the summaries to a file
#Need to add a function to display the saved summaries
#Need to add a function to delete the saved summaries
#Need to add a function to search for a specific summary
#Need to add a function to display the specific summary
#Want to make it more user friendly
#Want to add more error handling
#Ideally, would like to have the function summarize the entire paper not the abstract
#Would like to add a function to display the full article
#Would like to add a function to display the full article in a new tab
>>>>>>> 96053b9 (Reinitialized repository in the correct directory)
