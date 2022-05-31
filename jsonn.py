import os
import json
from json import JSONEncoder
import numpy as np
import face_recognition


class numpyarray(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


data = []
for b in os.listdir('photo'):

    for a in os.listdir(f'photo/{b}'):
        # print(b, a)
        name = a.split(".")[0]
        path = f"photo/{b}/{a}"
        pic = face_recognition.load_image_file(path)
        encode_pic = face_recognition.face_encodings(pic)[0]

        i = {'name': name,
             'path': path,
             'dir': b,
             'encode': encode_pic}

        data.append(i)

encode = json.dumps(data, cls=numpyarray)


def main():
    with open('student.json', 'w') as outfile:
        outfile.write(encode)


main()
