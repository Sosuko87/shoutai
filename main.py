import scratchattach as sa
import time
import os

with open("set.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]
username = lines[0]
get = lines[1]
print(f"招待ユーザ名 {username}、スタジオID {get}")

session = sa.login(username, os.environ.get("SCRATCH_PASSWORD"))
studio = session.connect_studio(get)
with open("user.txt", "r", encoding="utf-8") as f:
    for user in f:
        if not user.strip():
            continue
        invite = user.rstrip("\n")
        try:
            studio.invite_curator(invite)
            print(f"{invite}の招待に成功しました")
        except:
            print(f"{invite}の招待に失敗しました")
        time.sleep(5)