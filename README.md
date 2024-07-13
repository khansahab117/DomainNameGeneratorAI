# Domain Name Finder

This project is a Python script that uses OpenAI's GPT-3.5-turbo model to generate domain names based on user input and check their availability for .com

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### OpenAI API Key

1. Go to [OpenAI's website](https://platform.openai.com/signup) and sign up for an account if you haven't already.
2. Once logged in, navigate to the [API keys page](https://platform.openai.com/account/api-keys).
3. Click on "Create new secret key" and copy the generated key.

### Environment Setup

1. Clone this repository to your local machine.

2. Create a `.env` file in the root directory of the project and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

    Replace `your_api_key_here` with the API key you copied from OpenAI.

3. Create and activate a virtual environment:

    **Windows:**
    python -m venv venv
    .\venv\Scripts\activate
    
    **macOS and Linux:**
    python3 -m venv venv
    source venv/bin/activate

4. Install the required packages:
   
    pip install -r requirements.txt

**Note:** This project uses version 0.27 of the OpenAI library. Newer versions may not be compatible with the current code setup.

## Usage

Run the script using:
python domainFinder.py

Follow the prompts to input domain name descriptions. The script will generate domain suggestions and check their availability.

## Important Note

This project uses an older version (0.27) of the OpenAI library. Newer versions may not be compatible with the current code setup. If you encounter issues, make sure you're using the correct version of the OpenAI library.

## License

[MIT License](LICENSE)



