console.log("Live Editor : Correctif Auto-resize...");

const htmlIcon = `<svg viewBox="0 0 512 512" width="14" height="14" style="vertical-align: middle; margin-right: 5px;" fill="#fb7e14"><path d="M0 48v416l190.7 48 190.7-48V48H0zm307.3 147.1L299.7 268l-109 29.5-109-29.5-7.7-86.4h48.3l3.8 43.1 64.6 17.5 64.6-17.5 7.4-83h-192l-8.5-96h248.8l-7.7 86.4z"/></svg>`;
const cssIcon = `<svg viewBox="0 0 512 512" width="14" height="14" style="vertical-align: middle; margin-right: 5px;" fill="#2965f1"><path d="M0 48v416l190.7 48 190.7-48V48H0zm307.3 147.1L299.7 268l-109 29.5-109-29.5-7.7-86.4h48.3l3.8 43.1 64.6 17.5 64.6-17.5 7.4-83h-192l-8.5-96h248.8l-7.7 86.4z"/></svg>`;

function initLiveEditors() {
    document.querySelectorAll(".live-editor").forEach((el) => {
        if (el.dataset.initialized) return;
        el.dataset.initialized = "true";
        setupStandardEditor(el);
    });

    document.querySelectorAll(".live-editor-dual").forEach((el) => {
        if (el.dataset.initialized) return;
        el.dataset.initialized = "true";
        setupDualEditor(el);
    });
}

function setupStandardEditor(el) {
    const code = el.textContent.trim();
    el.innerHTML = `
        <div class="editor-header"><span>${htmlIcon} HTML / CSS</span></div>
        <textarea class="editor-input" spellcheck="false">${code}</textarea>
        <div class="editor-preview-label">Rendu en direct :</div>
        <div class="editor-preview"></div>
    `;
    const textarea = el.querySelector(".editor-input");
    const preview = el.querySelector(".editor-preview");
    setupIframe(textarea, null, preview);
}

function setupDualEditor(el) {
    const rawContent = el.textContent.trim();
    let htmlPart = "";
    let cssPart = "";
    
    if (rawContent.includes("---css---")) {
        const parts = rawContent.split("---css---");
        htmlPart = parts[0].replace("---html---", "").trim();
        cssPart = parts[1].trim();
    }

    el.innerHTML = `
        <div class="editor-dual-container">
            <div class="editor-pane">
                <div class="editor-header"><span>${htmlIcon} HTML</span></div>
                <textarea class="editor-input html-input" spellcheck="false" placeholder="Code HTML...">${htmlPart}</textarea>
            </div>
            <div class="editor-pane">
                <div class="editor-header"><span>${cssIcon} CSS</span></div>
                <textarea class="editor-input css-input" spellcheck="false" placeholder="Code CSS...">${cssPart}</textarea>
            </div>
        </div>
        <div class="editor-preview-label">Rendu en direct :</div>
        <div class="editor-preview"></div>
    `;
    
    const htmlInput = el.querySelector(".html-input");
    const cssInput = el.querySelector(".css-input");
    const preview = el.querySelector(".editor-preview");
    setupIframe(htmlInput, cssInput, preview);
}

function setupIframe(htmlInput, cssInput, preview) {
    const iframe = document.createElement("iframe");
    iframe.className = "preview-iframe";
    iframe.style.width = "100%";
    iframe.style.border = "none";
    iframe.style.minHeight = "60px"; // Min height plus petit
    iframe.style.height = "100px";
    preview.appendChild(iframe);
    
    const baseStyle = "<style>body{font-family: sans-serif; padding:15px; margin:0; line-height:1.5; background:white; overflow:hidden;} img{max-width:100%; height:auto; border-radius:4px;} h1{color:#5c27fe; border-bottom:1px solid #ddd; padding-bottom:5px; margin-top:0;}";

    const update = () => {
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        if (doc) {
            doc.open();
            const userCss = cssInput ? `<style>${cssInput.value}</style>` : "";
            doc.write(baseStyle + "</style>" + userCss + htmlInput.value);
            doc.close();
            
            // Calcul stable de la hauteur
            setTimeout(() => {
                if (doc.body) {
                    // On réduit temporairement pour forcer le recalcul
                    iframe.style.height = "1px";
                    const newHeight = Math.max(doc.body.scrollHeight, doc.documentElement.scrollHeight, 60);
                    iframe.style.height = newHeight + "px";
                }
            }, 10);
        }
    };

    htmlInput.addEventListener("input", update);
    if (cssInput) cssInput.addEventListener("input", update);
    setTimeout(update, 500);
}

setInterval(initLiveEditors, 1000);
initLiveEditors();
