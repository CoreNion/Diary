// タグのWidthを自動調整
const setTagWidth = function (input) {
  const tempSpan = document.createElement("span");
  tempSpan.style.visibility = "hidden";
  tempSpan.style.position = "absolute";
  tempSpan.style.whiteSpace = "nowrap";
  tempSpan.textContent = input.value || input.placeholder;
  document.body.appendChild(tempSpan);
  input.style.width = (tempSpan.scrollWidth + 5) + "px";
  document.body.removeChild(tempSpan);
};

// タグ追加ボタンをクリックしたときの処理
const addTagBtn = document.getElementById("tags__add");
addTagBtn.addEventListener("click", function () {
  // テンプレートからタグ要素を引っ張ってきて追加
  const template = document.getElementById("tag-template");
  var tag = template.content.cloneNode(true);
  document.getElementById("id_tags").insertBefore(tag, addTagBtn);

  // 追加された最後のタグ要素にフォーカス
  const added = document.getElementById("id_tags").querySelectorAll(":nth-last-child(2)")[0].querySelector(".tag__input");
  added.focus();
  // 追加されたタグ要素の幅を調整
  added.addEventListener("input", function (event) {
    setTagWidth(event.target);
  });
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

/// テキストエリアの高さを自動調整
// 読み込み時
document.addEventListener("DOMContentLoaded", function () {
  const content = document.getElementById("id_content");
  content.style.height = "auto";
  content.style.height = document.getElementById("id_content").scrollHeight + "px";
});

document.getElementById("id_content").addEventListener("input", function (event) {
  this.style.height = "auto";
  this.style.height = this.scrollHeight + "px";
});

document.querySelectorAll(".tag__input").forEach(function(input) {
  setTagWidth(input);
  input.addEventListener("input", function(event) {
    setTagWidth(event.target);
  });
});

// 送信ボタンの処理
document.getElementById("submit__btn").addEventListener("click", function (event) {
  /// フォームの検証
  const title = document.getElementById("id_title");
  if (!title.value.trim()) {
    title.setCustomValidity("タイトルを入力してください");
    title.reportValidity();
    return;
  } else if (title.value.length > 100) {
    title.setCustomValidity("タイトルは100文字以内で入力してください");
    title.reportValidity();
    return;
  }

  const date = document.getElementById("id_date");
  const time = document.getElementById("id_time");
  if (!time.value.trim() || !date.value.trim()) {
    date.setCustomValidity("日時を入力してください");
    date.reportValidity();
    return;
  }

  const content = document.getElementById("id_content");
  if (!content.value.trim()) {
    content.setCustomValidity("本文を入力してください");
    content.reportValidity();
    return;
  }

  // 送信
  document.getElementById("editor-form").submit();
});