import re

def create_progress_bar(percentage, length=20):
    filled = int(length * percentage / 100)
    bar = '█' * filled + '░' * (length - filled)
    return f'{bar} {percentage}%'

def extract_keywords(text):
    # Convert to lowercase and find all words 3+ letters
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # Junk words ATS doesn't care about
    stop_words = {'the', 'and', 'for', 'with', 'that', 'this', 'from', 
                  'you', 'are', 'will', 'our', 'your', 'have', 'has',
                  'required', 'looking', 'team', 'work', 'role', 'job'}
    
    # Keep only non-junk words, remove duplicates
    keywords = list(set([w for w in words if w not in stop_words]))
    return keywords

def match_resume(job_desc, resume_text):
    keywords = extract_keywords(job_desc)
    resume_lower = resume_text.lower()
    
    matched = [word for word in keywords if word in resume_lower]
    missing = [word for word in keywords if word not in resume_lower]
    
    score = int(len(matched) / len(keywords) * 100) if keywords else 0
    
    return score, matched, missing[:10]  # Top 10 missing only

# ----- PASTE YOUR TEXTS HERE -----
job_description = """
Paste job description here
"""

resume_text = """
Paste your resume text here - PDF or Word, just copy-paste the text
"""
# ---------------------------------

score, matched, missing = match_resume(job_description, resume_text)

print("=" * 40)
print("ATS RESUME SCANNER V3")
print("=" * 40)
print(f"\nMatch Score: {create_progress_bar(score)}")
print(f"\nMatched Keywords ({len(matched)}): {', '.join(matched)}")
print(f"\nTop Missing Keywords: {', '.join(missing)}")
print("\n" + "=" * 40)
