from transformers import pipeline

# Load a text generation model
generator = pipeline("text-generation", model="gpt2")

print("Welcome to AI Creative Writer!")
mode = input("Do you want a 'poem' or 'story'? ").strip().lower()
prompt = input("Enter your topic or first line: ")

# Add style based on mode
if mode == "poem":
    prompt = f"Write a short, beautiful poem about {prompt}:"
elif mode == "story":
    prompt = f"Write a short, creative story about {prompt}:"
else:
    print("Invalid choice! Defaulting to story mode.")

# Generate text
result = generator(prompt, max_length=80, num_return_sequences=1)
print("\n--- Your AI Creation ---\n")
print(result[0]['generated_text'])
