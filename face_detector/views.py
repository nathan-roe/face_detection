import face_recognition
import cv2
import os
from .models import User
from django.contrib import messages
import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
def root(request):
    return render(request, 'index.html')
def detect_face(request):
    # KNOWN_FACES_DIR = 'face_detector/static/known_faces'

    KNOWN_FACES_DIR = 'media'
    
    # UNKNOWN_FACES_DIR = 'unknown_faces'
    # tolerance works best for (0) at 0.6
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = "hog"

    video = cv2.VideoCapture(0) #Can put in a video feed using its filename

    # video = cv2.VideoCapture(0)

    print('loading known faces')

    known_faces = []
    known_names = []

    for name in os.listdir(KNOWN_FACES_DIR):
        print(f'Name in known faces dir: {name}')
        # for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        # print(f'File name: {filename}')
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}")
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)
    print("processing unknown faces")
    print(known_names)
    while True:
        # print(filename)
        # image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')

        ret, image = video.read()
        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                print(f'Match found: {match}')
                # draw rectangle
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2]+22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

                cv2.destroyAllWindows()

                request.session['img_url'] = f"/media/{match}"
                print(f" detect img_url = {request.session['img_url']}")
                user_list = User.objects.filter(image=f'/media/{match}')
                print(user_list)
                request.session['uuid'] = user_list[0].id 
                return redirect('/dashboard')
                
        # cv2.imshow(filename, image)
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(10000):
            print('Did not detect a face')
            context = {
                'error': 'There was an error detecting your face. Try again or login with your email and password'
            }
            return render(request, 'index.html', context)
        # cv2.destroyAllWindows()
    return redirect('/')
def process_reg(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        myfile = request.FILES['post_image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(f"You just uploaded this image: {uploaded_file_url}")
        top_secret_pw = bcrypt.hashpw(request.POST['post_password'].encode(), bcrypt.gensalt()).decode()  
        created_user = User.objects.create(
            first_name=request.POST['post_first'],
            last_name=request.POST['post_last'],
            email=request.POST['post_email'],
            password=top_secret_pw,
            image=uploaded_file_url
        )
        request.session['img_url'] = uploaded_file_url
        request.session['uuid'] = created_user.id
        print(f"process_reg img_url = {request.session['img_url']}")
        return redirect('/dashboard')
def process_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:

        user_list = User.objects.filter(email=request.POST['post_login_email'])
        print(f"process_login user_list = {user_list}")
        request.session['uuid'] = user_list[0].id  
        this_user = User.objects.get(id=request.session['uuid'])
        request.session['img_url'] = this_user.image.name
        return redirect('/dashboard')
def logout(request):
    request.session.flush()
    return redirect('/')
def dashboard(request):
    this_user = User.objects.get(id=request.session['uuid'])
    img_url = request.session['img_url']


    # print(this_user.user_image.image)
    context = {
        'this_user':this_user,
        'img_url':img_url
    }
    return render(request, 'dashboard.html', context)
def edit_page(request):
    this_user = User.objects.get(id=request.session['uuid'])
    context = {
        'this_user':this_user
    }
    return render(request, 'edit_page.html', context)








    