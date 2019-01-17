# face_check

This is a face compare module that takes two urls of a image and a modifiable threshold
then return whether it thinks the two images shows the same person.

There is only one function so far:
face_check.face_match(addr1, addr2, threshold=0.45)
The returned value is a boolean.

The core module came from https://github.com/ageitgey/face_recognition.
