#!/bin/bash
set -e

echo "Building Elm frontend..."

# Navigate to frontend directory
cd "$(dirname "$0")/../frontend"

# Check if node_modules exists, if not prompt to install
if [ ! -d "node_modules" ]; then
    echo "node_modules not found. Installing dependencies..."
    npm install
fi

# Build Elm app
echo "Compiling Elm..."
npm run build

# Copy HTML and other assets to dist
echo "Copying assets to dist..."
cp public/index.html ../dist/

echo "✓ Frontend build complete!"
echo "Files available in dist/ directory"
