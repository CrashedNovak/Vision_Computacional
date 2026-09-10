"""
Usage: Parcial1_webcam_byn.py [--camid=N] [--umbral=U]
    
Options:
    -c, --camid=N  [default: 0]
    -u, --umbral=U  [default: 127]
"""

import sys
import cv2
from docopt import docopt

def byn (frame, umbral):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    v_umbral, binaria = cv2.threshold(gris, umbral, 255, cv2.THRESH_BINARY)
    return binaria

if __name__ == "__main__":
    args = docopt(__doc__)
    try:
        camid = int(args['--camid'])
        umbral = int(args['--umbral'])
    except ValueError:
        print("camid y umbral deben ser numeros enteros", file=sys.stderr)
        exit(1)

    if not (0 <= umbral <= 255):
        print("umbral debe estar entre 0 y 255", file=sys.stderr)
        exit(1)

    cap = cv2.VideoCapture(camid)
    if not cap.isOpened():
        print(f"no se pudo abrir la camara {camid}", file=sys.stderr)
        exit(1)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_bn = byn(frame, umbral)
            cv2.imshow('Webcam blanco y negro', frame_bn)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()