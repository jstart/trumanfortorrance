// Language switching by URL hash: #es, #ko, #ja, #zh, #en. A card can be targeted as #es-tax, or as #tax in the visitor's language.
(function () {
  var codes = SITE_CONFIG.languages;
  var langAttr = { en: "en", es: "es", ko: "ko", ja: "ja", zh: "zh-Hant" };
  var links = document.querySelectorAll(".langnav__link");

  function parse(hash) {
    var m = /^#(en|es|ko|ja|zh)(?:-([a-z]+))?$/.exec(hash || "");
    if (m) return { lang: m[1], card: m[2] || "" };
    var c = /^#(trash|tax|care|medicare|food|hip|focal)$/.exec(hash || "");
    return c ? { lang: guess(), card: c[1] } : null;
  }
  function guess() {
    var saved = "";
    try { saved = localStorage.getItem("senior-guide-lang") || ""; } catch (e) {}
    if (codes.indexOf(saved) >= 0) return saved;
    var nav = (navigator.language || "en").toLowerCase().slice(0, 2);
    return codes.indexOf(nav) >= 0 ? nav : "en";
  }
  function show(lang, card) {
    codes.forEach(function (c) { document.getElementById("lang-" + c).hidden = c !== lang; });
    Array.prototype.forEach.call(links, function (a) {
      a.setAttribute("aria-current", a.getAttribute("data-lang") === lang ? "true" : "false");
    });
    document.documentElement.lang = langAttr[lang];
    try { localStorage.setItem("senior-guide-lang", lang); } catch (e) {}
    var target = card ? document.getElementById(lang + "-" + card) : null;
    if (target) { target.scrollIntoView(); } else { window.scrollTo(0, 0); }
  }
  function route() {
    var p = parse(location.hash);
    if (p) { show(p.lang, p.card); return; }
    var lang = guess();
    show(lang, "");
    if (history.replaceState) history.replaceState(null, "", "#" + lang);
  }
  window.addEventListener("hashchange", route);
  route();
})();
