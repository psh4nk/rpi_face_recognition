# Raspberry Pi Face Detection

## Instructions

1. Clone this repository to your Raspberry Pi:

    ```bash
    git clone https://github.com/psh4nk/rpi_face_recognition
    ```

1. Run xrdp.sh on your Raspberry Pi:

    ```bash
    chmod u+x ./xrdp.sh
    ./xrdp.sh
    ```

1. Update capture-face.py and find-best.face.py to replace all instances of "Chuck" with your name.

1. Connect to your Raspberry Pi with XRDP on your Windows machine.

1. In the XRDP window, run capture-face.py to capture face images on your Pi.

1. Once you have a dataset/[your name] folder populated with images of your face, run find-best-face.py to determine which images are the best candidates for face recognition.

1. Repeat this process for any other faces you want your application to recognize.

[Add face recognition with Raspberry Pi](https://www.raspberrypi.com/news/add-face-recognition-with-raspberry-pi-hackspace-38/)