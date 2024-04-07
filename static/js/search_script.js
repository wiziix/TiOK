function getCountOfDisplayedElements(elements) {
    return Array.from(elements).filter(el => el.style.display === '').length;
}

document.getElementById('searchInput').addEventListener('input', function (event) {
    const searchNum = event.target.value;
    const table = document.querySelectorAll("table");

    table.forEach(function (item) {
        itemText = item.childNodes[1].childNodes[5].textContent;

        if (itemText.length > searchNum) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }

        if (getCountOfDisplayedElements(document.querySelectorAll('table')) === 0) {
            element = document.getElementById("message");
            element.style.visibility = 'visible';
        }
    });
});

