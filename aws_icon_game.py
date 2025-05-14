#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import random
import os
import requests
from PIL import Image, ImageTk
from io import BytesIO

class AWSIconGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Service Icon Game")
        self.root.geometry("600x500")
        self.root.configure(bg="#232F3E")  # AWS dark blue background
        
        # Game state
        self.score = 0
        self.lives = 3
        self.aws_services = self.load_aws_services()
        self.current_service = None
        self.icon_cache = {}  # Cache for downloaded icons
        
        # UI elements
        self.setup_ui()
        
        # Start the game
        self.next_question()
    
    def load_aws_services(self):
        """Load AWS services data with their icons and names"""
        # Comprehensive list of AWS services
        services = [
            # Compute
            {"name": "Amazon EC2", "icon": "ec2.png"},
            {"name": "AWS Lambda", "icon": "lambda.png"},
            {"name": "Amazon ECS", "icon": "ecs.png"},
            {"name": "Amazon EKS", "icon": "eks.png"},
            {"name": "AWS Fargate", "icon": "fargate.png"},
            {"name": "AWS Batch", "icon": "batch.png"},
            {"name": "Amazon Lightsail", "icon": "lightsail.png"},
            {"name": "AWS Elastic Beanstalk", "icon": "elasticbeanstalk.png"},
            
            # Storage
            {"name": "Amazon S3", "icon": "s3.png"},
            {"name": "Amazon EBS", "icon": "ebs.png"},
            {"name": "Amazon EFS", "icon": "efs.png"},
            {"name": "Amazon S3 Glacier", "icon": "glacier.png"},
            {"name": "AWS Storage Gateway", "icon": "storagegateway.png"},
            
            # Database
            {"name": "Amazon RDS", "icon": "rds.png"},
            {"name": "Amazon DynamoDB", "icon": "dynamodb.png"},
            {"name": "Amazon Aurora", "icon": "aurora.png"},
            {"name": "Amazon Redshift", "icon": "redshift.png"},
            {"name": "Amazon ElastiCache", "icon": "elasticache.png"},
            {"name": "Amazon Neptune", "icon": "neptune.png"},
            {"name": "Amazon DocumentDB", "icon": "documentdb.png"},
            
            # Networking & Content Delivery
            {"name": "Amazon VPC", "icon": "vpc.png"},
            {"name": "Amazon CloudFront", "icon": "cloudfront.png"},
            {"name": "Amazon Route 53", "icon": "route53.png"},
            {"name": "AWS Direct Connect", "icon": "directconnect.png"},
            {"name": "Elastic Load Balancing", "icon": "elb.png"},
            {"name": "AWS Global Accelerator", "icon": "globalaccelerator.png"},
            
            # Security, Identity & Compliance
            {"name": "AWS IAM", "icon": "iam.png"},
            {"name": "Amazon Cognito", "icon": "cognito.png"},
            {"name": "AWS Shield", "icon": "shield.png"},
            {"name": "AWS WAF", "icon": "waf.png"},
            {"name": "AWS KMS", "icon": "kms.png"},
            {"name": "AWS Secrets Manager", "icon": "secretsmanager.png"},
            
            # Management & Governance
            {"name": "Amazon CloudWatch", "icon": "cloudwatch.png"},
            {"name": "AWS CloudTrail", "icon": "cloudtrail.png"},
            {"name": "AWS Config", "icon": "config.png"},
            {"name": "AWS CloudFormation", "icon": "cloudformation.png"},
            {"name": "AWS Systems Manager", "icon": "systemsmanager.png"},
            {"name": "AWS Organizations", "icon": "organizations.png"},
            
            # Application Integration
            {"name": "Amazon SNS", "icon": "sns.png"},
            {"name": "Amazon SQS", "icon": "sqs.png"},
            {"name": "AWS Step Functions", "icon": "stepfunctions.png"},
            {"name": "Amazon EventBridge", "icon": "eventbridge.png"},
            {"name": "Amazon MQ", "icon": "mq.png"},
            
            # Developer Tools
            {"name": "AWS CodePipeline", "icon": "codepipeline.png"},
            {"name": "AWS CodeBuild", "icon": "codebuild.png"},
            {"name": "AWS CodeDeploy", "icon": "codedeploy.png"},
            {"name": "AWS CodeCommit", "icon": "codecommit.png"},
            
            # Analytics
            {"name": "Amazon Athena", "icon": "athena.png"},
            {"name": "Amazon EMR", "icon": "emr.png"},
            {"name": "Amazon Kinesis", "icon": "kinesis.png"},
            {"name": "AWS Glue", "icon": "glue.png"},
            
            # Machine Learning
            {"name": "Amazon SageMaker", "icon": "sagemaker.png"},
            {"name": "Amazon Rekognition", "icon": "rekognition.png"},
            {"name": "Amazon Comprehend", "icon": "comprehend.png"},
            
            # API Services
            {"name": "Amazon API Gateway", "icon": "apigateway.png"},
            {"name": "Amazon AppSync", "icon": "appsync.png"}
        ]
        return services
    
    def setup_ui(self):
        """Set up the game UI"""
        # Header
        header_frame = tk.Frame(self.root, bg="#232F3E")
        header_frame.pack(pady=20)
        
        self.title_label = tk.Label(
            header_frame, 
            text="AWS Service Icon Game", 
            font=("Arial", 24, "bold"),
            fg="#FF9900",  # AWS orange
            bg="#232F3E"
        )
        self.title_label.pack()
        
        # Score and lives
        stats_frame = tk.Frame(self.root, bg="#232F3E")
        stats_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            stats_frame,
            text=f"Score: {self.score}",
            font=("Arial", 14),
            fg="white",
            bg="#232F3E"
        )
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        self.lives_label = tk.Label(
            stats_frame,
            text=f"Lives: {'❤️' * self.lives}",
            font=("Arial", 14),
            fg="white",
            bg="#232F3E"
        )
        self.lives_label.pack(side=tk.RIGHT, padx=20)
        
        # Icon display
        self.icon_frame = tk.Frame(self.root, bg="#232F3E")
        self.icon_frame.pack(pady=20)
        
        self.icon_label = tk.Label(self.icon_frame, bg="#232F3E")
        self.icon_label.pack()
        
        # Answer options
        self.options_frame = tk.Frame(self.root, bg="#232F3E")
        self.options_frame.pack(pady=20)
        
        self.option_buttons = []
        for i in range(3):
            btn = tk.Button(
                self.options_frame,
                text="",
                font=("Arial", 12),
                width=25,
                bg="#FF9900",
                activebackground="#EC7211",
                fg="black",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)
    
    def load_image(self, icon_name):
        """Load an image from the images directory"""
        try:
            # Check if image is in cache
            if icon_name in self.icon_cache:
                return self.icon_cache[icon_name]
            
            # Try to load from local directory
            image_path = os.path.join("images", icon_name)
            if os.path.exists(image_path):
                img = Image.open(image_path)
            else:
                # Create a placeholder image
                img = Image.new('RGB', (100, 100), color='#FF9900')
            
            img = img.resize((100, 100), Image.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            
            # Cache the image
            self.icon_cache[icon_name] = photo_img
            return photo_img
        except Exception as e:
            print(f"Error loading image: {e}")
            # Return a placeholder if image can't be loaded
            placeholder = Image.new('RGB', (100, 100), color='#FF9900')
            return ImageTk.PhotoImage(placeholder)
    
    def next_question(self):
        """Set up the next question"""
        # Select a random service
        self.current_service = random.choice(self.aws_services)
        
        # Load the icon
        icon_image = self.load_image(self.current_service["icon"])
        self.icon_label.configure(image=icon_image)
        self.icon_label.image = icon_image  # Keep a reference
        
        # Create answer options (1 correct, 2 incorrect)
        options = [self.current_service["name"]]
        
        # Add two incorrect options
        other_services = [s for s in self.aws_services if s != self.current_service]
        incorrect_options = random.sample(other_services, 2)
        options.extend([s["name"] for s in incorrect_options])
        
        # Shuffle options
        random.shuffle(options)
        
        # Update buttons
        for i, option in enumerate(options):
            self.option_buttons[i].config(text=option)
        
        # Store correct answer index
        self.correct_index = options.index(self.current_service["name"])
    
    def check_answer(self, selected_index):
        """Check if the selected answer is correct"""
        if selected_index == self.correct_index:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", f"Yes, that's {self.current_service['name']}!")
            self.next_question()
        else:
            self.lives -= 1
            self.lives_label.config(text=f"Lives: {'❤️' * self.lives}")
            
            if self.lives > 0:
                messagebox.showinfo("Incorrect", f"Sorry, that was {self.current_service['name']}. You have {self.lives} lives left.")
                self.next_question()
            else:
                messagebox.showinfo("Game Over", f"Game Over! Your final score is {self.score}.")
                self.show_game_over()
    
    def show_game_over(self):
        """Show game over screen and restart option"""
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game over message
        game_over_frame = tk.Frame(self.root, bg="#232F3E")
        game_over_frame.pack(expand=True)
        
        game_over_label = tk.Label(
            game_over_frame,
            text="Game Over!",
            font=("Arial", 24, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        game_over_label.pack(pady=10)
        
        score_label = tk.Label(
            game_over_frame,
            text=f"Your final score: {self.score}",
            font=("Arial", 18),
            fg="white",
            bg="#232F3E"
        )
        score_label.pack(pady=10)
        
        restart_button = tk.Button(
            game_over_frame,
            text="Play Again",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.restart_game
        )
        restart_button.pack(pady=20)
        
        quit_button = tk.Button(
            game_over_frame,
            text="Quit",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.root.destroy
        )
        quit_button.pack(pady=10)
    
    def restart_game(self):
        """Restart the game"""
        self.score = 0
        self.lives = 3
        
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Set up UI again
        self.setup_ui()
        
        # Start new game
        self.next_question()

def main():
    root = tk.Tk()
    game = AWSIconGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
