from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(...)

# Servir HTML + imágenes
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Luego los routers...
app.include_router(whatsapp_router)
app.include_router(lead_router)