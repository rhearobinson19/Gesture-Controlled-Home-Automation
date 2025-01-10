import requests

def send_control_signal(device_id, action):
    url = f"http://<device_control_url>/control"
    payload = {'device_id': device_id, 'action': action}
    response = requests.post(url, json=payload)
    return response.status_code


send_control_signal(1, "turn_on")
