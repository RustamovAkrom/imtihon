import asyncio
import os
# import requests
import httpx
import json

class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()



path = 'descriptions'
url = 'http://164.92.64.76/desc/'

def get_url_response():
    response = httpx.get(url)
    return response.status_code


async def read_path():
    global path
    status_code = str(get_url_response())

    file_name = os.listdir(path)
    for i in file_name:

        new_path = path +'/'+ i
        
        with FileManager(new_path, 'r') as f:
            split_data = f.read().split('\n')
            name = split_data[0]
            price = split_data[1]
            text = split_data[2]

        with FileManager("Response.txt", 'a+') as w:
            w.write(str(i + ' ' + status_code + '\n'))

        print(name, price, text)

            
async def main():
    task1 = await asyncio.create_task(read_path())
    
    task2 = await asyncio.create_task(get_url_response())
    # print(task2)
    print(task1)

if __name__=='__main__':
    # os.replace('descriptions/001 200.txt', 'descriptions/001.txt')
    asyncio.run(read_path())
    
