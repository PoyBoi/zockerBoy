<h1 align="center">
zockerBoy - Zocket Assignment
</h1>

<hr/>

## Usage

- cd to the working directory "zockerBoy"
- Install the requirements using the following command:
    ```
    pip install -r requirements. txt
    ```
- Run the following command to run the program:
    ```
    python main.py --i <location of image to be used> --d <device to be used, 0 for cpu, 1 for cuda device> 
    ```
    - There are example images provided inside the "images" folder
    - Example Usage:
        ```
        python main.py --i images/1.jpg --d 1
        ```

<hr/>

## Path Taken
1. Started off with Color Palette detection:
    1. Used color thief
2. Then went onto make text overlay detection:
    1. Tried using pyTesseract natively
        1. Had issues with implementing it due to bad OCR results
    2. Used cv2 to turn it into bw (better results than rgb)
    3. Used CV2 to make boxes around text and compile it
    4. Used pyTesseract to detect text from those boxes
        1. Had to mess around with the config to see which method gives most matches based on e-media
        2. Added thresholding to it make sure only the high % matches get through
        3. Had to mess around with the threshold to see what works the best
3. Object Detection:
    1. Tried using yoloX
        1. dependancies weren't resolving, wheels weren't building
            1. Severe python interpreter problems faced, had to re-do path
        2. tried moondream
            1. models specified had too varying tensor values, couldn't find a suitable sigmoid loss model for it to fit into
        3. tried mmdetection
            1. it's also viable for commercial usage
            2. had to build gcc/mingw
            3. had to build mmDetection and it's sub-packages from base to work with cuda 12.1 and my version of cuDNN
                1. Built core labelling and idenitfication
                2. Built tracking
                3. Test tracking on image and videos with boxes made
                    1. Used an instance of yoloX for the same (which is also commercially viable)
        4. Tried yoloV8
            1. Faster inference
            2. Better trained model
            3. made argparser to catch output
                1. Checked documentation, turns out they have a thing to for that anyways
4. Logo Detection:
    1. Tried using yolov8:
        1. Lengthy to convert dataset into yoloV8 format
        2. Local machine cannot train efficiently enough (3060)
        3. Bad documentation
    2. trying to use yoloV3/4/5:
        1. 