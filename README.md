# Artificial Analytics Data Downloader

This project connects to the Artificial Analytics API to download AI model benchmark data including evaluations, pricing, and speed metrics.

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd aa-data-analytics

# Set up virtual environment
python -m venv venv

# Activate virtual environment (Windows Git Bash)
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your API key (get one from https://artificialanalysis.ai/documentation)

# Run the script
python download_data.py
```

## Overview

Artificial Analysis provides comprehensive benchmarks and performance data for various AI models across different categories:

- **LLM Models**: Evaluations, pricing, and speed metrics for language models
- **Text-to-Image**: ELO ratings for text-to-image generation models
- **Text-to-Video**: ELO ratings for text-to-video generation models
- **Image Editing**: ELO ratings for image editing models
- **Text-to-Speech**: ELO ratings for text-to-speech models

## Project Structure

```
aa-data-analytics/
├── download_data.py      # Main script to download data from API
├── requirements.txt      # Python dependencies
├── .env.example         # Template for environment variables
├── .env                 # Your API key (create from .env.example, not in git)
├── .gitignore          # Files to exclude from version control
├── README.md           # This file
├── data/               # Downloaded data (created automatically)
└── venv/               # Virtual environment (created during setup)
```

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. Clone this repository

2. Create and activate a virtual environment:

**Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
python -m venv venv
source venv/Scripts/activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Note:** Always activate the virtual environment before running the script or installing dependencies.

4. Set up your API key:

**Windows (Command Prompt or PowerShell):**
```bash
copy .env.example .env
```

**macOS/Linux/Git Bash:**
```bash
cp .env.example .env
```

Then edit the `.env` file and replace `your_api_key_here` with your actual API key. Get a free API key from [Artificial Analysis Documentation](https://artificialanalysis.ai/documentation).

5. To deactivate the virtual environment when you're done:

```bash
deactivate
```

## Configuration

### API Key Setup

This project uses environment variables to securely manage the API key:

1. **Get an API Key**: Visit [Artificial Analysis Documentation](https://artificialanalysis.ai/documentation) to obtain a free API key (1,000 requests/day limit)

2. **Create .env file**: Copy the example file and add your key
   ```bash
   cp .env.example .env
   ```

3. **Edit .env**: Open `.env` and replace the placeholder with your actual API key:
   ```
   AA_API_KEY=your_actual_api_key_here
   ```

**Security Notes:**
- The `.env` file is already included in `.gitignore` and will not be committed to version control
- Never commit API keys directly in code
- Each developer should maintain their own `.env` file locally

## Usage

Ensure your virtual environment is activated, then run the download script:

```bash
# Make sure virtual environment is activated (you should see (venv) in your prompt)
python download_data.py
```

The script will:
1. Connect to all available API endpoints
2. Download the latest data
3. Save each dataset as JSON files in the `data/` directory
4. Create both timestamped and "latest" versions of each file
5. Generate a summary report

### Example Output

```
============================================================
Artificial Analytics Data Downloader
============================================================

Downloading llms_models data from https://artificialanalysis.ai/api/v2/data/llms/models...
[OK] Successfully downloaded llms_models data
  Saved to: data/llms_models_20241118_062230.json
  Saved to: data/llms_models_latest.json

Downloading text_to_image data from https://artificialanalysis.ai/api/v2/data/media/text-to-image...
[OK] Successfully downloaded text_to_image data
  Saved to: data/text_to_image_20241118_062230.json
  Saved to: data/text_to_image_latest.json

...

Summary saved to: data/download_summary.txt

============================================================
Download complete!
============================================================
Successfully downloaded: 5/5 endpoints
```

## Output

Downloaded data is saved in the `data/` directory:

- `llms_models_latest.json` - Latest LLM model benchmarks
- `text_to_image_latest.json` - Text-to-image model ratings
- `text_to_video_latest.json` - Text-to-video model ratings
- `image_editing_latest.json` - Image editing model ratings
- `text_to_speech_latest.json` - Text-to-speech model ratings
- `download_summary.txt` - Summary of the download operation

Timestamped versions are also saved for historical tracking.

## API Information

- **API Documentation**: https://artificialanalysis.ai/documentation
- **Base URL**: https://artificialanalysis.ai/api/v2
- **Authentication**: API key via `x-api-key` header
- **Rate Limit**: 1,000 requests per day

## Data Structure

Each endpoint returns JSON data with model information including:
- Model names and identifiers
- Performance metrics
- Pricing information (where applicable)
- Benchmark scores and ratings

## Troubleshooting

### Virtual Environment Issues

**Windows PowerShell - Execution Policy Error:**
If you get an error about execution policies, run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Virtual environment not activating:**
- Ensure you're in the project root directory
- Check that the `venv` folder exists
- Try using the appropriate activation command for your shell

### API Issues

**"AA_API_KEY environment variable is not set" Error:**
- Ensure you've created a `.env` file from `.env.example`
- Verify your `.env` file contains `AA_API_KEY=your_actual_key`
- Make sure the `.env` file is in the project root directory
- Check that you've installed `python-dotenv` via `pip install -r requirements.txt`

**403 Forbidden / Authentication Error:**
- Verify the API key in your `.env` file is correct
- Ensure there are no extra spaces or quotes around the API key in `.env`
- Check if you've exceeded the daily rate limit (1,000 requests/day)
- Get a new API key from https://artificialanalysis.ai/documentation if needed

**Connection Timeout:**
- Check your internet connection
- The script has a 30-second timeout per request
- Try running the script again

**Empty or Missing Data:**
- Check the `data/` directory was created
- Review `data/download_summary.txt` for error details
- Verify API endpoints are still active

### Package Installation Issues

**pip install fails:**
- Ensure virtual environment is activated (you should see `(venv)` in your prompt)
- Update pip: `python -m pip install --upgrade pip`
- On macOS/Linux, you may need `python3` instead of `python`

## License

This project is for downloading publicly available data from Artificial Analysis. Please refer to Artificial Analysis's terms of service for data usage restrictions.
