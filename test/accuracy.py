import json
import re

# Load batch results
with open("results/batch_results.json", "r") as f:
    results = json.load(f)

# Target pattern: digits + _1_ + 3 letters
pattern = re.compile(r'^\d+_1_[a-zA-Z]{3}$')

total_images = len(results)
correct_extractions = 0
non_null_outputs = 0

for item in results:
    text = item["extracted_text"]

    if text is not None:
        non_null_outputs += 1

        if pattern.match(text):
            correct_extractions += 1

accuracy = (correct_extractions / total_images) * 100

print("Total images:", total_images)
print("Non-null extractions:", non_null_outputs)
print("Correct pattern matches:", correct_extractions)
print(f"Accuracy: {accuracy:.2f}%")
