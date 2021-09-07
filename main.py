# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import easyocr
import cv2
import time
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.


    # For the first time it downloads the models for the languages chosen below.
    # Not all languages are compatible with each other so you cannot put
    # multiple languages below
    # reader = easyocr.Reader(['hi', 'te', 'en'])  #Hindi, telugu, and English
    # The above gives error that Telugu is only compatible with English.

    # So let us just use Hindi and English
    # To use GPU you need to have CUDA configured for the pytorch library.
    reader = easyocr.Reader(['en','de'], gpu=True)  # Hindi, telugu, and English
    start = time.time()
    img = cv2.imread('images/cameraWEB31.JPG',0)
    ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                                 cv2.THRESH_OTSU)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    results = reader.readtext(img, detail=1, paragraph=False)  # Set detail to 0 for simple text output
    # Paragraph=True will combine all results making it easy to capture it in a dataframe.
    print(results)
    print(time)


    for (bbox, text, prob) in results:
        # Define bounding boxes
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))

        # Remove non-ASCII characters to display clean text on the image (using opencv)
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

        # Put rectangles and text on the image
        cv2.rectangle(img, tl, br, (0, 255, 0), 2)
        cv2.putText(img, text, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    # show the output image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
