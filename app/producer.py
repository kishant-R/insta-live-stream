import time

def produce_data(count):
    data_list = []

    for i in range(count):
        message = f"Live Stream Event {i}"
        print(f"[Producer] Generated: {message}")
        data_list.append(message)
        time.sleep(1)

    return data_list
