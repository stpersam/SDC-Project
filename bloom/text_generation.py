from transformers import GPT2LMHeadModel, GPT2Tokenizer


class TextGenerator():

    def __init__(self, model_name="bigscience/bloom"):
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=max_length, num_beams=num_beams, no_repeat_ngram_size=no_repeat_ngram_size, top_k=top_k, top_p=top_p)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text