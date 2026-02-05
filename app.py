import streamlit as st
from db import get_db
from ai import detect_emotion, generate_response

st.set_page_config(page_title="AI Mental Health Companion")

st.title("🧠 AI Mental Health Companion")

# Session state
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# ---------- AUTH ----------
if st.session_state.user_id is None:
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            db = get_db()
            cur = db.cursor(dictionary=True)
            cur.execute(
                "SELECT * FROM users WHERE email=%s AND password=%s",
                (email, password)
            )
            user = cur.fetchone()

            if user:
                st.session_state.user_id = user["id"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        name = st.text_input("Name")
        r_email = st.text_input("Email", key="r_email")
        r_pass = st.text_input("Password", type="password", key="r_pass")

        if st.button("Register"):
            db = get_db()
            cur = db.cursor()
            cur.execute(
                "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
                (name, r_email, r_pass)
            )
            db.commit()
            st.success("Registered successfully")

# ---------- MAIN APP ----------
else:
    st.subheader("How are you feeling today?")
    mood = st.selectbox("Select mood", ["Happy", "Neutral", "Sad", "Stress", "Anxiety"])

    if st.button("Save Mood"):
        db = get_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO mood_checkins (user_id, mood, mood_score) VALUES (%s,%s,%s)",
            (st.session_state.user_id, mood, 3)
        )
        db.commit()
        st.success("Mood saved")

    st.divider()
    st.subheader("Chat")

    user_msg = st.text_input("Type your message")

    if st.button("Send"):
        emotion = detect_emotion(user_msg)
        reply = generate_response(emotion)

        db = get_db()
        cur = db.cursor()
        cur.execute(
            "INSERT INTO chats (user_id,message,emotion) VALUES (%s,%s,%s)",
            (st.session_state.user_id, user_msg, emotion)
        )
        db.commit()

        st.write("🧑 You:", user_msg)
        st.write("🤖 AI:", reply)

    if st.button("Logout"):
        st.session_state.user_id = None
        st.rerun()
