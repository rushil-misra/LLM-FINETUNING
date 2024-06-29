from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

class Summarizer:
    def __init__(self, model_name='google/flan-t5-base',model_path=r"C:\Users\Rushil Misra\Documents\projects\SUMMARISATION\trained_model\PYTHON"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path, torch_dtype=torch.bfloat16)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def summarize(self,text):
        input = self.tokenizer(text, return_tensors = "pt")
        generation = self.model.generate(input["input_ids"],max_new_tokens = 100,)
        output = self.tokenizer.decode(generation[0],skip_special_tokens=True)

        return output
    
