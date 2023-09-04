# How to write .md file
- https://www.markdownguide.org

### 1. 제목
- '#' 을 사용하여 제목을 표시
- '#' 의 갯수에 따라 제목의 레벨이 변경 (1~6개)
- ex.
    - # H1  --> # H1 
    - ## H2 --> ## H2 
    - ### H3  --> ### H3 
    - #### H4  --> #### H4 
    - ##### H5  --> ##### H5 
    - ###### H6  --> ###### H6 



### 2. 텍스트 스타일
- bold : '**Bold**' or '__Bold__'
- italic : '*italic*' or '_italic_'
- bold & italic : '*** Bold & italic ***' or '___ Bold & italic ___'
- 취소선 : '~~~취소선~~~'
  

### 3. 목록
##### 3.1 순서 있는 목록
1. 1st
2. 2nd
3. 3rd

##### 3.2 순서 없는 목록
- 1st
- 2st
- 3rd


### 4. 링크
- [google](링크 주소)
- [google](https://www.google.com/)


### 5. 이미지
- ![Alt text](image.png)
- 사용 방법 : ![이미지 대체 텍스트](이미지URL)
- -->> md 파일에 이미지 복사해도 됨


### 6. 코드
- 한줄 코드 : ''code''
- 여러줄 코드 -->> 한줄 띄워줘야함.


sample

    code1

    code2

    code3

sample end


- 여러줄 코드

  <pre> <code> pre, code 태그 사용 </code> </pre>
  
사용 예시 
<pre>
<code>
  var_1 = [1, 2, 3]
</code>
</pre>


### 7. 인용 & BlockQuote
- 사용 방법 : ' > 인용문 '
> 인용문

- '>' 블로 인용 문자 사용
- ex
  - > block_1   : > block_1
  - >   > block_2 : >   > block_2
  - >   >   > block_3 : >   >   > block_3



### 8. 구분선
-  사용 방법 : --- 사용
---


### 9. 체크박스
- 사용 방법 : [x] 체크, [ ] 언체크
- [x] 체크
- [ ] 언체크

