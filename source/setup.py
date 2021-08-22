import platform
import psutil
import writer

#constant for multi platforming
uname = platform.uname()


def main():
    configure_arr = writer.configure()
    write_content = checks(configure_arr)
    writer.write_info(write_content)


#checks the ticked boxes
def checks(check_arr):
    content = []

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
    content = ["CPU Info: "]
    try:
        content.append("Cores:", psutil.cpu_count(logical=False))

        content.append("Cores:", psutil.cpu_count(logical=False))
        content.append("Logical Cores:", psutil.cpu_count(logical=True))
        content.append(f"Max Frequency: {psutil.cpu_freq().current:.1f}Mhz")
        content.append(f"CPU Usage: {psutil.cpu_percent()}%")
        content.append("CPU Usage/Core:")
        for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            content.append(f"Core {i}: {perc}%")

    except Exception:
        pass

    return content


def memory_tests():
    content = ["Memory Info: "]

    return content


def disk_tests():
    content = ["Disk Info: "]

    for partition in psutil.disk_partitions():
        content.append((f"Device: {partition.device} ", f"\tMountpoint: {partition.mountpoint} ",
                       f"\tFile system type: {partition.fstype} "))
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

        content.append((f"Total Size: {partition_usage.total} ", f"Used: {partition_usage.used} ",
                       f"Percentage: {partition_usage.percent} "))

    return content


def othersys_tests():
    content = ["Other System Info: "]

    return content


def process_tests():
    content = ["Process Info: "]

    return content


if __name__ == "__main__":
    main()

