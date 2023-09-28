import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(5)  # Simulate a non-blocking sleep
    print("World")

asyncio.run(main())  # Run the asynchronous main function

'''In this example, the await asyncio.sleep(5) line pauses the execution of 
main for 1 second without blocking the entire program.
'''

#Another example
async def fetch_url(url):
    # Simulate an HTTP request (asynchronous I/O operation)
    await asyncio.sleep(1)
    return f"Response from {url}"

async def newMain():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response)

asyncio.run(newMain())
