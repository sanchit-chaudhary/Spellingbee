# Spelling Bee Adventure Game  
Interactive Spelling Bee Adventure Game for Kids - Built with Flask

**Made with ❤️ by Sanchit**  
If you'd like to reuse this project, feel free :-)

## ⚠️ License & Reuse Restrictions

For educational use only.  
To request access or permission, please email: [sanchit.chaudhary@live.com](mailto:sanchit.chaudhary@live.com)


## Overview

This is a Python-based Spelling Bee game for kids built with Flask web framework. The application provides an engaging spelling practice environment with age-appropriate difficulty levels, interactive help features, and colorful child-friendly design to help kids improve their spelling skills.

## System Architecture

### Frontend Architecture
- **Web Framework**: Flask with HTML/CSS/JavaScript for responsive web interface
- **Single-page Application**: All functionality contained within one main web page
- **Event-driven Architecture**: User interactions trigger AJAX calls for real-time feedback
- **Responsive Design**: Colorful, child-friendly interface with interactive help features
- **Audio Integration**: Text-to-speech pronunciation using Web Speech API

### Backend Architecture
- **Object-oriented Design**: Core functionality encapsulated in WordBank and Flask route classes
- **Word Management System**: Centralized word bank with age-appropriate categorized difficulty levels
- **Session Management**: Flask sessions for game state tracking across requests
- **Help System**: Interactive audio, hint, and sentence example features

## Key Components

### WordBank Class
- **Purpose**: Manages vocabulary sets with definitions for different age groups
- **Categories**:
  - Easy: Basic grammatical words and common vocabulary (50+ words with definitions)
  - Medium: Homophones and commonly confused words (60+ words with definitions)
  - Hard: Complex words with trigraphs, affixes, and foreign origins (50+ words with definitions)
- **Design Decision**: Words paired with kid-friendly definitions instead of showing actual words

### Main Application Components
- **Age Group Selection**: Dropdown for ages 5-6, 7-8, 9-10, 11-12 years
- **Spelling Interface**: Definition display and input field for spelling practice
- **Help System**: Audio pronunciation, hints, and sentence examples
- **Score Tracking**: Real-time scoring with encouraging feedback messages
- **Question Management**: Age-appropriate number of questions (5-10 based on age)

## Data Flow

1. **Initialization**: Application loads with default difficulty level
2. **Word Selection**: Random words chosen from selected difficulty category
3. **Typing Session**: User types displayed words while system tracks metrics
4. **Real-time Feedback**: Continuous calculation of speed and accuracy
5. **Session Completion**: Final results display and option to restart

## External Dependencies

### Core Dependencies
- **tkinter**: Built-in Python GUI toolkit (no external installation required)
- **random**: Built-in Python module for word randomization
- **typing**: Built-in Python module for type hints and better code documentation

### Development Dependencies
- No external package management (pip) dependencies
- Self-contained application design for easy deployment

## Deployment Strategy

### Flask Web Application Deployment (Recommended)
- **Server Requirements**: Flask web server with session management for game state
- **Port Configuration**: Runs on port 5000 with 0.0.0.0 binding for external access
- **Entry Points**: app.py (main) and wsgi.py (production deployment)

### Static Deployment Fallback (Limited Functionality)
- **Backup Method**: Current static deployment configuration with spellingchamp directory
- **Limitations**: Cannot provide full interactive spelling bee functionality without server
- **Build Process**: Use build.sh script to prepare static files
- **User Experience**: Shows deployment guidance and redirect instructions


## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

- June 28, 2025: Initial Flask web application setup

## Attribution

This game was created by **Sanchit** as a fun and educational project for children.  
If you'd like to reuse or contribute to this project, please contact:  
📧 [sanchit.chaudhary@live.com](mailto:sanchit.chaudhary@live.com)

