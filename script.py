import psutil
import requests
import time

api_url = 'url'

memory_threshold = 90


def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    return memory_percent


def send_alarm():
    payload = {'message': 'Память превысила порог'}
    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            print("HTTP-запрос отправлен успешно")
        else:
            print(f"Ошибка при отправке HTTP-запроса: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке HTTP-запроса: {e}")


def main():
    while True:
        memory_percent = check_memory_usage()
        if memory_percent > memory_threshold:
            send_alarm()
        time.sleep(300)


if __name__ == '__main__':
    main()
