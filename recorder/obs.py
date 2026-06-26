from obsws_python import ReqClient
import winsound

from config import (
    OBS_HOST,
    OBS_PORT,
    OBS_PASSWORD
)

client = ReqClient(
    host=OBS_HOST,
    port=OBS_PORT,
    password=OBS_PASSWORD
)


def start_recording():
    try:
        client.start_record()
        print("🔴 OBS recording started")

    except Exception as e:
        print(f"❌ OBS start error: {e}")
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)



def stop_recording():
    try:
        client.stop_record()
        print("⏹️ OBS recording stopped")

    except Exception as e:
        print(f"❌ OBS stop error: {e}")
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)
        winsound.Beep(1000 , 500)