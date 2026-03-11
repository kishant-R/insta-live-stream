from producer import produce_data
from consumer import consume_data


def main():
    stream_data = produce_data(5)
    consume_data(stream_data)


if __name__ == "__main__":
    main()
