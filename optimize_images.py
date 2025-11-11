#!/usr/bin/env python3
"""
Image Optimization Script for Hugo Site
Converts PNG/JPG images to WebP format for better compression
"""

import os
from pathlib import Path
from PIL import Image

def optimize_image(image_path, quality=80):
    """Convert image to WebP format"""
    img_path = Path(image_path)
    
    # Skip if already WebP
    if img_path.suffix.lower() == '.webp':
        print(f"⏭️  Skipping {img_path.name} (already WebP)")
        return None
    
    # Create WebP filename
    webp_path = img_path.with_suffix('.webp')
    
    try:
        # Open and convert image
        with Image.open(img_path) as img:
            # Convert RGBA to RGB if necessary (WebP doesn't support transparency well in all cases)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Save as WebP
            img.save(webp_path, 'WEBP', quality=quality, method=6)
            
            # Get file sizes
            original_size = img_path.stat().st_size
            new_size = webp_path.stat().st_size
            savings = ((original_size - new_size) / original_size) * 100
            
            print(f"✅ {img_path.name} → {webp_path.name}")
            print(f"   Original: {original_size/1024/1024:.2f}MB | WebP: {new_size/1024/1024:.2f}MB | Saved: {savings:.1f}%")
            
            return {
                'original': img_path,
                'webp': webp_path,
                'original_size': original_size,
                'new_size': new_size,
                'savings_percent': savings
            }
    
    except Exception as e:
        print(f"❌ Error processing {img_path.name}: {e}")
        return None

def update_markdown_references(images_dir, conversions):
    """Update markdown files to reference WebP images"""
    content_dir = images_dir.parent.parent / 'content'
    
    if not content_dir.exists():
        return
    
    updated_files = []
    
    for md_file in content_dir.rglob('*.md'):
        content = md_file.read_text(encoding='utf-8')
        original_content = content
        
        # Update image references
        for conversion in conversions:
            if conversion:
                old_name = conversion['original'].name
                new_name = conversion['webp'].name
                old_path = f"/images/{conversion['original'].relative_to(images_dir).as_posix()}"
                new_path = f"/images/{conversion['webp'].relative_to(images_dir).as_posix()}"
                
                if old_path in content:
                    content = content.replace(old_path, new_path)
        
        if content != original_content:
            md_file.write_text(content, encoding='utf-8')
            updated_files.append(md_file.relative_to(content_dir))
            print(f"📝 Updated references in: {md_file.relative_to(content_dir)}")
    
    return updated_files

def main():
    # Get the images directory
    script_dir = Path(__file__).parent
    images_dir = script_dir / 'static' / 'images'
    
    print("🖼️  Image Optimization Script")
    print("=" * 60)
    
    # Find all PNG and JPG images
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg']:
        image_files.extend(images_dir.rglob(ext))
    
    if not image_files:
        print("No images found to optimize.")
        return
    
    print(f"\nFound {len(image_files)} images to optimize\n")
    
    # Convert images
    conversions = []
    total_original = 0
    total_new = 0
    
    for img_path in image_files:
        result = optimize_image(img_path, quality=80)
        if result:
            conversions.append(result)
            total_original += result['original_size']
            total_new += result['new_size']
        print()
    
    # Summary
    if conversions:
        total_savings = ((total_original - total_new) / total_original) * 100
        print("=" * 60)
        print(f"📊 SUMMARY")
        print(f"   Images optimized: {len(conversions)}")
        print(f"   Total original size: {total_original/1024/1024:.2f}MB")
        print(f"   Total WebP size: {total_new/1024/1024:.2f}MB")
        print(f"   Total savings: {total_savings:.1f}% ({(total_original-total_new)/1024/1024:.2f}MB)")
        print("=" * 60)
        
        # Update markdown references
        print("\n🔄 Updating markdown file references...")
        updated_files = update_markdown_references(images_dir, conversions)
        
        if updated_files:
            print(f"\n✅ Updated {len(updated_files)} markdown files")
        else:
            print("\n⚠️  No markdown files needed updating")
        
        print("\n⚠️  IMPORTANT: Review changes before committing!")
        print("   The original PNG/JPG files are still present.")
        print("   After verifying WebP images work, you can delete the originals.")

if __name__ == '__main__':
    main()
