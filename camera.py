"""import cv2
import uuid

# Define a callback function to handle image capture button clicks
def capture_image(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Save the current frame as an image file
        filename = f"captured_image_{str(uuid.uuid4())}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved to {filename}")

# Define a callback function to handle video recording button clicks
def record_video(event, x, y, flags, param):
    global recording, video_writer

    if event == cv2.EVENT_LBUTTONDOWN:
        if not recording:
            # Start recording a video
            filename = f"recorded_video_{str(uuid.uuid4())}.avi"
            video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 20, (640,480))
            print(f"Recording started: {filename}")
            recording = True
        else:
            # Stop recording the video
            recording = False

def pause_video(event, x, y, flags, param):
    global paused

    if event == cv2.EVENT_LBUTTONDOWN:
        paused = not paused

def stop_video(event, x, y, flags, param):
    global recording, video_writer

    if event == cv2.EVENT_LBUTTONDOWN:
        if recording:
            # Stop recording the video
            recording = False
            video_writer.release()
            print(f"Recording stopped")

            # Save the video to a new file with a unique name
            new_filename = f"recorded_video_{str(uuid.uuid4())}.avi"
            os.rename(filename, new_filename)
            print(f"Video saved to {new_filename}")

# Create a named window to display the camera feed
cv2.namedWindow('Camera Feed')

# Create image capture and video recording buttons and bind the callback functions to them
cv2.setMouseCallback('Camera Feed', capture_image)
cv2.setMouseCallback('Camera Feed', record_video)
cv2.setMouseCallback('Camera Feed', pause_video)
cv2.setMouseCallback('Camera Feed', stop_video)

# Start the camera
cap = cv2.VideoCapture(0)

recording = False
paused = False
video_writer = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Camera Feed',frame)

    # Save the current frame to the video file if recording is enabled and not paused
    if recording and not paused:
        video_writer.write(frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy the window
cap.release()
cv2.destroyAllWindows()
"""
import time
import tkinter as tk
import cv2


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)

        # open video source (by default this will try to open the computer webcam)
        self.vid = cv2.VideoCapture(video_source)

        # create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # add a button to take a photo
        self.btn_snapshot = tk.Button(window, text="Take a photo", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        # add a button to start recording
        self.btn_start_record = tk.Button(window, text="Start recording", width=50, command=self.start_record)
        self.btn_start_record.pack(anchor=tk.CENTER, expand=True)

        # add a button to pause recording
        self.btn_pause_record = tk.Button(window, text="Pause recording", width=50, command=self.pause_record)
        self.btn_pause_record.pack(anchor=tk.CENTER, expand=True)

        # add a button to stop and save recording to a new file
        self.btn_stop_record = tk.Button(window, text="Stop and save recording", width=50, command=self.stop_record)
        self.btn_stop_record.pack(anchor=tk.CENTER, expand=True)

        # initialize recording state variables
        self.is_recording = False
        self.out = None
        self.frame_size = (int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # start the GUI
        self.window.mainloop()

    def snapshot(self):
        # get a frame from the video source
        ret, frame = self.vid.read()

        if ret:
            # create a unique filename for the snapshot
            filename = f"snapshot_{str(time.time())}.jpg"

            # save the snapshot as a JPEG file
            cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            print(f"Snapshot saved as {filename}")

    def start_record(self):
        # create a unique filename for the recording
        filename = f"recording_{str(time.time())}.avi"

        # initialize the video writer object
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(filename, fourcc, 20.0, self.frame_size)

        # set recording state variable to True
        self.is_recording = True

        print("Recording started")

    def pause_record(self):
        # set recording state variable to False
        self.is_recording = False

        print("Recording paused")

    def stop_record(self):
        if self.is_recording:
            # set recording state variable to False
            self.is_recording = False

            # release the video writer object
            self.out.release()

            # create a unique filename for the recording
            filename = f"recording_{str(time.time())}.avi"

            # rename the recording file to the final filename
            import os
            os.rename(filename, f"finished_{filename}")

            print(f"Recording saved as finished_{filename}")
        else:
            print("No recording to save")

