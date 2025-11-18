#!/usr/bin/env python3
"""
Download data from Artificial Analytics API
This script connects to all available free data endpoints and saves the results.
"""

import json
import os
from datetime import datetime
from pathlib import Path
import requests


# API Configuration
API_KEY = "aa_qETUMuuGkupxdvNENxihRqIAEypXWWhc"
BASE_URL = "https://artificialanalysis.ai/api/v2"

# Available endpoints
ENDPOINTS = {
    "llms_models": "/data/llms/models",
    "text_to_image": "/data/media/text-to-image",
    "text_to_video": "/data/media/text-to-video",
    "image_editing": "/data/media/image-editing",
    "text_to_speech": "/data/media/text-to-speech",
}

# Output directory
DATA_DIR = Path("data")


def download_endpoint_data(endpoint_name: str, endpoint_path: str) -> dict:
    """
    Download data from a specific API endpoint.

    Args:
        endpoint_name: Name identifier for the endpoint
        endpoint_path: API path for the endpoint

    Returns:
        JSON response data as dictionary
    """
    url = f"{BASE_URL}{endpoint_path}"
    headers = {
        "x-api-key": API_KEY,
        "Accept": "application/json"
    }

    print(f"Downloading {endpoint_name} data from {url}...")

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        print(f"✓ Successfully downloaded {endpoint_name} data")
        return data

    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {endpoint_name}: {e}")
        return None


def save_data(endpoint_name: str, data: dict) -> None:
    """
    Save downloaded data to a JSON file.

    Args:
        endpoint_name: Name identifier for the endpoint
        data: Data to save
    """
    if data is None:
        return

    # Create data directory if it doesn't exist
    DATA_DIR.mkdir(exist_ok=True)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = DATA_DIR / f"{endpoint_name}_{timestamp}.json"

    # Also save as latest
    latest_filename = DATA_DIR / f"{endpoint_name}_latest.json"

    try:
        # Save with timestamp
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Saved to: {filename}")

        # Save as latest
        with open(latest_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Saved to: {latest_filename}")

    except IOError as e:
        print(f"  Error saving {endpoint_name}: {e}")


def generate_summary(all_data: dict) -> None:
    """
    Generate a summary of the downloaded data.

    Args:
        all_data: Dictionary containing all downloaded data
    """
    # Ensure data directory exists
    DATA_DIR.mkdir(exist_ok=True)

    summary_file = DATA_DIR / "download_summary.txt"

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("Artificial Analytics Data Download Summary\n")
        f.write("=" * 50 + "\n")
        f.write(f"Download Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for endpoint_name, data in all_data.items():
            f.write(f"\n{endpoint_name}:\n")
            f.write("-" * 30 + "\n")

            if data is None:
                f.write("  Status: Failed to download\n")
            else:
                f.write("  Status: Successfully downloaded\n")

                # Try to extract some basic stats
                if isinstance(data, dict):
                    f.write(f"  Keys: {list(data.keys())}\n")

                    # Count items if it's a list
                    for key, value in data.items():
                        if isinstance(value, list):
                            f.write(f"  {key}: {len(value)} items\n")
                elif isinstance(data, list):
                    f.write(f"  Items: {len(data)}\n")

    print(f"\nSummary saved to: {summary_file}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("Artificial Analytics Data Downloader")
    print("=" * 60)
    print()

    all_data = {}

    # Download data from all endpoints
    for endpoint_name, endpoint_path in ENDPOINTS.items():
        data = download_endpoint_data(endpoint_name, endpoint_path)
        all_data[endpoint_name] = data

        # Save the data
        save_data(endpoint_name, data)
        print()

    # Generate summary
    generate_summary(all_data)

    print()
    print("=" * 60)
    print("Download complete!")
    print("=" * 60)

    # Print success summary
    successful = sum(1 for data in all_data.values() if data is not None)
    total = len(all_data)
    print(f"Successfully downloaded: {successful}/{total} endpoints")


if __name__ == "__main__":
    main()
