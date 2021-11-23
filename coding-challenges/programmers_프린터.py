def solution(priorities, location):
    queue = [(i, v) for i, v in enumerate(priorities)]
    answer = 0
    while True:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
