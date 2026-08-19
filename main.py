import json
import os

DATA_FILE = "prompts.json"

# 1. 초기 기본 데이터 (파일이 없을 경우 사용)
default_prompts = [
    {
        "id": 1,
        "title": "IT 기술 블로그 글 작성 페르소나",
        "content": "너는 10년 차 수석 IT 에디터야. 아래 전달하는 기술 주제를 초보자도 쉽게 이해할 수 있도록 명확하고 유쾌한 톤으로 설명해줘.",
        "category": "페르소나",
        "is_favorite": True,
        "usage_count": 0
    },
    {
        "id": 2,
        "title": "사이버펑크 도시 배경 이미지 생성",
        "content": "A futuristic cyberpunk city at night with neon signs, wet street reflections, highly detailed, cinematic lighting, 8k resolution --ar 16:9",
        "category": "이미지 생성",
        "is_favorite": False,
        "usage_count": 0
    },
    {
        "id": 3,
        "title": "파이썬 코드 리팩토링 및 주석 추가",
        "content": "다음 파이썬 코드를 PEP 8 스타일 가이드에 맞게 리팩토링하고, 각 함수의 역할과 주요 로직에 상세한 한국어 주석을 달아줘.",
        "category": "텍스트 생성",
        "is_favorite": False,
        "usage_count": 0
    }
]

# JSON 파일 불러오기
def load_prompts():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # 기존 데이터 호환성을 위해 usage_count 필드가 없으면 기본값 0 추가
                for p in data:
                    if "usage_count" not in p:
                        p["usage_count"] = 0
                return data
        except Exception as e:
            print(f"⚠️ 파일 불러오기 오류: {e}")
            return default_prompts
    else:
        # 파일이 없을 경우 기본 데이터를 저장 후 반환
        save_prompts(default_prompts)
        return default_prompts

# JSON 파일 저장하기
def save_prompts(prompts_data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(prompts_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"❌ 데이터 저장 중 오류 발생: {e}")

# 전역 프롬프트 리스트 로드
prompts = load_prompts()

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
    print("5. 프롬프트 상세 보기 (조회수 증가)")
    print("6. 즐겨찾기 관리")
    print("7. 프롬프트 수정/삭제")
    print("8. 인기 프롬프트 (조회수 Top N)")
    print("9. Markdown 파일로 내보내기")
    print("0. 프로그램 종료")
    print("=" * 40)
    return input("원하는 기능의 번호를 입력하세요: ").strip()

# [기능 1] 프롬프트 목록 보기
def show_prompt_list(prompts_list):
    print("\n" + "=" * 40)
    print("         📋 프롬프트 목록")
    print("=" * 40)
    
    if not prompts_list:
        print("등록된 프롬프트가 없습니다.")
        return

    for p in prompts_list:
        fav = "⭐ " if p["is_favorite"] else ""
        views = p.get("usage_count", 0)
        print(f"[ID: {p['id']}] {fav}{p['title']} [{p['category']}] (조회수: {views}회)")
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
        "is_favorite": False,
        "usage_count": 0
    }
    prompts.append(new_prompt)
    save_prompts(prompts)
    print(f"\n✅ '{title}' 프롬프트가 성공적으로 추가되었습니다!")

# [기능 3] 카테고리별 조회
def show_by_category():
    categories = list(set(p['category'] for p in prompts))
    
    if not categories:
        print("\n❌ 등록된 카테고리가 없습니다.")
        return

    print("\n[카테고리 목록]")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
        
    choice = input("\n조회할 카테고리 번호나 이름을 정확히 입력하세요: ").strip()
    target_category = ""
    
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

    filtered_prompts = [
        p for p in prompts 
        if keyword.lower() in p['title'].lower() or keyword.lower() in p['content'].lower()
    ]
    
    if not filtered_prompts:
        print(f"\n❌ '{keyword}'(으)로 검색된 결과가 없습니다.")
    else:
        print(f"\n[ 🔍 '{keyword}' 검색 결과 ]")
        show_prompt_list(filtered_prompts)

# [기능 5] 상세 보기 (조회수 증가 기능 포함)
def show_prompt_detail():
    choice = input("\n상세보기할 프롬프트 ID 번호를 입력하세요: ").strip()
    if not choice.isdigit():
        print("❌ 숫자(ID)를 입력해주세요.")
        return
        
    target_id = int(choice)
    for p in prompts:
        if p['id'] == target_id:
            # 조회수 증가 및 자동 저장
            p['usage_count'] = p.get('usage_count', 0) + 1
            save_prompts(prompts)

            print("\n" + "=" * 50)
            fav = "⭐ (즐겨찾기 됨)" if p["is_favorite"] else ""
            print(f"📌 제목: {p['title']} {fav}")
            print(f"📂 카테고리: {p['category']}")
            print(f"👀 조회수: {p['usage_count']}회")
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
                p['is_favorite'] = not p['is_favorite']
                save_prompts(prompts)
                status = "추가" if p['is_favorite'] else "해제"
                print(f"\n✅ '{p['title']}' 프롬프트가 즐겨찾기에 {status}되었습니다!")
                return
        print("\n❌ 해당 ID의 프롬프트를 찾을 수 없습니다.")
    else:
        print("❌ 잘못된 입력입니다.")

# [기능 7] 프롬프트 수정 및 삭제
def edit_or_delete_prompt():
    print("\n[프롬프트 수정/삭제]")
    print("1. 프롬프트 수정")
    print("2. 프롬프트 삭제")
    choice = input("원하는 작업 번호를 입력하세요: ").strip()
    
    if choice not in ["1", "2"]:
        print("❌ 잘못된 입력입니다.")
        return

    id_choice = input("대상 프롬프트 ID 번호를 입력하세요: ").strip()
    if not id_choice.isdigit():
        print("❌ 숫자를 입력해주세요.")
        return

    target_id = int(id_choice)
    target_prompt = next((p for p in prompts if p['id'] == target_id), None)

    if not target_prompt:
        print("\n❌ 해당 ID의 프롬프트를 찾을 수 없습니다.")
        return

    # 1. 수정 작업
    if choice == "1":
        print(f"\n--- [ID: {target_id}] 프롬프트 수정 ---")
        print("*(변경하지 않으려면 내용 없이 엔터를 치세요)*")
        
        new_title = input(f"새 제목 (기존: {target_prompt['title']}): ").strip()
        if new_title:
            target_prompt['title'] = new_title

        new_content = input(f"새 내용 (기존: {target_prompt['content']}): ").strip()
        if new_content:
            target_prompt['content'] = new_content

        new_category = input(f"새 카테고리 (기존: {target_prompt['category']}): ").strip()
        if new_category:
            target_prompt['category'] = new_category

        save_prompts(prompts)
        print(f"\n✅ [ID: {target_id}] 프롬프트가 성공적으로 수정되었습니다!")

    # 2. 삭제 작업
    elif choice == "2":
        confirm = input(f"⚠️ 정말로 '{target_prompt['title']}' 프롬프트를 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirm == 'y':
            prompts.remove(target_prompt)
            save_prompts(prompts)
            print(f"\n🗑️ [ID: {target_id}] 프롬프트가 삭제되었습니다.")
        else:
            print("\n작업이 취소되었습니다.")

# [기능 8] 인기 프롬프트 (조회수 Top N)
def show_top_prompts():
    if not prompts:
        print("\n등록된 프롬프트가 없습니다.")
        return

    count_str = input("\n상위 몇 개를 조회하시겠습니까? (기본값: 5): ").strip()
    limit = int(count_str) if count_str.isdigit() and int(count_str) > 0 else 5

    # 조회수 기준 내림차순 정렬
    sorted_prompts = sorted(prompts, key=lambda x: x.get('usage_count', 0), reverse=True)
    top_list = sorted_prompts[:limit]

    print(f"\n🔥 [ 조회수 Top {len(top_list)} 인기 프롬프트 ]")
    print("=" * 50)
    for idx, p in enumerate(top_list, 1):
        fav = "⭐ " if p["is_favorite"] else ""
        print(f"{idx}위. [ID: {p['id']}] {fav}{p['title']} [{p['category']}] - 👀 {p.get('usage_count', 0)}회")
    print("=" * 50)

# [기능 9] 카테고리별 Markdown 파일 내보내기
def export_to_markdown():
    if not prompts:
        print("\n❌ 내보낼 프롬프트 데이터가 없습니다.")
        return

    filename = input("\n저장할 마크다운 파일명을 입력하세요 (기본값: prompts_export.md): ").strip()
    if not filename:
        filename = "prompts_export.md"
    if not filename.endswith(".md"):
        filename += ".md"

    # 카테고리별로 프롬프트 그룹화
    categorized = {}
    for p in prompts:
        cat = p['category']
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(p)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 📄 GenAI 프롬프트 모음집\n\n")
            f.write("> 이 문서는 GenAI 프롬프트 관리자에서 내보낸 문서입니다.\n\n")

            for cat, p_list in categorized.items():
                f.write(f"## 📂 카테고리: {cat}\n\n")
                for p in p_list:
                    fav = "⭐ " if p["is_favorite"] else ""
                    f.write(f"### {fav}{p['title']} (ID: {p['id']})\n")
                    f.write(f"- **조회수**: {p.get('usage_count', 0)}회\n")
                    f.write("```text\n")
                    f.write(f"{p['content']}\n")
                    f.write("```\n\n")
                f.write("---\n\n")

        print(f"\n✅ 성공적으로 '{filename}' 파일로 내보냈습니다!")
    except Exception as e:
        print(f"\n❌ 내보내기 중 오류가 발생했습니다: {e}")

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
        elif menu_choice == "7":
            edit_or_delete_prompt()
        elif menu_choice == "8":
            show_top_prompts()
        elif menu_choice == "9":
            export_to_markdown()
        elif menu_choice == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다! 👋")
            break
        else:
            print("\n❌ 잘못된 번호입니다. 메뉴의 번호를 다시 확인해 주세요.")

if __name__ == "__main__":
    main()