from PIL import Image

# 이미지 파일 이름 (위에서 받은 파일명과 동일해야 해!)
image_path = "person_image.png"

try:
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지 보여주기 (기본 이미지 뷰어로 열림)
    img.show()

except FileNotFoundError:
    print(f"❌ 이미지 파일을 찾을 수 없습니다: {image_path}")
except Exception as e:
    print(f"⚠️ 오류 발생: {e}")
