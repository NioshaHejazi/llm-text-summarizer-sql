from transformers import BartForConditionalGeneration, BartTokenizer

# Path to your manually downloaded model
model_path = "./local_model/bart-large-cnn"

tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)

def summarize(text, max_length=130, min_length=30, do_sample=False):
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        do_sample=do_sample,
        early_stopping=True,
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

