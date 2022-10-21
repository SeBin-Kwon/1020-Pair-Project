# 🗂️ Django Project (Pair programming) 

> 일시 : 2022-10-21
>
> 팀 구성 : 3인 1팀 (1-14 권세빈, 노은빈, 이수경)



![221021](https://user-images.githubusercontent.com/106902415/197198156-219de00f-2ca0-4dc2-a279-53b349bd3864.gif)



## 🫧 Contributors

<a href="https://github.com/code-sum/221021-PJT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=code-sum/221021-PJT" />
</a>



## ⚙️ Stacks

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>



## 📑 Requirements 

> 페어 프로그래밍을 통한 회원제 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(images, CSS, JS) 다루기
- **Django Auth** 활용 회원 관리 구현
- **Media** 활용 동적 파일 다루기
- 모델간 **1 : N** 관계 매핑 코드 작성 및 활용
  - 유저 - 리뷰
  - 유저 - 댓글
  - 리뷰 - 댓글



## 🔥 Issues

- 문제 상황

  - `accounts` 기능과 `reviews` 기능을 구현하고 두 개의 앱을 연동하는 과정에서 DB 이슈 발생

    - `Comment` 모델의 `review_id` 가 `NOT NULL` 제약조건에 위배됨
    - `Comment` 모델의 `user` 가 외래키 필드가 아닌 `CharField()` 로 작성됨 

    ```python
    class Comment(models.Model):
        reivew = models.ForeignKey(Review, on_delete=models.CASCADE)
        user = models.CharField(max_length=20)
        content = models.CharField(max_length=80)
    ```

- 문제 해결

  ```python
  class Comment(models.Model):
      review = models.ForeignKey(Review, on_delete=models.CASCADE)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      content = models.CharField(max_length=80)
  ```

  

## ✒️ Reviews

- **권세빈** : 다같이 에러를 잡아내며 게시글과 댓글 기능을 구현해서 재밌었지만 꼭 안경쓰고 오타를 조심해야겠다고 생각했습니다. 그리고 CSS 공부를 좀 더 해야할 것 같습니다.
- **노은빈** : 구현 중간중간 에러를 팀원들과 함께 고쳐나가며 눈이 아팠지만 또 해결을 하니 좋았습니다.  또 Django 구현은 금방 했지만 CSS에서 자주 막혀서 공부를 좀 더 해야겠다고 생각했습니다 좋은 팀원 분들과 함께해서 아주 즐거웠습니당
- **이수경** : 게시글 목록에 마우스를 올리면 호버 효과가 적용되도록 팀원들과 열심히 노력했습니다! Django 를 활용해서 필수 기능을 구현할 때보다 훨씬 오랜 시간이 걸렸지만, CSS 를 복습할 수 있어서 좋은 경험이었습니다.