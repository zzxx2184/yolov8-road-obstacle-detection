# YOLOv8 기반 도로 장애물 탐지

직접 학습한 YOLOv8 모델을 활용하여 웹캠 영상에서
장애물을 탐지하고 빨간색 박스와 STOP 문구를 표시하는 개인 프로젝트입니다.

## 사용 기술
- Python
- Ultralytics YOLOv8
- OpenCV

## 주요 기능
- 웹캠 영상 입력
- 학습 모델을 활용한 객체 탐지
- 탐지 영역과 STOP 문구 표시
- Q 키를 눌러 종료

## 실행 방법
1. 필요한 라이브러리를 설치합니다.
   pip install -r requirements.txt
2. 학습한 best.pt 파일을 weights 폴더에 넣습니다.
3. 프로젝트 폴더에서 실행합니다.
   python detect_webcam.py

## 참고
- 탐지 코드의 모델 경로는 weights/best.pt로 설정합니다.
- 웹캠이 연결되어 있어야 합니다.
- STOP은 화면에 표시하는 문구이며 실제 차량 제동 기능은 없습니다.