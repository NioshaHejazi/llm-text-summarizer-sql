from transformers import BartTokenizer, BartForConditionalGeneration

model_name = "facebook/bart-large-cnn"
cache_dir = "./local_model"

# Download and cache model and tokenizer locally
print("Downloading tokenizer...")
BartTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

print("Downloading model...")
BartForConditionalGeneration.from_pretrained(model_name, cache_dir=cache_dir)

print("Done! Model is cached in:", cache_dir)
