#!/usr/bin/env python3
"""
Script to generate placeholder icons for the AWS Icon Game
"""
import os
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_icon(service_name, filename, size=(100, 100), bg_color="#FF9900", text_color="#232F3E"):
    """Create a placeholder icon with the service name"""
    try:
        print(f"Creating placeholder for {service_name}...")
        
        # Create a new image with AWS orange background
        img = Image.new('RGB', size, color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a system font, fall back to default if not available
        try:
            font = ImageFont.truetype("Arial", 12)
        except IOError:
            font = ImageFont.load_default()
        
        # Get the abbreviated name (first letters or short form)
        if " " in service_name:
            if service_name.startswith("AWS"):
                abbr = service_name.split(" ")[1][:3].upper()
            elif service_name.startswith("Amazon"):
                abbr = service_name.split(" ")[1][:3].upper()
            else:
                words = service_name.split(" ")
                abbr = ''.join([word[0] for word in words if word not in ['&', 'and', 'of', 'the']])
        else:
            abbr = service_name[:3].upper()
        
        # Calculate text position to center it
        text_width, text_height = draw.textsize(abbr, font=font) if hasattr(draw, 'textsize') else (30, 15)
        position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
        
        # Draw the text
        draw.text(position, abbr, fill=text_color, font=font)
        
        # Create images directory if it doesn't exist
        os.makedirs("images", exist_ok=True)
        
        # Save the image
        img.save(os.path.join("images", filename))
        print(f"Successfully created {filename}")
        return True
    except Exception as e:
        print(f"Error creating {filename}: {e}")
        return False

def main():
    """Main function to create all placeholder icons"""
    # Dictionary of AWS services with their icon filenames
    services = {
        # Compute
        "Amazon EC2": "ec2.png",
        "AWS Lambda": "lambda.png",
        "Amazon ECS": "ecs.png",
        "Amazon EKS": "eks.png",
        "AWS Fargate": "fargate.png",
        "AWS Batch": "batch.png",
        "Amazon Lightsail": "lightsail.png",
        "AWS Elastic Beanstalk": "elasticbeanstalk.png",
        
        # Storage
        "Amazon S3": "s3.png",
        "Amazon EBS": "ebs.png",
        "Amazon EFS": "efs.png",
        "Amazon S3 Glacier": "glacier.png",
        "AWS Storage Gateway": "storagegateway.png",
        
        # Database
        "Amazon RDS": "rds.png",
        "Amazon DynamoDB": "dynamodb.png",
        "Amazon Aurora": "aurora.png",
        "Amazon Redshift": "redshift.png",
        "Amazon ElastiCache": "elasticache.png",
        "Amazon Neptune": "neptune.png",
        "Amazon DocumentDB": "documentdb.png",
        
        # Networking & Content Delivery
        "Amazon VPC": "vpc.png",
        "Amazon CloudFront": "cloudfront.png",
        "Amazon Route 53": "route53.png",
        "AWS Direct Connect": "directconnect.png",
        "Elastic Load Balancing": "elb.png",
        "AWS Global Accelerator": "globalaccelerator.png",
        
        # Security, Identity & Compliance
        "AWS IAM": "iam.png",
        "Amazon Cognito": "cognito.png",
        "AWS Shield": "shield.png",
        "AWS WAF": "waf.png",
        "AWS KMS": "kms.png",
        "AWS Secrets Manager": "secretsmanager.png",
        
        # Management & Governance
        "Amazon CloudWatch": "cloudwatch.png",
        "AWS CloudTrail": "cloudtrail.png",
        "AWS Config": "config.png",
        "AWS CloudFormation": "cloudformation.png",
        "AWS Systems Manager": "systemsmanager.png",
        "AWS Organizations": "organizations.png",
        
        # Application Integration
        "Amazon SNS": "sns.png",
        "Amazon SQS": "sqs.png",
        "AWS Step Functions": "stepfunctions.png",
        "Amazon EventBridge": "eventbridge.png",
        "Amazon MQ": "mq.png",
        
        # Developer Tools
        "AWS CodePipeline": "codepipeline.png",
        "AWS CodeBuild": "codebuild.png",
        "AWS CodeDeploy": "codedeploy.png",
        "AWS CodeCommit": "codecommit.png",
        
        # Analytics
        "Amazon Athena": "athena.png",
        "Amazon EMR": "emr.png",
        "Amazon Kinesis": "kinesis.png",
        "AWS Glue": "glue.png",
        
        # Machine Learning
        "Amazon SageMaker": "sagemaker.png",
        "Amazon Rekognition": "rekognition.png",
        "Amazon Comprehend": "comprehend.png",
        
        # API Services
        "Amazon API Gateway": "apigateway.png",
        "Amazon AppSync": "appsync.png"
    }
    
    # Create each placeholder icon
    success_count = 0
    for service_name, filename in services.items():
        if create_placeholder_icon(service_name, filename):
            success_count += 1
    
    print(f"\nCreated {success_count} of {len(services)} placeholder icons")

if __name__ == "__main__":
    main()
