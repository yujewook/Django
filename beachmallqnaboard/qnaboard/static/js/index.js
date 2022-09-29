// $("li").click(function () {
//     if ($(this).hasClass("active")) {
//       $(this).children().css("display", "none");
//       $(this).removeClass();
//     } else {
//       $(this).addClass("active");
//       $(this).children().css("display", "block");
//     }
//   });

// $(document).ready(function(){

// 	$('.cate .catearea').hide();

// 	$('.catemom').mouseover(function(){
// 		$('.catearea').slideDown();

// 	});
// 	$('.catemom').mouseleave(function(){
// 		$('.catearea').hide();
// 	});

// 상단 카테고리 슬라이드
$(document).ready(function () {
  // $(".catemom")
  //   .mouseenter(function () {
  //     var submenu = $(this).next("ul"); // submenu 가 화면상에 보일때는 위로 보드랍게 접고 아니면 아래로 보드랍게 펼치기
  //     if (submenu.is(":visible")) {
  //       submenu.slideUp();
  //     } else {
  //       submenu.slideDown();
  //     }
  //   })
  //   // .mouseover(function () {
  //   //   var submenu = $(this).next("ul") // submenu 가 화면상에 보일때는 위로 보드랍게 접고 아니면 아래로 보드랍게 펼치기
  //   //   .slideDown();
  //   // })
  //   .click(function () {
  //     $(this).next("ul").slideDown();
  //   })
  //   .mosueover(function () {
  //     $(this).slideUp();
  //   });
  $("nav li").hover(
    function () {
      $("ul", this).stop().slideDown(100);
    },
    function () {
      $("ul", this).stop().slideUp(200);
    }
  );
});

// 검색어 순위
$(function () {
  const ticker = function () {
    setTimeout(function () {
      $("#ticker li:first").animate({ marginTop: "-20px" }, 200, function () {
        $(this).detach().appendTo("ul#ticker").removeAttr("style");
      });
      ticker();
    }, 4000);
  };
  ticker();
});

// 상단으로 오는 버튼
function clickme() {
  window.scrollTo({top:0, left:0, behavior:'smooth'});
}