from flask import Flask, render_template, request, jsonify, session
import random
from typing import Dict, List

app = Flask(__name__)
app.secret_key = 'spelling_bee_secret_key_2025'

class WordBank:
    """Manages the word banks for different difficulty levels and categories"""
    
    def __init__(self):
        # Easy words with definitions/hints and example sentences
        self.easy_words = {
            "that": "A word used to point to something specific",
            "above": "Higher than something else",
            "where": "In what place or location",
            "there": "In that place (not here)",
            "their": "Belonging to them",
            "which": "What one (used for choosing)",
            "what": "Used when asking about something",
            "when": "At what time",
            "with": "Together or using something",
            "this": "The thing near me now",
            "these": "More than one of this",
            "those": "More than one of that (over there)",
            "they": "Those people or things",
            "them": "Those people (as an object)",
            "then": "At that time, or next",
            "have": "To own or possess something",
            "said": "Past tense of speak",
            "each": "Every single one",
            "more": "A greater amount",
            "many": "A large number of",
            "time": "Hours, minutes, seconds",
            "very": "Extremely or really",
            "after": "Following something in time",
            "words": "Things we speak or write",
            "first": "Number one, before all others",
            "water": "Clear liquid we drink",
            "been": "Past tense of 'be'",
            "call": "To shout or telephone",
            "make": "To create or build",
            "down": "Toward the ground",
            "find": "To discover or locate",
            "head": "The part of body with your brain",
            "took": "Past tense of take",
            "just": "Only or recently",
            "name": "What you are called",
            "came": "Past tense of come",
            "right": "Correct or the opposite of left",
            "think": "To use your mind",
            "great": "Really good or large",
            "help": "To assist someone",
            "much": "A large amount",
            "before": "Earlier in time",
            "line": "A long thin mark",
            "means": "The way to do something",
            "same": "Exactly alike",
            "tell": "To say something to someone",
            "follow": "To go behind someone",
            "want": "To wish for something",
            "show": "To let someone see",
            "also": "Too, as well",
            "around": "On all sides",
            "form": "Shape or to make",
            "three": "The number after two",
            "small": "Not big",
            "again": "One more time",
            "turn": "To rotate or change direction"
        }
        
        # Medium words with definitions/hints
        self.medium_words = {
            "past": "Time that has already happened",
            "passed": "Went by or succeeded in a test",
            "quite": "Very or rather",
            "quiet": "Not making noise",
            "affect": "To influence or change something",
            "effect": "The result of a change",
            "accept": "To agree to receive something",
            "except": "Not including, but all others",
            "they're": "They are (contraction)",
            "your": "Belonging to you",
            "you're": "You are (contraction)",
            "its": "Belonging to it",
            "it's": "It is (contraction)",
            "too": "Also, or more than enough",
            "two": "The number 2",
            "brake": "Device to stop a vehicle",
            "break": "To crack or damage something",
            "steal": "To take without permission",
            "steel": "Strong metal made from iron",
            "flour": "Powder made from grain for baking",
            "flower": "Colorful part of a plant",
            "hear": "To listen with your ears",
            "meat": "Food from animals",
            "meet": "To come together with someone",
            "peace": "No fighting or war",
            "piece": "A part of something",
            "principal": "Head of a school",
            "principle": "A basic rule or belief",
            "weather": "Rain, sun, snow conditions",
            "whether": "If something will happen or not",
            "advice": "Helpful suggestions (noun)",
            "advise": "To give suggestions (verb)",
            "breath": "Air going in and out (noun)",
            "breathe": "To take air in and out (verb)",
            "choose": "To pick or select (present)",
            "chose": "To pick or select (past)",
            "loose": "Not tight or secure",
            "lose": "To misplace or not win",
            "desert": "Hot, sandy place with little water",
            "dessert": "Sweet food after dinner",
            "fair": "Equal treatment or a fun event",
            "fare": "Price to travel or food",
            "mail": "Letters and packages",
            "male": "Boy or man",
            "pain": "When something hurts",
            "pane": "Sheet of glass in window",
            "plain": "Simple or flat land",
            "plane": "Flying machine",
            "rain": "Water falling from clouds",
            "reign": "Period when a king/queen rules",
            "sail": "Travel by boat or boat's cloth",
            "sale": "Selling things, often cheaper",
            "tail": "Back end of an animal",
            "tale": "A story",
            "wait": "To stay until something happens",
            "weight": "How heavy something is",
            "wear": "To put on clothes",
            "wood": "Material from trees",
            "would": "Past form of will",
            "write": "To make words with a pen",
            "scene": "A view or part of a play",
            "seen": "Past tense of see",
            "threw": "Past tense of throw",
            "through": "From one side to the other",
            "weak": "Not strong",
            "week": "Seven days",
            "whole": "Complete, all of it",
            "hole": "Empty space or opening"
        }
        
        # Hard words with definitions/hints
        self.hard_words = {
            "courageous": "Very brave and fearless",
            "accommodation": "A place to stay, like a hotel",
            "bazaar": "A market with many shops",
            "extraordinary": "Very unusual or amazing",
            "magnificent": "Very beautiful or impressive",
            "unnecessary": "Not needed",
            "embarrassment": "Feeling ashamed or awkward",
            "restaurant": "Place where you buy and eat meals",
            "mediterranean": "Sea between Europe and Africa",
            "parallel": "Lines that never meet, always same distance apart",
            "privilege": "Special right or advantage",
            "guarantee": "Promise that something will work",
            "rhythm": "Regular beat in music or movement",
            "pneumonia": "Serious lung infection",
            "psychology": "Study of how the mind works",
            "scheme": "A plan or plot",
            "chocolate": "Sweet brown candy made from cocoa",
            "parachute": "Large cloth that helps you fall safely from a plane",
            "machine": "Device with moving parts that does work",
            "champagne": "Bubbly wine for celebrations",
            "moustache": "Hair grown above the upper lip",
            "technique": "Skillful way of doing something",
            "antique": "Something old and valuable",
            "boutique": "Small shop selling fashionable items",
            "colleague": "Person you work with",
            "intrigue": "Secret plotting or mystery",
            "fatigue": "Extreme tiredness",
            "vague": "Not clear or definite",
            "plague": "Widespread disease",
            "dialogue": "Conversation between people",
            "catalogue": "List of items for sale",
            "synagogue": "Jewish place of worship",
            "unconscious": "Not awake or aware",
            "disadvantage": "Something that makes success harder",
            "misunderstood": "Not understood correctly",
            "international": "Between different countries",
            "underground": "Below the surface of the earth",
            "supernatural": "Beyond natural or scientific explanation",
            "neighborhood": "Area where people live near each other",
            "breakthrough": "Important discovery or progress",
            "headquarters": "Main office of an organization",
            "straightforward": "Simple and easy to understand",
            "overwhelming": "Too much to handle",
            "sophisticated": "Complex and advanced",
            "pronunciation": "How words are spoken",
            "occasionally": "Sometimes, but not often",
            "definitely": "Certainly, without doubt",
            "separate": "Apart from each other",
            "maintenance": "Keeping something in good condition",
            "independence": "Freedom to make your own choices",
            "significance": "Importance or meaning",
            "intelligence": "Ability to learn and understand",
            "difference": "How things are not the same",
            "reference": "Mention of something or source of information",
            "preference": "What you like better",
            "conference": "Large meeting for discussion"
        }
    
    def get_words_for_age_group(self, age_group: str) -> Dict[str, str]:
        """Return appropriate words with definitions based on age group"""
        easy_list = list(self.easy_words.keys())
        medium_list = list(self.medium_words.keys()) 
        hard_list = list(self.hard_words.keys())
        
        if age_group == "5-6":
            # Shorter, simpler words
            selected_words = easy_list[:30]
        elif age_group == "7-8":
            # Mix of easy and some medium
            selected_words = easy_list + medium_list[:20]
        elif age_group == "9-10":
            # Mostly medium with some hard
            selected_words = easy_list[-20:] + medium_list + hard_list[:15]
        else:  # 11-12
            # Medium and hard words
            selected_words = medium_list + hard_list
        
        # Return dictionary with selected words and their definitions
        result = {}
        for word in selected_words:
            if word in self.easy_words:
                result[word] = self.easy_words[word]
            elif word in self.medium_words:
                result[word] = self.medium_words[word]
            elif word in self.hard_words:
                result[word] = self.hard_words[word]
        
        return result

# Initialize word bank
word_bank = WordBank()

def generate_sentence(word):
    """Generate a simple sentence using the word"""
    sentences = {
        # Easy words
        "that": "I like that book on the shelf.",
        "above": "The bird is flying above the tree.",
        "where": "Where did you put my toy?",
        "there": "Put the book over there please.",
        "their": "The children left their bags at school.",
        "which": "Which color do you like best?",
        "what": "What time is it now?",
        "when": "When will we have lunch?",
        "with": "I want to play with my friend.",
        "this": "This is my favorite game.",
        "water": "I drink water when I'm thirsty.",
        "make": "Let's make a cake together.",
        "find": "Can you help me find my shoes?",
        "right": "Turn right at the corner.",
        "think": "I think it will rain today.",
        "help": "Can you help me with this?",
        
        # Medium words
        "past": "We walked past the old house.",
        "passed": "She passed the test with flying colors.",
        "quite": "The movie was quite good.",
        "quiet": "Please be quiet in the library.",
        "affect": "Rain can affect our picnic plans.",
        "effect": "The medicine had a good effect.",
        "accept": "I accept your invitation to the party.",
        "except": "Everyone came except Tom.",
        "brake": "Press the brake to stop the car.",
        "break": "Don't break the glass vase.",
        "flower": "She picked a beautiful flower.",
        "flour": "We need flour to bake the bread.",
        
        # Hard words
        "courageous": "The firefighter was very courageous.",
        "accommodation": "We found nice accommodation for our trip.",
        "restaurant": "We ate dinner at a fancy restaurant.",
        "chocolate": "She loves chocolate ice cream.",
        "parachute": "The skydiver opened his parachute.",
        "machine": "This machine makes delicious smoothies."
    }
    
    return sentences.get(word.lower(), f"Here is an example with the word: The {word} is important.")

@app.route('/get_sentence/<word>')
def get_sentence(word):
    """Get an example sentence for a word"""
    sentence = generate_sentence(word)
    return jsonify({'sentence': sentence})

@app.route('/get_hint/<word>')
def get_hint(word):
    """Get a hint for the word"""
    words_dict = session.get('words_dict', {})
    definition = words_dict.get(word, "No definition available")
    return jsonify({'hint': definition})

@app.route('/')
def index():
    """Main page with age selection"""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game with selected age group"""
    age_group = request.json.get('age_group')
    
    if not age_group:
        return jsonify({'error': 'Please select an age group'}), 400
    
    # Get words for the age group
    words_dict = word_bank.get_words_for_age_group(age_group)
    word_list = list(words_dict.keys())
    random.shuffle(word_list)
    
    # Determine number of questions based on age
    if age_group == "5-6":
        total_questions = 5
    elif age_group == "7-8":
        total_questions = 7
    else:
        total_questions = 10
    
    # Store game state in session
    session['words_dict'] = words_dict
    session['word_list'] = word_list
    session['current_question'] = 0
    session['correct_answers'] = 0
    session['total_questions'] = total_questions
    session['age_group'] = age_group
    
    return jsonify({
        'success': True,
        'total_questions': total_questions,
        'age_group': age_group
    })

@app.route('/get_question')
def get_question():
    """Get the current question"""
    current_q = session.get('current_question', 0)
    word_list = session.get('word_list', [])
    words_dict = session.get('words_dict', {})
    total_q = session.get('total_questions', 10)
    
    if current_q >= total_q:
        return jsonify({'game_over': True})
    
    if current_q < len(word_list):
        current_word = word_list[current_q]
    else:
        # If we run out of words, shuffle and reuse
        random.shuffle(word_list)
        current_word = word_list[0]
        session['word_list'] = word_list
    
    # Get the definition for the current word
    definition = words_dict.get(current_word, "No definition available")
    
    # Reset the question answered flag for new question
    session['question_answered'] = False
    
    return jsonify({
        'word': current_word,
        'definition': definition,
        'question_number': current_q + 1,
        'total_questions': total_q,
        'score': session.get('correct_answers', 0)
    })

@app.route('/check_answer', methods=['POST'])
def check_answer():
    """Check the submitted answer"""
    user_answer = request.json.get('answer', '').strip().lower()
    current_q = session.get('current_question', 0)
    word_list = session.get('word_list', [])
    
    if current_q >= len(word_list):
        return jsonify({'error': 'No current question'}), 400
    
    # Check if this question was already answered
    if session.get('question_answered', False):
        return jsonify({'error': 'Question already answered'}), 400
    
    correct_word = word_list[current_q].lower()
    is_correct = user_answer == correct_word
    
    if is_correct:
        session['correct_answers'] = session.get('correct_answers', 0) + 1
    
    # Mark question as answered
    session['question_answered'] = True
    session['current_question'] = current_q + 1
    
    response = {
        'correct': is_correct,
        'correct_word': word_list[current_q],
        'score': session.get('correct_answers', 0),
        'question_number': current_q + 2,
        'total_questions': session.get('total_questions', 10)
    }
    
    # Check if game is over
    if session['current_question'] >= session.get('total_questions', 10):
        response['game_over'] = True
        response['final_score'] = session.get('correct_answers', 0)
        response['total_questions'] = session.get('total_questions', 10)
        response['percentage'] = (session.get('correct_answers', 0) / session.get('total_questions', 10)) * 100
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)