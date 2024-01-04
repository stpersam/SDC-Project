from transformers import AutoTokenizer, AutoModelForCausalLM


class TextGenerator():

    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-560m")
        self.tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")

    def generate_text(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text