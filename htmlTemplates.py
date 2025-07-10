css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

body, .stApp {
    background: linear-gradient(135deg, #232526 0%, #414345 100%);
    font-family: 'Inter', sans-serif;
    color: #f5f6fa;
}

header, .stHeader {
    background: transparent !important;
}

.stSidebar {
    background: #18181b !important;
    border-radius: 20px 0 0 20px;
    box-shadow: 2px 0 12px rgba(0,0,0,0.15);
}

.stSidebar .stButton>button {
    background: #6366f1;
    color: #fff;
    border-radius: 8px;
    font-weight: 600;
    transition: background 0.2s;
}
.stSidebar .stButton>button:hover {
    background: #818cf8;
}

.stTextInput>div>div>input {
    background: #23272f;
    color: #f5f6fa;
    border-radius: 8px;
    border: 1px solid #6366f1;
    padding: 12px;
    font-size: 1.1rem;
}

.stFileUploader {
    background: #23272f;
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 2px 12px rgba(99,102,241,0.08);
    margin-bottom: 24px;
}

.stButton>button {
    background: linear-gradient(90deg, #6366f1 0%, #60a5fa 100%);
    color: #fff;
    border-radius: 8px;
    font-weight: 600;
    padding: 10px 24px;
    font-size: 1rem;
    transition: background 0.2s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #818cf8 0%, #93c5fd 100%);
}

.stMarkdown, .stText {
    font-size: 1.1rem;
    color: #f5f6fa;
}

.chat-bubble {
    max-width: 70%;
    padding: 16px 20px;
    margin: 12px 0;
    border-radius: 18px;
    font-size: 1.1rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    animation: fadeIn 0.5s;
}
.user-bubble {
    background: linear-gradient(90deg, #6366f1 0%, #60a5fa 100%);
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 4px;
}
.bot-bubble {
    background: #23272f;
    color: #f5f6fa;
    margin-right: auto;
    border-bottom-left-radius: 4px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px);}
    to { opacity: 1; transform: translateY(0);}
}

.stSpinner {
    color: #6366f1 !important;
}
</style>
"""