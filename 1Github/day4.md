### GitHub 기반 원격 저장소 활용

1. Push

   1. 로컬 저장소의 버전을 원격저장소로 보낸다

   ```markdown
   git push
   ```

2. Pull

   1. 원격저장소의 버전을 로컬 저장소로 가져온다

   ```markdown
   git pull
   ```

3. 초기 원격 저장소 설정하는 법

   1. New Repository
   2. 저장소 설정하기
   3. url 확인
   4. 로컬 저장소에 원격 저장소 정보 설정하기

      ```markdown
          git remote add origin httpd://github.com/yun0727/test.git
      ```

   5. 원격 저장소의 정보를 확인함

      ```markdown
      git remote -v
      ```

   6. 로컬 저장소의 버전을 원격 저장소로 push 하기

      ```markdown
      git push <원격 저장소 이름> <브랜치 이름>

      git add .
      git commit -m 'README'
      git push origin main
      ```

   7. 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

      ```markdown
          git pull <원격저장소 이름> <브랜치 이름>
      ```

4. 원격 저장소 프로젝트 시작

   1. 원격 저장소를 복제하여 가저옴

      ```markdown
      git colne <원격 저장소 주소>
      ```

5. 명령어 정리

   1. clone : 원격저장소 복제
   2. pull : 원격 저장소 커밋 가져오기
   3. git init : 로컬에서 새로운 프로젝트 시작
   4. git clone : 원격에 있는 프로젝트 시작
   5. git pull : 프로젝트 개발 중 다른 사람 커밋 받아오기
   6. git push : 내가 한 로컬 프로젝트 개발 공유
   7. 원격 저장소 복제

      ```markdown
          git clone <url>
      ```

   8. git remote : 원격 저장소 정보 확인

      ```markdown
      git remote -v
      ```

   9. 원격 저장소 추가

      ```markdown
      git remote add <원격저장소><url>
      ```

   10. 원격 저장소 삭제

       ```markdown
           git remote rm <원격 저장소>
       ```

   11. 원격 저장소에 push

       ```markdown
       git push <원격 저장소><브랜치>
       ```

   12. 원격 저장소로부터 pull

       ```markdown
       git pull<원격 저장소><브랜치>
       ```

### .gitignore

1. 일반적인 개발 프로젝트에서 버전관리를 별도로 하지 않는 파일/디렉토리가 발생
2. git 저장소에 .gitignore 파일 생성하고 해당 내용을 관리한다.
3. 이미 커밋된 파일은 반드시 삭제를 하여야 .gitignore로 적용된다.
4. https://gitignore.io
5. 확장자 없이 .gitignore만 작성
