# -*- coding:utf-8 -*-
import cv2
import sys


def detect_bubble():
    src = cv2.imread('02.circles.jpeg')
        
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # 블러를 통해 노이즈 제거
    blr = cv2.GaussianBlur(gray, (0, 0), 1.0)

    # 트랙바 함수 정의
    def on_trackbar(pos):
        # 트랙바 초기값 정보 받아오기
        rmin = cv2.getTrackbarPos('minRadius', 'img')
        rmax = cv2.getTrackbarPos('maxRadius', 'img')
        th = cv2.getTrackbarPos('threshold', 'img')
        
        # 받아온 정보를 cv2.HoughCircles에 입력
        circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 0.5, 50, param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
        # circles = cv2.Hough_GRADIENT_ALT(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
        
        dst = src.copy() # 복사한 입력영상 위에 원 그리기
        if circles is not None:
            for i in range(circles.shape[1]): # 검출된 원 갯수만큼 반복
                cx, cy, radius = circles[0][i] # i번째 원에 데이터 저장
                cv2.circle(dst, (cx, cy), int(radius), (0, 0, 255), 2, cv2.LINE_AA) # 저장된 데이터를 이용해 원 그리기
        
        cv2.imshow('img', dst)
        
    # 트랙바 생성
    cv2.imshow('img', src)

    # 트랙바 범위
    cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
    cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
    cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)

    # 트랙바 초깃값
    cv2.setTrackbarPos('minRadius', 'img', 10) # 초기값 10
    cv2.setTrackbarPos('maxRadius', 'img', 80)
    cv2.setTrackbarPos('threshold', 'img', 40)

    cv2.waitKey()

    cv2.destroyAllWindows()



def test():
    # 원본 이미지 & 결과 이미지 선언
    src = cv2.imread("1.jpg")
    dst = src.copy()

    # 전처리를 위한 그레이스케일 이미지 사용
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # 원 검출(검출 이미지, 검출 방법, 해상도 비율, 최소 거리, 캐니 엣지 임계값, 중심 임계값, 최소 반지름, 최대 반지름)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 250, param2 = 10, minRadius = 80, maxRadius = 120)


    # circles는 (1, N, 3)차원 형태를 가짐
    for i in circles[0]:
        cv2.circle(dst, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), 5)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    detect_bubble()