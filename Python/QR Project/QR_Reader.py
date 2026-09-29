import cv2

def main():
   
    camera = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    if not camera.isOpened():
        print("Unable to open the camera.")
        return

    print("Press 'q' to exit.")

    while True:
        ok, frame = camera.read()
        if not ok:
            print("No image received from the camera.")
            break

        data, points, _ = detector.detectAndDecode(frame)

        if data:
            print("QR code found:", data)
            cv2.putText(
                frame,
                data,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )

        cv2.imshow("QR Reader", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
