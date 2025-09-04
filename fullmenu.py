# Smart Menu Base: All-in-One Menu Dashboard (Student Edition)
# -------------------------------------------------------
# Streamlit multi-page app with 4 sections:
# - Python Tasks
# - HTML/JS Tasks
# - Linux System via SSH
# - Docker Containers via SSH

import streamlit as st
from streamlit_option_menu import option_menu
import os
import paramiko
import pywhatkit as py
from instagrapi import Client
from twilio.rest import Client as TwilioClient
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
import webbrowser
import time
import requests
from bs4 import BeautifulSoup
from functools import wraps
import threading
from datetime import datetime
import subprocess
import pyttsx3
import qrcode
from PIL import Image

st.set_page_config(page_title="Smart Menu Base Dashboard", layout="wide")

# ------------------ Sidebar Navigation ------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=100)
    selected = option_menu(
    menu_title="Smart Menu Base",
    options=[
        "Home", 
        "Python Tasks", 
        "HTML/JS Tasks", 
        "Linux Menu", 
        "Docker Menu", 
        "Machine Learning", 
        "Windows Tasks",
        "File Explorer"  # 🗂️ New Option
    ],
    icons=[
        "house", 
        "code-slash", 
        "globe", 
        "terminal", 
        "box", 
        "activity", 
        "windows",
        "folder"  # 🗂️ Icon for File Explorer
    ]
)
    
    # ------------------ Page Content Based on Selection ------------------
if selected == "Home":
    st.title("🏠 Welcome to Smart Menu Dashboard")

elif selected == "Python Tasks":
    st.subheader("🐍 Python Tasks")

elif selected == "HTML/JS Tasks":
    st.subheader("🌐 HTML & JS Tasks")
   
elif selected == "Linux Menu":
    st.subheader("💻 Linux Menu")

elif selected == "Docker Menu":
    st.subheader("🐳 Docker Menu")

elif selected == "Machine Learning":
    st.subheader("🤖 Machine Learning Section")
  
elif selected == "Windows Tasks":
    st.subheader("🪟 Windows Tasks")

elif selected == "File Explorer":
    st.subheader("🗂️ File Explorer")
   
# ------------------ Utilities ------------------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

logs = []
def log_task(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logs.append(f"[{datetime.now()}] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper

# ------------------ Home ------------------
if selected == "Home":
    st.title("🧠 Smart Menu Base Dashboard")
    st.markdown("""
    Welcome to **Smart Menu Base**, your all-in-one operational dashboard.

    **Features:**
    * 📲 Automate real-world tasks (WhatsApp, Email, Instagram)
    * 🌐 Use HTML/JS tools (Camera, Location, SMS)
    * 🐧 Control Linux machines via SSH with voice and GUI
    * 🐳 Manage Docker containers interactively
    * 🤖 Ask Gemini AI anything
    * 📊 Upload CSV and Train Machine Learning Models (Linear Regression, Random Forest)
    * 📈 Visualize graphs and make real-time predictions
    * 🌗 Light/Dark Mode Toggle + Toast Alerts + Floating Helpbot
    """)
   # ------------------ Python Tasks ------------------
elif selected == "Python Tasks":
    st.header("🐍 Python Automation Tasks")
    task = st.selectbox("Choose a task:", [
    "Send WhatsApp Message", "Send Email", "Post to Instagram",
    "Make a Call", "Ask Gemini AI", "Scrape Website", "Text-to-Speech"])

    @log_task
    def whatsapp():
        mob = st.text_input("Enter mobile number:")
        msg = st.text_input("Enter message:")
        hour = st.number_input("Hour (24h format):", 0, 23, value=datetime.now().hour)
        minute = st.number_input("Minute:", 0, 59, value=(datetime.now().minute + 2) % 60)
        if st.button("Send WhatsApp"):
            py.sendwhatmsg(mob, msg, int(hour), int(minute))
            st.success("✅ WhatsApp Message Scheduled")
        
    	

    @log_task
    def email():
        sender = st.text_input("Sender Email")
        password = st.text_input("Password", type="password")
        subject = st.text_input("Subject")
        msg = st.text_area("Message")
        receiver = st.text_input("Receiver Email")
        if st.button("Send Email"):
            py.send_mail(sender, password, subject, msg, receiver)
            st.success("✅ Email Sent Successfully")

    @log_task
    def insta():
        username = st.text_input("Instagram Username")
        password = st.text_input("Password", type="password")
        path = st.text_input("Image Path")
        caption = st.text_input("Caption")
        if st.button("Post to Instagram"):
            cs = Client()
            cs.login(username, password)
            cs.photo_upload(path, caption)
            st.success("✅ Instagram Post Uploaded")

    @log_task
    def call():
        account_sid = st.text_input("Twilio SID", type="password")
        auth_token = st.text_input("Auth Token", type="password")
        sender_num = st.text_input("Twilio Number")
        receiver_num = st.text_input("Receiver Number")
        if st.button("Make Call"):
            client = TwilioClient(account_sid, auth_token)
            client.calls.create(to=receiver_num, from_=sender_num, url="https://demo.twilio.com/docs/voice.xml")
            st.success("📞 Call Made Successfully")

    @log_task
    def gemini():
        prompt = st.text_area("Ask Gemini anything")
        api_key = st.text_input("Enter your Gemini API Key", type="password")
        if st.button("Ask Gemini"):
            if api_key:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("models/gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.code(response.text, language="markdown")
            else:
                st.error("Please enter your Gemini API key")

    @log_task
    def scrape():
        url = st.text_input("Website URL")
        tag = st.text_input("HTML Tag (e.g., h1, p)")
        if st.button("Scrape Content"):
            try:
                res = requests.get(url)
                soup = BeautifulSoup(res.text, "html.parser")
                results = soup.find_all(tag)
                for t in results:
                    st.write(t.text)
            except Exception as e:
                st.error(f"Error: {e}")

    @log_task
    def text_to_speech():
        text = st.text_area("Enter text to speak:")
        if st.button("Speak Now"):
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            st.success("🗣️ Spoke the text aloud!")

    @log_task
    def qr_code():
        data = st.text_input("Enter text or URL for QR Code:")
        if st.button("Generate QR Code"):
            if data:
                img = qrcode.make(data)
                img.save("qrcode.png")
                st.image("qrcode.png", caption="Your QR Code")
                st.success("✅ QR Code saved as qrcode.png")
            else:
                st.warning("Please enter some text or URL")


    if task == "Send WhatsApp Message": whatsapp()
    elif task == "Send Email": email()
    elif task == "Post to Instagram": insta()
    elif task == "Make a Call": call()
    elif task == "Ask Gemini AI": gemini()
    elif task == "Scrape Website": scrape()
    elif task == "Text-to-Speech": text_to_speech()
    elif task == "QR Code Generator": qr_code()



    with st.expander("📜 Show Logs"):
        st.code("\n".join(logs))
    if st.button("💾 Export Logs to TXT"):
        with open("smartops_logs.txt", "w") as f:
            f.write("\n".join(logs))
        st.success("Logs saved to smartops_logs.txt")

# ------------------ HTML/JS Tasks ------------------
elif selected == "HTML/JS Tasks":
    st.header("🌐 HTML/JS Integration")
    st.markdown("Launch your browser-based utilities.")
    html_options = {
    "Open Camera": "camera2.html",
    "Send SMS": "sms.html",
    "Location & GPS": "gps.html",
    "Gmail Info": "mail.html",
    "Post to Facebook/Twitter": "twitter_fb.html",
    "WhatsApp Web": "whatmsg.html",
    "Weather Info": "weather.html"   }

    choice = st.selectbox("Choose task to open:", list(html_options.keys()))
    if st.button("Launch HTML Task"):
        # Use a generic path or let user specify
        html_folder = st.text_input("Enter path to HTML files folder:", value="./html_files")
        file_path = os.path.abspath(f"{html_folder}/{html_options[choice]}")
        if os.path.exists(file_path):
            webbrowser.open(f"file://{file_path}")
            st.success(f"🚀 Launched {choice}")
        else:
            st.error(f"File not found: {file_path}")

# ------------------ Linux Menu ------------------
elif selected == "Linux Menu":
    st.header("🐧 Linux Remote Terminal + AI")
    host = st.text_input("Remote Host")
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    cmd = st.text_area("Enter Linux command")
    if st.button("Run Command via SSH"):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=user, password=password)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            st.text("Output:")
            st.code(stdout.read().decode())
            st.text("Errors:")
            st.code(stderr.read().decode())
            ssh.close()
        except Exception as e:
            st.error(str(e))

    st.markdown("### 📘 Suggested Commands")
    if st.button("Show 50+ Basic Linux Commands"):
        with st.expander("📗 Commands"):
            st.code("""
ls -l
cd /home
pwd
mkdir test
touch file.txt
rm file.txt
cp file1 file2
mv file1 file2
cat file.txt
nano file.txt
vim file.txt
chmod +x file.sh
chown user:user file.txt
ps aux
top
htop
kill -9 PID
ifconfig
ip a
df -h
du -sh
mount
dumpe2fs
fdisk -l
mkfs.ext4 /dev/sdb1
parted /dev/sdb
lsblk
blkid
useradd test
passwd test
usermod -aG sudo test
userdel test
groupadd dev
groupdel dev
ping google.com
traceroute google.com
netstat -tulnp
ss -tuln
ufw enable
ufw allow 22
ufw status
journalctl
systemctl status sshd
systemctl start nginx
systemctl enable docker
crontab -e
echo "Hello"
exit
reboot
shutdown now
            """, language="bash")

    st.markdown("### 🤖 Ask Gemini to Explain Linux Commands")
    command = st.text_input("🔧 Enter Linux command to understand")
    api_key = st.text_input("Enter your Gemini API Key", type="password")
    if st.button("💬 Ask Gemini to Explain"):
        if api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("models/gemini-1.5-flash")
                query = f"Explain the command: `{command}`. What does it do? How and when is it used?"
                response = model.generate_content(query)
                if hasattr(response, 'text'):
                    st.markdown("### 🤖 Gemini's Explanation:")
                    st.write(response.text)
                else:
                    st.warning("⚠️ No response from Gemini.")
            except Exception as e:
                st.error(f"Gemini Error: {e}")
        else:
            st.error("Please enter your Gemini API key")


# ------------------ Docker Menu ------------------
# ------------------ Docker Menu ------------------
elif selected == "Docker Menu":
    st.header("🐳 Docker via SSH (Remote Execution)")
    host = st.text_input("Remote Host (e.g., 192.168.1.100)", key="docker_host")
    user = st.text_input("Username", key="docker_user")
    password = st.text_input("Password", type="password", key="docker_pass")
    docker_command = st.text_area("Enter Docker command (e.g., docker ps -a)", key="docker_cmd")

    if st.button("Run Docker Command via SSH"):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=user, password=password)
            stdin, stdout, stderr = ssh.exec_command(docker_command)
            output = stdout.read().decode()
            errors = stderr.read().decode()

            if output:
                st.code(output)
            if errors:
                st.error(errors)
            ssh.close()
        except Exception as e:
            st.error(f"SSH Connection Failed: {e}")

    st.markdown("### 🧩 Common Docker Commands with Descriptions")
    docker_tasks = {
        "📦 Show All Containers": "docker ps -a",
        "📂 Show All Images": "docker images",
        "🚀 Run Ubuntu Container": "docker run -it ubuntu bash",
        "🔍 Inspect a Container": "docker inspect <container_id>",
        "🛑 Stop a Container": "docker stop <container_id>",
        "❌ Remove a Container": "docker rm <container_id>",
        "🧹 Remove an Image": "docker rmi <image_id>",
        "🔄 Restart a Container": "docker restart <container_id>",
        "📡 Show Running Containers": "docker ps",
        "🐳 Enter Container Shell": "docker exec -it <container_id> bash",
        "🧱 Build Image from Dockerfile": "docker build -t myapp .",
        "🌐 Show Docker Networks": "docker network ls",
        "💾 Show Docker Volumes": "docker volume ls"
    }

    selected_task = st.selectbox("Choose a Docker Operation", list(docker_tasks.keys()))
    if selected_task:
        st.code(docker_tasks[selected_task], language="bash")

    # ---------------- Gemini for Docker ----------------
    st.subheader("🐳 Ask Gemini to Explain Docker Command")
    docker_input = st.text_input("🐳 Enter Docker command to explain", key="docker_input_text")
    docker_api_key = st.text_input("Enter your Gemini API Key", type="password", key="docker_gemini_key")

    if "show_docker_explanation" not in st.session_state:
        st.session_state["show_docker_explanation"] = False

    if st.button("💬 Explain with Gemini"):
        if docker_input.strip() == "":
            st.warning("Please enter a Docker command first.")
        elif not docker_api_key:
            st.error("Please enter your Gemini API key")
        else:
            st.session_state["show_docker_explanation"] = True

    if st.session_state["show_docker_explanation"]:
        try:
            genai.configure(api_key=docker_api_key)
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            prompt = f"Explain the Docker command: `{docker_input}` in simple language with usage examples."
            response = model.generate_content(prompt, stream=False)
            content = getattr(response, "text", str(response))
            st.markdown("### 📘 Gemini's Explanation:")
            st.write(content)
        except Exception as e:
            st.error(f"❌ Gemini Error: {e}")# ------------------ Machine Learning Section ------------------
# ------------------ Machine Learning Section ------------------
elif selected == "Machine Learning":
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error, r2_score

    st.header("🤖 Machine Learning Playground")

    # Upload CSV
    uploaded_file = st.file_uploader("📂 Upload your CSV dataset", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.success("✅ File Uploaded Successfully")
        st.dataframe(data.head())

        with st.form("ml_form"):
            st.subheader("🔍 Select Features & Target")
            all_columns = list(data.columns)
            target = st.selectbox("🎯 Select Target Column", all_columns)
            features = st.multiselect("📊 Select Feature Columns", [col for col in all_columns if col != target])
            model_type = st.selectbox("🤖 Choose Model", ["Linear Regression", "Random Forest"])
            submit = st.form_submit_button("🚀 Train Model")

        if submit:
            if len(features) == 0:
                st.error("Please select at least one feature column.")
            else:
                try:
                    # Clean and prepare data
                    data = data.dropna()
                    X = data[features].select_dtypes(include=['number'])
                    y = data[target]
                    y = y.loc[X.index]

                    # Train-test split
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    # Choose model
                    model = LinearRegression() if model_type == "Linear Regression" else RandomForestRegressor()

                    # Train model
                    model.fit(X_train, y_train)
                    predictions = model.predict(X_test)

                    # Results
                    st.success("✅ Model Trained Successfully!")
                    st.markdown(f"**R² Score:** {r2_score(y_test, predictions):.4f}")
                    st.markdown(f"**MSE:** {mean_squared_error(y_test, predictions):.4f}")

                    # Plot predictions vs actual
                    fig, ax = plt.subplots()
                    sns.scatterplot(x=y_test, y=predictions, ax=ax)
                    ax.set_xlabel("Actual")
                    ax.set_ylabel("Predicted")
                    ax.set_title("📈 Actual vs Predicted")
                    st.pyplot(fig)

                    # Feature importances (only for Random Forest)
                    if model_type == "Random Forest":
                        importances = model.feature_importances_
                        fig2, ax2 = plt.subplots()
                        sns.barplot(x=importances, y=X.columns, ax=ax2)
                        ax2.set_title("📌 Feature Importance")
                        st.pyplot(fig2)

                    # Predict new data
                    st.subheader("🔮 Predict on New Data")
                    new_input = []
                    for feat in X.columns:
                        val = st.number_input(f"Enter value for {feat}", value=float(data[feat].mean()))
                        new_input.append(val)
                    if st.button("🔍 Predict Now"):
                        result = model.predict([new_input])
                        st.success(f"🎯 Predicted {target}: {result[0]:.4f}")

                except Exception as e:
                    st.error(f"⚠️ Error during training: {e}")
# ------------------ Windows Tasks ------------------
elif selected == "Windows Tasks":
    st.header("🪟 Windows Automation Tasks")

    windows_task = st.selectbox("Choose a Windows Task:", [
        "Open Notepad", "Open Calculator", "Open Command Prompt", "Open File Explorer",
        "Open Chrome", "Open MS Word", "Open MS Excel", "Open Specific Folder",
        "Play Music Folder", "Shutdown", "Restart", "Lock Screen"
    ])

    if windows_task == "Open Notepad":
        st.success("Opening Notepad...")
        os.system("notepad")

    elif windows_task == "Open Calculator":
        st.success("Opening Calculator...")
        os.system("calc")

    elif windows_task == "Open Command Prompt":
        st.success("Opening CMD...")
        os.system("start cmd")

    elif windows_task == "Open File Explorer":
        st.success("Opening Explorer...")
        os.system("explorer")

    elif windows_task == "Open Chrome":
        st.success("Opening Chrome Browser...")
        os.system("start chrome")

    elif windows_task == "Open MS Word":
        st.success("Opening Microsoft Word...")
        os.system("start winword")

    elif windows_task == "Open MS Excel":
        st.success("Opening Microsoft Excel...")
        os.system("start excel")

    elif windows_task == "Open Specific Folder":
        folder_path = st.text_input("Enter full folder path:")
        if st.button("Open Folder"):
            if os.path.exists(folder_path):
                os.startfile(folder_path)
                st.success("📂 Folder opened.")
            else:
                st.error("❌ Path not found.")

    elif windows_task == "Play Music Folder":
        music_dir = "C:\\Users\\Public\\Music"  # Customize this path
        try:
            os.startfile(music_dir)
            st.success("🎵 Music folder opened.")
        except:
            st.error("❌ Unable to open music folder.")

    elif windows_task == "Shutdown":
        st.warning("System will shutdown in 5 seconds.")
        os.system("shutdown /s /t 5")

    elif windows_task == "Restart":
        st.warning("System will restart in 5 seconds.")
        os.system("shutdown /r /t 5")

    elif windows_task == "Lock Screen":
        st.info("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
elif selected == "File Explorer":
    import shutil
    import datetime
    from google.generativeai import configure, GenerativeModel

    st.title("📁 SmartFile AI - Intelligent File Manager")

    # ✅ Gemini setup (only once in app)
    file_explorer_api_key = st.text_input("Enter your Gemini API Key", type="password", key="file_explorer_key")
    
    if file_explorer_api_key:
        configure(api_key=file_explorer_api_key)
        model = GenerativeModel("gemini-1.5-flash")

    # ✅ Utility Functions
    def list_files(directory):
        try:
            entries = []
            for file in os.listdir(directory):
                path = os.path.join(directory, file)
                size = os.path.getsize(path)
                modified = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
                file_type = "Folder" if os.path.isdir(path) else "File"
                entries.append({
                    "Name": file,
                    "Size (KB)": round(size / 1024, 2),
                    "Type": file_type,
                    "Modified": modified
                })
            return entries
        except Exception as e:
            return f"Error: {e}"

    def rename_file(directory, old_name, new_name):
        try:
            os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            return "✅ Renamed successfully."
        except Exception as e:
            return f"❌ Error: {e}"

    def delete_path(directory, name):
        try:
            full_path = os.path.join(directory, name)
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
            else:
                return "⚠️ Invalid file or folder name."
            return "🗑️ Deleted successfully."
        except Exception as e:
            return f"❌ Error: {e}"

    def create_dir(directory, folder_name):
        try:
            os.makedirs(os.path.join(directory, folder_name), exist_ok=True)
            return "📁 Directory created successfully."
        except Exception as e:
            return f"❌ Error: {e}"

    def interpret_query(query, file_info_list):
        if not file_explorer_api_key:
            return "Please enter your Gemini API key to use AI features."
        file_names = [item["Name"] for item in file_info_list]
        prompt = f"""
        Given this list of files and folders:
        {file_names}
        Respond to this query: "{query}"
        Return only relevant file/folder names.
        """
        response = model.generate_content(prompt)
        return response.text

    # ✅ Input
    directory = st.text_input("📂 Enter the directory path you want to manage")

    st.sidebar.header("⚙️ Choose an Action")
    action = st.sidebar.radio("Select Operation", [
        "List Files", "Rename File", "Delete File/Folder", 
        "Create Directory", "AI File Search", "Folder Summary"
    ])

    if directory:
        if action == "List Files":
            result = list_files(directory)
            if isinstance(result, list):
                sort_by = st.selectbox("Sort by", ["Name", "Size (KB)", "Type", "Modified"])
                sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)
                result.sort(key=lambda x: x[sort_by], reverse=(sort_order == "Descending"))
                st.dataframe(result)
            else:
                st.error(result)

        elif action == "Rename File":
            old_name = st.text_input("🔤 Old file/folder name")
            new_name = st.text_input("🆕 New name")
            if st.button("Rename"):
                st.success(rename_file(directory, old_name, new_name))

        elif action == "Delete File/Folder":
            name = st.text_input("🗑️ Enter name to delete")
            if st.button("Delete"):
                st.warning(delete_path(directory, name))

        elif action == "Create Directory":
            folder_name = st.text_input("📂 New folder name")
            if st.button("Create"):
                st.success(create_dir(directory, folder_name))

        elif action == "AI File Search":
            query = st.text_input("💬 Ask about files (e.g., 'Show all PDFs')")
            files = list_files(directory)
            if st.button("Search") and isinstance(files, list):
                response = interpret_query(query, files)
                st.info(response)

        elif action == "Folder Summary":
            files = list_files(directory)
            if st.button("Summarize") and isinstance(files, list):
                if file_explorer_api_key:
                    summary_prompt = f"Summarize the contents of the following files and folders:\n{[f['Name'] for f in files]}"
                    response = model.generate_content(summary_prompt)
                    st.write(response.text)
                else:
                    st.error("Please enter your Gemini API key to use AI features.")
    else:
        st.info("👆 Enter a valid directory path to begin.")

    st.markdown("---")
    st.caption("🚀 Built with ❤️ by Drishti Baghel")
