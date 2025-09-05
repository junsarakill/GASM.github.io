# 섀버 WB 멀리건 포함 드로우 확률 계산기

# 특정 카드를 특정 턴 까지 뽑을 확률 계산 (멀리건 포함)

"""
nck 조합 계산
"""
def combinations(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k
    
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)

    return result

"""
하이퍼기하 분포 확률 계산
    N_pop (int): 덱 매수
    N_success_pop (int): 특정 카드 수
    n_sample (int): 총 드로우 카드 수
    k_success_sample (int): 뽑은 카드 중 특정 카드 수
"""
def hypergeometric_probability(N_pop, N_success_pop, n_sample, k_success_sample):
    if k_success_sample < 0 or k_success_sample > n_sample or \
       k_success_sample > N_success_pop or \
       n_sample - k_success_sample > N_pop - N_success_pop:
        return 0.0
    
    prob = (combinations(N_success_pop, k_success_sample) * \
            combinations(N_pop - N_success_pop, n_sample - k_success_sample)) / \
           combinations(N_pop, n_sample)
    return prob


"""
    섀도우버스 월즈 비욘드 규칙에 따라 특정 카드(target_copies)를
    특정 턴(target_turn)까지 뽑을 확률을 계산

    1. 초기 패에 있음
    + 2. 멀리건 후 있음 (1 실패*2 확률)
    + 3. x 턴까지 드로우해서 뽑음 (1 실패 *2 실패 * 3 확률)
    = result
"""
def calc_draw_prob(target_copies, target_turn):
    
    total_deck_size = 40
    
    # 1. 초기 4장 손패에 원하는 카드가 없을 확률 계산
    prob_no_target_initial_hand = hypergeometric_probability(
        N_pop=total_deck_size,
        N_success_pop=target_copies,
        n_sample=4, # 초기 핸드 4장
        k_success_sample=0 # 특정 카드가 0장일 확률
    )
    
    # 2. 멀리건 했을 때 원하는 카드가 없을 확률 계산 (초기 핸드에 없었다는 전제 하에)
    # 멀리건한 카드가 덱으로 돌아오므로, 다시 40장 덱에서 뽑는 것과 동일합니다.
    prob_no_target_mulligan_hand = hypergeometric_probability(
        N_pop=total_deck_size,
        N_success_pop=target_copies,
        n_sample=4, # 멀리건으로 새로 뽑는 4장
        k_success_sample=0 # 특정 카드가 0장일 확률
    )
    
    # 초기 핸드에도, 멀리건 핸드에도 원하는 카드가 없을 확률
    prob_no_target_after_mulligan = (prob_no_target_initial_hand 
                                  * prob_no_target_mulligan_hand)
    
    # 3. 턴 드로우로 원하는 카드를 뽑을 확률 계산 (앞 단계에서 모두 실패했다는 전제 하에)
    
    # 3턴까지 총 뽑는 드로우 카드 수 (1턴, 2턴, 3턴 드로우)
    num_turn_draws = max(0, target_turn - 0) # 초기 드로우와 멀리건 이후 턴 드로우 수
        # 0턴 시작 -> 1턴 시작: 1드로우
        # 1턴 시작 -> 2턴 시작: 1드로우
        # 2턴 시작 -> 3턴 시작: 1드로우
        # 총 3 드로우 (3턴을 원한다면)

    if num_turn_draws == 0:
        # 0턴 (시작 핸드 및 멀리건만 고려)일 경우, 턴 드로우는 없음
        prob_no_target_in_turn_draws = 1.0
    else:
        # 이 시점에서 이미 8장 (초기 4 + 멀리건 4)의 카드 번호는 확정된 상태
        # 그 카드들 안에 타겟 카드는 없음
        # 남은 덱은 40 - (이미 뽑은 8장 중 현재 손에 없는 4장) = 36장
        # 하지만 멀리건으로 다시 덱에 넣은 4장이 있으니, 정확히 말하면
        # '현재 손에 들고 있는 4장'을 제외한 나머지 36장에서 드로우가 발생.
        # 즉, '현재 손에 없는' 총 36장의 카드 중 해당 카드가 나올 확률
        # 여기서 하이퍼기하 분포를 사용하는 대신, 단순히 뽑히지 않을 확률을 곱해 나갑니다.

        # target_copies : 덱에 남아있는 특정 카드의 수
        # cards_remaining_in_deck : 현재 손에 없는 카드 수
        # num_turn_draws : 앞으로 뽑을 카드 수
        
        # 특정 카드가 turn_draws 동안 나오지 않을 확률
        prob_no_target_in_turn_draws = 1.0
        
        # 초기에 뽑은 4장 중 특정 카드가 없었고 (prob_no_target_initial_hand),
        # 멀리건으로 뽑은 4장 중 특정 카드가 없었다는 것은 (prob_no_target_mulligan_hand),
        # 현재 손패에는 특정 카드가 없다는 의미입니다.
        # 즉, 덱에는 target_copies의 카드들이 온전히 다 있다고 가정하고 드로우합니다.
        
        # 뽑을 카드 수가 현재 덱의 전체 카드 수보다 많을 경우를 방지
        actual_draw_count = min(num_turn_draws, total_deck_size - 4) # 손패에 있는 4장을 제외한 실제 덱의 카드 수

        cards_left_for_draws = total_deck_size - 4 # 현재 손패에 있는 4장을 제외한 덱 크기
        
        for i in range(num_turn_draws):
            # i번째 드로우에서 특정 카드가 나오지 않을 확률
            # (총 덱 크기 - 4 - i)는 이미 뽑아서 손패에 있거나, 혹은 덱의 제일 앞에서 뽑힌 카드
            # 덱의 크기가 계속 줄어드는 비복원 추출 방식
            if cards_left_for_draws - i <= 0: # 덱이 다 떨어졌을 경우
                prob_no_target_in_turn_draws *= 0
                break
            prob_no_target_in_turn_draws *= (cards_left_for_draws - i - target_copies) / (cards_left_for_draws - i)
            # 여기서는 손패에 있는 4장을 제외한 36장 중에서 뽑는 것으로 계산합니다.
            # 실제 게임 로직에 가깝게, 4장 손패를 제외한 36장 덱에서 순차적으로 뽑는다는 가정입니다.

    # 4. 최종 확률 (전체에서 특정 카드가 한 장도 나오지 않을 확률을 뺀다)
    # 초기 핸드에도 없고 AND 멀리건 핸드에도 없고 AND 턴 드로우에도 없을 확률
    prob_not_found_at_all = prob_no_target_after_mulligan * prob_no_target_in_turn_draws
    
    # 1 - (한 장도 나오지 않을 확률) = 적어도 한 장 나올 확률
    prob_at_least_one = 1 - prob_not_found_at_all
    
    return prob_at_least_one

"""
턴 수 입력받아 드로우 확률 계산
"""
def run_draw_calc():
    # 사용자로부터 턴 수 입력받기
    while True:
        try:
            # input() 함수로 사용자 입력을 받습니다.
            # 입력받은 값은 문자열이므로 int()로 정수형 변환합니다.
            print("------------------------------------------------------------------")
            user_input_turn = input("계산하고 싶은 턴 수를 입력해주세요 (예: 3): ")
            target_turn = int(user_input_turn)
            if target_turn < 1:
                print("턴 수는 1 이상이어야 합니다. 다시 입력해주세요.")
            else:
                break # 유효한 입력이 들어오면 루프를 종료합니다.
        except ValueError:
            # 사용자가 숫자가 아닌 것을 입력했을 때 발생하는 오류 처리
            print("유효한 숫자를 입력해주세요.")

    # 턴 수에 따라 결과 출력
    print(f"\n--- 섀도우버스 월즈 비욘드, 40장 덱 기준, 멀리건 포함, {target_turn}턴 시작 시 손패 확률 ---")

    # target_turn 변수는 이 코드 블록 밖에서 정의되었다고 가정합니다.

    # 특정 카드가 덱에 1장에서 3장까지 있을 경우를 반복문으로 처리
    # num_copies는 1, 2, 3으로 변합니다.
    for num_copies in range(1, 4):
        prob_n_copies = calc_draw_prob(num_copies, target_turn) # calc_draw_prob 함수는 이미 정의되어 있다고 가정합니다.
        print(f"덱에 특정 카드 {num_copies}장 있을 때: {prob_n_copies:.2%}")

    print("------------------------------------------------------------------")


# --- 스크립트 실행 부분 (다른 함수들은 위에 그대로 있다고 가정) ---

if __name__ == "__main__":
    while True:
        # 이 함수 이름이 calculate_card_draw_probability_shadowverse_wb 이거나
        # 혹은 run_card_probability_calculator 일 수 있습니다.
        # 기존 스크립트의 실행 함수 이름에 맞춰 변경해주세요.
        run_draw_calc() # 확률 계산 함수 실행

        while True:
            # 사용자에게 계속할지 종료할지 선택지를 묻습니다.
            repeat_choice = input("\n계속하려면 Enter를 누르거나, 종료하려면 'exit'을 입력하세요: ").lower().strip()
            
            if repeat_choice == '': # 사용자가 Enter 키만 누른 경우
                break # 내부 루프를 종료하고 외부 루프(다시 계산)로 이동
            elif repeat_choice == 'exit': # 사용자가 'exit'을 입력한 경우
                print("프로그램을 종료합니다.")
                # 'exit_program' 플래그를 설정하여 외부 루프도 종료하도록 합니다.
                # (또는 sys.exit()를 직접 사용할 수도 있습니다만, 플래그 방식이 더 유연합니다.)
                _should_exit_program = True 
                break # 내부 루프 종료
            else: # 유효하지 않은 입력인 경우
                print("유효하지 않은 입력입니다. 계속하려면 Enter, 종료하려면 'exit'을 입력해주세요.")
        
        # 내부 루프에서 프로그램 종료가 요청되었는지 확인하여 외부 루프를 종료합니다.
        if '_should_exit_program' in locals() and _should_exit_program:
            break # 전체 프로그램 루프 종료
