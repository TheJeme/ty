# ty
cli app file format conversion tool.

## Usage
```bash
ty <input_file> <output_file>
```

## Example
```bash
ty input.jpg output.png
```

## List of supported file formats

### Image
jpg, png, gif, bmp, webp

### Audio
mp3, wav, ogg, flac, aac

### Video
mp4, webm, mkv, avi, mov

## Other
pdf, docx, xlsx, pptx, txt, json, yaml, xml, csv


## Build
```bash
pyinstaller --name ty __main__.py
```