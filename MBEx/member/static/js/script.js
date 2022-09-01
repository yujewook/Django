//# 데이터를 안보내고 그냥 페이지에서 java 스크립에서
var idcheck = "아이디를 입력해라";
var passwdck = "비번을 입력해라";
var repasswdck = "비번이 다름 ㅋㅋ";
var nameck = "이름을 입력해라";



//중복 확인
function confirm() {
   if( ! inputform.id.value ) {
      alert( idcheck );
      inputform.id.focus()   
   } else {
      url = "confirm" + "?id=" + inputform.id.value
      open( url, "confirm", "toolbar=no, menubar=no, scrollbar=no, status=no, width=500, height=300" )
   }
}
//중복한 안된 아이디 화면에 다시 넣어주기
function setid(id){
	opener.document.inputform.id.value = id;
	window.close();
}



// 가입 페이지
function inputcheck() {
   if( ! inputform.id.value ) {
      alert( idcheck );
      inputform.id.focus();
      return false;
   } else if( ! inputform.passwd.value ) {
      alert( passwdck );
      inputform.passwd.focus();
      return false;
   } else if( inputform.passwd.value != inputform.repasswd.value ) {
      alert( repasswdck );
      inputform.passwd.focus();
      return false;
   } else if( ! inputform.name.value ) {
      alert( nameck );
      inputform.name.focus();
      return false;
   }
   
}


// 메인 페이지
function maincheck() {
   if( ! mainform.id.value ) {
      alert( idcheck )
      mainform.id.focus();
      return false;
   } else if( ! mainform.passwd.value ) {
      alert( passwdck );
      mainform.passwd.focus();
      return false;
   }
   
}
