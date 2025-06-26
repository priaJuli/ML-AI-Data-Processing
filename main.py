# main.py
from fastapi import FastAPI
from routes import authentication, users, items, posts, transactions

# Create the FastAPI app instance
app = FastAPI(
    title="Modular FastAPI Example",
    description="A demonstration of a structured FastAPI application with JWT authentication.",
    version="1.0.0",
)

# --- Include Routers ---
# The order of inclusion can matter for middleware, but for routers it's generally flexible.
# We include the authentication router first, without a prefix, so the path is just /token.
app.include_router(authentication.router)

# Include other routers with their respective prefixes and tags for organization.
app.include_router(users.router)
app.include_router(items.router)
app.include_router(posts.router)
app.include_router(transactions.router)


@app.get("/")
async def root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to the Modular FastAPI App!"}

