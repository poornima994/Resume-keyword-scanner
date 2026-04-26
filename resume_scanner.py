import re

# Get job description 
job_desc = input("Paste the job description here: ").lower()

# Auto-extract keywords: words 3+ letters, ignore common words
common_words = {"the", "and", "for", "with", "you", "are", "job", "will", "this", "that", "from", "have", "role", "our", "team", "work"}
keywords = list(set([word for word in re.findall(r'\b[a-z]{3,}\b', job_desc) if word not in common_words]))
print("Auto-detected keywords:", keywords[:15])  # Show first 15

# Get your resume text
print("\nNow paste your resume text:")
resume_text = input().lower()

# Check which keywords are in your resume
found_keywords = []
missing_keywords = []

for word in keywords:
    if word in resume_text:
        found_keywords.append(word)
    else:
        missing_keywords.append(word)

# Results
print("\n--- Results ---")
print("Found keywords:", found_keywords[:15])
print("Missing keywords:", missing_keywords[:10])
print(f"Match Score: {len(found_keywords)}/{len(keywords)} = {round(len(found_keywords)/len(keywords)*100)}%")
