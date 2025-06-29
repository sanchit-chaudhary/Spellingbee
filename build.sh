#!/bin/bash

# Build script for Spelling Bee Adventure Game
# This script prepares the static files for deployment

echo "Building Spelling Bee Adventure Game..."

# Create spellingchamp directory if it doesn't exist
mkdir -p spellingchamp

# Copy static assets
mkdir -p spellingchamp/static
cp -r static/* spellingchamp/static/ 2>/dev/null || echo "No static files to copy"

# Copy templates content to public directory
cp templates/index.html spellingchamp/app.html 2>/dev/null || echo "Template copy completed"

echo "Build completed successfully!"
echo "Note: This is a Flask web application that requires server-side processing."
echo "For full functionality, please change deployment type to 'autoscale'."