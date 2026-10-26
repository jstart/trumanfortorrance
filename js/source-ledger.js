// Optional filtering for the static evidence ledger; all rows remain readable without JS.
(function () {
  var search = document.getElementById("search");
  var category = document.getElementById("category");
  var count = document.getElementById("count");
  var rows = Array.prototype.slice.call(document.querySelectorAll("tbody tr"));

  function filter() {
    var query = search.value.toLowerCase();
    var prefix = category.value;
    var visible = 0;
    rows.forEach(function (row) {
      row.hidden = row.textContent.toLowerCase().indexOf(query) < 0 ||
        (prefix && row.cells[2].textContent.trim().indexOf(prefix) !== 0);
      if (!row.hidden) visible++;
    });
    count.textContent = visible + " sources";
  }

  search.addEventListener("input", filter);
  category.addEventListener("change", filter);
  filter();
})();
