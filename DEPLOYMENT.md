# Spelling Bee Adventure - Deployment Guide

## Quick Fix for Current Deployment Error

The deployment is currently configured for **static hosting**, but this is a **Flask web application** that requires server-side processing.

### Recommended Solution (Best Experience)

**Change deployment type from "static" to "autoscale":**

1. Go to your Replit deployment settings
2. Change `deploymentTarget` from `"static"` to `"autoscale"`
3. Remove the `publicDir = "spellingchamp"` line
4. Deploy the application

This will enable the full interactive spelling bee game with:
- Real-time scoring
- Session management
- Audio pronunciation
- Dynamic word generation
- Age-appropriate difficulty levels

### Alternative: Current Static Deployment

If you need to keep static deployment, the following files have been created:

- `spellingchamp/` - Public directory with static fallback
- `spellingchamp/index.html` - Landing page explaining the limitation
- `build.sh` - Script to prepare static files
- `wsgi.py` - WSGI entry point for production

**Limitations of static deployment:**
- No server-side game logic
- No session management
- Limited interactivity
- Cannot save progress

### Files Created to Fix Deployment Issues

1. **spellingchamp/index.html** - Static landing page
2. **build.sh** - Build script for static files
3. **wsgi.py** - WSGI entry point for Flask deployment
4. **DEPLOYMENT.md** - This deployment guide

### Deployment Configuration Files

The application includes:
- `app.py` - Main Flask application
- `templates/index.html` - Main game interface
- `static/` - Static assets (images, CSS)
- `pyproject.toml` - Python dependencies

### Testing Deployment

- **Local testing**: Run `python app.py` and visit http://localhost:5000
- **Production**: Use autoscale deployment for full functionality
- **Static fallback**: Shows guidance message and deployment instructions

## Summary

**For the best user experience, change the deployment type to "autoscale" instead of "static".**

The static deployment setup has been created as a fallback, but the full spelling bee game requires Flask server functionality.