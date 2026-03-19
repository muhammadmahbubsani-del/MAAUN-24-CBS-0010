from collections import deque

# 1. Initialize
application_inbox = deque()           # ← Queue (FIFO)
processed_history = []                # ← Stack (LIFO)

# 2. Ingest messy data
messy_names = [
    "  TechCorp   ",
    "Bio-gen",
    "  quantumLeap  ",
    "nanoHealth!"
]

for raw in messy_names:
    clean_name = raw.strip().lower()          # clean + lowercase
    application_inbox.append(clean_name)      # add to queue (right side)

print("Inbox:", list(application_inbox))
# Expected: ['techcorp', 'bio-gen', 'quantumleap', 'nanohealth!']

# 3. Process FIFO (normal approval flow)
while application_inbox:                    # while queue not empty
    name = application_inbox.popleft()      # take from front
    print(f"Approving: {name}")
    processed_history.append(name)          # push to stack

print("\nAll processed. History stack:", processed_history)

# 4. Simulate a mistake → Undo last action (LIFO)
if processed_history:
    reverted = processed_history.pop()      # pop from end (last approved)
    print(f"Reverting approval for: {reverted}")
    application_inbox.append(reverted)      # put it back to queue

print("Inbox after revert:", list(application_inbox))