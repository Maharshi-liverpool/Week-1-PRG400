import asyncio
import time

async def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter:", letter)
        await asyncio.sleep(1.5)

async def main():
    start_time = time.time()

    # Run both tasks at the same time
    await asyncio.gather(
        print_numbers(),
        print_letters()
    )

    end_time = time.time()
    print("\nTotal time taken:", round(end_time - start_time, 2), "seconds")

# Required to run asyncio programs
if __name__ == "__main__":
    asyncio.run(main())
