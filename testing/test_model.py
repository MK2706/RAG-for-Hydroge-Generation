import sys
sys.path.append('/content/RAG-for-Hydroge-Generation')  # Adjust the path as needed

import Model_Summary as mld
import Model_QA as mldq

# Test the summarize function
try:
    test_summary = mld.summarize("This is a test input to check summarization.")
    print("Summarization output:", test_summary)
except Exception as e:
    print("Error in summarization:", e)

# Test the QA function
try:
    test_answer = mldq.generate_answer("What is the capital of France?")
    print("QA output:", test_answer)
except Exception as e:
    print("Error in QA:", e)
