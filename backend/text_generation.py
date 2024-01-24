# Import necessary modules from the transformers library
from transformers import AutoTokenizer, AutoModelForCausalLM

# Define a class for text generation
class TextGenerator():

    # Constructor method to initialize the TextGenerator class
    def __init__(self):
        # Load a pre-trained language model for causal language modeling
        self.model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-560m")
        
        # Load the corresponding tokenizer for the pre-trained model
        self.tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")

    # Method to generate text based on a given prompt
    def generate_text(self, prompt):
        # Encode the input prompt using the tokenizer and convert it to PyTorch tensor
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        # Generate text using the pre-trained language model
        # Parameters:
        #   - max_length: Maximum length of the generated text
        #   - num_beams: Number of beams for beam search during generation
        #   - no_repeat_ngram_size: Size of n-grams to avoid repetition in the generated text
        #   - top_k: Number of top words to consider during generation
        #   - top_p: Cumulative probability for nucleus sampling
        output = self.model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95)
        
        # Decode the generated output to obtain the final text, skipping special tokens
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Return the generated text
        return generated_text
