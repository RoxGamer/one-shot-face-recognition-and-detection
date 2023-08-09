import cv2
import face_recognition
import streamlit as st
import numpy as np

def main():
    st.title("Real-time Face Recognition App")
    
    # Take user's image and name as input
    uploaded_image = st.file_uploader("Upload a photo of yourself", type=["jpg", "jpeg", "png"])
    user_name = st.text_input("Enter your name")

    if uploaded_image is not None and user_name != "":
        known_image = face_recognition.load_image_file(uploaded_image)
        known_face_encoding = face_recognition.face_encodings(known_image)[0]

        st.write("Hello, " + user_name + "! Your webcam is being used to detect and recognize your face.")

        stframe = st.empty()
        video_capture = cv2.VideoCapture(0)
        
        capture_button = st.button("Capture")

        while True:
            ret, frame = video_capture.read()

            if not ret:
                break

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                results = face_recognition.compare_faces([known_face_encoding], face_encoding)

                if results[0]:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, user_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown User", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            stframe.image(frame, channels="BGR")
            
            if capture_button:
                break

        video_capture.release()

if __name__ == "__main__":
    main()
