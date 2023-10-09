import subprocess
import threading
import os

def start_worker(week, port, processes):
    proc = subprocess.Popen(
        ['http-server', f'./{week}', '-p', f'{port}'],
        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True
    )
    
    processes.append(proc)
    proc.wait()

    #subprocess.call(['http-server', f'./{week}', '-p', f'{port}'], stdout=open(os.devnull, "w"), shell=True, stderr=subprocess.STDOUT)

def stop_worker(proc):
    print('Stopping worker... ', end='')
    proc.terminate()
    print('OK')

def main():
    weeks = [x for x in os.listdir('.') if x.startswith('week')]

    threads = []
    processes = []
    port = 3000

    for week in weeks:
        print(f'Starting {week} worker on port {port}... ', end='')
        t = threading.Thread(target=start_worker, args=(week,port,processes))
        t.daemon = True
        threads.append(t)

        print('OK')
        port += 1
    
    for t in threads:
        t.start()

    input('\nPress any key to close workers...')

    for p in processes:
        stop_worker(p)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()