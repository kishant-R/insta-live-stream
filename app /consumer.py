def consume_data(data_list):

    print("[Consumer] Processing data")

    with open("stream_output.txt", "a") as file:
        for item in data_list:
            file.write(item + "\n")
            print(f"[Consumer] Stored: {item}")

    print("[Consumer] Completed")
