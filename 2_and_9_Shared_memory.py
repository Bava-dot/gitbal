from multiprocessing import Process, Value
import time

def writer(shared_data):
    shared_data.value = 42  # Writing data into shared memory
    print("Writer Process: Written data:", shared_data.value)

def reader(shared_data):
    time.sleep(1)  # Wait for writer to write data
    print("Reader Process: Read data:", shared_data.value)

if __name__ == "__main__":
    shared_data = Value('i', 0)  # Initialize shared memory (integer)

    writer_process = Process(target=writer, args=(shared_data,))
    reader_process = Process(target=reader, args=(shared_data,))

    writer_process.start()
    reader_process.start()

    writer_process.join()
    reader_process.join()


# code for using string in shared memory above is for integer

# from multiprocessing import Process, shared_memory
# import time

# # Define a shared memory name
# SHM_NAME = "shared_memory_example"

# def writer():
#     # Create shared memory block with a predefined name and size
#     shm = shared_memory.SharedMemory(name=SHM_NAME, create=True, size=1024)  # 1024 bytes of shared memory
#     try:
#         # Write a message into shared memory
#         message = b"Hello from the writer process!"
#         shm.buf[:len(message)] = message
#         print("Writer: Data written to shared memory.")

#         # Keep the shared memory alive for the reader to access it
#         time.sleep(5)
#     finally:
#         # Close and unlink shared memory when done
#         shm.close()
#         shm.unlink()

# def reader():
#     # Give the writer some time to write data
#     time.sleep(1)

#     # Connect to the existing shared memory block created by the writer
#     shm = shared_memory.SharedMemory(name=SHM_NAME)
#     try:
#         # Read the data from shared memory and decode
#         message = bytes(shm.buf[:]).rstrip(b'\x00').decode('utf-8')
#         print("Reader: Data read from shared memory:", message)
#     finally:
#         # Close shared memory when done
#         shm.close()

# if __name__ == "__main__":
#     # Create the writer process to write to shared memory
#     writer_process = Process(target=writer)
#     writer_process.start()

#     # Create the reader process to read from shared memory
#     reader_process = Process(target=reader)
#     reader_process.start()

#     # Wait for both processes to complete
#     writer_process.join()
#     reader_process.join()
