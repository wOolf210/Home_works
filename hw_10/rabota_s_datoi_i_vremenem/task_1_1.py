import datetime
import pytz

def get_time():
    gmt_time = datetime.datetime.now(pytz.utc)
    print(f"GMT: {gmt_time.strftime('%Y-%m-%d %H:%M:%S')}")
    local_time = gmt_time.astimezone(pytz.timezone('Europe/Moscow'))
    print(f"Local: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    get_time()
