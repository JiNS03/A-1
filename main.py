# main.py

# 1. 기본 프롬프트 데이터 (최소 3개 이상 등록)
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

# 2. 메뉴 출력 및 사용자 입력 함수
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
    choice = input("원하는 기능의 번호를 입력하세요: ").strip()
    return choice

# 3. 메인 실행 함수
def main():
    while True:
        menu_choice = show_menu()
        
        if menu_choice == "1":
            print("\n[안내] 프롬프트 목록 보기 기능 (구현 예정)")
        elif menu_choice == "2":
            print("\n[안내] 프롬프트 추가 기능 (구현 예정)")
        elif menu_choice == "3":
            print("\n[안내] 카테고리별 조회 기능 (구현 예정)")
        elif menu_choice == "4":
            print("\n[안내] 키워드 검색 기능 (구현 예정)")
        elif menu_choice == "5":
            print("\n[안내] 프롬프트 상세 보기 기능 (구현 예정)")
        elif menu_choice == "6":
            print("\n[안내] 즐겨찾기 관리 기능 (구현 예정)")
        elif menu_choice == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n[오류] 잘못된 번호입니다. 메뉴의 번호를 다시 확인해 주세요.")

if __name__ == "__main__":
    main()