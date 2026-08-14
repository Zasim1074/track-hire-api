from fastapi import FastAPI

app = FastAPI(
    title="track-hire-api",
    version="1.0.0",
    description="User based(HR & Candidate) workflow with proper Authentication and Authorization and other customization",
)


@app.get("/")
def root():
    return {"message": "Welcome back Jaseem, Let's work on backend as well!"}
