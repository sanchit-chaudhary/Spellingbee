import tkinter as tk
from tkinter import ttk, messagebox
import random
import os
from typing import Dict, List, Tuple

# Configure display
if 'DISPLAY' not in os.environ:
    os.environ['DISPLAY'] = ':0'

class WordBank:
    """Manages the word banks for different difficulty levels and categories"""
    
    def __init__(self):
        # Easy words - grammatical and basic vocabulary
        self.easy_words = [
            "that", "above", "themselves", "where", "there", "their", "which", "what",
            "when", "with", "this", "these", "those", "they", "them", "then",
            "have", "said", "each", "more", "many", "time", "very", "after",
            "words", "first", "water", "been", "call", "who", "make", "may",
            "down", "side", "find", "head", "took", "just", "name", "came",
            "right", "think", "great", "help", "through", "much", "before",
            "line", "too", "means", "old", "any", "same", "tell", "boy",
            "follow", "want", "show", "also", "around", "form", "three",
            "small", "set", "put", "end", "why", "again", "turn", "here"
        ]
        
        # Medium words - homophones and commonly confused words
        self.medium_words = [
            "past", "passed", "quite", "quiet", "affect", "effect", "accept", "except",
            "there", "their", "they're", "your", "you're", "its", "it's", "to", "too", "two",
            "brake", "break", "steal", "steel", "flour", "flower", "hear", "here",
            "meat", "meet", "peace", "piece", "principal", "principle", "weather", "whether",
            "advice", "advise", "breath", "breathe", "choose", "chose", "loose", "lose",
            "desert", "dessert", "fair", "fare", "mail", "male", "pain", "pane",
            "plain", "plane", "rain", "reign", "sail", "sale", "tail", "tale",
            "wait", "weight", "wear", "where", "wood", "would", "right", "write",
            "scene", "seen", "threw", "through", "weak", "week", "whole", "hole"
        ]
        
        # Hard words - trigraphs, affixes, and foreign words
        self.hard_words = [
            "courageous", "accommodation", "bazaar", "extraordinary", "magnificent",
            "unnecessary", "embarrassment", "restaurant", "Mediterranean", "parallel",
            "privilege", "guarantee", "rhythm", "pneumonia", "psychology", "scheme",
            "chocolate", "parachute", "machine", "champagne", "moustache", "technique",
            "antique", "boutique", "colleague", "intrigue", "fatigue", "vague",
            "plague", "dialogue", "catalogue", "synagogue", "rogue", "vogue",
            "unconscious", "disadvantage", "misunderstood", "international", "underground",
            "supernatural", "extraordinary", "neighborhood", "breakthrough", "headquarters",
            "straightforward", "overwhelming", "sophisticated", "pronunciation", "occasionally",
            "definitely", "separate", "maintenance", "independence", "significance",
            "intelligence", "difference", "reference", "preference", "conference"
        ]
    
    def get_words_for_age_group(self, age_group: str) -> List[str]:
        """Return appropriate words based on age group"""
        age_mapping = {
            "5-6 years": self.easy_words[:30],  # Shorter, simpler words
            "7-8 years": self.easy_words + self.medium_words[:20],  # Mix of easy and some medium
            "9-10 years": self.easy_words[-20:] + self.medium_words + self.hard_words[:15],  # Mostly medium with some hard
            "11-12 years": self.medium_words + self.hard_words  # Medium and hard words
        }
        return age_mapping.get(age_group, self.easy_words)

class SpellingBeeGame:
    """Main game logic and UI"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Spelling Bee Adventure 🐝")
        self.root.geometry("800x600")
        self.root.configure(bg="#FFF8DC")  # Light yellow background
        
        # Game state variables
        self.word_bank = WordBank()
        self.current_words = []
        self.current_word = ""
        self.current_question = 0
        self.total_questions = 10
        self.correct_answers = 0
        self.game_started = False
        
        # Style configuration
        self.setup_styles()
        
        # Initialize UI
        self.setup_ui()
        
    def setup_styles(self):
        """Configure custom styles for ttk widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure('Game.TButton',
                       font=('Comic Sans MS', 12, 'bold'),
                       foreground='white',
                       background='#4CAF50',
                       padding=10)
        
        # Configure label style
        style.configure('Title.TLabel',
                       font=('Comic Sans MS', 24, 'bold'),
                       foreground='#2E8B57',
                       background='#FFF8DC')
        
        style.configure('Question.TLabel',
                       font=('Comic Sans MS', 16, 'bold'),
                       foreground='#4B0082',
                       background='#FFF8DC')
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#FFF8DC")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(main_frame, text="🐝 Spelling Bee Adventure 🐝", style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Setup area
        self.setup_frame = tk.Frame(main_frame, bg="#FFF8DC")
        self.setup_frame.pack(pady=20)
        
        # Age group selection
        age_label = tk.Label(self.setup_frame, text="Select your age group:", 
                            font=('Comic Sans MS', 14, 'bold'),
                            bg="#FFF8DC", fg="#2E8B57")
        age_label.pack(pady=10)
        
        self.age_var = tk.StringVar()
        age_options = ["5-6 years", "7-8 years", "9-10 years", "11-12 years"]
        self.age_combo = ttk.Combobox(self.setup_frame, textvariable=self.age_var,
                                     values=age_options, state="readonly",
                                     font=('Arial', 12), width=15)
        self.age_combo.pack(pady=10)
        self.age_combo.current(0)  # Default selection
        
        # Start button
        start_btn = tk.Button(self.setup_frame, text="🚀 Start Spelling Adventure!",
                             command=self.start_game,
                             font=('Comic Sans MS', 14, 'bold'),
                             bg="#FF6B6B", fg="white",
                             padx=20, pady=10,
                             cursor="hand2")
        start_btn.pack(pady=20)
        
        # Game area (hidden initially)
        self.game_frame = tk.Frame(main_frame, bg="#FFF8DC")
        
        # Progress indicator
        self.progress_label = tk.Label(self.game_frame, text="",
                                      font=('Comic Sans MS', 12, 'bold'),
                                      bg="#FFF8DC", fg="#4B0082")
        self.progress_label.pack(pady=10)
        
        # Word display area
        word_frame = tk.Frame(self.game_frame, bg="#E6E6FA", relief=tk.RAISED, bd=3)
        word_frame.pack(pady=20, padx=50, fill=tk.X)
        
        self.word_label = tk.Label(word_frame, text="",
                                  font=('Comic Sans MS', 20, 'bold'),
                                  bg="#E6E6FA", fg="#4B0082",
                                  pady=20)
        self.word_label.pack()
        
        # Input area
        input_label = tk.Label(self.game_frame, text="Type the spelling:",
                              font=('Comic Sans MS', 14, 'bold'),
                              bg="#FFF8DC", fg="#2E8B57")
        input_label.pack(pady=(20, 5))
        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.game_frame, textvariable=self.entry_var,
                             font=('Arial', 16), width=30,
                             justify='center')
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda e: self.check_spelling())
        
        # Submit button
        submit_btn = tk.Button(self.game_frame, text="✓ Check Spelling",
                              command=self.check_spelling,
                              font=('Comic Sans MS', 12, 'bold'),
                              bg="#4CAF50", fg="white",
                              padx=20, pady=8,
                              cursor="hand2")
        submit_btn.pack(pady=10)
        
        # Feedback area
        self.feedback_label = tk.Label(self.game_frame, text="",
                                      font=('Comic Sans MS', 14, 'bold'),
                                      bg="#FFF8DC", pady=10)
        self.feedback_label.pack(pady=10)
        
        # Next button (hidden initially)
        self.next_btn = tk.Button(self.game_frame, text="➡️ Next Word",
                                 command=self.next_question,
                                 font=('Comic Sans MS', 12, 'bold'),
                                 bg="#2196F3", fg="white",
                                 padx=20, pady=8,
                                 cursor="hand2")
        
        # Score area
        self.score_label = tk.Label(self.game_frame, text="",
                                   font=('Comic Sans MS', 12, 'bold'),
                                   bg="#FFF8DC", fg="#FF6B6B")
        self.score_label.pack(pady=10)
    
    def start_game(self):
        """Initialize and start a new game"""
        if not self.age_var.get():
            messagebox.showwarning("Age Group Required", "Please select your age group first!")
            return
        
        # Get words for selected age group
        self.current_words = self.word_bank.get_words_for_age_group(self.age_var.get())
        random.shuffle(self.current_words)
        
        # Reset game state
        self.current_question = 0
        self.correct_answers = 0
        self.game_started = True
        
        # Adjust total questions based on age group
        age_group = self.age_var.get()
        if age_group == "5-6 years":
            self.total_questions = 5
        elif age_group == "7-8 years":
            self.total_questions = 7
        else:
            self.total_questions = 10
        
        # Hide setup, show game
        self.setup_frame.pack_forget()
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        
        # Start first question
        self.next_question()
    
    def next_question(self):
        """Move to the next question"""
        if self.current_question >= self.total_questions:
            self.end_game()
            return
        
        # Select next word
        if self.current_question < len(self.current_words):
            self.current_word = self.current_words[self.current_question]
        else:
            # If we run out of words, shuffle and reuse
            random.shuffle(self.current_words)
            self.current_word = self.current_words[0]
        
        # Update UI
        self.progress_label.config(text=f"Question {self.current_question + 1} of {self.total_questions}")
        self.word_label.config(text=f'Spell this word: "{self.current_word}"')
        self.entry_var.set("")
        self.entry.focus_set()
        self.feedback_label.config(text="")
        self.next_btn.pack_forget()
        
        # Update score display
        self.score_label.config(text=f"Score: {self.correct_answers}/{self.current_question}")
    
    def check_spelling(self):
        """Check if the entered spelling is correct"""
        user_input = self.entry_var.get().strip().lower()
        correct_spelling = self.current_word.lower()
        
        if not user_input:
            messagebox.showwarning("Empty Input", "Please enter a spelling!")
            return
        
        if user_input == correct_spelling:
            self.correct_answers += 1
            self.feedback_label.config(text="🎉 Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(
                text=f"❌ Incorrect. The correct spelling is: {self.current_word}",
                fg="red"
            )
        
        self.current_question += 1
        
        # Show next button or end game
        if self.current_question < self.total_questions:
            self.next_btn.pack(pady=10)
        else:
            # Small delay before ending game
            self.root.after(2000, self.end_game)
        
        # Update score
        self.score_label.config(text=f"Score: {self.correct_answers}/{self.current_question}")
    
    def end_game(self):
        """End the game and show results"""
        # Calculate percentage
        percentage = (self.correct_answers / self.total_questions) * 100
        
        # Generate encouraging message
        if percentage >= 90:
            message = "🌟 Outstanding! You're a spelling superstar!"
            emoji = "🏆"
        elif percentage >= 80:
            message = "🎉 Excellent work! You're getting really good at spelling!"
            emoji = "⭐"
        elif percentage >= 70:
            message = "👍 Great job! Keep practicing and you'll be even better!"
            emoji = "🎯"
        elif percentage >= 60:
            message = "😊 Good effort! Practice makes perfect!"
            emoji = "📚"
        else:
            message = "💪 Nice try! Keep practicing - you'll improve with time!"
            emoji = "🌱"
        
        # Show results dialog
        result_text = f"""
{emoji} Game Complete! {emoji}

Final Score: {self.correct_answers} out of {self.total_questions}
Percentage: {percentage:.1f}%

{message}

Would you like to play again?
        """
        
        play_again = messagebox.askyesno("Game Complete", result_text)
        
        if play_again:
            self.restart_game()
        else:
            self.root.quit()
    
    def restart_game(self):
        """Restart the game"""
        self.game_frame.pack_forget()
        self.setup_frame.pack(pady=20)
        self.game_started = False
        
        # Reset variables
        self.current_question = 0
        self.correct_answers = 0
        self.entry_var.set("")
        self.feedback_label.config(text="")
    
    def run(self):
        """Start the application"""
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
        
        # Start the main loop
        self.root.mainloop()

def main():
    """Main function to run the Spelling Bee game"""
    try:
        game = SpellingBeeGame()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
