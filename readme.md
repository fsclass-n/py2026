# 내 컴퓨터에서 원격 리포지토리 만들기
git init
# 브랜치 변경 (master -> main)
git branch -m master main
# 원격 리포지토리 목록 보기
gh repo list
# 원격 리포지토리 생성 + 로컬 디렉토리 연결
gh repo create py2026 --public --source=.
# 삭제 권한 추가
gh auth refresh -h github.com -s delete_repo
# 원격 리포지토리 삭제
gh repo delete <username>/<repo-name> --yes
# 예) gh repo delete fsclass-n/team --yes
