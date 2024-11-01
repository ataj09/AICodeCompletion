
def complete_code(prefix, suffix, tokenizer, device , model, max_length=100):
    input_code = f"<fim_prefix>{prefix}<fim_suffix>{suffix}<fim_middle>"

    inputs = tokenizer.encode(input_code, return_tensors="pt").to(device)
    outputs = model.generate(inputs, pad_token_id = tokenizer.eos_token_id, max_new_tokens=max_length)

    generated_code = tokenizer.decode(outputs[0])

    fim_middle_loc = generated_code.find("<fim_middle>") + 12

    return generated_code[fim_middle_loc:-13] # [len(prefix):-len(suffix)]  # Return only the completion part


