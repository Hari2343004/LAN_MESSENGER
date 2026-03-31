from fastapi import FastAPI, WebSocket, WebSocketDisconnect, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from shared import save_file, get_file_path, list_files, file_exists

app = FastAPI()

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# WebSocket Connections
# -----------------------------
connections = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    print("Client connected")

    try:
        while True:
            data = await websocket.receive_text()
            print("Message:", data)

            for conn in connections:
                if conn != websocket:
                   await conn.send_text(data)

    except WebSocketDisconnect:
       if websocket in connections:
        connections.remove(websocket)
       print("Client disconnected")


# -----------------------------
# File Upload
# -----------------------------
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    filename = save_file(file.filename, content)

    print(f"Uploaded: {filename}")
    return {"status": "success", "filename": filename}


# -----------------------------
# File Download
# -----------------------------
@app.get("/download/{filename}")
def download_file(filename: str):
    if file_exists(filename):
        return FileResponse(get_file_path(filename), filename=filename)
    return {"error": "File not found"}


# -----------------------------
# File List
# -----------------------------
@app.get("/files")
def get_files():
    return {"files": list_files()}


# -----------------------------
# Root
# -----------------------------
@app.get("/")
def root():
    return {"message": "LAN Messenger Running"}