import  threading
import requests
import  time


def get_data(urls):

    st = time.time()

    json_array = []

    for url in urls:
        json_array.append(requests.get(url).json())

    et = time.time()
    elapsed_time = et - st
    print(f"Start time : {st}, End time: {et}, Elapsed time: {elapsed_time}")

    return json_array


urls = ['https://postman-echo.com/delay/3'] * 10

print(urls)

#get_data(urls) #36 seconds