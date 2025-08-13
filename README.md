# Simple Python App
A minimal Python FastAPI app with pytest tests for DevOps AI Agent.

## Setup
1. Clone: `git clone https://github.com/yourusername/simple-python-app.git`
2. Install: `pip install -r requirements.txt`
3. Run tests: `pytest tests/ -v`
4. Run locally: `uvicorn api.index:app --reload`
5. Deploy: `vercel --prod`

## Endpoints
- GET `/add?a=2&b=3`: Returns `{"result": 5}`
- GET `/divide?a=6&b=2`: Returns `{"result": 3}`
