import platform
import psutil
from source import writer
from source import create_gui

uname = platform.uname()


def main():
    write_content = checks()
    writer.write_info(write_content)


#checks the ticked boxes
def checks(check_arr):
    content = ""

    if check_arr[0]:
        cpu_content = cpu_tests()
        content.append(cpu_content)
    if check_arr[1]:
        memory_content = memory_tests()
        content.append(memory_content)
    if check_arr[2]:
        disk_content = disk_tests()
        content.append(disk_content)
    if check_arr[3]:
        othersys_content = othersys_tests()
        content.append(othersys_content)
    if check_arr[4]:
        process_content = process_tests()
        content.append(process_content)

    return content


def cpu_tests():
    content = "CPU Info:\n"
    try:
        content.append("Cores:", psutil.cpu_count(logical=False), "\n")
        content.append("Logical Cores:", psutil.cpu_count(logical=True), "\n")
        content.append(f"Max Frequency: {psutil.cpu_freq().current:.1f}Mhz\n")
        content.append(f"CPU Usage: {psutil.cpu_percent()}%\n")
        content.append("CPU Usage/Core:")
        for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            content.append(f"Core {i}: {perc}%")

    except Exception:
        pass


def memory_tests():
    pass


def disk_tests():
    pass


def othersys_tests():
    pass


def process_tests():
    pass


if __name__ == "__main__":
    main()


"""
CPU
Memory
Disks
(Network)
Other system info
Processes
"""