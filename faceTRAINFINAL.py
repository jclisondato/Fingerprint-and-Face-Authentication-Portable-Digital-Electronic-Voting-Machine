import  os
import pickle
import face_recognition



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")
faceencodePKL = open('faceencode.pkl', 'wb')


class FaceTrain:
    known_face_encodings = []
    known_face_names = []


    def __init__(self):
        self.encode_faces()

    def encode_faces(self):
        count = 0
        for root, dirs, files in os.walk(image_dir):
            count += (len(files))
        print(count)
        actualcount=0
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                actualcount += 1
                print(f"{actualcount}/{count}")
                path = os.path.join(root, file)
                label = os.path.basename(root).replace("-", " ").lower()
                face_image = face_recognition.load_image_file(path)
                face_encoding = face_recognition.face_encodings(face_image)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(label)
        faceencode = []
        for name,encoded in zip(self.known_face_names,self.known_face_encodings):
            faceencode.append([name,encoded])
        pickle.dump(faceencode, faceencodePKL)
        faceencodePKL.close()

if __name__ == '__main__':
    fr = FaceTrain()

