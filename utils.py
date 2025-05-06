## ----------------------------------------------------------
## 사용자 정의 함수들
## ----------------------------------------------------------
## 모듈로딩

## ----------------------------------------------------------
## 함수기능 : 텐서의 속성 출력
## 함수이름 : printTensorInfo
## 매개변수 : tname - 텐서이름
##			 tobject - 텐서객체
## 반 환 값 : 없음
## ----------------------------------------------------------
## 텐서 속성 확인
def printTensorInfo(tname, tobject):
	print(f'{tname}-----------------------------')
	print(f'shape  : {tobject.shape}	 {tobject.size()}' )
	print(f'ndim   : {tobject.ndim}      {tobject.dim() }')
	print(f'device : {tobject.device}')
	print(f'dtype  : {tobject.dtype}' )
	print(f'tensor : {tobject}')