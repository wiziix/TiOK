function enforceMinMax(el) {
  if (el.target.value != "") {
    if (el.target.value < 1) {
      el.target.value = 1;
    }
    else if (el.target.value > 200) {
       el.target.value = 200;
    }
  }
}

document.getElementById('searchInputStart').addEventListener('input', function (event) {
    enforceMinMax(event);
    const searchEnd = (document.getElementById("searchInputFinish").value === "") ?
        200 : document.getElementById("searchInputFinish").value;

    const searchBeg = event.target.value;
    const table = document.querySelectorAll("table");

    table.forEach(function (item) {
        itemText = item.childNodes[1].childNodes[5].textContent;

        if (itemText.length >= searchBeg && itemText.length <= searchEnd) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }

    });
});

document.getElementById('searchInputFinish').addEventListener('input', function (event) {
    enforceMinMax(event);
    const searchEnd = event.target.value;
    const searchBeg = (document.getElementById("searchInputStart").value === "") ?
        1: document.getElementById("searchInputStart");
    const table = document.querySelectorAll("table");


    table.forEach(function (item) {
        itemText = item.childNodes[1].childNodes[5].textContent;

        if (itemText.length >= searchBeg && itemText.length <= searchEnd) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }

    });
});

