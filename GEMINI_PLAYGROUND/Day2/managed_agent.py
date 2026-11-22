from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

text_input = "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=text_input,
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
