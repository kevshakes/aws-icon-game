#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os
from PIL import Image, ImageTk
import json
from datetime import datetime

class AWSIconGameMultiplayer:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Service Icon Game - Multiplayer")
        self.root.geometry("800x600")
        self.root.configure(bg="#232F3E")  # AWS dark blue background
        
        # Game state
        self.players = []
        self.current_player_index = 0
        self.aws_services = self.load_aws_services()
        self.current_service = None
        self.icon_cache = {}  # Cache for downloaded icons
        self.game_mode = None  # 'single' or 'multi'
        self.high_scores = self.load_high_scores()
        
        # Start with mode selection
        self.show_welcome_screen()
    
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            if os.path.exists("high_scores.json"):
                with open("high_scores.json", "r") as f:
                    return json.load(f)
            return []
        except:
            return []
    
    def save_high_scores(self):
        """Save high scores to file"""
        try:
            with open("high_scores.json", "w") as f:
                json.dump(self.high_scores, f)
        except:
            pass
    
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
    
    def show_welcome_screen(self):
        """Show welcome screen with game mode selection"""
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Welcome frame
        welcome_frame = tk.Frame(self.root, bg="#232F3E")
        welcome_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            welcome_frame,
            text="AWS Service Icon Game",
            font=("Arial", 28, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(
            welcome_frame,
            text="Test your knowledge of AWS service icons!",
            font=("Arial", 14),
            fg="white",
            bg="#232F3E"
        )
        desc_label.pack(pady=10)
        
        # Mode selection buttons
        mode_frame = tk.Frame(welcome_frame, bg="#232F3E")
        mode_frame.pack(pady=30)
        
        single_button = tk.Button(
            mode_frame,
            text="Single Player",
            font=("Arial", 16),
            width=15,
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.start_single_player
        )
        single_button.pack(pady=10)
        
        multi_button = tk.Button(
            mode_frame,
            text="Multiplayer",
            font=("Arial", 16),
            width=15,
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.setup_multiplayer
        )
        multi_button.pack(pady=10)
        
        # High scores button
        high_scores_button = tk.Button(
            welcome_frame,
            text="High Scores",
            font=("Arial", 12),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.show_high_scores
        )
        high_scores_button.pack(pady=20)
        
        # Quit button
        quit_button = tk.Button(
            welcome_frame,
            text="Quit",
            font=("Arial", 12),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.root.destroy
        )
        quit_button.pack(pady=10)
    
    def show_high_scores(self):
        """Show high scores screen"""
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # High scores frame
        scores_frame = tk.Frame(self.root, bg="#232F3E")
        scores_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            scores_frame,
            text="High Scores",
            font=("Arial", 24, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        title_label.pack(pady=20)
        
        # Sort high scores
        sorted_scores = sorted(self.high_scores, key=lambda x: x["score"], reverse=True)
        
        # Display scores
        if sorted_scores:
            for i, score_data in enumerate(sorted_scores[:10]):  # Show top 10
                score_text = f"{i+1}. {score_data['name']}: {score_data['score']} points ({score_data['date']})"
                score_label = tk.Label(
                    scores_frame,
                    text=score_text,
                    font=("Arial", 14),
                    fg="white",
                    bg="#232F3E"
                )
                score_label.pack(pady=5)
        else:
            no_scores_label = tk.Label(
                scores_frame,
                text="No high scores yet!",
                font=("Arial", 14),
                fg="white",
                bg="#232F3E"
            )
            no_scores_label.pack(pady=20)
        
        # Back button
        back_button = tk.Button(
            scores_frame,
            text="Back to Menu",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.show_welcome_screen
        )
        back_button.pack(pady=30)
    
    def start_single_player(self):
        """Start single player mode"""
        self.game_mode = 'single'
        player_name = simpledialog.askstring("Player Name", "Enter your name:", parent=self.root)
        if not player_name:
            player_name = "Player 1"
        
        self.players = [{"name": player_name, "lives": 3, "score": 0}]
        self.current_player_index = 0
        self.setup_game_ui()
        self.next_question()
    
    def setup_multiplayer(self):
        """Setup multiplayer game"""
        self.game_mode = 'multi'
        
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Player setup frame
        setup_frame = tk.Frame(self.root, bg="#232F3E")
        setup_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            setup_frame,
            text="Multiplayer Setup",
            font=("Arial", 24, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        title_label.pack(pady=20)
        
        # Player count selection
        count_frame = tk.Frame(setup_frame, bg="#232F3E")
        count_frame.pack(pady=20)
        
        count_label = tk.Label(
            count_frame,
            text="Number of Players:",
            font=("Arial", 14),
            fg="white",
            bg="#232F3E"
        )
        count_label.pack(side=tk.LEFT, padx=10)
        
        player_counts = [2, 3, 4, 5, 6]
        self.player_count_var = tk.StringVar(self.root)
        self.player_count_var.set(str(player_counts[0]))
        
        count_menu = tk.OptionMenu(
            count_frame,
            self.player_count_var,
            *[str(c) for c in player_counts]
        )
        count_menu.config(bg="#FF9900", activebackground="#EC7211", width=5)
        count_menu.pack(side=tk.LEFT)
        
        # Start button
        start_button = tk.Button(
            setup_frame,
            text="Enter Player Names",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.get_player_names
        )
        start_button.pack(pady=20)
        
        # Back button
        back_button = tk.Button(
            setup_frame,
            text="Back to Menu",
            font=("Arial", 12),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.show_welcome_screen
        )
        back_button.pack(pady=10)
    
    def get_player_names(self):
        """Get names for all players"""
        player_count = int(self.player_count_var.get())
        
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Names frame
        names_frame = tk.Frame(self.root, bg="#232F3E")
        names_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            names_frame,
            text="Enter Player Names",
            font=("Arial", 24, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        title_label.pack(pady=20)
        
        # Name entry fields
        self.name_entries = []
        for i in range(player_count):
            player_frame = tk.Frame(names_frame, bg="#232F3E")
            player_frame.pack(pady=10)
            
            player_label = tk.Label(
                player_frame,
                text=f"Player {i+1}:",
                font=("Arial", 14),
                fg="white",
                bg="#232F3E",
                width=10,
                anchor="e"
            )
            player_label.pack(side=tk.LEFT)
            
            name_entry = tk.Entry(
                player_frame,
                font=("Arial", 14),
                width=20
            )
            name_entry.insert(0, f"Player {i+1}")
            name_entry.pack(side=tk.LEFT, padx=10)
            self.name_entries.append(name_entry)
        
        # Start button
        start_button = tk.Button(
            names_frame,
            text="Start Game",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.start_multiplayer
        )
        start_button.pack(pady=20)
        
        # Back button
        back_button = tk.Button(
            names_frame,
            text="Back",
            font=("Arial", 12),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.setup_multiplayer
        )
        back_button.pack(pady=10)
    
    def start_multiplayer(self):
        """Start multiplayer game with entered player names"""
        self.players = []
        for entry in self.name_entries:
            name = entry.get().strip()
            if not name:
                name = f"Player {len(self.players) + 1}"
            self.players.append({"name": name, "lives": 3, "score": 0})
        
        self.current_player_index = 0
        self.setup_game_ui()
        self.next_question()
    
    def setup_game_ui(self):
        """Set up the game UI"""
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.root, bg="#232F3E")
        header_frame.pack(pady=10)
        
        self.title_label = tk.Label(
            header_frame, 
            text="AWS Service Icon Game", 
            font=("Arial", 24, "bold"),
            fg="#FF9900",  # AWS orange
            bg="#232F3E"
        )
        self.title_label.pack()
        
        # Player info
        self.player_frame = tk.Frame(self.root, bg="#232F3E")
        self.player_frame.pack(pady=5, fill=tk.X)
        
        # Will be populated in update_player_info
        
        # Icon display
        self.icon_frame = tk.Frame(self.root, bg="#232F3E")
        self.icon_frame.pack(pady=10)
        
        self.icon_label = tk.Label(self.icon_frame, bg="#232F3E")
        self.icon_label.pack()
        
        # Answer options
        self.options_frame = tk.Frame(self.root, bg="#232F3E")
        self.options_frame.pack(pady=10)
        
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
        
        # Update player info
        self.update_player_info()
    
    def update_player_info(self):
        """Update the player information display"""
        # Clear existing player info
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        
        current_player = self.players[self.current_player_index]
        
        # Current player indicator
        current_label = tk.Label(
            self.player_frame,
            text=f"Current Player: {current_player['name']}",
            font=("Arial", 14, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        current_label.pack(pady=5)
        
        # Score and lives for current player
        stats_frame = tk.Frame(self.player_frame, bg="#232F3E")
        stats_frame.pack()
        
        score_label = tk.Label(
            stats_frame,
            text=f"Score: {current_player['score']}",
            font=("Arial", 12),
            fg="white",
            bg="#232F3E"
        )
        score_label.pack(side=tk.LEFT, padx=20)
        
        lives_label = tk.Label(
            stats_frame,
            text=f"Lives: {'❤️' * current_player['lives']}",
            font=("Arial", 12),
            fg="white",
            bg="#232F3E"
        )
        lives_label.pack(side=tk.RIGHT, padx=20)
        
        # All players status
        if self.game_mode == 'multi' and len(self.players) > 1:
            all_players_frame = tk.Frame(self.player_frame, bg="#232F3E")
            all_players_frame.pack(pady=10)
            
            all_players_label = tk.Label(
                all_players_frame,
                text="All Players:",
                font=("Arial", 12),
                fg="white",
                bg="#232F3E"
            )
            all_players_label.pack()
            
            for i, player in enumerate(self.players):
                player_status = tk.Label(
                    all_players_frame,
                    text=f"{player['name']}: {player['score']} pts, {'❤️' * player['lives']}",
                    font=("Arial", 10),
                    fg="white" if i != self.current_player_index else "#FF9900",
                    bg="#232F3E"
                )
                player_status.pack()
    
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
        current_player = self.players[self.current_player_index]
        
        if selected_index == self.correct_index:
            # Correct answer
            current_player["score"] += 1
            messagebox.showinfo("Correct!", f"Yes, that's {self.current_service['name']}!")
        else:
            # Incorrect answer
            current_player["lives"] -= 1
            messagebox.showinfo("Incorrect", f"Sorry, that was {self.current_service['name']}.")
        
        # Check if current player is out
        if current_player["lives"] <= 0:
            # Add to high scores if single player
            if self.game_mode == 'single':
                self.high_scores.append({
                    "name": current_player["name"],
                    "score": current_player["score"],
                    "date": datetime.now().strftime("%Y-%m-%d")
                })
                self.save_high_scores()
            
            if self.game_mode == 'multi':
                messagebox.showinfo("Player Out", f"{current_player['name']} is out of the game!")
                
                # Check if only one player remains
                active_players = [p for p in self.players if p["lives"] > 0]
                if len(active_players) == 1:
                    winner = active_players[0]
                    self.show_game_over(winner)
                    return
                elif len(active_players) == 0:
                    # All players lost at the same time (unlikely but possible)
                    self.show_game_over(None)
                    return
            else:
                # Single player game over
                self.show_game_over(current_player)
                return
        
        # Move to next player in multiplayer mode
        if self.game_mode == 'multi':
            self.advance_to_next_player()
        
        # Update display and show next question
        self.update_player_info()
        self.next_question()
    
    def advance_to_next_player(self):
        """Advance to the next player who still has lives"""
        original_index = self.current_player_index
        
        while True:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            
            # If we've checked all players and come back to the original, break
            if self.current_player_index == original_index:
                break
            
            # If this player has lives, break
            if self.players[self.current_player_index]["lives"] > 0:
                break
    
    def show_game_over(self, winner=None):
        """Show game over screen"""
        # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Game over frame
        game_over_frame = tk.Frame(self.root, bg="#232F3E")
        game_over_frame.pack(expand=True)
        
        # Game over message
        game_over_label = tk.Label(
            game_over_frame,
            text="Game Over!",
            font=("Arial", 28, "bold"),
            fg="#FF9900",
            bg="#232F3E"
        )
        game_over_label.pack(pady=20)
        
        # Winner message (for multiplayer)
        if self.game_mode == 'multi':
            if winner:
                winner_label = tk.Label(
                    game_over_frame,
                    text=f"Winner: {winner['name']}!",
                    font=("Arial", 20),
                    fg="white",
                    bg="#232F3E"
                )
                winner_label.pack(pady=10)
                
                score_label = tk.Label(
                    game_over_frame,
                    text=f"Score: {winner['score']}",
                    font=("Arial", 16),
                    fg="white",
                    bg="#232F3E"
                )
                score_label.pack(pady=5)
            else:
                tie_label = tk.Label(
                    game_over_frame,
                    text="It's a tie! All players are out.",
                    font=("Arial", 20),
                    fg="white",
                    bg="#232F3E"
                )
                tie_label.pack(pady=10)
        else:
            # Single player score
            score_label = tk.Label(
                game_over_frame,
                text=f"Your Score: {winner['score']}",
                font=("Arial", 20),
                fg="white",
                bg="#232F3E"
            )
            score_label.pack(pady=10)
        
        # Player rankings for multiplayer
        if self.game_mode == 'multi':
            rankings_frame = tk.Frame(game_over_frame, bg="#232F3E")
            rankings_frame.pack(pady=20)
            
            rankings_label = tk.Label(
                rankings_frame,
                text="Final Rankings:",
                font=("Arial", 16, "bold"),
                fg="white",
                bg="#232F3E"
            )
            rankings_label.pack(pady=10)
            
            # Sort players by score
            sorted_players = sorted(self.players, key=lambda p: p["score"], reverse=True)
            
            for i, player in enumerate(sorted_players):
                rank_label = tk.Label(
                    rankings_frame,
                    text=f"{i+1}. {player['name']}: {player['score']} points",
                    font=("Arial", 14),
                    fg="white",
                    bg="#232F3E"
                )
                rank_label.pack(pady=2)
        
        # Buttons frame
        buttons_frame = tk.Frame(game_over_frame, bg="#232F3E")
        buttons_frame.pack(pady=30)
        
        # Play again button
        play_again_button = tk.Button(
            buttons_frame,
            text="Play Again",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.show_welcome_screen
        )
        play_again_button.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_button = tk.Button(
            buttons_frame,
            text="Quit",
            font=("Arial", 14),
            bg="#FF9900",
            activebackground="#EC7211",
            command=self.root.destroy
        )
        quit_button.pack(side=tk.LEFT, padx=10)

def main():
    root = tk.Tk()
    game = AWSIconGameMultiplayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
