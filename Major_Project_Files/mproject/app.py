from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory
from flask_cors import CORS
import os
import subprocess
import time
from urllib.parse import unquote

import json
import uuid
import re

app = Flask(__name__)
CORS(app)  # Enable CORS

# Common config
EXTRACTED_DATA_PATH = 'extracted_data'
if not os.path.exists(EXTRACTED_DATA_PATH):
    os.makedirs(EXTRACTED_DATA_PATH)

# ========== FACEBOOK FOLDER PATHS ==========
folder_paths = {
    "Search History": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/search/your_search_history.html",
    "Pages Visit": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/pages/pages_and_profiles_you_follow.html",
    "Links Visited": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/link_history/link_history.html",
    "Comments & Reactions": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/comments_and_reactions/likes_and_reactions_1.html",
    "Followers": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/followers/who_you've_followed.html",
    "Friends": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/friends/people_you_may_know.html",
    "Account Activity": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-15_09_2024-btElH3ER/Redirect/Facebook_activity/account_activity.html",
    "Chats": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/facebook-sunandaphale-24_04_2025-GMEyvCpX/your_facebook_activity/messages/your_messages.html",


    "Friend" :r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/connections/followers_and_following/pending_follow_requests.html",
    "Meta Apps": r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.html",
    "Likes Posts":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/your_instagram_activity/likes/liked_posts.html",
    "Search History":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/logged_information/recent_searches/profile_searches.html",
    "Link History":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/logged_information/link_history/link_history.html",
    "Following":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/connections/followers_and_following/following.html",
    "Saved Post":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/your_instagram_activity/saved/saved_posts.html",
    "Recommended Topic":r"C:/Users/badal/Desktop/Major_Project_Files/mproject/instagram-sunanda.v17-2025-04-24-ls44xNLY/preferences/your_topics/recommended_topics.html"
    }

@app.route('/open-folder', methods=['POST'])
def open_folder():
    data = request.json
    folder_name = data.get("type")
    if not folder_name:
        return jsonify({"error": "Missing 'type' in request body"}), 400

    path = folder_paths.get(folder_name)
    if path and os.path.exists(path):
        try:
            os.startfile(path)
            return jsonify({"message": f"Opened '{folder_name}' successfully."})
        except Exception as e:
            return jsonify({"error": f"Failed to open: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid option or file does not exist."}), 404

# ========== BASIC ROUTES ==========
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo.html')
def demo():
    return render_template('WhatsApp.html')

@app.route('/facebook.html')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram.html')
def instagram():
    return render_template('instagram.html')

# ========== WHATSAPP ROUTES ==========
@app.route('/photos')
def photos():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Images', 'WhatsApp Images')
    photos = os.listdir(folder) if os.path.exists(folder) else []
    return render_template('photos.html', photos=photos)

@app.route('/videos')
def videos():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Video', 'WhatsApp Video')
    videos = os.listdir(folder) if os.path.exists(folder) else []
    return render_template('videos.html', videos=videos, folder='WhatsApp_Video')

@app.route('/documents')
def documents():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Documents', 'WhatsApp Documents')
    docs = os.listdir(folder) if os.path.exists(folder) else []
    return render_template('documents.html', documents=docs, timestamp=int(time.time()))

@app.route('/audio')
def audio():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Voice_Notes', 'WhatsApp Voice Notes')
    audios = os.listdir(folder) if os.path.exists(folder) else []
    return render_template('audio.html', audio=audios, folder='WhatsApp_Voice_Notes')

@app.route('/gifs')
def gifs():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Animated_Gifs', 'WhatsApp Animated Gifs')
    gifs = os.listdir(folder) if os.path.exists(folder) else []
    return render_template('gifs.html', gifs=gifs, folder='WhatsApp_Animated_Gifs')

@app.route('/texts')
def texts():
    return render_template('home.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/all-media')
def all_media():
    folder = os.path.join(EXTRACTED_DATA_PATH, 'WhatsApp_Stickers', 'WhatsApp Stickers')
    stickers = [f for f in os.listdir(folder) if f.lower().endswith('.webp')] if os.path.exists(folder) else []
    return render_template('stickers.html', stickers=stickers, folder='WhatsApp_Stickers')

@app.route('/extract', methods=['POST'])
def extract_data():
    data_type = request.json.get('type')
    extract_map = {
        "Photos": (extract_whatsapp_images, "/photos"),
        "Videos": (extract_whatsapp_videos, "/videos"),
        "Documents": (extract_whatsapp_documents, "/documents"),
        "Audio": (extract_whatsapp_audio, "/audio"),
        "Animated GIFs": (extract_whatsapp_animated_gifs, "/gifs"),
        "Extract All Media": (extract_all_whatsapp_media, "/all-media"),
        "Texts": (lambda: "WhatsApp texts displayed.", "/texts"),
        "Contacts": (lambda: "WhatsApp contacts displayed.", "/contacts")
    }

    if data_type in extract_map:
        func, redirect_url = extract_map[data_type]
        message = func()
        return jsonify({"message": message, "redirect": redirect_url})
    else:
        return jsonify({"message": "Invalid data type", "redirect": "/"})

# ========== EXTRACTION FUNCTIONS ==========
def run_adb_pull(src_path, folder_name):
    try:
        dst_path = os.path.join(EXTRACTED_DATA_PATH, folder_name)
        os.makedirs(dst_path, exist_ok=True)
        subprocess.run(['adb', 'pull', src_path, dst_path], check=True)
        return f"Data extracted from {src_path}"
    except subprocess.CalledProcessError as e:
        return f"ADB pull failed: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def extract_whatsapp_images(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/", 'WhatsApp_Images')
def extract_whatsapp_videos(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/", 'WhatsApp_Video')
def extract_whatsapp_documents(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/", 'WhatsApp_Documents')
def extract_whatsapp_audio(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes/", 'WhatsApp_Voice_Notes')
def extract_whatsapp_animated_gifs(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Animated Gifs/", 'WhatsApp_Animated_Gifs')
def extract_all_whatsapp_media(): return run_adb_pull("/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Stickers/", 'WhatsApp_Stickers')

# ========== SERVE MEDIA FILES ==========
@app.route('/media/<folder_name>/<subfolder_name>/<filename>')
def serve_media(folder_name, subfolder_name, filename):
    folder_path = os.path.join(EXTRACTED_DATA_PATH, folder_name, unquote(subfolder_name))
    filename = unquote(filename)
    if os.path.exists(os.path.join(folder_path, filename)):
        return send_from_directory(folder_path, filename)
    else:
        return "File not found", 404

# ================================ WHATSAPP EXPORT CHAT =========================

@app.route('/start', methods=['POST'])
def start_process():
    phone_number = request.form['phone_number']

    # Sample ADB sequence (coordinates are placeholders and need to be calibrated for each device)
    os.system("adb shell input keyevent 3")  # Go to home
    time.sleep(1)
    os.system("adb shell monkey -p com.whatsapp -c android.intent.category.LAUNCHER 1")  # Launch WhatsApp
    time.sleep(3)

    # Simulate tap on search bar (x=100, y=200)
    os.system("adb shell input tap 375 217")
    time.sleep(1)

    # Enter phone number
    os.system(f"adb shell input text {phone_number}")
    time.sleep(3)

    # Tap on result (x=150, y=300)
    os.system("adb shell input tap 429 393")
    time.sleep(3)

    # Tap on 3-dot menu to export
    os.system("adb shell input tap 678 118")  # 3-dot menu
    time.sleep(1)

    # os.system("adb shell input tap 533 654")  # Tap more option
    # time.sleep(1)

    os.system("adb shell input tap 361 807")  # Tap more option
    time.sleep(1)

    # for my number
    # os.system("adb shell input tap 608 309")  # Tap Export chat option
    # time.sleep(1)

    # for others number
    os.system("adb shell input tap 436 475")  # Tap Export chat option
    time.sleep(1)

    
    media_option = "without"  # or "include"
    if media_option == "without":
        os.system("adb shell input tap 222 847")
        time.sleep(3)
    elif media_option == "include":
        os.system("adb shell input tap 511 843")
        time.sleep(1)


    # Tap on email app
    # 3rd option
    os.system("adb shell input tap 363 1400")
    time.sleep(1)
    
    # 2nd option
    # os.system("adb shell input tap 239 1421")
    # time.sleep(1)


    # Tap on recipient field (replace with your exact coordinates)
    os.system("adb shell input tap  403 652")  # Tap on recipient field
    time.sleep(2)

    # Type the email address
    os.system('adb shell input text "bodalapranita@gmail.com"')
    time.sleep(2)


    os.system('adb shell input tap 229 514')
    time.sleep(2)

    
   
    # Tap on Send button (replace with your send button coordinates)
    os.system("adb shell input tap 572 127")
    time.sleep(0.5)


    # return render_template('home.html', status='Exported chat successfully!')
    return render_template('indexb.html', status='Exported chat successfully!')


# ============================INDEXB.HTML LOGIC=========================================

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def indexb():
    return render_template('indexb.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['chatfile']
    if file and file.filename.endswith('.txt'):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            chat = f.readlines()

        messages = []
        for line in chat:
            # Try dash format with 24-hour time
            match = re.match(r'^(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}) - (.*?): (.*)', line.strip())
            
            if not match:
                # Try square bracket format with 24-hour time
                match = re.match(r'^\[(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2})\] (.*?): (.*)', line.strip())

            if match:
                timestamp, sender, message = match.groups()
                messages.append({
                    'timestamp': timestamp,
                    'sender': sender,
                    'message': message
                })

        # Save as JSON
        json_filename = f"{uuid.uuid4().hex}.json"
        json_path = os.path.join(app.config['UPLOAD_FOLDER'], json_filename)
        with open(json_path, 'w', encoding='utf-8') as jf:
            json.dump(messages, jf, indent=2, ensure_ascii=False)

        return render_template('indexb.html', messages=messages, json_file=json_filename)

    return 'Invalid file format. Please upload a .txt file.'

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

















if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True, port=5000)
