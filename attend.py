# attend.py
import csv
import os
from datetime import date

FILE = "attendance.csv"

def load():
    """저장된 출석 기록을 불러옵니다."""
    records = []
    if os.path.exists(FILE):
        with open(FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # 빈 줄 건너뜀
                    records.append(row)
    return records

def save(records):
    """출석 기록 전체를 파일에 저장합니다."""
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(records)

def add_record(records):
    """날짜와 이름을 입력받아 출석을 추가합니다."""
    date_input = input(f"날짜를 입력하세요 (예: 2025-01-15, 엔터 = 오늘): ").strip()
    if not date_input:
        date_input = str(date.today())  # 엔터 치면 오늘 날짜 자동 입력

    name = input("이름을 입력하세요: ").strip()
    if not name:
        print("⚠️  이름을 입력해야 합니다.")
        return

    records.append([date_input, name])
    save(records)
    print(f"✅ [{date_input}] {name} 출석 완료!")

def show_records(records):
    """출석 목록을 출력합니다."""
    print("\n" + "=" * 30)
    print(f"  {'날짜':<15} {'이름'}")
    print("=" * 30)
    if not records:
        print("  기록이 없습니다.")
    else:
        for row in records:
            print(f"  {row[0]:<15} {row[1]}")
    print("=" * 30)
    print(f"  총 {len(records)}건\n")

def main():
    print("=== 스터디 출석부 ===")
    records = load()  # 시작할 때 기존 기록 불러오기

    while True:
        print("\n[1] 출석 입력   [2] 목록 보기   [3] 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_records(records)
        elif choice == "3":
            print("👋 종료합니다.")
            break
        else:
            print("⚠️  1, 2, 3 중에 선택해 주세요.")

if __name__ == "__main__":
    main()