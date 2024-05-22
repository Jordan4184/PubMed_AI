# PubMed AI Summarizer

This project is a **Streamlit** web application that fetches and summarizes PubMed articles using OpenAI's **GPT-3.5** model. The application provides a user-friendly interface for searching PubMed and obtaining succinct summaries of selected articles based on user preferences.

## Features

1. **Keyword-based Search**: Users can input a keyword to search for relevant articles on PubMed.
2. **Article Limit**: Users can specify the number of articles they wish to read.
3. **Summary Focus**: Users can choose the focus of the summary, such as the conclusion, methodology, results, or a general summary.
4. **Fetch and Summarize**: The application fetches the articles from PubMed and uses GPT-3.5 to generate summaries based on the selected focus.

## Installation

### Prerequisites

1. **Python**: Make sure you have Python installed (>= 3.7).
2. **Streamlit**: Install Streamlit using `pip`.
3. **Dotenv**: Install `python-dotenv` using `pip`.
4. **OpenAI**: Install `openai` using `pip`.
5. **Metapub**: Install `metapub` using `pip`.

### Setup

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Install Dependencies**:

    ```bash
    pip install streamlit python-dotenv openai metapub
    ```

3. **Environment Variables**:

   - Create a `.env` file in the root directory.
   - Add your API keys for OpenAI and PubMed:

    ```bash
    OPEN_AI_KEY=<Your OpenAI API Key>
    NCBI_API_KEY=<Your NCBI API Key>
    ```

## Usage

1. **Run the Application**:

   ```bash
   streamlit run app.py

# Using the Application:

**Keyword Search:** Enter the keyword to search for articles.
**Number of Articles:** Specify the number of articles to fetch.
**Summary Focus:** Choose the focus for the summary.
**Fetch and Summarize:** Click the button to fetch articles and generate summaries.

### How it Works

**Fetching Articles:** The app uses metapub to fetch articles from PubMed based on the given keyword.
The user specifies the number of articles to fetch.

**Generating Summaries:** The app uses OpenAI's GPT-3.5 model to generate summaries based on the chosen focus.
The focus can be "Conclusion", "Methodology", "Results", or "General".

**Display:** The app displays the article titles and their respective summaries.

## Future Enhancements

- Need to reformat streamlit app for headings
- Need to add more options for the summary focus
- Need to add a function to save the summaries to a file
- Need to add a function to display the saved summaries
- Need to add a function to delete the saved summaries
- Need to add a function to search for a specific summary
- Need to add a function to display the specific summary
- Want to make it more user friendly
- Want to add more error handling
- Ideally, would like to have the function summarize the entire paper not the abstract
- Would like to add a function to display the full article

### Acknowledgments
Streamlit
OpenAI
Metapub
