import asyncio

async def perform_task(task_name, delay):
    # Görevin tamamlanması
    await asyncio.sleep(delay)  # Simüle edilen bekleme süresi
    return f"{task_name} görevi tamamlandı"


async def main():
    task= [
        asyncio.create_task(perform_task("Görev 1", 3)),
        asyncio.create_task(perform_task("Görev 2", 5)),
        asyncio.create_task(perform_task("Görev 3", 2))
    ] 

    for x in task():
        print(x)




         
    

asyncio.run(main())

