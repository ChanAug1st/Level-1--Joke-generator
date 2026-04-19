


### Flow:
1. User interacts with the frontend (button click / input)
2. Frontend sends a request to backend API
3. Backend processes request and calls LLM API
4. LLM returns generated joke
5. Backend sends response back to frontend
6. Joke is displayed to user

---

## ⚙️ Technical Choices

### Frontend:
- React + Vite  
  → Chosen for fast development and simple component-based UI structure

### Backend:
- Python (FastAPI)  
  → Lightweight and easy to integrate with AI APIs

### AI Integration:
- External LLM API (Gemini API)  
  → Used for generating jokes dynamically

### Why this stack:
- Simple separation of concerns (frontend / backend / AI layer)
- Easy to extend (can add more AI features later)
- Fast development setup for learning and prototyping

---

## 🚀 Setup and Running Instructions


```bash
### 1. Clone the repository

git clone https://github.com/ChanAug1st/Level-1--Joke-generator.git
cd Level-1--Joke-generator

### **2. Backend Setup**
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

API_KEY=your_api_key_here

python main.py


### **3. Frontend Setup**
```bash
cd frontend

npm install

npm run dev
