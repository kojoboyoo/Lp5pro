import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, AutoConfig, RobertaTokenizer
import subprocess
from scipy.special import softmax
import numpy
import os



# Access the token using os.environ
TOKEN = os.environ.get("TOKEN")

# Access environment variable
token = os.environ.get("TOKEN")

# Constants
MODEL_PATH = "kojoboyoo/test_trainer"
# TOKEN = "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"

tokenizer = AutoTokenizer.from_pretrained("roberta-base")

# Load the model and configuration from the saved directory
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
config = AutoConfig.from_pretrained(MODEL_PATH)

# Define the Git remote URL with the personal access token

remote_url = f"git@hf.co:spaces/kojoboyoo/newzanzibar.git"


# Run the git remote set-url command
subprocess.run(["git", "remote", "set-url", "origin", remote_url])


def preprocess(text):
    return " ".join(
        ["@user" if t.startswith("@") and len(t) > 1 else ("http" if t.startswith("http") else t) for t in text.split(" ")]
    )


def sentiment_analysis(text):
    preprocessed_text = preprocess(text)

    # PyTorch-based models
    encoded_input = tokenizer(preprocessed_text, return_tensors="pt")
    output = model(**encoded_input)
    scores_ = output[0][0].detach().numpy()
    scores_ = softmax(scores_)

    # Format output dict of scores
    labels = ["Negative", "Neutral", "Positive"]
    scores = {l: float(s) for (l, s) in
 
zip(labels, scores_)}

    return scores


# Main Gradio execution
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Write your tweet here..."),
    outputs="label",
    examples=[["This is wonderful!"]],
)
if __name__ == "__main__":
  demo.launch()