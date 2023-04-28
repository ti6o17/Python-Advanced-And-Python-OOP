from collections import deque

que_eggs = deque(input().split(', '))
que_Lists_of_paper = deque(input().split(', '))
eggs_in_box = 0
while True:
    egg = que_eggs.popleft()
    if int(egg) <= 0:
        continue
    paper = que_Lists_of_paper.pop()
    if int(egg) + int(paper) <= 50 and not int(egg) == 13:
        eggs_in_box += 1
    elif int(egg) == 13:
        paper_left = que_Lists_of_paper.popleft()
        que_Lists_of_paper.append(paper_left)
        que_Lists_of_paper.appendleft(paper)
    if not que_Lists_of_paper:
        break
    if not que_eggs:
        break
if eggs_in_box == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f'Great! You filled {eggs_in_box} boxes.')
if que_eggs:
    print(f"Eggs left: {', '.join(que_eggs)}")
elif que_Lists_of_paper:
    print(f"Pieces of paper left: {', '.join(que_Lists_of_paper)}")
