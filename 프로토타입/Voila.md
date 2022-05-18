# Voila

## 프로토타입이 중요한 이유
* 혼자 확인할때는 jupyter notebook에서 함수 작성한 후 예측 함수 실행하며 성능 확인 가능
* 그러나 동료랑 함께 사용할때는... 
* ModuleNotFound Error, No module named 등등 라이브러리 의존성 에러 발생
* 테스트를 위해 추가 환경 설정 필요

#### Notebook 베이스로 프로토타입 만들기
* 모델 개발한 후 사람들과 테스트할 수 있는 프로토타입 먼저 만들어보기
* 이 모델이 어떤 결과를 변환하는가?를 테스트할 수 있음
* 웹 서비스 만드는 시간 아낄 수 있음
* ipywidget 같이 사용하면 간단한 대시보드 구축 가능

## Voila
* 대시보드 만드는 것
* 별도의 추가 코드 필요 X
* 고유한 템플릿 생성 가능

#### Voila 사용하기
```python
pip3 install voila

# JupyterLat 사용시
jupyter labextension install @jupyter-voila/jupyterlab-preview

# jupyter Notebook이나 jupyter Server를 사용한다면
jupyter serverextension enable voila --sys-prefix

# nbextension도 사용 가능하도록 하고 싶다면 다음과 같이 설정
voila --enable_nbextensions=True
jupyter notebook --VoilaConfiguration.enable_nbextensions=True

```

![image](https://user-images.githubusercontent.com/63588046/168943615-ee4c7b50-eb77-4c6a-bb8f-7d4374a87803.png)

![image](https://user-images.githubusercontent.com/63588046/168943672-430c75e3-3c35-403f-9fdf-06d173818b77.png)

![image](https://user-images.githubusercontent.com/63588046/168943707-841e92ba-b4b6-4b05-9bb1-62f9af040375.png)

![image](https://user-images.githubusercontent.com/63588046/168944268-09e2db96-bc3f-4f11-b348-795babb3e357.png)


* Voila는 30초 이상 진행되면 Timeout Error 발생 
* voila --ExecutePreprocessor.timeout=180  # 180초동안 제한시간 늘림
* jupyter notebook --ExecutePreprocessor.timeout=180  # 180초동안 제한시간 늘림


#### Voila 사용 팁
* vi ~/.jupyter/jupyter_notebook_config.py   # config파일로 진입
* c.NotebookApp.password = 'afjkl;akfaf'    # 비밀번호 설정


# ipywidget 
* 인터렉티브 효과를 줄 수 있음

```python
import ipywidgets as wedgets
from IPython.display import display

# 정수형 Slider   (IntSlider, FloatSlider(실수형), IntRangeSlider(범위형))
int_slider = widgets.IntSlider(
                  value=7,        # default 값
                  min=0,
                  max=10,
                  step=1,         # 한번에 이동할 단계
                  orientation='horizontal',   # 수직, 수평
                  description     # slider의 label
                  ) 
display(int_slider)

int_slider.value # int_slider 값
int_slider.value = 8 # int_slider 값을 바꿈


# Text Widget, 박스에 글자를 넣을 수 있게 해줌
widgets.BoundedIntText(
     value=7,
     min=0,
     max=10,
     step=1,
     description='Text : ',    # 박스 앞에 있는 글씨
     disabled=False
     
widgets.ToggleButton(
      value=False,                      # 기본값
      description='Click me',           # 박스 앞에 이름
      button_style='', # 'success', 'info', 'warning', 'danger', ''  # 버튼 스타일
      tooltip='Description',
      icon='check'                       # 글자 앞에 넣을 아이콘, https://fontawesome.com/v4.7/icons/ 에서 확인 가능


# CheckBox
widget.Checkbox(
    value=False,              # 기본으로 체크 X
    description='Check me',   # 체크박스 글씨
    indent=False              # 체크박스 중앙에 넣지 말기 (맨 앞에 체크박스)
    
# DropBox (보조박스)
widget.Dropdown(
    options=['1','2','3'],     # 바꿀 수 있는 값
    value='2',
    description='Number:',     # 박스 앞에 글씨
    disabled=False,
    )
    
# 라디오박스
widgets.RadioButtons(
    options=['pepperoni','pineapple','anchovies']
    description='Topping:',
    )


# 파일 업로드
widgets.FileUpload(
    accept='',          # 허용할 확장자
    multiple=False      # 여러파일 업로드 할 경우 True
    )
    

# 이미지 보여주기
file=open('metamong.png','rb')
image=file.read()
widgets.Image(
    value=image,
    format='png',
    width=300,
    height=400,
    )
    
# 날짜 선택
widgets.DatePicker(
    description='Pick a Datae',
    disabled=False
    )
    
# 버튼 이벤트
button = widgets.Button(description='Click Me!')
output = widgets.Output()
display(button, output)

def on_button_clicked(button):
  with output:
    print("hello world!")
    
button.on_click(on_button_clicked)

# Layout(HBox, VBox)  # 수평, 수직
slider = widgets.FloatSlider(description="%x$", value=4)
text = widgets.FloatText(disabled=True, description='$x^2$')
def compute(*ignore):
  text.value=str(slider.value**2)
slider.observe(coupute,'value')
widgets.VBox(slider, text)   # slider 값과 text값을 수직으로 보여라
```



## ipywidget 사용법

## ipywidget + voila
