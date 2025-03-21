# Chatbot 

This Python script takes user input, generates concise responses using a Language Model (LLM), and includes a basic content filtering mechanism to detect inappropriate content.

## Features
- Accepts user input as a query.
- Generates responses using Hugging Face's GPT-2 or FLAN-T5 model.
- Implements a filtering mechanism to block inappropriate words.

## Requirements
Install the following Python libraries:
```bash
pip install requests python-dotenv
```

## Setup
1. Get your Hugging Face API key from [Hugging Face](https://huggingface.co/).
2. Set the API key as an environment variable:
   - On Windows:
     ```bash
     set HF_API_TOKEN=your_api_key
     ```
   - On macOS/Linux:
     ```bash
     export HF_API_TOKEN=your_api_key
     ```
   Alternatively, you can store the API key in a `.env` file:
   ```env
   HF_API_TOKEN=your_api_key
   ```

## Usage
1. Run the script:
   ```bash
   python chatbot.py
   ```
2. Enter your query. For example:
   ```
   Enter your query: What's the weather like today?
   ```
   Output:
   ```
   Generated Response: I recommend checking the weather app for the latest forecast.
   ```

3. To exit, type `stop`, `bye`, or `quit`.

## Example
### Input:
```
Enter your query: What's the capital of France?
```
### Output:
```
Generated Response: The capital of France is Paris.
```

## Content Filtering
The script detects inappropriate words and blocks them in both user input and generated responses. Inappropriate content includes words like "bitch," "idiot," and others.

## Repository Structure
- `chatbot.py`: Main script to run the chatbot.
- `.env`: (Optional) File to store the API token securely.

## Notes
- This script uses the Hugging Face API (free tier available).
- Ensure your API key is kept private and not hardcoded in the script.

---



