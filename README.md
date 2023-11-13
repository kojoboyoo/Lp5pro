readme # Sentiment Analysis of COVID Vaccination Tweets with Hugging Face Transformers
 
## Overview
 
This sentiment analysis project leverages state-of-the-art language models, including RoBERTa, BERT, and DistilBERT, for sentiment classification on tweets related to COVID-19 vaccination. The models are fine-tuned on a labeled dataset, and a Gradio app is developed to provide an interactive interface for sentiment analysis.
 
![image](https://github.com/doeabla/Sentiment_analysis/assets/137217264/0f3b372c-b486-415b-91ad-f35d38983a0a)
 
## Features
 
- **RoBERTa, BERT, DistilBERT Models:** Utilizes powerful pre-trained models for sentiment analysis, including RoBERTa, BERT, and DistilBERT.
- **Training Data:** The models are trained on a dataset containing tweets specifically related to COVID-19 vaccination sentiments.
- **Gradio App:** An interactive Gradio app is developed to allow users to input text and obtain sentiment predictions using the RoBERTa model.
- **Hugging Face Integration:** Leverages Hugging Face's Model Hub for easy access to pre-trained language models, including RoBERTa, BERT, and DistilBERT.
 
## Requirements
 
- Python 3.x
- Required Python packages specified in requirements.txt
- Hugging Face Transformers Library
- Gradio Library
 
## Usage
 
Download the datasets used for this project in the dataset folder.
- The dataset consists of tweets collected and classified through Dataset.
- Tweets have been labeled as positive (👍), neutral (🤐), or negative (👎).
- Usernames and web addresses have been removed for privacy reasons.
 
### Installation
 
1. Clone the repository:
 
    ```bash
    git clone https://github.com/doeabla/Sentiment_analysis.git
    cd your-repository
    ```
 
2. Install the required Python packages:
 
    ```bash
    pip install -r requirements.txt
    ```
 
3. Install the Hugging Face Transformers Library:
 
    ```bash
    pip install transformers
    ```
 
4. Install the Gradio Library:
 
    ```bash
    pip install gradio
    ```
 
- Run the App: `gradio app.py`
- App link: [https://huggingface.co/spaces/kojoboyoo/newzanzibar](https://huggingface.co/spaces/kojoboyoo/newzanzibar)
 
## Evaluation Results
 
The models achieved competitive accuracies on the validation dataset, with evaluation losses providing insights into their performance.
 
![image](https://github.com/doeabla/Sentiment_analysis/assets/137217264/bd9dfa3d-21c9-4fa8-a03d-7ee8013192d3)
![image](https://github.com/doeabla/Sentiment_analysis/assets/137217264/99064a38-14c7-4b1d-802c-6744dd8f4c35)
 
## Gradio App
 
The Gradio app allows users to input text and receive sentiment predictions using the RoBERTa model in an interactive manner.
 
![image](https://github.com/doeabla/Sentiment_analysis/assets/137217264/781c43ca-accd-42ee-ac62-fc908d67d1a5)
![image](https://github.com/doeabla/Sentiment_analysis/assets/137217264/9159f3a6-afd1-4df0-94f9-2aab8856357c)
 
## Acknowledgements
 
We would like to thank Azubi Africa for the opportunity to learn how to perform sentiment analysis using Hugging Face and build an app with Gradio, and the team who made this possible despite the setbacks.
 
## Authors
 
| Name | GitHub link |
| ---- | ---- |
| Doe Edinam | [https://github.com/doeabla](https://github.com/doeabla) |
| Kofi Asare Bamfo | [https://github.com/akbamfo](https://github.com/akbamfo) |
| Enoch Taylor-Nketiah | [https://github.com/kojoboyoo](https://github.com/kojoboyoo) |
| Philip Tolutope Oludipe | |
 
| Project | Name | Published Article | Deployed app |
| ---- | -----| ----- | -----|
| LP5 | Sentiment analysis | [Sentiment analysis_LP5]([https://medium.com/@eadoe97/empowering-retail-businesses-the-retail-store-sales-prediction-app-2b0a8fbaba80](https://www.linkedin.com/feed/update/urn:li:activity:7128690670235443200/)) | [Hugging Face Model](https://huggingface.co/spaces/kojoboyoo/newzanzibar) |
 
Check out the configuration reference at [https://huggingface.co/docs/hub/spaces-config-reference](https://huggingface.co/docs/hub/spaces-config-reference)
