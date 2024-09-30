import whisper
import os
from tqdm import tqdm

# 현재 작업 디렉토리 기준으로 절대 경로 설정
audio_folder = os.path.abspath(os.path.join("audio"))

# Whisper 모델 로드
model = whisper.load_model("medium")

# "audio" 폴더 내의 모든 .mp3 파일을 리스트로 가져오기
audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".mp3")]

# tqdm를 이용해 파일 개수만큼 프로그레스 바를 생성하고 처리
for filename in tqdm(audio_files, desc="Processing audio files"):
    audio_file_path = os.path.join(audio_folder, filename)

    # Whisper로 오디오 파일에서 텍스트 추출
    result = model.transcribe(audio_file_path)

    # 변환된 텍스트를 "audio" 폴더에 .txt 파일로 저장
    output_text_path = os.path.join(audio_folder, f"{filename[:-4]}.txt")
    with open(output_text_path, "w") as f:
        f.write(result["text"])

    # 진행 상황 출력
    print(f"{filename} 변환 완료, 텍스트 파일 저장: {output_text_path}")
