def sj(jobs):
    t = 0
    waste_time = 0
    jobs.sort()
    for i in range(len(jobs)):
        waste_time += t
        t+=jobs[i]
    return waste_time
if __name__ == '__main__':
    jobs = list(map(int, input().split()))
    print(sj(jobs))
