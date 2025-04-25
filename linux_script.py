from datetime import datetime
from subprocess import (run)


def capture_out():
    result = run("ps aux", capture_output=True, shell=True, text=True).stdout
    output = result.splitlines()
    return output

def parse_processes(output):
    processes = []
    for line in output[1:]:
        columns = line.split()
        processes.append(columns)
    return processes

def get_users_list(processes):
    user_list = [process[0] for process in processes]
    return user_list

def get_count_proces(processes):
    count = (len(processes) -1)
    return count

def get_processes_by_user(processes):
    user_process_count = {}
    for process in processes:
        user = process[0]
        if user in user_process_count:
            user_process_count[user] += 1
        else:
            user_process_count[user] = 1
    return user_process_count

def get_total_memory_usage(processes):
    total_memory = sum(float(process[3]) for process in processes)
    return total_memory

def get_total_cpu(processes):
    total_cpu = sum(float(process[2]) for process in processes)
    return total_cpu

def get_all_process(processes):
    process_memory = {process[10]: float(process[3]) for process in processes}
    return process_memory

def get_process_with_max_memory(process_memory):
    if not process_memory:
        return None, 0.0
    max_memory_process = max(process_memory, key=process_memory.get)
    max_memory = process_memory[max_memory_process]
    max_memory_process = max_memory_process[:20]
    return max_memory_process, max_memory

def get_all_cpu(processes):
    process_cpu = {process[10]: float(process[2]) for process in processes}
    return process_cpu

def get_process_with_max_cpu(process_cpu):
    if not process_cpu:
        return None, 0.0
    max_process_cpu = max(process_cpu, key=process_cpu.get)
    max_cpu = process_cpu[max_process_cpu]
    max_process_cpu = max_process_cpu[:20]
    return max_process_cpu, max_cpu

if __name__ == "__main__":
    output = capture_out()
    processes = parse_processes(output)
    users_list = get_users_list(processes)
    count = get_count_proces(processes)
    total_memory = get_total_memory_usage(processes)
    total_cpu = get_total_cpu(processes)
    process_memory = get_all_process(processes)
    process_name, max_memory = get_process_with_max_memory(process_memory)
    process_cpu = get_all_cpu(processes)
    max_process_cpu, max_cpu = get_process_with_max_cpu(process_cpu)
    user_process_count = get_processes_by_user(processes)
    print(f"{run("ps aux", capture_output=True, shell=True, text=True).stdout}")
    print(f"Отчёт о состоянии системы:")
    print(f"Пользователи системы:: {users_list}")
    print(f"Процессов запущено: {count}")
    print("\nПользовательских процессов:")
    for user, count in user_process_count.items():
        print(f"{user}: {count}\n")
    print(f"Всего памяти используется: {total_memory} %")
    print(f"Всего CPU используется: {total_cpu} %")
    print(f"Больше всего памяти использует: {process_name} {max_memory}")
    print(f"Больше всего CPU использует: {max_process_cpu} {max_cpu}")



    report = (
        f'Отчет о состоянии системы:\n'
        f'Пользователи системы: {", ".join(users_list)}\n'
        f'Процессов запущено: {count}\n\n'
        f'Пользовательских процессов:\n'
        + '\n'.join([f'{user}: {count}' for user, count in user_process_count]) + '\n\n'
        f'Всего памяти используется: {total_memory} %\n'
        f'Всего CPU используется: {total_cpu} %\n'
        f'Больше всего памяти использует: {process_name} {max_memory}\n'
        f'Больше всего CPU использует: {max_process_cpu} {max_cpu}\n'
    )

    # Получаем строку с текущей датой и временем в формате 'дд.мм.ГГГГ_ЧЧ_ММ_СС'
    now = datetime.now()
    time_now = now.strftime("%d.%m.%Y_%H_%M_%S")

    # Открываем текстовый файл с именем формата: 'дд.мм.ГГГГ_ЧЧ_ММ_СС-scan.txt' и записываем отчёт
    with open(f'{time_now}-scan.txt', 'w', encoding='utf-8') as f:
        f.write(report)
