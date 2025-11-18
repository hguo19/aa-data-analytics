# Artificial Analytics Data Downloader

This project connects to the Artificial Analytics API to download AI model benchmark data including evaluations, pricing, and speed metrics.

## Overview

Artificial Analysis provides comprehensive benchmarks and performance data for various AI models across different categories:

- **LLM Models**: Evaluations, pricing, and speed metrics for language models
- **Text-to-Image**: ELO ratings for text-to-image generation models
- **Text-to-Video**: ELO ratings for text-to-video generation models
- **Image Editing**: ELO ratings for image editing models
- **Text-to-Speech**: ELO ratings for text-to-speech models

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the download script to fetch all available data:

```bash
python download_data.py
```

The script will:
1. Connect to all available API endpoints
2. Download the latest data
3. Save each dataset as JSON files in the `data/` directory
4. Create both timestamped and "latest" versions of each file
5. Generate a summary report

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

## License

This project is for downloading publicly available data from Artificial Analysis. Please refer to Artificial Analysis's terms of service for data usage restrictions.
