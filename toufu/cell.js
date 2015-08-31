// Forked from https://github.com/ctiml/campaign-finance.g0v.ctiml.tw
$(document).ready(function(){

  var shadow = function() {
    $('#ans-shadow').offset($('#ans').position());
  }
  $(window).resize(function(){
    shadow();
  });
  shadow();

  var submitAnswer = function(e) {
    if (e !== undefined) {
      e.preventDefault();
    }

    var ans = $('#ans').val();

    if ($(this).hasClass("quick-answer")) {
        ans = $(this).data('answer');
    }

    if (ans === "" && $(this).hasClass("no-content") === false) {
      return;
    }

    var p = $('.cell-info').data('p');
    var par = $('.cell-info').data('par');

    $('#submit,#no-content').attr('disabled', 'disabled');

    // trim 掉前後空白
    ans = jQuery.trim(ans);
    var url = 'submit.php';
    $.post(url, { p: p, par: par, ans: ans }, setProgress);
    getRandomImage();
    $('#submit,#no-content').removeAttr('disabled');

    $('#ans-shadow').val("");
  };

  var set_question = function(res){
      var img = $('<img></img>').attr('src', res.img_url).bind('error', function(){ getRandomImage(); });
      img.bind('load', function() {
        $('.cell-image').html(img);
        $('.cell-info').data({
          p: res.p,
          par: res.par,
          ans: res.ans
        })
        .text("")
        .append($('<span></span>').text("第 "+res.p+" 頁, 第 "+res.par+" 行 "));

        if (res.ans !== null) {
          $('.cell-info').append($('<span></span>').text(" 已經有" +res.cnt + "人填寫確認了。"));
	  $('#ans').val(res.ans);
        }
	res.p = ('000' + res.p).slice(-3);
        // $('.cell-info').append($('<span></span>').html('<a href="http://ckhis.ck.tp.edu.tw/~ljm/amis/index.php?p='+res.p+'" target="_blank">查看整頁</a>'));
        $('#unclear').show();
      });
  };

  var question_pools = [];

  var getRandomImage = function() {
    $('#ans').val("").focus();
    $('.cell-info').text("圖片載入中...");
    $('.cell-image').html("");
    $('#unclear').hide();

    if (question_pools.length) {
        set_question(question_pools.shift());
        return;
    }
    
    $.get('submit.php', setProgress);
    $.get('random.php', function(questions){
        question_pools = questions;
        set_question(question_pools.shift());
    });
  };
  getRandomImage();

  function thisIsEmpty() {
    var p = $('.cell-info').data('p');
    var par = $('.cell-info').data('par');
    var url = 'submit.php';
    $.post(url, { p: p, par: par, ans: '[這是空白]' }, setProgress);
    getRandomImage();
  }

  function setProgress(data) {
	  console.log(data);
    if(data['cnt'] != undefined) {
      var percent = Math.round(10000 * data['cnt'] / 15829) / 100;
      $('.bar').css('width', '' + percent + '%');
      $('#progress_text').text('已完成 ' + data['cnt'] + ' / 15829 (' + percent + '%)');
    }
  }

  $('#submit').click(submitAnswer);
  $('#no-content').click(thisIsEmpty);
  $('.quick-answer').click(submitAnswer);
  $('#quick-trigger').click(function(){
    $('.quick-answer').toggle();
    $('.open-close').text($('.quick-answer').is(':visible') ? "關閉" : "開啟");
  });
  $('#unclear').click(function() {
    var p = $('.cell-info').data('p');
    var par = $('.cell-info').data('par');
    var url = 'submit.php';
    $.post(url, { p: p, par: par, ans: '[圖片不清楚]' }, setProgress);
    getRandomImage();
  });

  $('#next').click(getRandomImage);

  $('#ans').keypress(function(e) {
    if (e.which == 13) {
      if (e.shiftKey) {
        thisIsEmpty();
      } else {
        submitAnswer();
      }
      e.preventDefault();
    }
  });

  var candidates = [];
  var candidate_index = 0;
  var search_candidates = function(ans, collection) {
    return collection.filter(function(a) {
      var escaped_ans = ans.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, "\\$&");
      return a.match("^" + escaped_ans + ".+");
    }).sort();
  }
  var find_candidate_index = function(ans_shadow) {
    var index = candidates.indexOf(ans_shadow);
    return (index < 0) ? 0 : index;
  }

});
