from pathlib import Path
from typing import List

import boto3
from mypy_boto3_rekognition.type_defs import (
    CelebrityTypeDef,
    RecognizeCelebritiesResponseTypeDef,
)
from PIL import Image, ImageDraw, ImageFont
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cliente AWS Rekognition
client = boto3.client("rekognition")


def get_photo_paths(input_folder: Path) -> List[Path]:
    """
    Retorna uma lista de caminhos para todas as imagens na pasta de entrada.
    """
    return list(input_folder.glob("*.[jp][pn]g"))  # Suporta .jpg e .png


def recognize_celebrities(photo_path: Path) -> RecognizeCelebritiesResponseTypeDef:
    """
    Chama a API Rekognition para identificar celebridades em uma imagem.
    """
    try:
        with open(photo_path, "rb") as image:
            response = client.recognize_celebrities(Image={"Bytes": image.read()})
        return response
    except Exception as e:
        logging.error(f"Erro ao reconhecer celebridades na imagem {photo_path}: {e}")
        raise


def draw_boxes_on_faces(
    image_path: Path,
    output_path: Path,
    face_details: List[CelebrityTypeDef],
    min_confidence: float = 90.0,
):
    """
    Desenha caixas ao redor dos rostos detectados e salva a imagem resultante.
    """
    try:
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 20)

        width, height = image.size

        for face in face_details:
            box = face["Face"]["BoundingBox"]
            left = int(box["Left"] * width)
            top = int(box["Top"] * height)
            right = int((box["Left"] + box["Width"]) * width)
            bottom = int((box["Top"] + box["Height"]) * height)

            confidence = face.get("MatchConfidence", 0.0)
            if confidence >= min_confidence:
                draw.rectangle([left, top, right, bottom], outline="red", width=3)

                text = face.get("Name", "")
                position = (left, top - 20)
                bbox = draw.textbbox(position, text, font=font)
                draw.rectangle(bbox, fill="red")
                draw.text(position, text, font=font, fill="white")

        image.save(output_path)
        logging.info(f"Imagem salva com resultados em: {output_path}")

    except Exception as e:
        logging.error(f"Erro ao desenhar caixas na imagem {image_path}: {e}")
        raise


def process_images(input_folder: Path, output_folder: Path):
    """
    Processa todas as imagens na pasta de entrada, identificando celebridades e
    salvando os resultados na pasta de saída.
    """
    photo_paths = get_photo_paths(input_folder)

    if not photo_paths:
        logging.info(f"Nenhuma imagem encontrada na pasta: {input_folder}")
        return

    for photo_path in photo_paths:
        try:
            logging.info(f"Processando imagem: {photo_path}")
            response = recognize_celebrities(photo_path)
            faces = response.get("CelebrityFaces", [])

            if not faces:
                logging.info(f"Nenhuma celebridade encontrada na imagem: {photo_path}")
                continue

            output_path = output_folder / f"{photo_path.stem}_processada.jpg"
            draw_boxes_on_faces(photo_path, output_path, faces)

        except Exception as e:
            logging.error(f"Erro ao processar a imagem {photo_path}: {e}")


if __name__ == "__main__":
    # Diretórios de entrada e saída
    base_folder = Path(__file__).parent / "images"
    input_folder = base_folder / "originais"
    output_folder = base_folder / "reconhecidas"

    # Certifique-se de que a pasta de saída existe
    output_folder.mkdir(parents=True, exist_ok=True)

    # Processar imagens
    process_images(input_folder, output_folder)
