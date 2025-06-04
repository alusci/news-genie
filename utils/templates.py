classify_intention_template = """
You are a helpful assistant that classifies the user's intention based on the input.
The input is a string that may contain various types of information. Your task is to classify the intention of the user based on the input.
The possible classifications are:
1. Informational: The user is looking for information or knowledge.
2. News: The user is looking for news or updates.
3. Other: The user's intention does not fall into the above categories.
Please classify the intention of the user based on the input string.
Input: {input}
Output: 
"""

info_template = """
You are a helpful assistant that generates an informational answer based on the user's input.
The input is a string that may contain various types of information. Your task is to generate an informational answer based on the input.

Please generate an informational answer based on the input string.
Input: {input}
Output: 
"""

validate_news_template = """""
You are a helpful assistant that generates news based on the user's input.
The input is a string that contain news. Your task is to validate the news to make sure it is not fake or misleading.
If the news is valid, please refine the answer as needed and provide the final output.

Input: {input}
Output: 
"""
