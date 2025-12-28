#!/bin/bash

set -e  # Exit on any error

echo "📝 Publishing blog..."

# 1. Sync posts from Obsidian to Hugo
echo "→ Syncing posts from Obsidian..."
rsync -av --delete /Users/rajdeep/Blogs/posts/ "/Users/rajdeep/Borrowed Ideas/content/posts/"

# 2. Process images (converts Obsidian syntax & copies images)
echo "→ Processing images..."
python3 "/Users/rajdeep/Borrowed Ideas/images.py"

# 3. Push to GitHub
echo "→ Pushing to GitHub..."
cd "/Users/rajdeep/Borrowed Ideas"
git add -A

# Only commit if there are changes
if git diff --staged --quiet; then
    echo "✓ No changes to publish."
else
    git commit -m "Post update: $(date '+%Y-%m-%d %H:%M')"
    git push
    echo ""
    echo "✓ Published! Vercel will deploy in ~30 seconds."
fi

