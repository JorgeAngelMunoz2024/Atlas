import requests

def preferences(title, location):
    title = ["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"],"excludedTitle":["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"]
    location = ["San Antonio"]
    payload = {"category":"newgrad:us:swe","excludeTitle":["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"],"excludedTitle":["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"],"location":[location]}
    response = requests.post("https://jobright.ai/swan/mini-sites/list?position=0&count=50", json=payload)
    return response.json()
url = "https://jobright.ai/swan/mini-sites/list?position=0&count=50"

payload = {"category":"newgrad:us:swe","excludeTitle":["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"],"excludedTitle":["AI Trainer","AI Tutor","AI Training","AI Coach","AI Reviewer","AI Rater","AI Content Evaluator","Search Quality Rater","Ads Quality Rater","Annotator","Annotation Specialist","Data Annotation","AI Annotation","Data Labeler","Data Labeling","Labeler","AI Data Specialist","Data Collector","Data Collection","Prompt Optimization","Prompt Creator"],"location":["San Antonio"]}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())