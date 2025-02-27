{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "22d46c6c-d102-4e9f-bc0f-08a3853dd77f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (1.42.0)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (5.5.1)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (8.1.8)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (19.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (13.9.4)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (3.1.44)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.25.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\asim\\desktop\\ml_project\\venv\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9e855dc1-d19a-4915-b362-4fb8b2780ac0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\Asim\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\Asim\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "2025-02-25 00:25:58.404 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.972 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Asim\\Desktop\\ml_project\\venv\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-02-25 00:26:02.975 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.978 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.984 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.987 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.991 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.994 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:02.999 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.002 Session state does not function when running a script without `streamlit run`\n",
      "2025-02-25 00:26:03.005 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.008 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.011 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.013 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.016 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.019 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-02-25 00:26:03.021 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import re\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "# Load pre-trained model and vectorizer\n",
    "with open('emotion_classifier_model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "with open('tfidf_vectorizer.pkl', 'rb') as file:\n",
    "    vectorizer = pickle.load(file)\n",
    "\n",
    "# Download NLTK resources\n",
    "nltk.download('stopwords')\n",
    "nltk.download('punkt')\n",
    "stop_words = set(stopwords.words('english'))\n",
    "\n",
    "# Preprocessing function\n",
    "def preprocess_text(text):\n",
    "    text = re.sub(r'[^a-zA-Z]', ' ', text)  # Remove special characters & numbers\n",
    "    text = text.lower()  # Convert to lowercase\n",
    "    words = word_tokenize(text)  # Tokenize text\n",
    "    words = [word for word in words if word not in stop_words]  # Remove stopwords\n",
    "    return ' '.join(words)  # Join words back into a single string\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Emotion Classifier\")\n",
    "st.write(\"Enter a sentence to predict its emotion.\")\n",
    "\n",
    "user_input = st.text_area(\"Enter your text here:\")\n",
    "\n",
    "if st.button(\"Predict Emotion\"):\n",
    "    if user_input:\n",
    "        cleaned_text = preprocess_text(user_input)\n",
    "        transformed_text = vectorizer.transform([cleaned_text])\n",
    "        prediction = model.predict(transformed_text)\n",
    "        st.success(f\"Predicted Emotion: {prediction[0]}\")\n",
    "    else:\n",
    "        st.warning(\"Please enter some text to classify.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48b1c406-48a5-402f-b85c-bd82a9c09af3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
