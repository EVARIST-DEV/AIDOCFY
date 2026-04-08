import PIL.Image
import PIL.ImageDraw
import os

def draw_visuals(original_image_path: str, extraction_data, output_filename: str) -> str:
    img = PIL.Image.open(original_image_path)
    draw = PIL.ImageDraw.Draw(img, "RGBA")
    w, h = img.size

    
    for field in extraction_data.extracted_data:
        box = field.bounding_box
        x0, y0 = box.left * w, box.top * h
        x1, y1 = x0 + (box.width * w), y0 + (box.height * h)
        draw.rectangle([x0, y0, x1, y1], fill=(0, 100, 255, 50), outline="blue", width=3)

  
    for signal in extraction_data.visual_trust_signals:
        if signal.detected:
            box = signal.bounding_box
            x0, y0 = box.left * w, box.top * h
            x1, y1 = x0 + (box.width * w), y0 + (box.height * h)
            draw.rectangle([x0, y0, x1, y1], fill=(0, 255, 0, 50), outline="green", width=4)
            
    
    output_path = os.path.join("static", "processed_images", output_filename)
    img.save(output_path)
    return output_path