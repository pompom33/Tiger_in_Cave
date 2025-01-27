# 플레이어 이동거리
possible_distance = [1, 2, 3]

#호랑이 초기 위치 설정
def initialize_tiger(): 
    import random
    tiger_first_loc = random.randint(15, 30)
    return tiger_first_loc

# 플레이어 이동방향
def user_direction_input(): 
    user_direction = input("📢동굴에 들어가려면 i, 나오려면 o를 입력하세요")
    return user_direction

#플레이어 이동거리
def user_distance_input(): 
    user_distance = input("📢얼마나 이동하시겠습니까?")
    return user_distance

#플레이어 이동 구현
def move_player(player_cur_loc, user_direction, user_distance): 
    player_old_loc = player_cur_loc
    if user_direction == "i":
        player_cur_loc += int(user_distance)
    if user_direction == "o":
        player_cur_loc -= int(user_distance)
    player_new_loc = int(player_cur_loc)
    if player_new_loc <= 0:
        player_new_loc = 0
    return player_new_loc

#플레이어 점수 계산
def add_score(score, user_direction, user_distance): 
    if user_direction == "i":
        score += int(user_distance)
    return score

#호랑이 이동 구현
def move_tiger(tiger_cur_loc): 
    tiger_new_loc = tiger_cur_loc - 4
    if tiger_new_loc < 0:
        tiger_new_loc = 1
    return tiger_new_loc

#게임 실행 함수
def play_game():
    cave_length = 30  #cave 설정
    cave = []
    for i in range(cave_length):
        cave.append("_")
    
    player_cur_loc = 0  #플레이어 위치 초기화
    score = 0           #점수 초기화
    
    initialize_tiger()  #호랑이 위치 초기화
    tiger_first_loc = initialize_tiger()
    tiger_cur_loc = tiger_first_loc
    
    print(cave)         #최초의 동굴 시각화
    
    while True:
        print("player cur loc", player_cur_loc, "score", score)
        
        user_direction = user_direction_input()
        if user_direction == "q":      #게임을 중단하려는 경우
            print("게임을 종료합니다.")
            break
        if user_direction not in ["i", "o"]:   # 잘못된 입력을 한 경우
            print("i 또는 o만 입력해주세요.(종료: q)")
            continue
        if player_cur_loc == 0 and user_direction == "o":     #첫 움직임을 'out'으로 입력한 경우
            print("처음에는 반드시 동굴에 들어가야 합니다(i 입력)")
            continue
            
        user_distance = user_distance_input()
        if user_distance == "q":      #게임을 중단하려는 경우
            print("게임을 종료합니다.")
            break
        if user_distance not in possible_distance:   # possible distance 이외의 잘못된 입력을 한 경우
            print("1부터 3까지의 숫자를 입력해주세요")
            continue
            
        else:                           # 플레이어 이동 사실 출력
            if user_direction == "i":
                print(f"{user_distance}만큼 들어갔습니다.")
            if user_direction == "o":
                print(f"{user_distance}만큼 나왔습니다.")

            move_player(player_cur_loc, user_direction, user_distance)
            move_tiger(tiger_cur_loc)
            player_new_loc = move_player(player_cur_loc, user_direction, user_distance)
            tiger_new_loc = move_tiger(tiger_cur_loc)
            score = add_score(score, user_direction, user_distance)
            cave[player_new_loc - 1] = "👩"
            cave[player_cur_loc - 1] = "_"
            
        if player_new_loc >= tiger_cur_loc: #패배할 경우
            if player_new_loc == 0:
                continue
            print(f"{player_new_loc}에서 호랑이에게 잡아먹혔습니다. 호랑이의 최초 위치는 {tiger_first_loc}이었습니다.")
            cave[player_new_loc - 1] = "🐱"
            print(cave)
            break
        if player_new_loc <= 0: #승리할 경우
            print(f"탈출했습니다! 점수는{score}입니다. 호랑이의 최초 위치는 {tiger_first_loc}이었습니다.")
            player_new_loc = 0
            cave[player_new_loc - 1] = "_"
            cave[player_cur_loc - 1] = "_"
            cave[tiger_new_loc - 1] = "🐱"
            print(cave)
            break
            
        print(cave)                      # 플레이어 이동한 결과 시각화
        player_cur_loc = player_new_loc  # new_loc을 cur_loc으로 전환(다음 loop을 위해)
        tiger_cur_loc = tiger_new_loc

