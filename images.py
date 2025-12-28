import os
import re
import shutil

# Source directories (Obsidian vault)
source_posts_dir = "/Users/rajdeep/Blogs/posts"
attachments_dir = "/Users/rajdeep/Blogs/assets/"

# Hugo directories
hugo_posts_dir = "/Users/rajdeep/Borrowed Ideas/content/posts"
static_images_dir = "/Users/rajdeep/Borrowed Ideas/static/images"

os.makedirs(static_images_dir, exist_ok=True)
os.makedirs(hugo_posts_dir, exist_ok=True)

for filename in os.listdir(source_posts_dir):
    if not filename.endswith(".md"):
        continue

    source_filepath = os.path.join(source_posts_dir, filename)

    with open(source_filepath, "r") as file:
        content = file.read()

    # Convert Obsidian image syntax ![[image.png]] to Markdown ![Image](/images/image.png)
    images = re.findall(
        r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|webp))\]\]', content, re.IGNORECASE)

    for image in images:
        markdown_image = f"![Image](/images/{image.replace(' ', '%20')})"
        content = content.replace(f"![[{image}]]", markdown_image)

        img_src = os.path.join(attachments_dir, image)
        if os.path.exists(img_src):
            shutil.copy(img_src, static_images_dir)

    # Write to Hugo content directory
    hugo_filepath = os.path.join(hugo_posts_dir, filename)
    with open(hugo_filepath, "w") as file:
        file.write(content)

print("Done")
