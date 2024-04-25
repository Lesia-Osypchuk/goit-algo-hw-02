import queue
import time
import threading
import random

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації заявок
def generate_request():
    while True:
        # Генеруємо унікальний номер заявки
        request_id = random.randint(1, 1000)
        # Додаємо заявку до черги
        request_queue.put(request_id)
        print(f"Заявка {request_id} додана до черги")
        time.sleep(random.uniform(0.5, 2))  # Затримка перед генерацією наступної заявки

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            # Видаляємо заявку з черги
            request_id = request_queue.get()
            print(f"Заявка {request_id} обробляється")
            # Симуляція обробки заявки
            time.sleep(random.uniform(1, 3))
        else:
            print("Черга порожня")
            time.sleep(1)  # Затримка перед перевіркою черги знову

# Запуск окремих потоків для генерації та обробки заявок
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

# Встановлюємо фоновий режим для потоків (daemon)
generator_thread.daemon = True
processor_thread.daemon = True

generator_thread.start()
processor_thread.start()

# Очікування введення користувача для завершення програми
input("Натисніть Enter для завершення виконання програми...\n")

print("Програма завершила виконання.")
