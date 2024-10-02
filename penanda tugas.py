import json

# Fungsi untuk memuat tugas dari file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan tugas ke file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Fungsi untuk menambahkan tugas
def add_task(tasks):
    task = input("Masukkan tugas baru: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Tugas '{task}' ditambahkan!")

# Fungsi untuk menampilkan tugas
def show_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Selesai" if task["done"] else "Belum Selesai"
        print(f"{i+1}. {task['task']} - {status}")

# Fungsi untuk menandai tugas sebagai selesai
def mark_task_done(tasks):
    show_tasks(tasks)
    task_num = int(input("Masukkan nomor tugas yang sudah selesai: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        save_tasks(tasks)
        print(f"Tugas '{tasks[task_num]['task']}' telah selesai!")
    else:
        print("Nomor tugas tidak valid.")

# Program utama
def main():
    tasks = load_tasks()
    while True:
        print("\n1. Tambah Tugas\n2. Tampilkan Tugas\n3. Tandai Tugas Selesai\n4. Keluar")
        choice = input("Pilih opsi: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
