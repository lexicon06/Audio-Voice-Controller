from RealtimeSTT import AudioToTextRecorder
import keyboard


def perform_action(action):
    action = action.lower()
    if "play" in action or "pause" in action:
        print("Action: Play/Pause")
        keyboard.send("play/pause media")
    elif "next" in action:
        print("Action: Next Song")
        keyboard.send("next track")
    elif "back" in action:
        print("Action: Previous Song")
        keyboard.send("previous track")
    elif "mute" in action:
        print("Action: Mute/Unmute")
        keyboard.send("volume mute")
    elif "volume up" in action:
        print("Action: Volume Up")
        keyboard.send("volume up")
    elif "volume down" in action:
        print("Action: Volume Down")
        keyboard.send("volume down")


def process_text(text):
    print(text)
    perform_action(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder()

    while True:
        recorder.text(process_text)
