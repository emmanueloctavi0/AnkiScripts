import requests
import sys

anki_url = 'http://localhost:8765'


def set_picture(path: str, note_id: int) -> None:

    path_list = path.split("\\")

    payload = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note_id,
                "fields": {
                    "sentence audio": ""
                },
                "audio": [{
                    "path": path,
                    "filename": path_list[-1],
                    "fields": [
                        "sentence audio"
                    ]
                }],
            }
        }
    }

    res = requests.post(anki_url, json=payload)
    print(res.text)


def get_last_note_id() -> int:
    res = requests.post(anki_url, json={
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": "added:1"
        }
    })

    result = res.json()['result']
    return int(result[-1])


if __name__ == '__main__':
    image_path = sys.argv[-1]
    print(f"Sending sound {image_path}")
    last_note_id = get_last_note_id()
    set_picture(image_path, last_note_id)
    print(last_note_id)
