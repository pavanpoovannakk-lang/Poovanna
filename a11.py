from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love eating idly in Coorg")
print(result)