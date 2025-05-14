#!/usr/bin/env python3
"""
Script to download AWS service icons for the AWS Icon Game
"""
import os
import requests
from io import BytesIO
from PIL import Image

def download_icon(url, filename, size=(100, 100)):
    """Download an icon from a URL and save it to the images directory"""
    try:
        print(f"Downloading {filename} from {url}...")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to download {filename}: HTTP {response.status_code}")
            return False
        
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img = img.resize(size, Image.LANCZOS)
        
        # Create images directory if it doesn't exist
        os.makedirs("images", exist_ok=True)
        
        # Save the image
        img.save(os.path.join("images", filename))
        print(f"Successfully saved {filename}")
        return True
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
        return False

def main():
    """Main function to download all icons"""
    # Dictionary of AWS service icons with their URLs
    icons = {
        "ec2.png": "https://d1.awsstatic.com/icons/jp/console_ec2_icon.64795d08c5e23e92c12cc2c6f91a01aa1b2d60f8.png",
        "s3.png": "https://d1.awsstatic.com/icons/jp/console_s3_icon.8373b9e7a80599afa7e0331eeb97d54f790c82ba.png",
        "rds.png": "https://d1.awsstatic.com/icons/jp/console_rds_icon.a478de57ff85a66d93ef078999e8d5f5bdd5cfce.png",
        "lambda.png": "https://d1.awsstatic.com/icons/jp/console_lambda_icon.dc7781a6b5f1f3cb267b0bac7c9208ce5bb8a2f6.png",
        "dynamodb.png": "https://d1.awsstatic.com/icons/jp/console_dynamodb_icon.0c655f0f1f7541dc238d4bfe873f8e5a0d454d2a.png",
        "cloudwatch.png": "https://d1.awsstatic.com/icons/jp/console_cloudwatch_icon.8c2a00a80275209372b0b5caf8c8a37d5c3e5a93.png",
        "sns.png": "https://d1.awsstatic.com/icons/jp/console_sns_icon.c972fdc0103e27b6a2a20b732839b3a0b8d17e85.png",
        "sqs.png": "https://d1.awsstatic.com/icons/jp/console_sqs_icon.d7ad274661bc6fd5b6ca0e6bf17da8a4f82b08b9.png",
        "iam.png": "https://d1.awsstatic.com/icons/jp/console_iam_icon.3eeed669dca9f9e20597cc51d904ed13b5ad4afb.png",
        "vpc.png": "https://d1.awsstatic.com/icons/jp/console_vpc_icon.d09340f3abe0c7f5d5a3ad664264cb834b11f9a8.png",
        "ecs.png": "https://d1.awsstatic.com/icons/jp/compute/ecs_blue.8aaa3a8fa5f8250f5047d35df5ff6c9001c23ac0.png",
        "eks.png": "https://d1.awsstatic.com/icons/jp/eks_blue.9d6b8d799a6c89a6664fdcb2a9c313c8a1d3e0f7.png",
        "cloudformation.png": "https://d1.awsstatic.com/icons/jp/console_cloudformation_icon.8f058b213317e7099ff8a5cfa848cff0e8e9a2b3.png",
        "apigateway.png": "https://d1.awsstatic.com/icons/jp/console_apigateway_icon.dc7f9b0b18ecf5aa96265a2e69183e7716e6be1e.png",
        "stepfunctions.png": "https://d1.awsstatic.com/icons/jp/console_states_icon.3b7c036f544db8e28663de2e7d8a0a5e8d73c642.png"
    }
    
    # Download each icon
    success_count = 0
    for filename, url in icons.items():
        if download_icon(url, filename):
            success_count += 1
    
    print(f"\nDownloaded {success_count} of {len(icons)} icons")
    if success_count < len(icons):
        print("Some icons could not be downloaded. You may need to manually download them.")
        print("See the README.md file for more information.")

if __name__ == "__main__":
    main()
