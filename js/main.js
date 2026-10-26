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
  var toolText = {
    en: { size: "Larger text", print: "Print" },
    es: { size: "Texto más grande", print: "Imprimir" },
    ko: { size: "큰 글씨", print: "인쇄" },
    ja: { size: "大きい文字", print: "印刷" },
    zh: { size: "放大文字", print: "列印" }
  };
  function setToolLabels(lang) {
    var sizeBtn = document.getElementById("size-toggle"), printBtn = document.getElementById("print-btn");
    if (sizeBtn) sizeBtn.querySelector(".tool__label").textContent = toolText[lang].size;
    if (printBtn) printBtn.querySelector(".tool__label").textContent = toolText[lang].print;
  }
  function setSize(large) {
    document.documentElement.setAttribute("data-size", large ? "large" : "normal");
    var b = document.getElementById("size-toggle");
    if (b) b.setAttribute("aria-pressed", large ? "true" : "false");
    try { localStorage.setItem("senior-guide-size", large ? "large" : "normal"); } catch (e) {}
  }
  function initTools() {
    var large = false;
    try { large = localStorage.getItem("senior-guide-size") === "large"; } catch (e) {}
    setSize(large);
    var b = document.getElementById("size-toggle"), p = document.getElementById("print-btn");
    if (b) b.addEventListener("click", function () { setSize(document.documentElement.getAttribute("data-size") !== "large"); });
    if (p) p.addEventListener("click", function () { window.print(); });
  }
  function show(lang, card) {
    codes.forEach(function (c) { document.getElementById("lang-" + c).hidden = c !== lang; });
    Array.prototype.forEach.call(links, function (a) {
      a.setAttribute("aria-current", a.getAttribute("data-lang") === lang ? "true" : "false");
    });
    document.documentElement.lang = langAttr[lang];
    setToolLabels(lang);
    try { localStorage.setItem("senior-guide-lang", lang); } catch (e) {}
    var target = card ? document.getElementById(lang + "-" + card) : null;
    if (target) {
      target.scrollIntoView({ behavior: "instant", block: "start" });
      // Fonts and layout can shift after load, so settle on the card once they are ready.
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(function () { target.scrollIntoView({ behavior: "instant", block: "start" }); });
      }
    } else {
      window.scrollTo({ top: 0, behavior: "instant" });
    }
  }
  function route() {
    var p = parse(location.hash);
    if (p) { show(p.lang, p.card); return; }
    var lang = guess();
    show(lang, "");
    if (history.replaceState) history.replaceState(null, "", "#" + lang);
  }
  initTools();
  // Reader tools also serve pages without translated language sections.
  if (document.querySelector(".lang")) {
    window.addEventListener("hashchange", route);
    route();
  }
})();
