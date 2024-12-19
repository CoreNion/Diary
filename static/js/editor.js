// タグ追加ボタンをクリックしたときの処理
const addTagBtn = document.getElementById("tags__add");
addTagBtn.addEventListener("click", function () {
  // テンプレートからタグ要素を引っ張ってきて追加
  const template = document.getElementById("tag-template");
  var tag = template.content.cloneNode(true);
  document.getElementById("id_tags").insertBefore(tag, addTagBtn);
});

// タグに何も入力されなかった場合はタグ要素削除
document.getElementById("id_tags").addEventListener("keydown", function (event) {
  // Backspaceで0文字になった場合は削除
  if (event.key === "Backspace" || event.key === "Delete") {
    checkEmptyTag(event);
  }
});
document.getElementById("id_tags").addEventListener("focusout", function (event) {
  // フォーカスが外れたときに0文字だったら削除
  checkEmptyTag(event);
});

/// タグが空文字だった場合は削除
function checkEmptyTag(event) {
  if (event.target && event.target.classList.contains("tag__input")) {
    if (event.target.value.trim() === "") {
      event.target.closest(".tag").remove();
    }
  }
}

// 送信ボタンの処理
document.getElementById("submit__btn").addEventListener("click", function (event) {
  // 送信
  document.getElementById("editor-form").submit();
});