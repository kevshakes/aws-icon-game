import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import time

class AWSIconGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Service Icon Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Game variables
        self.score = 0
        self.lives = 3
        self.current_service = None
        self.options = []
        self.difficulty = "easy"  # Default difficulty
        self.category = "all"     # Default category
        
        # UI elements
        self.setup_ui()
        
        # Load AWS services
        self.aws_services = self.load_aws_services()
        self.aws_services_by_category = self.categorize_services()
        
        # Start with the main menu
        self.show_main_menu()
    
    def setup_ui(self):
        # Create frames for different screens
        self.main_menu_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)
        self.game_over_frame = tk.Frame(self.root)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 14))
        
        # Configure main menu frame
        self.setup_main_menu()
        
        # Configure game frame
        self.setup_game_frame()
        
        # Configure game over frame
        self.setup_game_over_frame()
    
    def setup_main_menu(self):
        # Title
        title_label = ttk.Label(self.main_menu_frame, text="AWS Service Icon Game", 
                               font=("Arial", 24, "bold"))
        title_label.pack(pady=30)
        
        # Difficulty selection
        diff_frame = tk.Frame(self.main_menu_frame)
        diff_frame.pack(pady=20)
        
        ttk.Label(diff_frame, text="Select Difficulty:", 
                 font=("Arial", 16)).pack(side=tk.TOP, pady=10)
        
        self.difficulty_var = tk.StringVar(value="easy")
        
        diff_options = [
            ("Easy", "easy"),
            ("Medium", "medium"),
            ("Hard", "hard")
        ]
        
        for text, value in diff_options:
            ttk.Radiobutton(diff_frame, text=text, value=value, 
                           variable=self.difficulty_var).pack(anchor=tk.W, padx=20, pady=5)
        
        # Category selection
        cat_frame = tk.Frame(self.main_menu_frame)
        cat_frame.pack(pady=20)
        
        ttk.Label(cat_frame, text="Select Category:", 
                 font=("Arial", 16)).pack(side=tk.TOP, pady=10)
        
        self.category_var = tk.StringVar(value="all")
        
        cat_options = [
            ("All Services", "all"),
            ("Compute", "compute"),
            ("Storage", "storage"),
            ("Database", "database"),
            ("Networking", "networking"),
            ("Security", "security")
        ]
        
        for text, value in cat_options:
            ttk.Radiobutton(cat_frame, text=text, value=value, 
                           variable=self.category_var).pack(anchor=tk.W, padx=20, pady=5)
        
        # Start button
        start_button = ttk.Button(self.main_menu_frame, text="Start Game", 
                                 command=self.start_game, style="TButton")
        start_button.pack(pady=30)
    
    def setup_game_frame(self):
        # Top info frame
        info_frame = tk.Frame(self.game_frame)
        info_frame.pack(fill=tk.X, pady=10)
        
        # Lives display with heart symbols
        self.lives_label = ttk.Label(info_frame, text="♥ ♥ ♥", font=("Arial", 24, "bold"), foreground="red")
        self.lives_label.pack(side=tk.LEFT, padx=20)
        
        # Score display
        self.score_label = ttk.Label(info_frame, text="Score: 0", font=("Arial", 18))
        self.score_label.pack(side=tk.RIGHT, padx=20)
        
        # Difficulty display
        self.difficulty_label = ttk.Label(info_frame, text="Difficulty: Easy", font=("Arial", 14))
        self.difficulty_label.pack(side=tk.RIGHT, padx=20)
        
        # Icon display
        self.icon_frame = tk.Frame(self.game_frame, height=250, width=250)
        self.icon_frame.pack(pady=20)
        self.icon_frame.pack_propagate(False)
        
        self.icon_label = ttk.Label(self.icon_frame)
        self.icon_label.pack(expand=True, fill=tk.BOTH)
        
        # Options frame
        self.options_frame = tk.Frame(self.game_frame)
        self.options_frame.pack(pady=20, fill=tk.X)
        
        # Timer bar (for medium and hard difficulties)
        self.timer_frame = tk.Frame(self.game_frame, height=20)
        self.timer_frame.pack(fill=tk.X, padx=50, pady=10)
        
        self.timer_bar = tk.Canvas(self.timer_frame, height=20, bg="white", highlightthickness=0)
        self.timer_bar.pack(fill=tk.X)
        self.timer_rect = None
    
    def setup_game_over_frame(self):
        # Game over message
        game_over_label = ttk.Label(self.game_over_frame, text="Game Over!", 
                                   font=("Arial", 36, "bold"))
        game_over_label.pack(pady=30)
        
        # Final score
        self.final_score_label = ttk.Label(self.game_over_frame, text="Your Score: 0", 
                                         font=("Arial", 24))
        self.final_score_label.pack(pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.game_over_frame)
        buttons_frame.pack(pady=30)
        
        # Play again button
        play_again_button = ttk.Button(buttons_frame, text="Play Again", 
                                      command=self.show_main_menu)
        play_again_button.pack(side=tk.LEFT, padx=10)
        
        # Quit button
        quit_button = ttk.Button(buttons_frame, text="Quit", 
                                command=self.root.quit)
        quit_button.pack(side=tk.LEFT, padx=10)
    
    def show_main_menu(self):
        self.game_frame.pack_forget()
        self.game_over_frame.pack_forget()
        self.main_menu_frame.pack(expand=True, fill=tk.BOTH)
    
    def show_game_frame(self):
        self.main_menu_frame.pack_forget()
        self.game_over_frame.pack_forget()
        self.game_frame.pack(expand=True, fill=tk.BOTH)
    
    def show_game_over(self):
        self.main_menu_frame.pack_forget()
        self.game_frame.pack_forget()
        self.final_score_label.config(text=f"Your Score: {self.score}")
        self.game_over_frame.pack(expand=True, fill=tk.BOTH)
    
    def load_aws_services(self):
        # This would ideally be loaded from a JSON file or API
        # For now, we'll hardcode some services with their icon URLs
        return [
            {"name": "Amazon EC2", "icon_url": "https://d1.awsstatic.com/icons/jp/console_ec2_icon.64795d3c8ab3aeed3f26a66b599e94a0e0e7a061.png", "category": "compute"},
            {"name": "Amazon S3", "icon_url": "https://d1.awsstatic.com/icons/jp/console_s3_icon.3230f0abe9d6f30b448a29bdd5a0cc01c7c5d62f.png", "category": "storage"},
            {"name": "Amazon RDS", "icon_url": "https://d1.awsstatic.com/icons/jp/console_rds_icon.a7648d0a8a5d5e777b4d86c82f8961d59e1b9a23.png", "category": "database"},
            {"name": "Amazon DynamoDB", "icon_url": "https://d1.awsstatic.com/icons/jp/console_dynamodb_icon.0c150f04239658584f9a5e1ebd2c0b169d68c094.png", "category": "database"},
            {"name": "AWS Lambda", "icon_url": "https://d1.awsstatic.com/icons/jp/console_lambda_icon.8a26b4331d6a5d8c32d0644556ea4b2c5d475283.png", "category": "compute"},
            {"name": "Amazon VPC", "icon_url": "https://d1.awsstatic.com/icons/jp/console_vpc_icon.d8fbf33b5260555d0e35eaa47a2c1ca9b9d0e7ba.png", "category": "networking"},
            {"name": "Amazon CloudFront", "icon_url": "https://d1.awsstatic.com/icons/jp/console_cloudfront_icon.a04de0fbe800a67c6d2e7e0e25d4edf8fe3170fd.png", "category": "networking"},
            {"name": "Amazon SNS", "icon_url": "https://d1.awsstatic.com/icons/jp/console_sns_icon.8dd9a1c8758af3ea19318f7eb54b8716c9218b8e.png", "category": "application-integration"},
            {"name": "Amazon SQS", "icon_url": "https://d1.awsstatic.com/icons/jp/console_sqs_icon.d7ad380465533423271b5a5f24a9b2e7f7b3de49.png", "category": "application-integration"},
            {"name": "AWS IAM", "icon_url": "https://d1.awsstatic.com/icons/jp/console_iam_icon.3eeed669dca9f9e24dc47a00d8cdd96be1739257.png", "category": "security"},
            {"name": "Amazon CloudWatch", "icon_url": "https://d1.awsstatic.com/icons/jp/console_cloudwatch_icon.8c2b7e6fb4263a0d4ff1679e935376401d7e32ac.png", "category": "management"},
            {"name": "AWS Elastic Beanstalk", "icon_url": "https://d1.awsstatic.com/icons/jp/console_elasticbeanstalk_icon.8d82f504b8a8d1dce33e51e4bf4a8ce3b0b0092f.png", "category": "compute"},
            {"name": "Amazon ECS", "icon_url": "https://d1.awsstatic.com/icons/jp/ecs_blue.9f8b9d234a8bfd94f7c8ca4b8c1393ad6e3d18d9.png", "category": "compute"},
            {"name": "Amazon EKS", "icon_url": "https://d1.awsstatic.com/icons/jp/eks_blue.9f8b9d234a8bfd94f7c8ca4b8c1393ad6e3d18d9.png", "category": "compute"},
            {"name": "AWS Fargate", "icon_url": "https://d1.awsstatic.com/icons/jp/fargate.6b2c0f29f8af2fcc9f92c8d4c8cb9cac4c64d92e.png", "category": "compute"}
        ]
    
    def categorize_services(self):
        categories = {}
        for service in self.aws_services:
            category = service["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(service)
        return categories
    
    def get_services_for_current_category(self):
        if self.category == "all":
            return self.aws_services
        else:
            return self.aws_services_by_category.get(self.category, [])
    
    def start_game(self):
        # Get selected difficulty and category
        self.difficulty = self.difficulty_var.get()
        self.category = self.category_var.get()
        
        # Reset game state
        self.score = 0
        self.lives = 3
        self.update_score_display()
        self.update_lives_display()
        
        # Update difficulty display
        self.difficulty_label.config(text=f"Difficulty: {self.difficulty.capitalize()}")
        
        # Show game frame
        self.show_game_frame()
        
        # Start first question
        self.next_question()
    
    def next_question(self):
        # Clear any existing timer
        if hasattr(self, 'timer_id') and self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        
        # Get available services for the selected category
        available_services = self.get_services_for_current_category()
        
        if not available_services:
            messagebox.showerror("Error", "No services available for the selected category.")
            self.show_main_menu()
            return
        
        # Select a random service
        self.current_service = random.choice(available_services)
        
        # Determine number of options based on difficulty
        num_options = 3  # Easy
        if self.difficulty == "medium":
            num_options = 4
        elif self.difficulty == "hard":
            num_options = 5
        
        # Get options (including the correct one)
        self.options = [self.current_service]
        
        # Add incorrect options
        other_services = [s for s in available_services if s != self.current_service]
        if len(other_services) < num_options - 1:
            # If not enough services in the category, add from all services
            other_services = [s for s in self.aws_services if s != self.current_service]
        
        self.options.extend(random.sample(other_services, min(num_options - 1, len(other_services))))
        random.shuffle(self.options)
        
        # Load and display the icon
        self.load_and_display_icon()
        
        # Create option buttons
        self.create_option_buttons()
        
        # Start timer if not on easy mode
        if self.difficulty != "easy":
            self.start_timer()
    
    def load_and_display_icon(self):
        try:
            # Download the icon
            response = requests.get(self.current_service["icon_url"])
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            
            # Resize to fit
            img = img.resize((200, 200), Image.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(img)
            
            # Update label
            self.icon_label.config(image=photo)
            self.icon_label.image = photo  # Keep a reference
            
        except Exception as e:
            print(f"Error loading image: {e}")
            # Use a placeholder if image fails to load
            self.icon_label.config(text="[Icon]", font=("Arial", 24))
    
    def create_option_buttons(self):
        # Clear existing buttons
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        # Create new buttons
        for option in self.options:
            btn = ttk.Button(
                self.options_frame, 
                text=option["name"],
                command=lambda o=option: self.check_answer(o),
                width=30
            )
            btn.pack(pady=5)
    
    def start_timer(self):
        # Set time based on difficulty
        if self.difficulty == "medium":
            time_limit = 15  # 15 seconds
        else:  # hard
            time_limit = 8   # 8 seconds
        
        # Create timer bar
        self.timer_bar.delete("all")
        self.timer_rect = self.timer_bar.create_rectangle(
            0, 0, self.timer_bar.winfo_width(), 20, 
            fill="green", outline=""
        )
        
        self.time_remaining = time_limit
        self.update_timer()
    
    def update_timer(self):
        if self.time_remaining <= 0:
            # Time's up
            self.check_answer(None)
            return
        
        # Update timer bar
        width = self.timer_bar.winfo_width()
        new_width = (self.time_remaining / (15 if self.difficulty == "medium" else 8)) * width
        self.timer_bar.coords(self.timer_rect, 0, 0, new_width, 20)
        
        # Change color as time runs out
        if self.time_remaining < 3:
            self.timer_bar.itemconfig(self.timer_rect, fill="red")
        elif self.time_remaining < 6:
            self.timer_bar.itemconfig(self.timer_rect, fill="orange")
        
        # Decrement time and schedule next update
        self.time_remaining -= 0.1
        self.timer_id = self.root.after(100, self.update_timer)
    
    def check_answer(self, selected_option):
        # Cancel timer if it's running
        if hasattr(self, 'timer_id') and self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        
        if selected_option == self.current_service:
            # Correct answer
            self.score += 1
            self.update_score_display()
            
            # Flash green for correct answer
            self.flash_feedback("green")
            
        else:
            # Incorrect answer
            self.lives -= 1
            self.update_lives_display()
            
            # Flash red for incorrect answer
            self.flash_feedback("red")
            
            # Show correct answer
            correct_name = self.current_service["name"]
            messagebox.showinfo("Incorrect", f"The correct answer was: {correct_name}")
            
            if self.lives <= 0:
                # Game over
                self.show_game_over()
                return
        
        # Next question after a short delay
        self.root.after(1000, self.next_question)
    
    def flash_feedback(self, color):
        # Create a flash effect overlay
        flash = tk.Frame(self.game_frame, bg=color)
        flash.place(x=0, y=0, relwidth=1, relheight=1)
        flash.lift()  # Bring to front
        
        # Make it semi-transparent
        flash.configure(bg=color)
        flash.update()
        
        # Remove after a short delay
        self.root.after(300, flash.destroy)
    
    def update_score_display(self):
        self.score_label.config(text=f"Score: {self.score}")
    
    def update_lives_display(self):
        hearts = "♥ " * self.lives
        self.lives_label.config(text=hearts)

if __name__ == "__main__":
    root = tk.Tk()
    game = AWSIconGame(root)
    root.mainloop()
