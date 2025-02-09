from RealtimeSTT import AudioToTextRecorder
import keyboard

def perform_action(action):
    action = action.lower()
    actions = {
        "play": lambda: keyboard.send("play/pause media"),
        "pause": lambda: keyboard.send("play/pause media"),
        "next": lambda: keyboard.send("next track"),
        "back": lambda: keyboard.send("previous track"),
        "mute": lambda: keyboard.send("volume mute"),
        "volume up": lambda: keyboard.send("volume up"),
        "volume down": lambda: keyboard.send("volume down")
    }
    
    for key, func in actions.items():
        if key in action:
            print(f"Action: {key.capitalize()}")
            func()
            break

def process_text(text):
    print(text)
    perform_action(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder()

    while True:
        recorder.text(process_text)
