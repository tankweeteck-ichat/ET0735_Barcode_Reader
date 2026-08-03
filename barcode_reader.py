from picamera2 import Picamera2
import cv2
from pyzbar.pyzbar import decode

# -------------------------------------------------------
# Camera Initialization
# -------------------------------------------------------

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)
picam2.start()

print("Camera started.")
print("Press q to quit.")

last_barcode = ""

# -------------------------------------------------------
# Main Loop
# -------------------------------------------------------

while True:

    frame = picam2.capture_array()

    # Picamera2 returns RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    barcodes = decode(frame)

    for barcode in barcodes:

        x, y, w, h = barcode.rect

        # Draw green rectangle
        '''
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        '''
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # Display text above barcode
        '''
        text = f"{barcode_type}: {barcode_data}"

        cv2.putText(
            frame,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )
        '''
        # Avoid printing the same barcode repeatedly
        if barcode_data != last_barcode:

            last_barcode = barcode_data

            print()
            print("====================================")
            print("Barcode Detected")
            print("------------------------------------")
            print("Type :", barcode_type)
            print("Data :", barcode_data)
            print("====================================")

    #cv2.imshow("Barcode Reader", frame)
    '''
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    '''
picam2.stop()

#cv2.destroyAllWindows()