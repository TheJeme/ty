from PIL import Image
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import pandas as pd
import json
import yaml
import os
import sys

def main():
  input_file_path = sys.argv[1] if len(sys.argv) > 1 else input("Enter source file path: ")
  input_file_extension = input_file_path.split(".")[-1]
  
  output_file_path = sys.argv[2] if len(sys.argv) > 2 else input("Enter target file path: ")
  output_file_extension = output_file_path.split(".")[-1]

  if not os.path.isfile(input_file_path) :
    print("Invalid source file path")
    return

  if input_file_extension == "mp3" and output_file_extension == "mp4": # mp3 -> mp4
    audio = AudioSegment.from_mp3(input_file_path)
    audio.export(output_file_path, format="mp4")
  elif input_file_extension == "mp4" and output_file_extension == "mp3": # mp4 -> mp3
    video = VideoFileClip(input_file_path)
    audio = video.audio
    audio.write_audiofile(output_file_path)
  elif input_file_extension == "mp4" and output_file_extension == "gif": # mp4 -> gif
    video = VideoFileClip(input_file_path)
    video.write_gif(output_file_path)
  elif input_file_extension == "gif" and output_file_extension == "mp4": # gif -> mp4
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "json" and output_file_extension == "yaml": # json -> yaml
    with open(input_file_path, "r") as json_file:
      data = json.load(json_file)
      with open(output_file_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
  elif input_file_extension == "yaml" and output_file_extension == "json": # yaml -> json
    with open(input_file_path, "r") as yaml_file:
      data = yaml.load(yaml_file, Loader=yaml.FullLoader)
      with open(output_file_path, "w") as json_file:
        json.dump(data, json_file)
  elif input_file_extension == "json" and output_file_extension == "xml": # json -> xml
    with open(input_file_path, "r") as json_file:
      data = json.load(json_file)
      xml = "<root>\n"
      for key, value in data.items():
        xml += f"  <{key}>{value}</{key}>\n"
      xml += "</root>"
      with open(output_file_path, "w") as xml_file:
        xml_file.write(xml)
  elif input_file_extension == "xml" and output_file_extension == "json": # xml -> json
    with open(input_file_path, "r") as xml_file:
      xml = xml_file.read()
      data = {}
      for line in xml.split("\n"):
        if line.strip() == "<root>" or line.strip() == "</root>":
          continue
        key = line.split(">")[0].split("<")[-1]
        value = line.split(">")[-2].split("<")[-1]
        data[key] = value
      with open(output_file_path, "w") as json_file:
        json.dump(data, json_file)
  elif input_file_extension == "yaml" and output_file_extension == "xml": # yaml -> xml
    with open(input_file_path, "r") as yaml_file:
      data = yaml.load(yaml_file, Loader=yaml.FullLoader)
      xml = "<root>\n"
      for key, value in data.items():
        xml += f"  <{key}>{value}</{key}>\n"
      xml += "</root>"
      with open(output_file_path, "w") as xml_file:
        xml_file.write(xml)
  elif input_file_extension == "xml" and output_file_extension == "yaml": # xml -> yaml
    with open(input_file_path, "r") as xml_file:
      xml = xml_file.read()
      data = {}
      for line in xml.split("\n"):
        if line.strip() == "<root>" or line.strip() == "</root>":
          continue
        key = line.split(">")[0].split("<")[-1]
        value = line.split(">")[-2].split("<")[-1]
        data[key] = value
      with open(output_file_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
  elif input_file_extension == "json" and output_file_extension == "json": # json -> json
    with open(input_file_path, "r") as json_file:
      data = json.load(json_file)
      with open(output_file_path, "w") as json_file:
        json.dump(data, json_file)
  elif input_file_extension == "yaml" and output_file_extension == "yaml": # yaml -> yaml
    with open(input_file_path, "r") as yaml_file:
      data = yaml.load(yaml_file, Loader=yaml.FullLoader)
      with open(output_file_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
  elif input_file_extension == "xml" and output_file_extension == "xml": # xml -> xml
    with open(input_file_path, "r") as xml_file:
      xml = xml_file.read()
      with open(output_file_path, "w") as xml_file:
        xml_file.write(xml)
  elif input_file_extension == "mp3" and output_file_extension == "mp3": # mp3 -> mp3
    audio = AudioSegment.from_mp3(input_file_path)
    audio.export(output_file_path, format="mp3")
  elif input_file_extension == "mp4" and output_file_extension == "mp4": # mp4 -> mp4
    video = VideoFileClip(input_file_path)
    video.write_videofile(output_file_path)
  elif input_file_extension == "gif" and output_file_extension == "gif": # gif -> gif
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "jpg" and output_file_extension == "gif": # jpg -> gif
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "gif": # png -> gif
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "gif": # jpeg -> gif
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "gif": # bmp -> gif
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "gif": # webp -> gif
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "gif" and output_file_extension == "jpg": # gif -> jpg
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "gif" and output_file_extension == "png": # gif -> png
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "gif" and output_file_extension == "jpeg": # gif -> jpeg
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "gif" and output_file_extension == "bmp": # gif -> bmp
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "gif" and output_file_extension == "webp": # gif -> webp
    gif = Image.open(input_file_path)
    gif.save(output_file_path, save_all=True, append_images=[gif], loop=0)
  elif input_file_extension == "jpg" and output_file_extension == "jpg": # jpg -> jpg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "png": # png -> png
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "jpeg": # jpeg -> jpeg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpg" and output_file_extension == "png": # jpg -> png
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "jpg": # png -> jpg
    with Image.open(input_file_path) as image:
        if image.mode == 'P':
            image = image.convert('RGB')
        image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "png": # jpeg -> png
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "jpeg": # png -> jpeg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpg" and output_file_extension == "jpeg": # jpg -> jpeg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "jpg": # jpeg -> jpg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "bmp": # bmp -> bmp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "jpg": # bmp -> jpg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "png": # bmp -> png
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "jpeg": # bmp -> jpeg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "bmp": # jpeg -> bmp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpg" and output_file_extension == "bmp": # jpg -> bmp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "bmp": # png -> bmp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "webp": # webp -> webp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "jpg": # webp -> jpg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "png": # webp -> png
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "jpeg": # webp -> jpeg
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "webp" and output_file_extension == "bmp": # webp -> bmp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpg" and output_file_extension == "webp": # jpg -> webp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "png" and output_file_extension == "webp": # png -> webp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "jpeg" and output_file_extension == "webp": # jpeg -> webp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "bmp" and output_file_extension == "webp": # bmp -> webp
    image = Image.open(input_file_path)
    image.save(output_file_path)
  elif input_file_extension == "mp3" and output_file_extension == "wav": # mp3 -> wav
    audio = AudioSegment.from_mp3(input_file_path)
    audio.export(output_file_path, format="wav")
  elif input_file_extension == "wav" and output_file_extension == "mp3": # wav -> mp3
    audio = AudioSegment.from_wav(input_file_path)
    audio.export(output_file_path, format="mp3")
  elif input_file_extension == "wav" and output_file_extension == "wav": # wav -> wav
    audio = AudioSegment.from_wav(input_file_path)
    audio.export(output_file_path, format="wav")
  elif input_file_extension == "csv" and output_file_extension == "xlsx": # csv -> xlsx
    df = pd.read_csv(input_file_path)
    df.to_excel(output_file_path, index=False)
  elif input_file_extension == "xlsx" and output_file_extension == "csv": # xlsx -> csv
    df = pd.read_excel(input_file_path)
    df.to_csv(output_file_path, index=False)
  elif input_file_extension == "csv" and output_file_extension == "csv": # csv -> csv
    df = pd.read_csv(input_file_path)
    df.to_csv(output_file_path, index=False)
  elif input_file_extension == "xlsx" and output_file_extension == "xlsx": # xlsx -> xlsx
    df = pd.read_excel(input_file_path)
    df.to_excel(output_file_path, index=False)
  elif input_file_extension == "json" and output_file_extension == "csv": # json -> csv
    with open(input_file_path, "r") as json_file:
      data = json.load(json_file)
      df = pd.DataFrame(data)
      df.to_csv(output_file_path, index=False)
  elif input_file_extension == "csv" and output_file_extension == "json": # csv -> json
    df = pd.read_csv(input_file_path)
    df.to_json(output_file_path, orient="records")
  elif input_file_extension == "txt" and output_file_extension == "txt": # txt -> txt
    with open(input_file_path, "r") as txt_file:
      txt = txt_file.read()
      with open(output_file_path, "w") as txt_file:
        txt_file.write(txt)
  elif input_file_extension == "txt" and output_file_extension == "csv": # txt -> csv
    with open(input_file_path, "r") as txt_file:
      txt = txt_file.read()
      with open(output_file_path, "w") as csv_file:
        csv_file.write(txt)
  elif input_file_extension == "csv" and output_file_extension == "txt": # csv -> txt
    with open(input_file_path, "r") as csv_file:
      csv = csv_file.read()
      with open(output_file_path, "w") as txt_file:
        txt_file.write(csv)
  elif input_file_extension == "txt" and output_file_extension == "json": # txt -> json
    with open(input_file_path, "r") as txt_file:
      txt = txt_file.read()
      with open(output_file_path, "w") as json_file:
        json_file.write(json.dumps(txt))
  elif input_file_extension == "json" and output_file_extension == "txt": # json -> txt
    with open(input_file_path, "r") as json_file:
      txt = json.load(json_file)
      with open(output_file_path, "w") as txt_file:
        txt_file.write(txt)
  else:
    print("Conversion not supported")
    return

  print("Conversion successful")

if __name__ == "__main__":
  main()



