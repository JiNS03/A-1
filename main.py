# main.py

# 1. 기본 프롬프트 데이터
prompts = [
    {
        "id": 1,
        "title": "IT 기술 블로그 글 작성 페르소나",
        "content": "너는 10년 차 수석 IT 에디터야. 아래 전달하는 기술 주제를 초보자도 쉽게 이해할 수 있도록 명확하고 유쾌한 톤으로 설명해줘.",
        "category": "페르소나",
        "is_favorite": True
    },
    {
        "id": 2,
        "title": "사이버펑크 도시 배경 이미지 생성",
        "content": "A futuristic cyberpunk city at night with neon signs, wet street reflections, highly detailed, cinematic lighting, 8k resolution --ar 16:9",
        "category": "이미지 생성",
        "is_favorite": False
    },
    {
        "id": 3,
        "title": "파이썬 코드 리팩토링 및 주석 추가",
        "content": "다음 파이썬 코드를 PEP 8 스타일 가이드에 맞게 리팩토링하고, 각 함수의 역할과 주요 로직에 상세한 한국어 주석을 달아줘.",
        "category": "텍스트 생성",
        "is_favorite": False
    }
]

# ID 자동 생성을 위한 헬퍼 함수
def get_next_id():
    if not prompts:
        return 1
    return max(p['id'] for p in prompts) + 1

def show_menu():
    print("\n" + "=" * 40)
    print("      📄 GenAI 프롬프트 관리자 📄")
    print("=" * 40)
    print("1. 프롬프트 목록 보기")
    print("2. 프롬프트 추가")
    print("3. 카테고리별 조회")
    print("4. 키워드 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("0. 프로그램 종료")
    print("=" * 40)
    return input("원하는 기능의 번호를 입력하세요: ").strip()

# [기능 1] 프롬프트 목록 보기
def show_prompt_list(prompts_list):
    print("\n" + "=" * 40)
    print("         📋 프롬프트 전체 목록")
    print("=" * 40)
    
    if not prompts_list:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in prompts_list:
        fav = "⭐ " if p["is_favorite"] else ""
        print(f"[ID: {p['id']}] {fav}{p['title']} [{p['category']}]")
    print("=" * 40)

# [기능 2] 프롬프트 추가
def add_prompt():
    print("\n[새 프롬프트 추가]")
    title = input("제목을 입력하세요: ").strip()
    while not title:
        print("❌ 제목은 필수입니다.")
        title = input("제목을 다시 입력하세요: ").strip()

    content = input("내용을 입력하세요: ").strip()
    while not content:
        print("❌ 내용은 필수입니다.")
        content = input("내용을 다시 입력하세요: ").strip()

    category = input("카테고리를 입력하세요 (예: 텍스트 생성, 이미지 생성, 기타): ").strip()
    if not category:
        category = "기타"

    new_prompt = {
        "id": get_next_id(),
        "title": title,
        "content": content,
        "category": category,
        "is_favorite": False
    }
    prompts.append(new_prompt)
    print(f"\n✅ '{title}' 프롬프트가 성공적으로 추가되었습니다!")

# [기능 3] 카테고리별 조회
def show_by_category():
    # 현재 등록된 카테고리 중복 제거하여 목록 생성
    categories = list(set(p['category'] for p in prompts))
    
    print("\n[카테고리 목록]")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
        
    choice = input("\n조회할 카테고리 번호나 이름을 정확히 입력하세요: ").strip()
    target_category = ""
    
    # 번호로 입력한 경우와 이름으로 입력한 경우 모두 처리
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        target_category = categories[int(choice)-1]
    else:
        target_category = choice

    filtered_prompts = [p for p in prompts if p['category'] == target_category]
    if not filtered_prompts:
        print("\n❌ 해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        show_prompt_list(filtered_prompts)

# [기능 4] 키워드 검색
def search_prompt():
    keyword = input("\n검색할 키워드를 입력하세요: ").strip()
    if not keyword:
        print("❌ 키워드를 입력해야 합니다.")
        return

    # 제목이나 내용에 키워드가 포함된 프롬프트 필터링 (대소문자 구분 없음)
    filtered_prompts = [
        p for p in prompts 
        if keyword.lower() in p['title'].lower() or keyword.lower() in p['content'].lower()
    ]
    
    if not filtered_prompts:
        print(f"\n❌ '{keyword}'(으)로 검색된 결과가 없습니다.")
    else:
        print(f"\n[ 🔍 '{keyword}' 검색 결과 ]")
        show_prompt_list(filtered_prompts)

# [기능 5] 상세 보기
def show_prompt_detail():
    choice = input("\n상세보기할 프롬프트 ID 번호를 입력하세요: ").strip()
    if not choice.isdigit():
        print("❌ 숫자(ID)를 입력해주세요.")
        return
        
    target_id = int(choice)
    for p in prompts:
        if p['id'] == target_id:
            print("\n" + "=" * 50)
            fav = "⭐ (즐겨찾기 됨)" if p["is_favorite"] else ""
            print(f"📌 제목: {p['title']} {fav}")
            print(f"📂 카테고리: {p['category']}")
            print("-" * 50)
            print(f"📝 내용:\n{p['content']}")
            print("=" * 50)
            return
            
    print("\n❌ 해당 ID의 프롬프트를 찾을 수 없습니다.")

# [기능 6] 즐겨찾기 관리
def manage_favorites():
    print("\n[즐겨찾기 관리]")
    print("1. 즐겨찾기된 프롬프트만 보기")
    print("2. 즐겨찾기 추가/해제하기")
    choice = input("원하는 작업 번호를 입력하세요: ").strip()
    
    if choice == "1":
        favs = [p for p in prompts if p['is_favorite']]
        print("\n[ ⭐ 즐겨찾기 모아보기 ]")
        show_prompt_list(favs)
    elif choice == "2":
        id_choice = input("상태를 변경할 프롬프트 ID 번호를 입력하세요: ").strip()
        if not id_choice.isdigit():
            print("❌ 숫자를 입력해주세요.")
            return
            
        target_id = int(id_choice)
        for p in prompts:
            if p['id'] == target_id:
                # 상태 반전 (True <-> False)
                p['is_favorite'] = not p['is_favorite']
                status = "추가" if p['is_favorite'] else "해제"
                print(f"\n✅ '{p['title']}' 프롬프트가 즐겨찾기에 {status}되었습니다!")
                return
        print("\n❌ 해당 ID의 프롬프트를 찾을 수 없습니다.")
    else:
        print("❌ 잘못된 입력입니다.")

def main():
    while True:
        menu_choice = show_menu()
        
        if menu_choice == "1":
            show_prompt_list(prompts)
        elif menu_choice == "2":
            add_prompt()
        elif menu_choice == "3":
            show_by_category()
        elif menu_choice == "4":
            search_prompt()
        elif menu_choice == "5":
            show_prompt_detail()
        elif menu_choice == "6":
            manage_favorites()
        elif menu_choice == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다! 👋")
            break
        else:
            print("\n❌ 잘못된 번호입니다. 메뉴의 번호를 다시 확인해 주세요.")

if __name__ == "__main__":
    main()