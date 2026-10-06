import cv2
from ultralytics import YOLO

# 1. 회원님이 직접 학습시킨 모델 불러오기
model = YOLO("weights/best.pt")

# 2. 웹캠 켜기
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # 🚨 사람이나 킥보드 탄 형체를 놓치지 않게 확신도 0.2로 설정
        results = model(frame, conf=0.2)
        
        for result in results:
            for box in result.boxes:
                # 박스 좌표 추출
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # 🚨 [수정 사항] 빨간색 박스는 유지하되, 텍스트는 심플하게 "장애물"
                # 두께 3의 빨간색 사각형
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                
                # 가독성을 위해 검정색 배경에 흰색 글씨로 "장애물" 표시 (한글 깨짐 방지를 위해 영어 권장하나, 
                # 시스템에 따라 한글 출력이 안 될 수 있어 영어 'OBSTACLE'을 쓰고 시연 때 '장애물'이라 설명하시거나, 
                # 확실하게 'STOP'으로 표기하는 것이 논리적입니다.)
                
                # 만약 한글이 깨진다면 아래 label을 "STOP" 혹은 "OBSTACLE"로만 바꿔주세요!
                label = "STOP" 
                
                # 글자 배경 박스 (텍스트가 더 잘 보이게 함)
                cv2.rectangle(frame, (x1, y1 - 25), (x1 + 80, y1), (0, 0, 255), -1)
                cv2.putText(frame, label, (x1 + 5, y1 - 5), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # 시스템 창 이름
        cv2.imshow("Autopilot: Emergency Braking System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)