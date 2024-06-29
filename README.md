## summarization tool to create summarizations based on LLM model and finetuning
summ.ipynb is a gooogle colab jupyter notebook used to Instruction Fine-Tune flan t5 base model on <kmyoo/cnn-dailymail-v1-tiny> dataset and save it

main.py is a python file to define functions to retrieve the trained model and use it and its tokenizer to take in the input and generate output

run.py is a python file to create a streamlit website to provide the interface for the user to interact with the model and use it to create summarizations
